# Search within an offline help topic using Find

Use the Find field to search for text inside any AetherSDR offline help topic, without needing an internet connection.

## Before you start

- Open any help topic from the **Help** menu (e.g., **Getting Started…**, **AetherSDR Help…**).

## Steps

1. Press **Ctrl+F** to focus the Find field. The field has the placeholder text "Subject or term".
2. Type your search term. The **Next** and **Previous** buttons become enabled when the field is non-empty.
3. To jump to the next match, press **Enter** or click **Next**.
4. To jump to the previous match, press **Shift+Enter** or click **Previous**.

The search wraps around: when you reach the end of the document, pressing **Next** continues from the top, and vice versa for **Previous**. A status message (e.g., "Wrapped to top" or "No matches") appears next to the buttons.

## What each control does

| Control | Label / Purpose | Behavior |
|---------|----------------|----------|
| Find field | "Find:" with placeholder "Subject or term" | Type your search term. Includes a clear button (X) to reset. |
| Next button | "Next" | Jumps to the next match (wraps from end to top). Disabled when field is empty. |
| Previous button | "Previous" | Jumps to the previous match (wraps from top to end). Disabled when field is empty. |
| Find status | (indicator) | Shows "No matches" (with red border on the field) or "Wrapped to top/bottom". |

## Tips

- **Ctrl+F** activates the Find field and selects any existing text, so you can immediately type a new term.
- The find operation is case-sensitive? No — Qt's `find()` by default is case-insensitive, matching any occurrence regardless of capitalization.
- To clear the search and hide the match highlighting, click the X button in the Find field or delete the text and press Escape.

## Troubleshooting

- **"No matches" appears even though the word is visible** — The match might be inside a code block or heading styled differently. Try a broader term. The search looks for substrings, so "noise" will match "noise cancellation".
- **The Find field disappears when I close the dialog** — Each help topic opens in its own dialog, and the search state is not persisted. Reopen the topic and search again.

## Related

- [Open bundled getting-started guide](open-bundled-getting-started-guide.md)
- [Read the full AetherSDR help document](read-the-full-aethersdr-help-document.md)
