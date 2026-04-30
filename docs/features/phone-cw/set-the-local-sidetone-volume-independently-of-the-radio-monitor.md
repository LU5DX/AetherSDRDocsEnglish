# Set the CW sidetone volume

In AetherSDR v0.9.2.1, the local client-side sidetone and the radio's DAX-fed sidetone monitor are controlled together by a single set of controls. The separate Local STn button, Local sidetone volume slider, Follow toggle, and Local sidetone pitch slider have been removed. The **Sidetone** toggle and **Sidetone volume** slider in the CW sub-panel now drive both the radio's monitor and the client-side low-latency sidetone generator (~10 ms latency) in lockstep. Pitch and pan always follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically.

## Before you start

- AetherSDR must be connected to the radio.
- The active slice must be in a CW mode. The Phone/CW applet automatically switches to the CW sub-panel when a CW mode is selected.

## Steps

1. Click the `P/CW` tray button in the right sidebar to open the Phone/CW applet.
2. Confirm the CW sub-panel is visible. If the active slice is in a CW mode, the panel switches to CW controls automatically.
3. Click **Sidetone** to enable sidetone monitoring. This enables both the radio's DAX-fed monitor and the client-side low-latency sidetone generator at the same time.
4. Drag the **Sidetone volume** slider left or right to set the desired level. The range is 0–100. Both the radio-side monitor level (`mon_gain_cw`) and the local sidetone generator volume change together.

## What each control does

| Control         | Default | Valid range           |
|-----------------|---------|-----------------------|
| Sidetone        | —       | On / Off              |
| Sidetone volume | —       | 0–100                 |
| L / R pan (CW)  | 50      | 0–100                 |
| Pitch < / >     | 600 Hz  | 100–6000 Hz (step 10) |

**Sidetone** — Toggles CW sidetone monitoring. When enabled, the radio's DAX-fed monitor and the client-side sidetone generator (~10 ms latency) are both active. When disabled, neither produces audio. On Windows, the sidetone stream starts immediately on connect (v0.9.3, #2105 — AudioEngine init order fix).

**Sidetone volume** — Sets the volume of both the radio monitor and the local sidetone generator with a single slider. There is no longer a separate volume control for each.

**L / R pan (CW)** — Sets the stereo pan position. The same pan value is applied to both the radio monitor and the local sidetone generator using constant-power panning. The pan always reflects the radio's `mon_pan_cw` setting. Double-click the slider to return it to center (50).

**Pitch < / >** — Steps the CW sidetone and decode pitch by 10 Hz per click. Pitch is always synchronized with the radio's `cw_pitch` setting and applies to both the radio monitor and the local sidetone generator automatically. No separate follow toggle or manual pitch slider is needed.

## Phone panel notes

**Level gauge** — Shows microphone input peak level in dBFS (range −40 to +10 dBFS; red above 0). The gauge is suppressed to −150 when `met_in_rx` is off and the radio is not transmitting, except when the mic source is set to **PC**: in that case the gauge uses client-side metering and appears immediately on connect regardless of the `met_in_rx` state (v0.9.3, #2086).

**VOX** — When VOX is toggled via a keyboard shortcut, the Phone panel now refreshes instantly to reflect the new state (v0.9.3, #2084).

## Tips

- Because the radio monitor and the local sidetone generator are now linked, you cannot set different volume levels for each. If you hear doubled or phased audio, confirm that your system audio output and the radio's DAX audio output are not both routed to the same speakers or headphones simultaneously.
- Local sidetone generation remains active for paddle, straight key, and CWX-generated transmissions whenever **Sidetone** is enabled.
- The approximately 10 ms local sidetone latency is unchanged. At higher WPM, this remains preferable to the radio's round-trip DAX latency.

## Related

- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)