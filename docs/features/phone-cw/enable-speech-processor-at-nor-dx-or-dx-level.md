# Enable speech processor at NOR, DX, or DX+ level

Use the speech processor to apply compression to your transmitted audio. Three levels are available: NOR (normal), DX (moderate compression), and DX+ (maximum compression).

## Before you start

- AetherSDR must be connected to the radio. The Phone/CW applet is only active when a radio connection is established.
- The active slice must be in a phone mode (SSB, AM, FM). The Phone panel is hidden when the slice is in CW mode.

## Steps

1. Open the Phone/CW applet. If the Phone panel is not visible in the Applet Panel, click the **P/CW** tray button on the right sidebar.
2. Click **PROC** to enable the speech processor. The button highlights green when active.
3. Drag the **NOR/DX/DX+** slider to select the processor level:
   - Position 0: **NOR** — normal, light compression.
   - Position 1: **DX** — moderate compression.
   - Position 2: **DX+** — maximum compression.
4. Watch the **Compression** gauge to confirm the processor is applying gain reduction. The gauge fills from right to left; a reading between −25 dB and 0 dB indicates active compression.

## What each control does

| Control | Kind | Default | Valid range | Persisted setting |
|---|---|---|---|---|
| **PROC** | Toggle button | Off | On / Off | — |
| **NOR/DX/DX+** | Slider | 0 (NOR) | 0 (NOR), 1 (DX), 2 (DX+) | — |
| **Compression** | Meter (read-only) | — | −25 to 0 dB (reversed fill) | — |

## Tips

- The **Compression** gauge only shows meaningful readings while you are transmitting. At other times the reading will be near 0 dB.
- Increasing the **NOR/DX/DX+** slider without enabling **PROC** has no effect. Enable **PROC** first.
- Adjust **Mic gain** before increasing the processor level. Excessive mic gain into the processor can produce distortion. The **Level** gauge shows microphone peak level in dBFS; aim to keep peaks below 0 dBFS (red zone) on voice peaks.

## Troubleshooting

- **Compression gauge shows no activity while transmitting** — Confirm **PROC** is checked (button is highlighted). If the mic source is **PC**, verify the `PcMicGain` value is not set to 0; the radio does not report mic level for PC source, so the slider value is kept client-side only.
- **PROC button is not visible** — The Phone panel is only shown when the active slice is in a phone mode. If the slice is in CW mode, the CW panel is displayed instead. Switch the slice to SSB, AM, or FM to access PROC.

## Related

- [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md)
- [Pick a mic source (MIC, BAL, LINE, ACC, PC)](pick-a-mic-source-mic-bal-line-acc-pc.md)
- [Select a mic profile for a specific microphone](select-a-mic-profile-for-a-specific-microphone.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
