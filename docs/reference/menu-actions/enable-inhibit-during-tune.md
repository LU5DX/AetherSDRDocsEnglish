# Enable Inhibit during TUNE

Use `Settings > Inhibit during TUNE` to select which TX output lines the FLEX-8600 suppresses while the tuner is running. This prevents RF from reaching amplifiers or antenna switches that should not receive tuning power.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- Identify which TX output connectors on your radio are wired to equipment you want to protect during tuning.

## Steps

1. Click `Settings` in the menu bar.
2. Hover over `Inhibit during TUNE` to open the submenu.
3. Click one or more checkboxes from the list to enable inhibit on those outputs:
   - `None` — no outputs are suppressed during tuning.
   - `ACC TX` — suppresses the ACC TX line.
   - `TX1` — suppresses the TX1 output.
   - `TX2` — suppresses the TX2 output.
   - `TX3` — suppresses the TX3 output.
4. Repeat for each output you want inhibited. Selections are independent checkboxes; you may enable any combination.

## What each control does

| Checkbox | Effect during TUNE |
|---|---|
| `None` | No outputs are inhibited. Tuning RF passes through all configured TX lines. |
| `ACC TX` | The ACC TX control line is held inactive while the tuner runs. |
| `TX1` | TX1 output is suppressed while the tuner runs. |
| `TX2` | TX2 output is suppressed while the tuner runs. |
| `TX3` | TX3 output is suppressed while the tuner runs. |

## Tips

- If you use an external amplifier on TX1, check `TX1` to prevent tuning power from reaching it while the internal tuner steps through frequencies.
- `None` and the individual output checkboxes can interact: if `None` is the only selection, all outputs remain active. Checking any specific output overrides that for that line.
- Per-band inhibit settings are available in `Settings > TX Band Settings...`, which offers finer control at the band level.

## Related

- [Configuring AetherSDR Controls](configuring-aethersdr-controls.md)
- [USB Cables](usb-cables.md)
