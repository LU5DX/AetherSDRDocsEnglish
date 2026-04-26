# Upload a new firmware .ssdr to the radio

This page explains how to load a firmware image file onto your FLEX-8600 using AetherSDR. You would do this to update the radio to a new firmware version you have downloaded as a `.ssdr` file.

## Before you start

- AetherSDR must be connected to the radio. The Radio (tab) controls are unavailable without an active connection.
- Download the `.ssdr` firmware file to your computer before opening this dialog.
- Do not transmit or disconnect the radio during the upload.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. Click **Browse .ssdr...** to open a file chooser.
4. Navigate to and select your `.ssdr` firmware file, then confirm the selection.
5. Click **Upload Firmware**.
6. Watch the progress bar and status text beneath the button. Wait until the status indicates the upload is complete before doing anything else.

## Tips

- The firmware status area is blank until an upload begins. Once started, it shows progress and result text. If the status text does not update after clicking **Upload Firmware**, confirm the file you selected ends in `.ssdr` and that the radio is still connected.
- You can verify the current hardware version before and after the upload using the **HW Version** indicator on the same **Radio** tab.

## Troubleshooting

- **Browse .ssdr... opens but no file is selectable** — The file chooser filters for `.ssdr` files. Confirm your downloaded file has that extension and has not been renamed or extracted from an archive.
- **Upload Firmware is unresponsive** — Confirm AetherSDR is connected to the radio. The controls on the Radio tab require an active radio connection. Use `Settings > Connect to Radio...` if needed, then retry.
- **Upload appears to stall** — Do not interrupt the connection. Large firmware files take time to transfer. Wait for the status text to report a result before taking action.

## Related

- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)
- [Radio Setup overview](overview.md)
