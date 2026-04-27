# Toggle low-latency vs sharp filters per bandwidth

The Filters tab in Radio Setup lets you choose between low-latency and sharp DSP filters for each receive bandwidth, and optionally force low-latency filters when using digital modes.

## Before you start

- AetherSDR must be connected to the radio. The Filters tab is only available when a radio connection is active.
- Open Radio Setup via `Settings > Radio Setup...`.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **Filters** tab.
3. Click the **Low Latency / Sharp Filters** toggle button to switch between the two filter families for the current bandwidth. The button reflects the active selection.
4. To force low-latency filters whenever a digital mode (DIGU or DIGL) is active, check **Use Low Latency Filters for Digital Modes**.
5. Close the dialog. Settings take effect immediately.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Low Latency / Sharp Filters** | Toggle button | Switches the filter-family preference between low-latency and sharp filters for the selected bandwidth. |
| **Use Low Latency Filters for Digital Modes** | Checkbox | When checked, overrides the per-bandwidth filter choice and uses low-latency filters whenever a DIGU or DIGL slice is active. |

## Tips

- Low-latency filters reduce processing delay, which benefits real-time digital mode decoding and CW. Sharp filters provide steeper skirt selectivity, which is more useful for crowded SSB conditions.
- The **Use Low Latency Filters for Digital Modes** checkbox applies across all bandwidths, so you do not need to toggle the per-bandwidth setting each time you switch to a digital mode.

## Related

- [Radio Setup overview](overview.md)
- [Select iambic mode A or B for the radio keyer](select-iambic-mode-a-or-b-for-the-radio-keyer.md)
