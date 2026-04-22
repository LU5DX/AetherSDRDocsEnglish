# Switch between multiple slices using the A..H tab row

The RX Controls applet can be bound to any active slice on the radio. Use the slice tab row to move between slices A through H without leaving the applet.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The slice tab row is not shown when the radio reports only one slice.
- At least two slices must already exist on the radio. Create additional slices from the panadapter before using this procedure. See [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md).

## Steps

1. Open the RX Controls applet. If it is not visible, click the **RX** tray button on the right sidebar.
2. Locate the slice tab row at the top of the applet. It contains one button per active slice, labelled **A**, **B**, **C**, and so on, up to **H**.
3. Click the letter tab for the slice you want to control. The applet immediately rebinds to that slice.
4. Confirm the change: the **Slice badge** in the header row updates to show the selected letter, coloured by slice identity.

## What each control does

| Control | Behavior | Default | Valid range | Setting key |
|---|---|---|---|---|
| Slice tabs (A..H) | Selects which slice the RX applet is bound to. | — | 1–8 buttons, capped by the radio's maximum slice count | — |
| Slice badge | Displays the letter of the currently bound slice. | A | A / B / C / D / E / F / G / H | — |

## Tips

- The tab row is hidden entirely when the radio's maximum slice count is 1. It appears automatically once a second slice is created.
- Each tab letter is coloured by slice identity, matching the slice badge and panadapter markers, making it easy to identify slices at a glance.
- Switching tabs does not affect which slice is the TX slice. To change the TX slice, click the **TX (badge)** button in the applet header after switching tabs.

## Related

- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
- [RX Controls overview](overview.md)
- [Lock the slice to prevent accidental retuning](lock-the-slice-to-prevent-accidental-retuning.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
