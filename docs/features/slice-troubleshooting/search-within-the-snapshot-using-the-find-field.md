# Search within the Snapshot Using the Find Field

Use the Find field in the Slice Troubleshooting dialog to locate specific text within the current tab — either the Issue Summary or the JSON snapshot. This helps you quickly jump to a particular slice ID, antenna name, or error message without scrolling through the entire contents.

## Before you start

- A radio connection must be active.
- Open the Slice Troubleshooting dialog via `Help > Slice Troubleshooting...`.

## Steps

1. Open the Slice Troubleshooting dialog using `Help > Slice Troubleshooting...`.
2. Select the tab you want to search — **Issue Summary** or **JSON**.
3. Click the **Find:** field (placeholder text: "Search snapshot...").
4. Type the text you want to locate. The field has a clear button (X) to erase your entry.
5. Press **Enter** or click **Find Next** to jump to the next match. Searching wraps within the current tab.
6. Read the status label below the find field — it shows `<N> match(es) in current tab.` The number updates as you type.

## What each control does

| Control | Behavior |
| --- | --- |
| **Find:** | Text field for entering a search term. Highlights matching occurrences in the active tab. Empty terms produce no matches. |
| **Find Next** | Jumps to the next match of the search term in the active tab. Wraps within the current tab. |
| Status label | Shows the number of matches in the current tab, e.g. "5 match(es) in current tab." Also displays copy/export results like "Copied to clipboard". |

## Tips

- The search is scoped to the active tab only — switch tabs to search that tab's contents.
- Because search wraps, you can cycle through all matches by repeatedly clicking **Find Next** or pressing **Enter**.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
