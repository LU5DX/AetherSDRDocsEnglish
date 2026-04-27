# Set per-band TX max power and tune mode

Use this page to cap transmit power on a per-band basis and choose how the Tune function behaves. These settings are stored on the radio and apply regardless of which client connects.

## Before you start

- AetherSDR must be connected to the radio. The TX tab is not accessible without an active connection.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **TX** tab.
3. Click **TX Band Settings** to open the dedicated per-band power and tune dialog.
4. In the per-band table, locate the band you want to configure.
5. Adjust the power limit for that band as needed. The valid range for **Max Power:** is 0–100 %.
6. To change tune behavior, select the desired option from the **Tune Mode:** combo box.
7. Close the dialog when done. Settings are applied immediately to the radio.

## What each control does

| Control | Kind | Valid range / options | Behavior |
|---|---|---|---|
| **TX Band Settings** | Button | — | Opens the dedicated per-band power and tune dialog. |
| **Max Power:** | Spin box | 0–100 % | Sets the radio-level TX power cap for the selected band. |
| **Tune Mode:** | Combo box | See radio firmware options | Selects how the Tune button behaves when activated. |
| **Show TX in Waterfall:** | Toggle button | Enabled / Disabled | Draws the TX signal in the waterfall display during transmit. |
| **TX Follows Active Slice / Active Slice Follows TX** | Button pair | Mutually exclusive | Controls whether the TX slice follows the active slice or vice versa. |

## Tips

- **TX Band Settings** is also accessible directly from `Settings > TX Band Settings...` without opening Radio Setup first.
- The **Max Power:** spin box on the TX tab sets a radio-level cap. Per-band limits set inside **TX Band Settings** operate on top of this cap.

## Related

- [Radio Setup overview](overview.md)
- [Upload a new firmware .ssdr to the radio](upload-a-new-firmware-ssdr-to-the-radio.md)
