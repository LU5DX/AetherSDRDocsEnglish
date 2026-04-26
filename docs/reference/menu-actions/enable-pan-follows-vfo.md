# Enable Pan Follows VFO

`View > Pan Follows VFO` controls whether the panadapter automatically scrolls to keep the active VFO frequency visible when you tune outside the current view.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio so that the panadapter is active.

## Steps

1. Click `View` in the menu bar.
2. Click `Pan Follows VFO` to toggle the checkmark.
   - Checkmark present: the panadapter pans automatically to keep the VFO in view.
   - Checkmark absent: the panadapter stays fixed; the VFO can move outside the visible span without the view following.

## What each control does

| Control | Default | Behavior |
|---|---|---|
| `Pan Follows VFO` | On (checked) | When enabled, the panadapter scrolls whenever the VFO frequency moves outside the current display span. When disabled, the panadapter does not move regardless of VFO position. |

## Tips

- If you prefer to scroll the panadapter manually and tune by clicking within the displayed span, disable `Pan Follows VFO` and enable `View > Single-Click to Tune` so clicks retune the VFO without moving the panadapter center.

## Related

- [Enable Single-Click to Tune](enable-single-click-to-tune.md)
