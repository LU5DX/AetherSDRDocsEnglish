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

| Control                                                       | Default                                                                                                                  | Setting key                                                                                                        |
|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| **Spot Lines:**                                               | Enabled                                                                                                                  | `IsSpotsLinesEnabled`                                                                                              |
| Auto:                                                         | Automatically switch slice mode when clicking a spot that includes mode info (e.g. CW, FT8, RTTY).                       | Setting key changed from SpotsAutoMode to SpotAutoSwitchMode in v26.5.1.                                           |
| Signals (Signal History)                                      | Gold markers for detected voice-width signals on the panadapter.                                                         | New in v26.5.1 (#2426). Same toggle as View > Signal History Markers.                                              |
| QRM (Signal History)                                          | Red markers for persistent carriers and wideband interference.                                                           | New in v26.5.1 (#2426). Same toggle as View > QRM History Markers.                                                 |
| Clear All                                                     | Clears all DX spots, memory feed, Signal History markers and QRM markers from the spectrum.                              |                                                                                                                    |
| Spot text color picker                                        | Opens QColorDialog to pick spot text color.                                                                              |                                                                                                                    |
| Override Background: Enabled                                  | Enables custom spot background color.                                                                                    |                                                                                                                    |
| Override Background: Auto                                     | Auto-picks background color for contrast.                                                                                |                                                                                                                    |
| Spot background color picker                                  | Opens QColorDialog for spot background color.                                                                            |                                                                                                                    |
| Total Spots:                                                  | Live count of spots currently tracked across all sources.                                                                |                                                                                                                    |
| DXCC Coloring (section)                                       | Section header for DXCC coloring controls in the left column below the divider.                                          |                                                                                                                    |
| DXCC Colors:                                                  | Colors spots by worked/confirmed/needed DXCC status.                                                                     | Setting key changed from DxccColoringEnabled to IsDxccColoringEnabled in v26.5.1.                                  |
| Imported: (DXCC stats)                                        | Shows QSO count and entity count when a log is loaded.                                                                   | Format: '<N> QSOs / <M> entities'.                                                                                 |
| DXCC Color swatches (New DXCC / New Band / New Mode / Worked) | Opens a color picker for each DXCC status category.                                                                      | New in v26.5.1 -- replaces previous fixed DXCC color scheme.                                                       |
| Signal History (section)                                      | Section header for Signal History tunables in the right column below the divider.                                        | New in v26.5.1 (#2506). Consolidates S-History marker lifetime, QRM gate, edge threshold, colors and snap-to-step. |
| Marker Lifetime:                                              | How long an inactive Signal History marker persists before being removed.                                                | New in v26.5.1. Default 60 s.                                                                                      |
| QRM Gate:                                                     | How long a narrow carrier or wideband signal must persist before being classified as QRM.                                | New in v26.5.1. Default 6 s.                                                                                       |
| Edge Threshold:                                               | Threshold above noise floor for the slope edge walk that refines the S-History carrier-side edge.                        | New in v26.5.1. Lower = closer to carrier but more noise-sensitive. Default 3.0 dB.                                |
| Signal History color swatches (Signals / QRM)                 | Opens a color picker for the voice signal markers (gold) and QRM markers (red).                                          | New in v26.5.1.                                                                                                    |
| Snap to Step:                                                 | Rounds S-History click-to-tune to the nearest multiple of the active slice's step size, hiding the small carrier offset. | New in v26.5.1. Default Disabled.                                                                                  |
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
