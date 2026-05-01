# Enable speech processor at NOR, DX, or DX+ level

Turn on the FLEX-8600's built-in speech processor and choose how aggressively it compresses your transmitted audio. NOR gives mild compression; DX and DX+ increase processing for weaker-signal contacts.

## Before you start

- AetherSDR must be connected to the radio.
- The active slice must be in a phone mode (USB, LSB, AM, etc.). The Phone/CW applet shows Phone controls only when the active slice is not in CW mode.
- Open the Phone/CW applet by clicking the **P/CW** tray button on the right sidebar if it is not already visible.

## Steps

1. In the Phone/CW applet, click **PROC** to enable the speech processor. The button lights green when active.
2. Drag the **NOR/DX/DX+** slider to the desired compression level:
   - Position 0 — **NOR** (normal, least compression)
   - Position 1 — **DX**
   - Position 2 — **DX+** (most compression)
3. Watch the **Compression** gauge. The reversed fill shows how many dB of compression is being applied (range: −25 to 0 dB). Keep the reading out of the far left to avoid over-processing.
4. Watch the **Level** gauge to confirm microphone input is reaching the processor. The range is −40 to +10 dBFS; the meter goes red above 0 dBFS.
5. To disable the processor, click **PROC** again. The button returns to its unlit state.

## What each control does

| Control         | Kind          | Default |
|-----------------|---------------|---------|
| **PROC**        | Toggle button | Off     |
| **NOR/DX/DX+**  | Slider        | 0 (NOR) |
| **Level**       | Meter         | —       |
| **Compression** | Meter         | —       |

## Tips

- Set your mic gain before enabling the processor. A healthy **Level** reading before enabling **PROC** gives the processor useful signal to work with. See [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md).
- Start at **NOR** and move to **DX** or **DX+** only if signal reports warrant it. Heavy processing on strong signals sounds distorted to the receiving station.
- The **Compression** gauge reads 0 dB (no fill) when **PROC** is off or no audio is present.

## Troubleshooting

- **PROC button is not visible** — The applet is showing the CW panel. The Phone panel, including **PROC**, appears only when the active slice is in a phone mode, not CW.
- **Compression gauge shows 0 dB with PROC on** — The radio is not receiving audio from the selected mic source. Check the **Level** gauge and the **Mic source** setting. If **Mic source** is **PC**, the radio always reports mic level as 0; use the **Level** gauge in the applet instead.
- **NOR/DX/DX+ slider snaps back** — The slider has three valid positions (0, 1, 2). Dragging between snap points causes it to land on the nearest integer; this is expected behavior.
- **Level gauge does not appear on connect** — If **Mic source** is **PC**, the **Level** gauge now appears immediately on connect without requiring a transmit or `met_in_rx` to be active (v0.9.3, fix #2086). If the gauge is still absent, verify that **Mic source** is set to **PC** and that AetherSDR has finished connecting to the radio.
- **Phone panel does not refresh when VOX is toggled by keyboard shortcut** — This was resolved in v0.9.3 (#2084). Update to v0.9.3 or later if the Phone panel fails to update immediately when VOX is toggled via a keyboard shortcut.

## CW sidetone behavior (v0.9.1 and later)

The **Sidetone** toggle and **Sidetone volume** slider in the CW panel control both the radio's DAX-fed monitor and the client-side low-latency sidetone generator in lockstep. There is no longer a separate **Local STn** button, separate local volume slider, or **Follow** pitch toggle. Those controls have been removed.

- Enabling **Sidetone** turns on both the radio-side monitor and the client-side generator simultaneously.
- Adjusting **Sidetone volume** sets both `mon_gain_cw` on the radio and the local generator volume to the same value.
- Pitch and stereo pan always follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically. No manual override or follow toggle is needed.
- On Windows, the sidetone audio stream now starts immediately on connect rather than requiring a manual action (v0.9.3, fix #2105).

If you have settings from a previous version that reference `CwLocalSidetoneEnabled`, `CwLocalSidetoneVolume`, `CwLocalSidetonePitchFollow`, or `CwLocalSidetonePitchHz`, those keys are no longer read or written by AetherSDR and can be ignored.

## Level gauge behavior (v0.9.3)

When **Mic source** is set to **PC**, the **Level** gauge uses client-side metering and is not suppressed by the radio's `met_in_rx` flag. The gauge appears immediately on connect and shows the PC microphone input level whether or not the radio is transmitting. For all other mic sources, the gauge is suppressed to −150 dBFS when `met_in_rx` is off and the radio is not transmitting.

## NRL noise reduction availability (v0.9.4)

The NRL (noise reduction, row 4) DSP mode is now available on 6000-series radios as well as 8000-series radios. In previous releases, NRL was hidden unless the connected radio reported extended DSP firmware. It now remains visible regardless of firmware capability. NRS (row 5), RNN (row 6), and NRF (row 8) continue to require 8000-series firmware and are hidden on other hardware (#2177).

## SWR sweep controls (v0.9.4)

The ANT panel in the Spectrum Overlay Menu includes two new buttons and a power slider for running an SWR sweep across the current TX band.

| Control              | Kind          | Range  | Default | Description                                                                                     |
|----------------------|---------------|--------|---------|-------------------------------------------------------------------------------------------------|
| **Start Sweep**      | Button        | —      | —       | Runs a low-power tune sweep across the current TX band and plots SWR on the panadapter.         |
| **Clear Sweep**      | Button        | —      | —       | Removes the SWR sweep trace from the panadapter display.                                        |
| **PWR** (sweep power) | Slider       | 1–10 W | 1 W     | Sets the carrier power level used during the sweep. Adjust before clicking **Start Sweep**.     |

To run a sweep:

1. Open the Spectrum Overlay Menu and select the **ANT** panel.
2. Set the desired sweep carrier power with the **PWR** slider. The current wattage is shown to the right of the slider.
3. Click **Start Sweep**. The panel closes and the sweep runs; the result is plotted on the panadapter.
4. Click **Clear Sweep** to remove the trace when finished.

The **PWR** slider value is kept in sync if the sweep power is changed from another source (for example, a connected controller).

## Related

- [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md)
- [Pick a mic source (MIC, BAL, LINE, ACC, PC)](pick-a-mic-source-mic-bal-line-acc-pc.md)
- [Select a mic profile for a specific microphone](select-a-mic-profile-for-a-specific-microphone.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)