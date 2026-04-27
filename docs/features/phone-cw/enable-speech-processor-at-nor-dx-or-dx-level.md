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

| Control | Kind | Default | Range | Persisted key |
|---|---|---|---|---|
| **PROC** | Toggle button | Off | On / Off | — |
| **NOR/DX/DX+** | Slider | 0 (NOR) | 0 = NOR, 1 = DX, 2 = DX+ | — |
| **Level** | Meter | — | −40 to +10 dBFS (red above 0) | — |
| **Compression** | Meter | — | −25 to 0 dB (reversed fill) | — |

## Tips

- Set your mic gain before enabling the processor. A healthy **Level** reading before enabling **PROC** gives the processor useful signal to work with. See [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md).
- Start at **NOR** and move to **DX** or **DX+** only if signal reports warrant it. Heavy processing on strong signals sounds distorted to the receiving station.
- The **Compression** gauge reads 0 dB (no fill) when **PROC** is off or no audio is present.

## Troubleshooting

- **PROC button is not visible** — The applet is showing the CW panel. The Phone panel, including **PROC**, appears only when the active slice is in a phone mode, not CW.
- **Compression gauge shows 0 dB with PROC on** — The radio is not receiving audio from the selected mic source. Check the **Level** gauge and the **Mic source** setting. If **Mic source** is **PC**, the radio always reports mic level as 0; use the **Level** gauge in the applet instead.
- **NOR/DX/DX+ slider snaps back** — The slider has three valid positions (0, 1, 2). Dragging between snap points causes it to land on the nearest integer; this is expected behavior.

## Related

- [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md)
- [Pick a mic source (MIC, BAL, LINE, ACC, PC)](pick-a-mic-source-mic-bal-line-acc-pc.md)
- [Select a mic profile for a specific microphone](select-a-mic-profile-for-a-specific-microphone.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
