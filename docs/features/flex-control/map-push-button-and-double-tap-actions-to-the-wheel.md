# Map push-button and double-tap actions to the wheel

Configure what happens when you push (single-tap) or double-tap the physical FlexControl wheel or the virtual wheel in the AetherControl dialog.

## Before you start

- Open the AetherControl dialog: **Settings > AetherControl...**
- If using a physical FlexControl, ensure it is connected (see [Configure the AetherControl / FlexControl hardware controller](configure-the-aethercontrol-flexcontrol-hardware-controller.md)).

## Steps

1. In the AetherControl dialog, locate the **Push (action)** combo box near the wheel display.
2. Click the combo box and select an action from the list.
3. In the **Double-tap (action)** combo box directly below, select a second action.
4. Close the dialog. The new actions take effect immediately.

## What each control does

| Control | Default | Setting key | Behavior |
|---------|---------|-------------|----------|
| Push (action) combo box | – | `FlexControlButtonAction_*` | Selects the action triggered by a single push of the wheel. Options include: Tune Slice, Band Zoom, Segment Zoom, RIT, XIT, Master Volume, Headphone Volume, AGCT, APF, Clear RIT, Clear XIT, Toggle APF, Change Active Slice, Split Active Slice, MOX, RF Power, CW Speed, CWX Macros 1-12, Step Up, Step Down, Toggle Tune, Toggle Mute, Toggle Lock, Previous Slice, Toggle AGC, Slice AF Up, Slice AF Down, and None. |
| Double-tap (action) combo box | – | – | Selects the action triggered by two quick pushes of the wheel. Same action options as Push. |

Both combo boxes share the same list of available actions. See the source snippet for the complete list of `FlexActionDef` entries, which include all labels shown above.

## Related

- [Configure single- and double-tap actions for the PUSH button](configure-single-and-double-tap-actions-for-the-push-button.md)
