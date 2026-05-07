# Widen or narrow the filter using the mode-correct shortcut (all modes, including LSB/CWL/DIGL/RTTY)

Use the widen/narrow shortcut to step through per-mode filter width presets — one press widens the filter, the other narrows it. The shortcut always applies filter widths appropriate to the current slice mode, so you never get a CW-width filter in SSB or a broadcast-width filter in RTTY.

## Before you start

- A radio must be connected.
- The RX Controls applet must be visible (tray button **RX** on the right sidebar).

## Steps

1. In the RX Controls applet, click the **Mode combo** and select the mode you intend to use (USB, LSB, CW, AM, SAM, DIGU, DIGL, RTTY, FM, etc.). The filter preset list and step sizes update for that mode.
2. Click the left-pointing triangle button (◀) next to the filter width indicator to narrow the filter, or the right-pointing triangle button (▶) to widen it.

Each click moves through the mode’s preset list. The current filter width is shown on the **2.7K** (filter width) indicator.

## What each control does

| Control | Default | Behavior | Notes |
|---------|---------|----------|-------|
| **Filter width presets (◀ / ▶)** | See below | Steps through per-mode filter widths in descending (◀) or ascending (▶) order. | The `stepFilterWidth(direction)` method walks the per-mode preset list for mode-correct widen/narrow (#2208). |
| **2.7K (filter width)** | Mode-dependent | Displays the current slice filter bandwidth. | Updates when a preset is applied. The readout is shared with the VFO panel and uses mode-aware formatting (#2197). |

## Filter width presets by mode

| Mode | Presets (Hz) |
|------|-------------|
| USB, LSB | 1800, 2100, 2400, 2700, 2900, 3300 |
| AM, SAM | 5600, 6000, 8000, 10000, 12000, 14000 |
| CW | 50, 100, 250, 400 |
| DIGU, DIGL | 100, 300, 600, 1000, 1500, 2000 |
| RTTY | 250, 300, 350, 400, 500, 1000 |
| FM, NFM, DFM | No filter presets (buttons hidden) |

## Related

- [Pick a filter width preset for the current mode](pick-a-filter-width-preset-for-the-current-mode.md)
- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
