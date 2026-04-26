# Enable speech processor at NOR, DX, or DX+ level

Use the Phone/CW applet to switch on the speech processor and select how much compression the FLEX-8600 applies to your transmitted audio. NOR is normal processing, DX adds more compression, and DX+ applies the maximum.

## Before you start

- AetherSDR must be connected to the radio. The Phone/CW applet is only active when a radio connection is established.
- The active slice must be in a phone mode (SSB, AM, FM). The Phone panel is not shown when the slice is in CW mode.

## Steps

1. Click the **P/CW** tray button in the right sidebar to open the Phone/CW applet if it is not already visible.
2. Click **PROC** to enable the speech processor. The button lights green when active.
3. Drag the **NOR/DX/DX+** slider to the position that matches the desired compression level:
   - Position 0 (left): NOR — normal processing
   - Position 1 (center): DX — increased compression
   - Position 2 (right): DX+ — maximum compression
4. Watch the **Compression** gauge to confirm the amount of compression being applied. The gauge fills right-to-left and covers −25 to 0 dB.

## What each control does

| Control | Kind | Default | Valid range | Persisted key |
|---|---|---|---|---|
| **PROC** | Toggle button | Off | On / Off | — |
| **NOR/DX/DX+** | Slider | 0 (NOR) | 0 (NOR), 1 (DX), 2 (DX+) | — |
| **Compression** | Meter (read-only) | — | −25 to 0 dB (reversed fill) | — |
| **Level** | Meter (read-only) | — | −40 to +10 dBFS (red above 0) | — |

## Tips

- The **Compression** gauge shows compression in real time only while transmitting. Use it to verify that the processor is engaging and to avoid over-compression.
- The **Level** gauge shows microphone peak level in dBFS. Set mic gain before adjusting the processor level so the processor has a consistent signal to work with.
- The **NOR/DX/DX+** slider position is sent to the radio regardless of whether **PROC** is enabled, so you can pre-select the level before activating the processor.

## Troubleshooting

- **PROC button is visible but the Compression gauge never moves** — confirm the active slice is not in a CW mode; the Phone panel switches to the CW panel automatically when a CW mode is selected, hiding the processor controls.
- **Compression gauge reads 0 dB with PROC enabled** — the processor is active but receiving no input. Check the **Mic source** selection and the **Mic gain** slider. If the source is PC, note that the radio always reports mic level 0 for PC source; the gain is kept client-side in `PcMicGain`.

## Related

- [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md)
- [Pick a mic source (MIC, BAL, LINE, ACC, PC)](pick-a-mic-source-mic-bal-line-acc-pc.md)
- [Select a mic profile for a specific microphone](select-a-mic-profile-for-a-specific-microphone.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
