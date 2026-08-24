# Radio Health

The Radio Health dialog is a live, read-only diagnostic view of the connected radio's health and status registers, grouped by whatever the radio backend reports. It is useful for monitoring things like ADC overload flags, temperature, or other radio-reported telemetry without writing anything to the radio.

## Before you start

- A FLEX-8600 radio must be connected to AetherSDR.
- The radio must report health registers; if it doesn't, the dialog explains that instead of showing an empty table.

## How it works

The dialog polls the radio backend every 500 ms for a health snapshot and displays it in a table with two columns: **Register** and **Value**. Registers are grouped under bold section headers as reported by the backend.

- A dash (—) in the **Value** column means the radio has not reported that register — this is *not* the same as a value of zero.
- Boolean values render as **Yes** or **No** rather than `true`/`false` or `1`/`0`. For example, an ADC overload flag reads "Yes" or "No", not a count.
- Numeric values are shown with two decimal places where applicable.
- If the radio reports no health registers at all, the dialog shows the message "This radio reports no health registers." instead of an invented or zero-filled table.
- If no radio is connected, the dialog shows "Not connected."

The dialog is strictly read-only. Nothing on this screen writes to the radio.

## What each control does

| Control | Description |
|---|---|
| **Health register table** | Lists health/status registers in two columns: **Register** and **Value**. Rows are selectable but not editable. Alternating row colors and no grid lines make it easy to read. |
| **Copy** | Copies the entire health snapshot to the clipboard as plain text, including section headings and indented register/value pairs. The status line briefly changes to "Copied to clipboard" to confirm. |
| **Status line** | Shows "Updating every 500 ms" while the dialog is live, or the messages noted above when idle. |

## Tips

- The table keeps your scroll position and row selection intact between refreshes, which makes it practical to watch a specific register while it updates.
- Use **Copy** to capture a snapshot for a support ticket or a forum post — the clipboard text is already formatted with section headings.
- The dialog's position and size are remembered between sessions (persisted in `RadioHealthDialogGeometry`), so you can leave it open in a corner while operating.

## Troubleshooting

- **The table is empty but the radio is connected** — Either the radio reports no health registers, or the backend hasn't received any yet. The status line will tell you which: "This radio reports no health registers." means the radio genuinely has none to show.
- **Values show as a dash (—)** — The radio has not reported that particular register yet. This is expected for registers that only appear under certain conditions; wait for the next refresh cycle. A dash is never an invented zero.

## Related

- [View the connected radio's health registers](../../getting-started/setup/view-the-connected-radio-s-health-registers.md)
