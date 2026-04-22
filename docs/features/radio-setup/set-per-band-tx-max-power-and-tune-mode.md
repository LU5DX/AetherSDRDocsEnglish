# Set per-band TX max power and tune mode

This page explains how to set a global TX power cap and choose the tune mode for your FLEX-8600, then open the per-band power and tune table to configure each band individually.

## Before you start

- AetherSDR must be connected to the radio. These controls are not available while disconnected.
- Know which bands you want to limit and what maximum power level (as a percentage) you need.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **TX** tab.
3. To set a radio-wide power cap, adjust **Max Power:** to the desired value (0–100 %).
4. To change how the tune button behaves, select the desired mode from the **Tune Mode:** drop-down.
5. To configure power and tune settings on a per-band basis, click **TX Band Settings**. This opens the dedicated per-band power and tune dialog.
6. In the per-band dialog, set the power and tune parameters for each band as needed.
7. Close the dialog when finished. Settings are applied to the radio immediately.

Alternatively, you can open the per-band dialog directly from the menu without going through Radio Setup: use `Settings > TX Band Settings...`.

## What each control does

| Control | Kind | Valid range | Behavior |
|---|---|---|---|
| **Max Power:** | Spinbox | 0–100 % | Sets a radio-level TX power cap that applies across all slices. |
| **Tune Mode:** | Combo box | See radio options | Selects how the tune button behaves when activated. |
| **TX Band Settings** | Push button | — | Opens the per-band power and tune dialog where you can set TX power, tune power, inhibit settings, and external amp control for each band individually. |
| **Show TX in Waterfall:** | Toggle button | On / Off | Draws the TX signal in the waterfall display while transmitting. |
| **TX Follows Active Slice / Active Slice Follows TX** | Push button | Mutually exclusive | Controls whether the TX follows the active slice or the active slice follows TX. |

## Tips

- **Max Power:** is a radio-level cap. It does not replace per-band limits set in the TX Band Settings dialog; both apply.
- If you only need to adjust a single band quickly, use `Settings > TX Band Settings...` to skip the Radio Setup dialog entirely.

## Related

- [Radio Setup overview](overview.md)
- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)
