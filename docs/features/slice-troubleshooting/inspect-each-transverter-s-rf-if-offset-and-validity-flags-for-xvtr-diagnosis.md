# Inspect each transverter's RF/IF, offset and validity flags for XVTR diagnosis

The Slice Troubleshooting dialog captures a snapshot of every transverter configured on your FLEX-8600 and displays its RF frequency, IF frequency, frequency offset, and validity flags. Use this when a transverter-based slice is misbehaving — wrong frequency, missing reception, or unexpected mode — and you need to confirm what the radio actually reports for each XVTR entry.

## Before you start

- AetherSDR must be connected to the radio. The dialog requires an active radio connection.
- Any transverters you want to inspect must already be configured on the FLEX-8600.

## Steps

1. Click `Help > Slice Troubleshooting...` to open the Slice Troubleshooting dialog.
2. Click the `Issue Summary` tab. Scan the bullet list for any XVTR validity warnings. The summary flags entries where `is_valid` is false or `has_is_valid` is false.
3. Click the `JSON` tab to see the full snapshot. Locate the transverter entries in the JSON. Each XVTR entry reports the following fields:
   - `name` — the label assigned to the transverter
   - `index` and `order` — position identifiers
   - `rf_freq_mhz` — the RF (over-the-air) frequency in MHz
   - `if_freq_mhz` — the IF (radio input) frequency in MHz
   - `offset_mhz` — the difference applied between IF and RF, in MHz
   - `is_valid` — whether the transverter entry is marked valid (`Yes` / `No`)
   - `has_is_valid` — whether the radio reported a validity flag at all (`Yes` / `No`)
   - `rx_only` — whether the entry is receive-only
   - `max_power` — maximum power in the XVTR entry
4. If you made changes to transverter settings after opening the dialog, click `Refresh Snapshot` to re-read the current state from the radio before drawing any conclusions.
5. To share the findings, click `Copy Summary` to copy the plain-language issue list to the clipboard, `Copy JSON` to copy the full JSON, or `Export JSON...` to save the JSON to a file.
6. Click `Close` when finished.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| `Issue Summary` tab | Tab | Plain-language bullet list of detected problems, including XVTR validity issues. |
| `JSON` tab | Tab | Full JSON snapshot containing all transverter entries with RF, IF, offset, and validity fields. |
| `Refresh Snapshot` | Button | Re-reads slice and transverter state from the radio into the snapshot. |
| `Copy Summary` | Button | Copies the issue summary to the clipboard. |
| `Copy JSON` | Button | Copies the full JSON snapshot to the clipboard. |
| `Export JSON...` | Button | Saves the full JSON snapshot to a file. |
| `Close` | Button | Closes the dialog. |

## Tips

- If `has_is_valid` is `No` for a transverter, the radio did not report a validity flag for that entry at all. This is distinct from `is_valid` being `No`, which means the radio reported the entry as explicitly invalid.
- Click `Refresh Snapshot` after adjusting transverter settings in SmartSDR or on the radio before re-reading the values. The snapshot is not updated automatically.
- The `offset_mhz` field should equal `rf_freq_mhz` minus `if_freq_mhz`. If it does not match your transverter configuration, that discrepancy is a likely cause of frequency errors on the slice.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
