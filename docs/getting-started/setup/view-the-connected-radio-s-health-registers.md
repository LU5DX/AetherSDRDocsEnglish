# View the connected radio's health registers

Open the Radio Health dialog to view live, read-only health and status registers reported by the connected radio. This is useful for diagnosing issues like ADC overloads or checking that a FIFO is moving.

## Before you start

- A radio must be connected to AetherSDR.

## Steps

1. Select **Help > Radio Health...**.
2. Read the current values in the health register table. The table refreshes automatically every 500 ms.
3. (Optional) Click **Copy** to copy the current snapshot to the clipboard for pasting into a support request or log.

## What each control does

| Control | Behavior |
| --- | --- |
| Health register table | Shows the radio's health/status registers as reported by the backend. Values are grouped by section headings. A register the radio has not reported shows a dash (—), not zero. Booleans display as Yes or No. |
| Copy | Copies the health snapshot, including section headings, to the clipboard. The status label changes to "Copied to clipboard" briefly. |
| Close | Closes the dialog. |

## Tips

- A dash means the radio has not reported that value — it is not the same as a value of zero.
- The table rows are rebuilt only when the set of registers changes, so your scroll position and row selection stay put while you read.
- Nothing in this dialog writes to the radio; it is diagnostic read-out only.
- If the radio reports no health registers, the status label shows "This radio reports no health registers." instead of an empty table.

## Troubleshooting

- **Status shows "Not connected."** — No radio is connected, or the connection was lost. Connect to a radio first ([Connect to a local LAN radio](connect-to-a-local-lan-radio.md) or one of the other connection topics) and reopen the dialog.

## Related

- [Radio Health overview](../../features/radio-health/overview.md)
- [Check how many external clients are connected to each channel](check-how-many-external-clients-are-connected-to-each-channel.md)
