# Set per-band TX max power and tune mode

This page explains how to set the maximum transmit power and tune mode for each amateur band on your FLEX-8600. Use these settings to protect amplifiers, satisfy band-specific power limits, or configure how the Tune function behaves.

## Before you start

- AetherSDR must be connected to the radio. These controls are unavailable without an active radio connection.
- Identify which bands you want to configure before opening the dialog.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **TX** tab.
3. To set a radio-level power cap that applies across all bands, adjust **Max Power:** to a value between 0 and 100 %.
4. To select how the Tune button behaves, choose an option from the **Tune Mode:** drop-down.
5. To open per-band power and tune settings, click **TX Band Settings**. This opens the dedicated per-band dialog where you can adjust TX power, tune power, inhibit settings, and external amp control for each band individually.
6. Alternatively, open the per-band dialog directly via `Settings > TX Band Settings...` without going through Radio Setup.
7. Close the dialog when done. Settings are applied immediately to the radio.

## What each control does

| Control | Kind | Valid range | Behavior |
|---|---|---|---|
| **Max Power:** | Spinbox | 0–100 % | Sets a radio-level TX power cap that limits output across all bands. |
| **Tune Mode:** | Drop-down | Options depend on radio firmware | Selects how the Tune button behaves when activated. |
| **TX Band Settings** | Button | — | Opens the per-band TX power, tune power, inhibit, and amp control dialog. |
| **Show TX in Waterfall:** | Toggle | On / Off | Draws the TX signal in the waterfall display during transmit. |
| **TX Follows Active Slice / Active Slice Follows TX** | Button | Mutually exclusive | Controls whether the TX follows the active slice or the active slice follows TX. |

## Tips

- The **Max Power:** spinbox on the TX tab is a global cap. Per-band limits set in the TX Band Settings dialog operate within that ceiling.
- You can reach the same TX Band Settings dialog from `Settings > TX Band Settings...` without opening Radio Setup first.
- Use **Inhibit during TUNE** (available under the `Settings` menu) to suppress specific TX outputs — ACC TX, TX1, TX2, or TX3 — during tuning.

## Related

- [Radio Setup overview](overview.md)
- [Assign a USB cable as CAT, BCD, bit or PTT](assign-a-usb-cable-as-cat-bcd-bit-or-ptt.md)
