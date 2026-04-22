# Set per-band TX max power and tune mode

This page explains how to set a radio-wide TX power cap and choose a tune mode in AetherSDR, and how to open the dedicated per-band TX power and tune settings for the FLEX-8600.

## Before you start

- The radio must be connected. `Settings > Radio Setup...` is unavailable without an active radio connection.
- Know the maximum power level you want to allow, in percent (0–100 %).

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **TX** tab.
3. To set a radio-wide power cap, adjust **Max Power:** to the desired value (0–100 %).
4. To change how the tune button behaves, select the desired option from the **Tune Mode:** drop-down.
5. To configure power and tune settings on a per-band basis, click **TX Band Settings**. This opens the dedicated per-band TX power and tune dialog.

   Alternatively, open the per-band dialog directly via `Settings > TX Band Settings...`.

## What each control does

| Control | Kind | Valid range | Behavior |
|---|---|---|---|
| **Max Power:** | Spinbox | 0–100 % | Sets a radio-level TX power cap that applies across all bands. |
| **Tune Mode:** | Combo box | Modes listed in the drop-down | Selects how the tune button behaves when activated. |
| **TX Band Settings** | Button | — | Opens the per-band dialog where you can set TX power, tune power, inhibit settings, and external amp control for each individual band. |
| **Show TX in Waterfall:** | Toggle button | — | When enabled, draws the TX signal in the waterfall display during transmission. |
| **TX Follows Active Slice / Active Slice Follows TX** | Button | — | Mutually exclusive modes controlling whether the TX follows the active slice or the active slice follows TX. |

## Tips

- **Max Power:** applies at the radio level across all bands. Use the per-band dialog (opened via **TX Band Settings**) to impose finer limits on individual bands.
- The `Settings > TX Band Settings...` menu item opens the per-band dialog directly without going through the Radio Setup dialog.

## Related

- [Radio Setup overview](overview.md)
- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)
