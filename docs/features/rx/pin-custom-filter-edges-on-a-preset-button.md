# Pin custom filter edges on a preset button

Use the filter width preset buttons to save exact lo/hi passband edges for the current mode, so every click of that preset restores your precise boundaries rather than a generic width.

## Steps

1. Right-click the **Filter width presets** button you want to customise (for example, the **2700 Hz** button in USB mode).
2. Choose **Set Custom Edges…** from the context menu.
3. In the dialog, enter the exact **lo** and **hi** values in Hz, then confirm.
4. Click that preset button to verify the **Filter width label** updates and the **Filter passband widget** moves to your pinned edges.

To revert, right-click the same preset button and choose **Reset to Default**.

## What each control does

| Control | Behavior |
|---|---|
| **Filter width presets** | Click to apply the preset filter width, or the pinned lo/hi edges if custom edges have been saved. Right-click to open a menu with **Set Custom Edges…** (enter exact lo/hi Hz) and **Reset to Default**. |
| **Filter passband widget** | Drag the lo/hi edges to adjust the filter passband interactively; emits `filterChanged(lo, hi)`. |
| **Filter width label** (2.7K) | Read-only indicator showing the current filter bandwidth; updates when any preset is applied. |

## Tips

- Custom edges are stored per mode (e.g. `FilterPresets_USB`, `FilterPresets_CW`). Pinning edges on a USB preset does not affect CW presets.
- A preset button stores either a plain width (e.g. `2700`) or a `lo:hi` pair (e.g. `-2700:0`) when custom edges are set. You can have some buttons use plain widths and others use pinned edges within the same mode.
- The **Filter passband widget** shows signed offsets — negative values appear for LSB and CW filters where the passband sits below the carrier. Use this to confirm your pinned edges landed on the correct side of the tuned frequency.
- Filter preset buttons are hidden in FM, NFM, and DFM modes; custom edge pinning applies only to SSB, CW, AM, SAM, DIG, and RTTY modes.

## Related

- [rx-applet.md](rx-applet.md)
- [filter-passband-widget.md](filter-passband-widget.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
