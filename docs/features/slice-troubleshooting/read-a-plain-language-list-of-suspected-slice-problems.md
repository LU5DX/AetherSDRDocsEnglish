# Read a plain-language list of suspected slice problems

The Slice Troubleshooting dialog inspects your current slice, panadapter, transverter, and DAX channel state and presents a plain-language summary of detected problems. Use it when audio is missing, a slice behaves unexpectedly, or you want a quick sanity check before contacting support.

## Before you start

- AetherSDR must be connected to the radio. The dialog requires an active radio connection.

## Steps

1. Click `Help > Slice Troubleshooting...`.
2. The dialog opens. The **Issue Summary** tab is shown by default.
3. Read the bullet list of detected problems. Each bullet describes a specific suspected issue such as missing audio, a stuck mute, a missing antenna assignment, or an XVTR validity problem.
4. If the list does not reflect recent changes you made to slice state, click **Refresh Snapshot** to re-read the current state from the radio.
5. Click **Close** when finished.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Issue Summary** (tab) | Tab | Displays a plain-language bullet list of detected problems. |
| **JSON** (tab) | Tab | Displays the full JSON snapshot of slices and DAX channels. |
| **Refresh Snapshot** | Button | Re-reads slice state into the snapshot. Use this after changing slice configuration. |
| **Copy Summary** | Button | Copies the issue summary text to the clipboard. |
| **Copy JSON** | Button | Copies the full JSON snapshot to the clipboard. |
| **Export JSON...** | Button | Saves the JSON snapshot to a file. |
| **Close** | Button | Closes the dialog. |
| Status label | Indicator | Shows the result of the last copy or export action (for example, `Copied to clipboard`). |

## Tips

- If no problems are found, the **Issue Summary** tab will be empty or show no bullets. Switch to the **JSON** tab to inspect raw slice state if you need to dig deeper.
- After changing a slice setting — such as unmuting or reassigning an antenna — click **Refresh Snapshot** before re-reading the summary. The dialog does not update automatically.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Inspect each transverter's RF/IF, offset and validity flags for XVTR diagnosis](inspect-each-transverter-s-rf-if-offset-and-validity-flags-for-xvtr-diagnosis.md)
