# Enable Inhibit during TUNE

Use `Settings > Inhibit during TUNE` to select which TX outputs the FLEX-8600 suppresses while the tuner is running. This prevents RF from reaching amplifiers or antenna ports that should not be keyed during a tune cycle.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- Confirm which TX output ports are in use at your station before changing these settings.

## Steps

1. Click `Settings` in the menu bar.
2. Hover over `Inhibit during TUNE` to open the submenu.
3. Click any combination of the following checkboxes to enable inhibit on those outputs during tuning:
   - `None`
   - `ACC TX`
   - `TX1`
   - `TX2`
   - `TX3`

   A checkmark next to an item means that output will be suppressed during a tune cycle. Selecting `None` indicates no outputs are inhibited.

## What each control does

| Checkbox | Effect when checked |
|----------|---------------------|
| `None` | No TX outputs are suppressed during tuning. |
| `ACC TX` | Suppresses the ACC TX output during tuning. |
| `TX1` | Suppresses the TX1 output during tuning. |
| `TX2` | Suppresses the TX2 output during tuning. |
| `TX3` | Suppresses the TX3 output during tuning. |

## Tips

- You can check multiple outputs simultaneously. For example, checking `TX1` and `TX2` inhibits both ports while leaving `TX3` active.
- Per-band inhibit settings are available in `Settings > TX Band Settings...`, which provides finer control over inhibit behavior by band.

## Related

- [Configuring AetherSDR Controls](configuring-aethersdr-controls.md)
