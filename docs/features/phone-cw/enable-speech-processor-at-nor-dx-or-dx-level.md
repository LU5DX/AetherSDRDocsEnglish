# Enable speech processor at NOR, DX, or DX+ level

Use the Phone/CW applet to switch on the speech processor and choose how aggressively it compresses your transmit audio. Higher levels increase average power on voice peaks, which can improve copy in difficult conditions.

## Before you start

- AetherSDR must be connected to the radio. The Phone/CW applet is only active with a radio connection.
- The active slice must be in a phone mode (SSB, AM, FM). In CW mode the applet switches to the CW panel and the processor controls are not shown.

## Steps

1. Locate the Phone/CW applet in the Applet Panel (right sidebar). If it is not visible, click the **P/CW** tray button on the right sidebar to show it.
2. In the row containing **PROC**, click **PROC** to enable the speech processor. The button lights green when active.
3. Move the **NOR/DX/DX+** slider to the desired level:
   - Position 0 (left): **NOR** — normal compression
   - Position 1 (center): **DX** — moderate compression
   - Position 2 (right): **DX+** — maximum compression
4. Watch the **Compression** gauge to confirm the processor is applying compression. The gauge fills from right to left; a reading further left indicates more compression.

## What each control does

| Control | Kind | Default | Valid range | Persisted key |
|---|---|---|---|---|
| **PROC** | Toggle button | Off | On / Off | — |
| **NOR/DX/DX+** | Slider | 0 (NOR) | 0 (NOR), 1 (DX), 2 (DX+) | — |
| **Compression** | Meter (read-only) | — | −25 to 0 dB (reversed fill) | — |
| **Level** | Meter (read-only) | — | −40 to +10 dBFS (red above 0) | — |

## Tips

- The **Compression** gauge uses reversed fill: the bar grows from right to left as compression increases. A bar reaching the left edge indicates heavy limiting.
- The **Level** gauge shows microphone peak in dBFS. Keep peaks below 0 dBFS (the red region starts above 0) before enabling heavy compression; driving the processor with an overloaded input produces distortion rather than louder average audio.
- If **Mic source** is set to **PC**, the mic gain value is stored client-side as `PcMicGain` (default 50, range 0–100) because the radio always reports a level of 0 for that source. Adjust **Mic gain** before increasing processor level to set a clean input.

## Troubleshooting

- **PROC button is not visible** — The active slice is in a CW mode. Switch the slice to a phone mode; the applet will show the Phone panel.
- **Compression gauge shows 0 dB with PROC on** — The processor is enabled but receiving little or no input signal. Confirm **Mic source** and **Mic gain** are set correctly, and that the radio is transmitting.
- **No change in signal quality between NOR, DX, and DX+** — Verify PROC is checked (lit green). Moving the **NOR/DX/DX+** slider has no effect when PROC is off.

## Related

- [Phone/CW overview](overview.md)
- [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md)
- [Pick a mic source (MIC, BAL, LINE, ACC, PC)](pick-a-mic-source-mic-bal-line-acc-pc.md)
- [Select a mic profile for a specific microphone](select-a-mic-profile-for-a-specific-microphone.md)
