# Toggle low-latency vs sharp filters per bandwidth

The Filters tab in Radio Setup lets you choose between low-latency and sharp DSP filters for each receive bandwidth, and optionally force low-latency filters in digital modes. Use low-latency filters when you need minimal processing delay; use sharp filters when you need tighter stopband rejection.

## Before you start

- AetherSDR must be connected to the radio. The Filters tab is not accessible without an active radio connection.
- Open Radio Setup via `Settings > Radio Setup...`.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **Filters** tab.
3. For each bandwidth entry, click the **Low Latency / Sharp Filters** toggle button to switch between the two filter families. The button reflects the current selection for that bandwidth.
4. If you operate digital modes (DIGU/DIGL) and want low-latency filters applied automatically, check **Use Low Latency Filters for Digital Modes**.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Low Latency / Sharp Filters** | Toggle button | Switches the filter-family preference between low-latency and sharp for the associated bandwidth. |
| **Use Low Latency Filters for Digital Modes** | Checkbox | When checked, forces low-latency filters whenever the slice is in DIGU or DIGL mode, regardless of the per-bandwidth setting. |

## Tips

- Sharp filters have steeper skirts and better adjacent-signal rejection, which benefits crowded SSB and CW operation. Low-latency filters reduce group delay, which benefits digital mode decoders that are sensitive to processing latency.
- The **Use Low Latency Filters for Digital Modes** checkbox acts as an override: even if a bandwidth is set to sharp, digital mode slices will use low-latency filters when this option is checked.

## Related

- [Radio Setup overview](overview.md)
- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
