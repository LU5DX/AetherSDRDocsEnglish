# Slice Troubleshooting Overview

The Slice Troubleshooting dialog captures a full snapshot of your radio's slice, panadapter, transverter, and DAX channel state and checks it for common problems. Use it to diagnose audio, mute, antenna, and transverter issues, or to collect diagnostic data before contacting support.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The dialog requires an active radio connection.

## How it works

Open the dialog from `Help > Slice Troubleshooting...`. AetherSDR reads the current state of every slice, panadapter, transverter, and DAX channel and builds a snapshot. The snapshot is available in two forms: a plain-language issue summary and a full JSON representation. You can refresh the snapshot at any time, copy either form to the clipboard, or save the JSON to a file.

The dialog checks for likely problems automatically, including missing audio, stuck mute conditions, missing antenna assignments, and transverter validity issues. Detected problems appear as a bullet list on the Issue Summary tab.

No settings are persisted by this dialog. It reads radio state at the moment you open it or click Refresh Snapshot.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| Issue Summary (tab) | Tab | Displays a plain-language bullet list of detected problems with the current slice configuration. |
| JSON (tab) | Tab | Displays the full JSON snapshot of slices, panadapters, transverters, and DAX channels. |
| Refresh Snapshot | Button | Re-reads the current slice state and rebuilds the snapshot. Click this after changing any slice configuration. |
| Copy Summary | Button | Copies the issue summary text to the clipboard. |
| Copy JSON | Button | Copies the full JSON snapshot to the clipboard. |
| Export JSON... | Button | Opens a file dialog to save the JSON snapshot to a file. |
| Close | Button | Closes the dialog. |
| Status label | Indicator | Displays the result of the last copy or export action, for example "Copied to clipboard". |

## Tips

- Click Refresh Snapshot after making any change to slice, antenna, or transverter settings so the snapshot reflects the updated state before you copy or export it.
- Use Copy Summary to paste a concise problem list into a forum post or support ticket. Use Copy JSON or Export JSON... when the support team asks for full diagnostic data.

## Related

- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Inspect each transverter's RF/IF, offset and validity flags for XVTR diagnosis](inspect-each-transverter-s-rf-if-offset-and-validity-flags-for-xvtr-diagnosis.md)
