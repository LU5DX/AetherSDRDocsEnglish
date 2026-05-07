# Select a mic profile for a specific microphone

Use the "Mic profile" combo box in the Phone/CW applet to load a named microphone processing profile stored on the radio. Different microphones often need different EQ and processing settings; switching profiles applies the correct configuration for the connected mic without adjusting each parameter manually.

## Before you start

- AetherSDR must be connected to the radio. The "Mic profile" combo box is only populated when a connection is active.
- The active slice must be in a voice mode (SSB, AM, FM). The Phone/CW applet shows the Phone sub-panel in voice modes; in CW mode the mic profile controls are not visible.

## Steps

1. Click the "P/CW" tray button in the right sidebar to open the Phone/CW applet, if it is not already visible.
2. Confirm that the Phone sub-panel is displayed. If the applet shows CW controls, the active slice is in a CW mode — switch the slice to a voice mode first.
3. Click the "Mic profile" combo box. The list is populated from the profiles stored on the radio.
4. Select the profile name that matches your microphone. The profile loads immediately.

## What each control does

| Control     | Kind      | Behavior                                             |
|-------------|-----------|------------------------------------------------------|
| Mic profile | Combo box | Loads the named mic processing profile on the radio. |

## Tips

- The available profile names come from the radio, not from AetherSDR. To create or rename profiles, use the radio's own profile management. In AetherSDR you can also open `Profiles > Profile Manager...` to manage transmit profiles.
- Selecting a profile does not change the "Mic source" or "Mic gain" settings; adjust those separately if needed.

## CW sidetone behavior (v0.9.2.1)

In v0.9.2.1 the separate "Local STn" button, local sidetone volume slider, "Follow" pitch toggle, and manual local pitch slider have been removed. The single **Sidetone** toggle and **Sidetone volume** slider in the CW panel now control both the radio's DAX-fed monitor and the client-side low-latency sidetone generator (CwSidetoneGenerator, ~10 ms latency) in lockstep. There are no longer any independent local-sidetone controls or associated settings keys (`CwLocalSidetoneEnabled`, `CwLocalSidetoneVolume`, `CwLocalSidetonePitchFollow`, `CwLocalSidetonePitchHz`).

Pitch and pan continue to follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically; no manual override is needed or available.

## Changes in v0.9.3

### Level gauge — PC mic source exception

Previously the Level gauge was suppressed to −150 dBFS whenever `met_in_rx` was off and the radio was not transmitting, regardless of mic source. Starting in v0.9.3, this suppression no longer applies when the selected mic source is **PC**. Because PC-source metering is driven by client-side audio rather than the radio's `met_in_rx` flag, the gauge now appears immediately on connect when the mic source is set to PC (#2086).

No change in behavior occurs for hardware mic sources (MIC, BAL, LINE, ACC); those continue to be suppressed when `met_in_rx` is off and the radio is not transmitting.

### VOX toggle now refreshes the Phone panel instantly

