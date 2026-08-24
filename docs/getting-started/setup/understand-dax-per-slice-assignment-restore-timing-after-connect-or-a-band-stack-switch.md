# Understand DAX per-slice assignment restore timing after connect or a band-stack switch

This page explains when AetherSDR restores your DAX channel-to-slice assignments after connecting to a radio or switching bands in a band stack, so you know what to expect and can verify routing is correct.

## Before you start

- DAX must be enabled (the Enable button in the DAX Audio applet shows "Enabled")
- You are connected to a FLEX-8600 radio

## Steps

1. Open the DAX Audio applet by clicking the **DAX** tray button on the right sidebar.
2. Connect to your radio or switch to a different band-stack entry.
3. Observe the per-channel status labels (DAX 1 through DAX 8) and the TX status label.
4. Immediately after connect or band-stack switch, these labels may show "—" for a brief moment before populating with slice letters such as "Slice A" or "Slice B".
5. Wait for the labels to settle. The restore happens as the radio propagates slice state to AetherSDR; it is not instant.

## What each control does

| Control | Default | Valid range | Persisted setting key |
|---|---|---|---|
| **DAX Enable** button | off | on/off | `AutoStartDAX` |
| **DAX 1–8 gain+meter** | 0.5 | 0.0–1.0 | `DaxRxGain1` … `DaxRxGain8` |
| **TX gain+meter** | 0.5 | 0.0–1.0 | `DaxTxGain` |
| **DAX 1–8 assignment status** | "—" | "—" or "Slice A"…"Slice H" | `DaxChannel_Slice{letter}` |
| **TX assignment status** | "—" | "—" or "Slice A"…"Slice H" | (radio-reported) |

## Tips

- The per-channel status labels are updated whenever a slice's DAX channel changes. After a band-stack switch, slices may be recreated, so assignments are re-propagated and the labels briefly reset to "—" before repopulating.
- If you have many slices, give the radio a second or two to push all slice state before relying on the displayed assignments for routing audio to digital software.

## Troubleshooting

- **DAX channel status labels stay "—" after connect** — DAX may not be enabled yet. Click **Enable** in the DAX Audio applet; assignments only populate while the DAX bridge is running.
- **Assignments appear but audio is on the wrong channel** — Check that you are looking at the correct slice letter in the status label, and verify the DAX channel routing in your digital software matches what AetherSDR displays.

## Related

- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](../../features/dax/enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [See which slice is currently using each DAX channel](../../features/dax/see-which-slice-is-currently-using-each-dax-channel.md)
- [Identify which slice is the TX slice](../../features/dax/identify-which-slice-is-the-tx-slice.md)
