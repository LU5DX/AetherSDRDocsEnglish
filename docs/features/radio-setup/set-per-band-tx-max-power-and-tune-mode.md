# Set per-band TX max power and tune mode

Use this page to cap transmit power and select tune mode for each amateur band on your FLEX-8600. These settings let you protect amplifiers, antennas, or band-specific hardware from over-power conditions.

## Before you start

- AetherSDR must be connected to the radio. The TX (tab) and TX Band Settings dialog are only available with an active radio connection.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **TX** tab.
3. To set a radio-level power cap that applies across all bands, adjust **Max Power:** (0–100 %).
4. To select how the tune button behaves, choose an option from the **Tune Mode:** drop-down.
5. To configure power and tune settings per band, click **TX Band Settings**. This opens the dedicated per-band power and tune dialog.
6. In the TX Band Settings dialog, locate the band row you want to adjust and set the power and tune values for that band.
7. Close the TX Band Settings dialog when done, then close Radio Setup.

Alternatively, open the per-band dialog directly via `Settings > TX Band Settings...`.

## What each control does

| Control | Kind | Valid range | Behavior |
|---|---|---|---|
| **Max Power:** | Spinbox | 0–100 % | Sets a radio-level TX power cap applied across all bands. |
| **Tune Mode:** | Combo box | Options set by radio firmware | Selects how the tune button behaves when activated. |
| **TX Band Settings** | Button | — | Opens the per-band power and tune dialog. |
| **Show TX in Waterfall:** | Toggle | — | Draws the TX signal in the waterfall display. |
| **TX Follows Active Slice / Active Slice Follows TX** | Button | Mutually exclusive | Controls whether the TX follows the active slice or the active slice follows TX. |

## Tips

- **Max Power:** on the TX tab is a global cap. Per-band limits set in TX Band Settings operate within that cap.
- You can reach TX Band Settings without opening Radio Setup by using `Settings > TX Band Settings...` directly from the menu.

## Related

- [Radio Setup overview](overview.md)
- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)