Toggling VOX via a keyboard shortcut now causes the Phone panel to refresh immediately. Previously, the panel did not update until some other UI event occurred. This was corrected by having the VOX setters emit `phoneStateChanged` (#2084).

### Sidetone stream on Windows

On Windows, the client-side sidetone stream (CwSidetoneGenerator) now starts correctly as soon as AetherSDR connects to the radio. A bug in the AudioEngine initialization order prevented the stream from starting until the applet was interacted with manually (#2105).

## Changes in v0.9.7
### Compression gauge gated on transmit state

The **Compression** gauge now reads 0 dB whenever the radio is not transmitting. Previously the gauge could show a stale non-zero reading during receive because it was driven directly by meter flow regardless of transmit state. Starting in v0.9.7 the gauge is gated on the radio's interlock TRANSMITTING state (and requires the speech processor to be enabled): it only shows a live compression value while the radio is actually transmitting. This change is handled via the `updateCompression()` slot, which is independent of the mic level path.

### Breakin now fully honors the radio's break_in setting

The **Breakin** toggle now correctly controls QSK behavior end-to-end. In earlier versions, an internal auto-PTT envelope caused the keying path to force TX regardless of the **Breakin** setting, which masked Breakin OFF and eliminated QSK hang time. That envelope has been removed. The behavior is now:

- **Breakin ON (QSK):** key edges trigger TX immediately; the break-in delay set by the **Delay (CW)** slider holds the relay after the last element.
- **Breakin OFF:** keyed characters are queued; the operator engages PTT manually to transmit.

### RADE mode support

When RADE mode is active, the **Mic gain** slider and **Level** gauge switch to client-side behavior:

- The **Mic gain** slider acts as a client-side RADE gain control and uses the `PcMicGain` setting, the same key used for the PC mic source. Slider changes are not sent to the radio as `mic_level` commands while RADE is active, preventing silent overwrite of the hardware mic setting.
- The **Level** gauge remains active during receive (RX) when RADE is active, mirroring the existing PC mic exception introduced in v0.9.3. This allows the gauge to show input level even when `met_in_rx` is off and the radio is not transmitting.
- When RADE deactivates, the slider reverts to showing the radio's `mic_level` value and the Level gauge is reset to −150 dBFS until the next transmit or `met_in_rx` event.

The `PcMicGain` setting is shared between the PC mic source path and the RADE path; both are client-authoritative with respect to the radio.

### Sidetone bus shared with Quindar tones

The sidetone audio bus is now shared with Quindar tones. The two are mutually exclusive at the mode level: Quindar tones are active only outside CW mode, and the CW sidetone generator is active only in CW mode. No user action is required; the applet manages the switch automatically when the active slice mode changes.

### Final brickwall limiter on TX path

A brickwall limiter (`ClientFinalLimiter`) is now always present at the very end of the TX audio path, after the user-configurable DSP chain and PC mic gain. No sample can exceed the configured ceiling regardless of upstream processing. Enable the limiter and set its ceiling in **Settings → Audio → TX Limiter** (`ClientFinalLimiter*` keys in AppSettings).

### TX test-tone generator

A sine-wave test-tone generator (`ClientTxTestTone`) is now available at the head of the TX path. When enabled, it overrides microphone input before the DSP chain runs. Use it for setup and calibration. Access it from **Settings → Audio → TX Test Tone**.

### Quindar tone generator

A Quindar tone generator is now included in the TX path (#2262). It sits after the user DSP chain and PC mic gain but before the final brickwall limiter, so the tone is unaffected by Compressor/EQ but is still bounded by the configured ceiling. The tone is driven automatically by the PTT coordinator on phone modes and is bypassed on CW and digital modes. No user configuration is required for the tone itself; the Quindar local monitor sink can be started and stopped via **Settings → Audio → Quindar**.

### Master TX bypass

A master **BYPASS** button is now available in both the docked Chain applet and the channel strip. Engaging bypass snapshots all currently-enabled TX DSP stages and disables them. Disengaging bypass restores only the stages that were enabled before bypass was engaged; any stages turned on manually while bypass was active are left on. The current bypass state is reflected by the `txBypassChanged` signal.

### Waveform scope shows actual transmitted envelope

The strip's **Waveform CE-SSB** panel now listens to a post-chain scope feed (`txPostChainScopeReady`) that taps the audio stream after the user DSP chain, PC mic gain, and the final brickwall limiter — the exact int16 data packetised into VITA-49 and sent to the radio. Previously the scope tapped an earlier point in the chain and could not reflect limiter action.

### saveClientReverbSettings emits clientReverbStateChanged

`saveClientReverbSettings()` now emits `clientReverbStateChanged()` after persisting reverb parameters. UI surfaces bound to the reverb (strip panel, docked applet, floating editor) update from this single notification instead of polling on a timer. No user action is required.

### Compression gauge gated on transmit state

The **Compression** gauge now reads 0 dB whenever the radio is not transmitting. Previously the gauge could show a stale non-zero reading during receive because it was driven directly by meter flow regardless of transmit state. Starting in v0.9.7 the gauge is gated on the radio's interlock TRANSMITTING state (and requires the speech processor to be enabled): it only shows a live compression value while the radio is actually transmitting. This change is handled via the `updateCompression()` slot, which is independent of the mic level path.

### Breakin now fully honors the radio's break_in setting

The **Breakin** toggle now correctly controls QSK behavior end-to-end. In earlier versions, an internal auto-PTT envelope caused the keying path to force TX regardless of the **Breakin** setting, which masked Breakin OFF and eliminated QSK hang time. That envelope has been removed. The behavior is now:

- **Breakin ON (QSK):** key edges trigger TX immediately; the break-in delay set by the **Delay (CW)** slider holds the relay after the last element.
- **Breakin OFF:** keyed characters are queued; the operator engages PTT manually to transmit.

### RADE mode support

When RADE mode is active, the **Mic gain** slider and **Level** gauge switch to client-side behavior:

- The **Mic gain** slider acts as a client-side RADE gain control and uses the `PcMicGain` setting, the same key used for the PC mic source. Slider changes are not sent to the radio as `mic_level` commands while RADE is active, preventing silent overwrite of the hardware mic setting.
- The **Level** gauge remains active during receive (RX) when RADE is active, mirroring the existing PC mic exception introduced in v0.9.3. This allows the gauge to show input level even when `met_in_rx` is off and the radio is not transmitting.
- When RADE deactivates, the slider reverts to showing the radio's `mic_level` value and the Level gauge is reset to −150 dBFS until the next transmit or `met_in_rx` event.

The `PcMicGain` setting is shared between the PC mic source path and the RADE path; both are client-authoritative with respect to the radio.

### Sidetone bus shared with Quindar tones

The sidetone audio bus is now shared with Quindar tones. The two are mutually exclusive at the mode level: Quindar tones are active only outside CW mode, and the CW sidetone generator is active only in CW mode. No user action is required; the applet manages the switch automatically when the active slice mode changes.

## Related

- [Pick a mic source (MIC, BAL, LINE, ACC, PC)](pick-a-mic-source-mic-bal-line-acc-pc.md)
- [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md)
- [Enable speech processor at NOR, DX, or DX+ level](enable-speech-processor-at-nor-dx-or-dx-level.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
