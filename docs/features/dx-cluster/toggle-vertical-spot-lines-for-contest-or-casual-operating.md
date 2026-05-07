# Toggle vertical spot lines for contest or casual operating

By default, AetherSDR draws a vertical line from the spectrum baseline up to each spot label on the panadapter. This page explains how to turn those lines off — useful during contests when the display becomes cluttered — and how to turn them back on for casual operating.

## Before you start

- At least one spot source (DX cluster, RBN, WSJT-X, POTA, SpotCollector, or FreeDV) must be configured and delivering spots, or the effect of the change will not be visible.
- The master spot overlay must be on (`IsSpotsEnabled` set to Enabled). If spots are off, spot lines have no visible effect.

## Steps

There are two ways to reach the "Spot Lines:" toggle. Use whichever is more convenient.

**Via SpotHub:**

1. Click `Settings > SpotHub...`.
2. Click the **Display** tab.
3. Click **Spot Lines:** to toggle it. The button shows **Enabled** (lines drawn) or **Disabled** (lines hidden). The change takes effect immediately.

**Via Spot Settings:**

1. Right-click the panadapter spot overlay to open the context menu and select the spot settings option, which opens the **Spot Settings** window.
2. Click **Spot Lines:** to toggle it. The button shows **Enabled** or **Disabled**. The change takes effect immediately.

## What each control does

| Control         | Default | Setting key           |
|-----------------|---------|-----------------------|
| **Spot Lines:** | Enabled | `IsSpotsLinesEnabled` |
## Tips

- Disable **Spot Lines:** before a contest session. With dozens or hundreds of spots on screen, removing the lines significantly reduces visual noise.
- Re-enable **Spot Lines:** for casual DXing or band-scanning, where the lines help you identify exactly which signal each label corresponds to.
- The setting is persisted immediately; there is no Save button to click.

## Related

- [Turn spots on or off](../spot-settings/turn-spots-on-or-off.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Clear all spots from the panadapter](clear-all-spots-from-the-panadapter.md)
- [SpotHub overview](overview.md)
- [Spot Settings overview](../spot-settings/overview.md)
