# Toggle Low-Latency vs Sharp Filters per Bandwidth

Use this page to switch the radio's DSP filter family between low-latency and sharp response, and to force low-latency filters for digital modes. Low-latency filters reduce processing delay at the cost of steeper rolloff; sharp filters maximise adjacent-signal rejection.

## Before you start

- AetherSDR must be connected to the radio. The Filters tab is not accessible when disconnected.
- Open Radio Setup via `Settings > Radio Setup...`.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **Filters** tab.
3. Click **Low Latency / Sharp Filters** to toggle between the two filter families. The button reflects the current selection.
4. If you want low-latency filters applied automatically whenever a slice is in DIGU or DIGL mode, check **Use Low Latency Filters for Digital Modes**.

## What each control does

| Control | Kind | Behavior | Default | Setting key |
|---|---|---|---|---|
| **Low Latency / Sharp Filters** | Toggle button | Switches the filter family applied to all receive slices — low-latency (less delay) or sharp (steeper skirts). | — | — |
| **Use Low Latency Filters for Digital Modes** | Checkbox | When checked, overrides the filter family selection and uses low-latency filters whenever a slice is in a digital mode (DIGU/DIGL). | — | — |

## Related

- [Radio Setup overview](overview.md)
