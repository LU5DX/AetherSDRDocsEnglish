# Toggle low-latency vs sharp filters per bandwidth

Use this page to switch between low-latency and sharp filter families for each receive bandwidth, and to force low-latency filters when operating digital modes. Choosing the right filter family trades off audio delay against filter skirt steepness.

## Before you start

- AetherSDR must be connected to the radio. The Filters tab is not accessible without an active radio connection.
- Open Radio Setup by clicking `Settings > Radio Setup...`.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **Filters** tab.
3. For each bandwidth you want to change, click **Low Latency / Sharp Filters** to toggle between the two filter families. The button reflects the current state for that bandwidth.
4. To force low-latency filters whenever a digital mode (DIGU or DIGL) is active, check **Use Low Latency Filters for Digital Modes**.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Low Latency / Sharp Filters** | Toggle button | Switches the filter family for the selected bandwidth between low-latency and sharp. Low-latency filters reduce processing delay; sharp filters provide steeper skirts with more delay. |
| **Use Low Latency Filters for Digital Modes** | Checkbox | When checked, low-latency filters are applied automatically for DIGU and DIGL slices regardless of the per-bandwidth setting. |

## Tips

- Use sharp filters for SSB or CW work where adjacent-channel rejection matters more than delay.
- Use low-latency filters when operating digital modes that depend on timing-sensitive decoding, or enable **Use Low Latency Filters for Digital Modes** to have this applied automatically.

## Related

- [Radio Setup overview](overview.md)
