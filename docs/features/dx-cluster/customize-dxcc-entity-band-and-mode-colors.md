# Customize DXCC entity, band and mode colors

After loading an ADIF log for DXCC coloring, you can assign separate spot colors for needed DXCC entities, new bands on worked entities, new modes on worked entities, and already-worked entities. This helps you spot the rarest openings at a glance.

## Before you start

- You have an ADIF log file ready (from your logger or from a previous export).
- DXCC Coloring is enabled. See [Enable DXCC coloring from an ADIF log](enable-dxcc-coloring-from-an-adif-log.md).

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **Display** tab.
3. If DXCC Coloring is not already on, click the **DXCC Colors:** toggle button to enable it.
4. Click **Log File (ADIF):** and select your ADIF file. The app loads the log and shows a count like `<N> QSOs / <M> entities`.
5. Locate the four **DXCC Color** swatch buttons under the **DXCC Coloring** section.
6. Click a swatch to open a color picker:
   - **New DXCC** – spots for entities not confirmed in your log.
   - **New Band** – spots for an entity you have worked, but on a band you have not.
   - **New Mode** – spots for an entity/band combination that is worked, but not on this mode.
   - **Worked** – spots for entities, bands, and modes already confirmed.
7. Pick a color and close the picker. Spots on the panadapter update immediately.

## What each control does

| Control | Setting key | Behavior |
|---------|-------------|----------|
| **DXCC Colors:** toggle | `IsDxccColoringEnabled` | Enables or disables all DXCC coloring. |
| **Log File (ADIF):** | `DxccAdifFilePath` | Opens a file dialog to select an ADIF log. The file is watched for changes and reloaded automatically. |
| **Imported:** indicator | none | Shows `N QSOs / M entities` when a log is loaded; shows `(no log loaded)` otherwise. |
| **New DXCC** color swatch | `DxccColorNewEntity` | Color for spots whose DXCC entity is not yet confirmed in the log. |
| **New Band** color swatch | `DxccColorNewBand` | Color for spots of a worked entity on a band not yet confirmed. |
| **New Mode** color swatch | `DxccColorNewMode` | Color for spots of a worked entity and band on a mode not yet confirmed. |
| **Worked** color swatch | `DxccColorWorked` | Color for spots already confirmed in the log. |

## Tips

- The ADIF file is watched for changes automatically — there is no separate "reload" button. If your logger updates the file, AetherSDR picks up the changes on the next file modification event.
- DXCC coloring overrides the per-source spot colors you may have set on the Cluster, RBN, WSJT-X, or other tabs. To use per-source colors instead, turn **DXCC Colors:** off.

## Troubleshooting

- **Colors don't change on the panadapter** — Make sure a log file is loaded (check the **Imported:** indicator shows a count, not `(no log loaded)`). Also verify the **DXCC Colors:** toggle is enabled (shows a green fill).
- **Spots all show the same color** — Confirm your ADIF file contains valid QSO records with DXCC entity information. Only contacts that include a valid entity, band, and mode are used for comparison.

## Related

- [Enable DXCC coloring from an ADIF log](enable-dxcc-coloring-from-an-adif-log.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)