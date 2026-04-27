# Read a plain-language list of suspected slice problems

The Slice Troubleshooting dialog analyzes your current slice, panadapter, transverter, and DAX channel state and presents a plain-language summary of detected problems. Use this when you suspect a configuration issue — such as missing audio, a stuck mute, a missing antenna, or an invalid transverter — and want a quick diagnosis without reading raw data.

## Before you start

- AetherSDR must be connected to your FLEX-8600 radio. The dialog requires an active radio connection.

## Steps

1. Click `Help > Slice Troubleshooting...`.
2. Click the **Issue Summary** tab if it is not already selected.
3. Read the bullet list of detected problems.
4. If you have recently changed slice settings and want the list to reflect the current state, click **Refresh Snapshot**.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Issue Summary** | Tab | Displays a plain-language bullet list of detected problems, including missing audio, stuck mute, missing antenna, and transverter validity issues. |
| **JSON** | Tab | Displays the full JSON snapshot of slices and DAX channels. |
| **Refresh Snapshot** | Button | Re-reads slice state into the snapshot. Click this after changing slice settings. |
| **Copy Summary** | Button | Copies the issue summary text to the clipboard. |
| **Copy JSON** | Button | Copies the full JSON snapshot to the clipboard. |
| **Export JSON...** | Button | Saves the full JSON snapshot to a file. |
| **Close** | Button | Closes the dialog. |

The status label below the buttons confirms the result of the last copy or export action (for example, `Copied to clipboard`).

## Tips

- Click **Refresh Snapshot** after making any slice, antenna, or DAX changes before sharing or re-reading the summary. The snapshot is not updated automatically.
- If you need to send the details to support, use **Copy Summary** to paste the plain-language list into an email or forum post, or use **Export JSON...** to attach the full snapshot as a file.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Inspect each transverter's RF/IF, offset and validity flags for XVTR diagnosis](inspect-each-transverter-s-rf-if-offset-and-validity-flags-for-xvtr-diagnosis.md)
