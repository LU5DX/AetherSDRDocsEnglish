# Inspect each transverter's RF/IF, offset and validity flags for XVTR diagnosis

The Slice Troubleshooting dialog captures a snapshot that includes a formatted entry for every transverter the radio reports. Use this to verify that a transverter's RF frequency, IF frequency, offset, and validity flags are what you expect — without needing to parse raw SmartSDR protocol output.

## Before you start

- AetherSDR must be connected to the radio. The dialog requires an active radio connection.
- At least one transverter must be configured on the FLEX-8600 for XVTR entries to appear in the snapshot.

## Steps

1. Click `Help > Slice Troubleshooting...` to open the Slice Troubleshooting dialog.
2. Click the `JSON (tab)` tab to view the full snapshot, or click the `Issue Summary (tab)` tab for a plain-language summary that flags XVTR validity problems.
3. Locate the transverter entries in the output. Each transverter is reported in the format:

   ```
   - `<name>` idx `<index>`, order `<order>`, RF `<rf_freq_mhz> MHz`, IF `<if_freq_mhz> MHz`, offset `<offset_mhz> MHz`, valid `<Yes/No>`, has is_valid `<Yes/No>`, rx only `<Yes/No>`, max power `<max_power>`
   ```

4. Check the `valid` field. If it shows `No`, the transverter is not considered valid by the radio. Check the `has is_valid` field — if that also shows `No`, the radio has not yet reported a validity state for that transverter.
5. Verify the `RF`, `IF`, and `offset` values match your transverter's configuration.
6. If you changed transverter settings in the radio after opening the dialog, click `Refresh Snapshot` to re-read the current state.
7. To share the data with support, click `Copy JSON` to copy the full snapshot to the clipboard, or click `Export JSON...` to save it to a file. To copy only the issue summary, click `Copy Summary`.
8. Click `Close` when finished.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| `Issue Summary (tab)` | Tab | Shows a plain-language bullet list of detected problems, including XVTR validity issues. |
| `JSON (tab)` | Tab | Shows the full JSON snapshot, including all transverter entries with RF, IF, offset, and validity fields. |
| `Refresh Snapshot` | Button | Re-reads slice and transverter state from the radio into the snapshot. |
| `Copy Summary` | Button | Copies the issue summary text to the clipboard. |
| `Copy JSON` | Button | Copies the full JSON snapshot to the clipboard. |
| `Export JSON...` | Button | Saves the full JSON snapshot to a file. |
| `Close` | Button | Closes the dialog. |

## Tips

- The `has is_valid` field distinguishes between a transverter that is explicitly invalid and one whose validity state has simply not been received yet. If `has is_valid` is `No`, wait a moment and click `Refresh Snapshot` before drawing conclusions.
- The `offset` value is derived from the RF and IF frequencies. If the offset looks wrong, compare the `RF` and `IF` values against what is configured in the radio's transverter setup.
- The status label at the bottom of the dialog confirms the result of copy and export actions (for example, it will show `Copied to clipboard` after clicking `Copy JSON`).

## Related

- [Slice Troubleshooting overview](overview.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
