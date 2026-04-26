# Understanding Slices and VFOs

A slice is a independent receive (and optionally transmit) channel within a single panadapter. Understanding how slices map to VFOs is the foundation for using AetherSDR effectively, whether you are monitoring one frequency or running split operation across several bands simultaneously.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. Slices are created and managed by the radio firmware; they do not exist without a live connection.
- The RX Controls applet (RX tray button in the right sidebar) must be visible to interact with slice controls.

## What a slice is

The FLEX-8600 supports up to eight simultaneous slices, labelled A through H. Each slice is an independently tunable receive channel with its own:

- VFO frequency (shown in the **Frequency label** in the RX Controls applet)
- Mode (USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, RTTY)
- Filter passband
- AGC, AF gain, squelch, RIT, and XIT settings
- RX and TX antenna assignment

Each slice is bound to a panadapter. The panadapter's **Slice title** indicator (e.g. "Slice A") shows which slice owns that display.

## What the VFO is

Within AetherSDR, the term VFO refers to the tuned frequency of a slice. There is no separate VFO A / VFO B concept at the application level; instead, each lettered slice carries its own frequency. Working "split" means designating one slice as the TX slice (using the **TX (badge)** button) while receiving on another.

The current frequency for the active slice is displayed in the **Frequency label** in the RX Controls applet. Click the label to enter edit mode (**Frequency edit**), type a frequency in MHz, and press Enter to tune.

## Switching between slices

When the radio has more than one slice active, a row of tabs labelled **A**, **B**, **C**, and so on appears at the top of the RX Controls applet. Click a tab to bind the applet to that slice. The **Slice badge** (coloured letter in the applet) confirms which slice is currently shown.

In the panadapter, each slice appears as its own overlay on the spectrum. The **Slice title** in each panadapter title bar identifies the associated slice. In multi-pan layouts you can click the **Spectrum / waterfall** area of a panadapter to activate it.

## Designating the TX slice

Only one slice transmits at a time. Click the **TX (badge)** button in the RX Controls applet for the slice you want to transmit on. This sets that slice as the TX slice. To work split, tune one slice to the transmit frequency and click its **TX (badge)**, then return to the receiving slice using the tab row.

## Locking a slice

To prevent a slice from being retuned accidentally, click the **🔓 / 🔒** toggle button in the RX Controls applet. The icon changes to a closed padlock when tune-lock is active. A locked slice ignores all frequency change requests.

## What each control does

| Control | Description | Default | Valid range |
|---|---|---|---|
| Slice tabs (A..H) | Selects which slice the RX Controls applet is bound to. | — | 1–8 tabs, capped by hardware |
| Slice badge | Displays the letter of the currently active slice. | A | A–H |
| 🔓 / 🔒 | Toggles tune-lock; locked slice ignores frequency changes. | 🔓 (unlocked) | — |
| Frequency label | Displays current VFO frequency with dotted grouping. | 0.000.000 | — |
| Frequency edit | Type a frequency in MHz and press Enter to tune. | — | 0.001–54.000 MHz (up to 450.000 MHz on XVTR) |
| TX (badge) | Sets this slice as the TX slice. | — | — |
| Slice title (panadapter) | Shows which slice is bound to the panadapter. | Slice A | Slice A–Slice H |

## Tips

- The slice tab row is hidden when only one slice is active (maximum slices ≤ 1).
- Double-click the **L / R pan** slider to reset it to centre (50) for any slice.
- RIT and XIT offsets are per-slice. Zero them with **RIT 0** and **XIT 0** before switching operating tasks.

## Related

- [Switch between multiple slices using the A..H tab row](../../features/rx/switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Lock the slice to prevent accidental retuning](../../features/rx/lock-the-slice-to-prevent-accidental-retuning.md)
- [Tune the radio to a frequency (type MHz in the readout)](../../features/rx/tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Click the spectrum to activate a panadapter (multi-slice mode)](../../features/panadapter/click-the-spectrum-to-activate-a-panadapter-multi-slice-mode.md)
- [Use RIT to offset the receive frequency for a drifting station](../../features/rx/use-rit-to-offset-the-receive-frequency-for-a-drifting-station.md)
- [Use XIT to offset the transmit frequency without changing RX](../../features/rx/use-xit-to-offset-the-transmit-frequency-without-changing-rx.md)
- [Make your first QSO with AetherSDR](../tutorials/first-qso.md)
- [Understanding the AetherSDR applet panel](understanding-applets.md)
