# SpotHub Display tab reference

The Display tab in SpotHub controls how spot labels appear on the panadapter: how many stack vertically, where they sit, how large the text is, and how long each spot lives before it fades. It also includes Signal History marker controls and DXCC coloring options. Adjust these settings to reduce clutter on a busy band or make spots more readable on a small screen.

## Before you start

- AetherSDR must be running. A radio connection is not required to change these settings.
- At least one spot source (DX cluster, RBN, WSJT-X, SpotCollector, POTA, or FreeDV) should be active so you can see the effect of your changes in real time.
- The master spot overlay must be on. On the Display tab, confirm the **Spots:** toggle reads Enabled.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **Display** tab.
3. Confirm **Spots:** is set to Enabled. If it is not, click it to enable the overlay.
4. To show or hide memory-channel overlays on the panadapter, click **Memories:**.
5. To control how many spots stack vertically before they start overlapping, drag the **Levels:** slider. Higher values allow more rows of spot labels.
6. To move the spot labels up or down on the panadapter, drag the **Position:** slider.
7. To change the text size of spot labels, drag the **Font Size:** slider.
8. To set how long a spot remains visible before it disappears, drag the **Spot Lifetime:** slider. The value is in seconds.
9. **Auto:** is enabled by default. When on, AetherSDR automatically switches the slice mode when you click a spot that carries mode information (e.g. CW, FT8, RTTY). Click **Auto:** to toggle this behaviour.
10. To show or hide Signal History voice signal markers, click **Signals (Signal History):**.
11. To show or hide QRM markers, click **QRM (Signal History):**.
12. To clear all DX spots, memory feed, Signal History markers, and QRM markers from the spectrum, click **Clear All**.
13. To set the override color for all spots, click **Override Colors:** to enable, then click the color picker button next to it to choose a color.
14. To enable custom spot background colors, click **Override Background: Enabled**. To have the background color auto-picked for contrast, click **Override Background: Auto**.
15. To set background opacity, drag the **Background Opacity:** slider.
16. To show or hide the vertical lines drawn from the spectrum up to each spot label, click **Spot Lines:**. The button displays Enabled when the feature is on. Disable this during contests to reduce visual clutter.
17. To enable DXCC coloring, click **DXCC Colors:** and load an ADIF log file using **Log File (ADIF):**.
18. Click the color swatches under the DXCC Coloring section to choose colors for New DXCC, New Band, New Mode, and Worked statuses.
19. Adjust Signal History marker behaviour using the **Marker Lifetime:**, **QRM Gate:**, and **Edge Threshold:** sliders.
20. Click the color swatches under the Signal History section to choose colors for Signals and QRM markers.
21. Toggle **Snap to Step:** to round S-History click-to-tune to the nearest multiple of the active slice's step size.
22. Close the dialog. Changes take effect immediately.

## What each control does

| Control | Setting key | Behavior |
|---------|-------------|----------|
| **Spots:** | `IsSpotsEnabled` | Master toggle for the spot overlay on the panadapter. |
| **Memories:** | `IsMemorySpotsEnabled` | Toggles memory-channel overlay on panadapter. |
| **Auto:** | `SpotAutoSwitchMode` | Automatically switch slice mode when clicking a spot that includes mode info (e.g. CW, FT8, RTTY). Setting key changed from `SpotsAutoMode` in v26.5.1. |
| **Signals (Signal History)** | `SHistoryMarkersEnabled` | Gold markers for detected voice-width signals on the panadapter. New in v26.5.1. Same toggle as View > Signal History Markers. |
| **QRM (Signal History)** | `SHistoryQrmEnabled` | Red markers for persistent carriers and wideband interference. New in v26.5.1. Same toggle as View > QRM History Markers. |
| **Clear All** | — | Clears all DX spots, memory feed, Signal History markers and QRM markers from the spectrum. |
| **Levels:** | `SpotsMaxLevel` | Number of vertical stacking rows for spot labels. |
| **Position:** | `SpotsStartingHeightPercentage` | Vertical position of the spot label band on the panadapter. |
| **Font Size:** | `SpotFontSize` | Size of the text in each spot label. |
| **Spot Lifetime:** | `DxClusterSpotLifetimeSec` | Seconds a spot label remains visible before fading. |
| **Spot Lines:** | `IsSpotsLinesEnabled` | Draws vertical lines from the spectrum up to each spot label. Default: Enabled. Disable during contests to reduce visual clutter. |
| **Override Colors:** | `IsSpotsOverrideColorsEnabled` | Forces a single text color for all spots. The button always displays "Enabled" regardless of state. Pressing it toggles the feature on or off. |
| Spot text color picker | `SpotsOverrideColor` | Opens QColorDialog to pick spot text color. Default: `#FFFF00`. |
| **Override Background: Enabled** | `IsSpotsOverrideBackgroundColorsEnabled` | Enables custom spot background color. |
| **Override Background: Auto** | `IsSpotsOverrideToAutoBackgroundColorEnabled` | Auto-picks background color for contrast. |
| Spot background color picker | `SpotsOverrideBgColor` | Opens QColorDialog for spot background color. Default: `#000000`. |
| **Background Opacity:** | `SpotsBackgroundOpacity` | Opacity of the spot background color. |
| **Total Spots:** | — | Live count of spots currently tracked across all sources. |
| **DXCC Colors:** | `IsDxccColoringEnabled` | Colors spots by worked/confirmed/needed DXCC status. Setting key changed from `DxccColoringEnabled` in v26.5.1. The button always displays "Enabled" regardless of state. |
| **Log File (ADIF):** | `DxccAdifFilePath` | Loads an ADIF log file to drive DXCC coloring. Auto-watches the file for changes after selection. Setting key changed from `DxccAdifPath` in v26.5.1. |
| **Imported: (DXCC stats)** | — | Shows QSO count and entity count when a log is loaded. Format: `<N> QSOs / <M> entities`. |
| DXCC Color swatches (New DXCC / New Band / New Mode / Worked) | `DxccColorNewEntity`, `DxccColorNewBand`, `DxccColorNewMode`, `DxccColorWorked` | Opens a color picker for each DXCC status category. New in v26.5.1. |
| **Marker Lifetime:** | `SHistoryLifetimeS` | How long an inactive Signal History marker persists before being removed. Default 60 s. New in v26.5.1. |
| **QRM Gate:** | `SHistoryQrmGateS` | How long a narrow carrier or wideband signal must persist before being classified as QRM. Default 6 s. New in v26.5.1. |
| **Edge Threshold:** | `SHistorySoftEdgeDb` | Threshold above noise floor for the slope edge walk that refines the S-History carrier-side edge. Default 3.0 dB. New in v26.5.1. |
| Signal History color swatches (Signals / QRM) | `SHistoryColorSignals`, `SHistoryColorQrm` | Opens a color picker for the voice signal markers (gold) and QRM markers (red). New in v26.5.1. |
| **Snap to Step:** | `SHistorySnapToStep` | Rounds S-History click-to-tune to the nearest multiple of the active slice's step size, hiding the small carrier offset. Default Disabled. New in v26.5.1. The button always displays "Enabled" regardless of state. |

