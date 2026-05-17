# TX Band Settings overview

The TX Band Settings dialog lets you view and configure per-band transmit parameters on your FLEX-8600, including power limits, tune power, inhibit settings, and external amplifier control. Use this page to tailor TX behavior for each amateur radio band.

## Before you start

- A FLEX-8600 radio must be connected and powered on.
- The application must have an active radio connection.

## How it works

The TX Band Settings dialog opens a tabbed interface showing one tab per band. Each tab contains transmit configuration controls specific to that band:

- **Power limits** – Set the maximum power output (in watts) for the selected band. Adjustable from 0 W up to the radio’s maximum.
- **Tune power** – Set the power level used during tune operations. Typically lower than the main power limit to avoid overdriving the antenna.
- **Band enable/disable** – Toggle whether the band is available for transmit. Disabling a band prevents accidental transmission outside allowed frequencies.
- **Inhibit settings** – Control which TX outputs (ACC TX, TX1, TX2, TX3) are suppressed during tuning. Configured via the menu `Settings > Inhibit during TUNE`.
- **External amplifier control** – Configure relay and keying outputs for external amplifiers per band.

The dialog is also accessible from the main menu: **`Settings > TX Band Settings...`**

## What each control does

| Control | Purpose | Default | Valid range | Setting key |
|---|---|---|---|---|
| Per-band settings (tab) | Shows transmit configuration for a single band, including power limits, enable/disable toggles, and inhibit options. | (none) | (varies by control inside tab) | (none) |
| Band Enable checkbox | Enables or disables TX on the selected band. Unchecked = TX inhibited. | (enabled) | On/Off | (per-band key internal to radio) |
| Power Limit slider/input | Sets maximum TX power for the band. | (varies by band) | 0 – radio max (W) | (per-band key internal to radio) |
| Tune Power slider/input | Sets power used during tuning. | (varies) | 0 – radio max (W) | (per-band key internal to radio) |

## Tips

- Use band enable/disable to prevent accidental transmission on bands where you don’t have a license or antenna.
- The **Inhibit during TUNE** menu lets you suppress specific TX outputs (ACC TX, TX1, TX2, TX3) while tuning — useful to avoid keying an amplifier during tune cycles.
- Changes made in the TX Band Settings are sent directly to the radio; no separate “Save” button is needed.

## Related

- [Radio Setup...](radio-setup-dialog.md)
- [Inhibit during TUNE](inhibit-during-tune.md)
