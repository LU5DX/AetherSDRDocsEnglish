# Find all actions in a category

The Keyboard Shortcuts dialog includes a category filter that narrows the action table to a single group of related actions. Use this when you want to review or edit every binding in one area — for example, all VFO actions or all panadapter actions — without scrolling through the full list.

## Before you start

- No radio connection is required.
- Open the dialog via `View > Configure Shortcuts...`.

## Steps

1. Open `View > Configure Shortcuts...`.
2. In the filter row above the action table, locate the **Category:** combo box.
3. Click **Category:** and select the category you want to view.
4. The action table immediately updates to show only actions in that category, with columns **Action**, **Category**, **Current Key**, and **Default Key**.
5. To return to the full list, set **Category:** back to **All**.

## Tips

- You can combine **Category:** with the **Filter:** text field to narrow results further. Both filters apply simultaneously — the table shows only rows that match both the text and the selected category.
- The keyboard map above the table uses color-coded keys by category. The legend row beneath the map identifies which color belongs to each category, so you can spot a category's keys at a glance before opening the filter.
- The dialog now supports theme-aware styling. Colors for key labels, category labels, and the selected key display automatically adapt to the current theme.

## Import and export keyboard shortcuts

The dialog includes **Import...** and **Export...** buttons in the bottom button row. Use these to transfer your custom keyboard shortcut bindings between AetherSDR installations or to share them with other operators.

### Export shortcuts

1. Open `View > Configure Shortcuts...`.
2. Click **Export...**.
3. In the file dialog, choose a location and name for the CSV file. The dialog remembers the last directory you used.
4. Click **Save**. AetherSDR writes a CSV file containing the action name, current key, and default key for every binding.

### Import shortcuts

1. Open `View > Configure Shortcuts...`.
2. Click **Import...**.
3. In the file dialog, locate and select a previously exported CSV file.
4. Click **Open**. AetherSDR reads the file and applies the imported bindings.

   - If an action in the file does not exist in your AetherSDR release, it is skipped and listed in the import summary.
   - If an imported binding uses a key that is already assigned, the existing local binding for that key is cleared (displaced) and listed in the summary.
5. After import, the action table and keyboard map update to show the new bindings. A message box reports the number of actions imported and, if applicable, the number of skipped or displaced bindings. Click **Show Details...** to view the full lists.

## Related

- [Keyboard Shortcuts overview](overview.md)
- [Rebind a keyboard shortcut](rebind-a-keyboard-shortcut.md)
- [See the default key for any action](see-the-default-key-for-any-action.md)