## Double-clicking a spot to tune

Double-clicking a row in the Spot List table tunes the active slice to the spot frequency. AetherSDR also forwards the mode extracted from the spot comment (for example CW, FT8, or SSB) so the slice mode switches automatically to match the spot, not only the frequency.

## Tips

- If spot labels overlap badly on a crowded band, increase **Levels:** to add more stacking rows, or decrease **Spot Lifetime:** so old spots clear sooner.
- Disable **Spot Lines:** during contests or on very busy bands to reduce visual clutter without hiding the spot labels themselves.
- WSJT-X spots have their own per-source lifetime setting (**Spot Life:** on the WSJT-X tab, stored as `WsjtxSpotLife`). The **Spot Lifetime:** slider on the Display tab applies to all other sources.
- When **Override Colors:** is disabled, each spot source uses its configured color from the source's tab.
- Signal History markers are independent of DX spots. Use **Clear All** to remove both simultaneously.
- The SpotHub dialog now uses theme-aware colors. Status indicators for connection state are styled with the current theme's accent, label, and danger colors instead of hardcoded values. This ensures consistent appearance with the rest of the application.
- Toggle buttons for **Override Colors:**, **Spot Lines:**, **DXCC Colors:**, and **Snap to Step:** always display "Enabled" regardless of their current state. The button's checked state (pressed or unpressed) indicates whether the feature is on or off.
- The Spot List tab's band-filter checkboxes use a flowing layout that wraps to new rows when the dialog is narrow, keeping each checkbox readable instead of compressing them horizontally. This avoids the illegible squashing that could occur in earlier versions.

## Troubleshooting

- **Spot labels are not visible at all** — Check that **Spots:** on the Display tab is set to Enabled (`IsSpotsEnabled`). Also confirm at least one spot source is connected and receiving spots.
- **Spot lines are not visible** — Check that **Spot Lines:** is set to Enabled. If the background is light, the lines may be difficult to see.
- **DXCC coloring is not working** — Confirm **DXCC Colors:** is enabled and that you have loaded an ADIF log file using **Log File (ADIF):**.
- **Signal History markers are not appearing** — Check that **Signals (Signal History):** or **QRM (Signal History):** is set to Enabled. These markers only appear when the radio is receiving signals.
- **Double-clicking a spot does not switch the slice mode** — Confirm **Auto:** is enabled. Also check that the spot comment contains a recognisable mode string. Mode extraction relies on the comment text supplied by the spot source; spots with no mode information in the comment will still tune the frequency but will not change the mode.

## Related

- [SpotHub overview](overview.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Clear all spots from the panadapter](clear-all-spots-from-the-panadapter.md)
- [Start WSJT-X UDP listener and filter for CQ, POTA or calls to me](start-wsjt-x-udp-listener-and-filter-for-cq-pota-or-calls-to-me.md)
- Edit startup commands for cluster sources
<!-- docmesh:llm version=V26.8.4 date=2026-08-01 -->