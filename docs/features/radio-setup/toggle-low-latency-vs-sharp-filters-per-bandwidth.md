# Toggle low-latency vs sharp filters per bandwidth

The Filters tab lets you choose between low-latency and sharp filter families for each bandwidth, and optionally force low-latency filters when operating digital modes.

## Before you start

- AetherSDR must be connected to the radio. The Filters tab is unavailable when no radio is connected.
- Open Radio Setup via `Settings > Radio Setup...`.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **Filters** tab.
3. Click **Low Latency / Sharp Filters** to toggle between the two filter families for the current bandwidth. The button state reflects which family is active.
4. To force low-latency filters whenever you are operating DIGU or DIGL, check **Use Low Latency Filters for Digital Modes**.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Low Latency / Sharp Filters** | Toggle button | Switches the filter family between low-latency and sharp for each bandwidth setting. |
| **Use Low Latency Filters for Digital Modes** | Checkbox | When checked, low-latency filters are applied automatically in DIGU and DIGL regardless of the global toggle. |

## Tips

- Low-latency filters reduce processing delay at the cost of steeper skirt selectivity. Sharp filters improve adjacent-signal rejection but add latency. For CW contesting or weak-signal work, sharp filters are generally preferable. For digital mode decoding where timing matters, low-latency filters may reduce decode errors.
- The **Use Low Latency Filters for Digital Modes** checkbox acts independently of the per-bandwidth toggle, so you can run sharp filters on SSB and CW while digital modes automatically switch to low-latency.

## Related

- [Radio Setup overview](overview.md)
