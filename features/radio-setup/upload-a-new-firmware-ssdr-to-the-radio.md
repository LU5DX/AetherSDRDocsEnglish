# Upload a new firmware .ssdr to the radio

Use this page to load a new firmware image onto your FLEX-8600 from a local `.ssdr` file. You would do this to update the radio firmware manually without relying on an internet-based update check.

## Before you start

- AetherSDR must be connected to the radio. The Radio tab is not accessible without an active connection.
- Download the `.ssdr` firmware file to your computer before opening the dialog.
- Do not disconnect the radio or close the dialog while the upload is in progress.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the `Radio` tab.
3. Click `Browse .ssdr...` to open a file chooser.
4. Navigate to and select your `.ssdr` firmware file, then confirm the selection.
5. Click `Upload Firmware`.
6. Watch the progress bar and status text below the button. Wait until the status indicates the upload is complete before taking any further action.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| `Check for Update` | Push button | Queries the radio for available firmware updates. |
| `Browse .ssdr...` | Push button | Opens a file dialog to choose a local `.ssdr` firmware image. |
| `Upload Firmware` | Push button | Begins the firmware upload. A progress bar and status text appear and update during the transfer. |

## Tips

- Use `Check for Update` first if you are unsure whether your current firmware is already up to date.
- The firmware status area below `Upload Firmware` is empty until an upload begins. If the text stops updating unexpectedly, do not disconnect the radio; wait to confirm whether the transfer completed.

## Troubleshooting

- **`Upload Firmware` has no effect** — Confirm that a file has been selected with `Browse .ssdr...` first. The button requires a file path to be set before it will proceed.
- **Upload starts but does not complete** — Do not close the dialog or disconnect the radio. Check that the network connection between your computer and the radio is stable. If the upload fails, you can attempt it again by clicking `Upload Firmware` without re-browsing, provided the file path is still shown.

## Related

- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)
- [Radio Setup overview](overview.md)
