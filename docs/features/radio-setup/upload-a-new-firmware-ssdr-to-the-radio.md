# Upload a New Firmware .ssdr to the Radio

This page explains how to load a firmware image file onto your FLEX-8600 using the Radio Setup dialog. You would do this to update the radio to a specific firmware version without using the automatic update check.

## Before you start

- AetherSDR must be connected to the radio. The Radio (tab) will not populate correctly without a live connection.
- Obtain the `.ssdr` firmware file from FlexRadio and note where it is saved on your computer.
- Do not transmit during the upload.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. Click **Browse .ssdr...** to open a file chooser.
4. Navigate to the `.ssdr` file on your computer, select it, and confirm.
5. Click **Upload Firmware**.
6. Watch the progress bar and status text below the button. Wait until the status indicates the upload is complete before doing anything else.
7. Reboot the radio as directed by the firmware release notes to apply the new firmware.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Check for Update** | Button | Queries for available firmware updates automatically. Use this instead of **Browse .ssdr...** if you want AetherSDR to find the update for you. |
| **Browse .ssdr...** | Button | Opens a file dialog to select a local `.ssdr` firmware image. |
| **Upload Firmware** | Button | Starts the upload using the file selected with **Browse .ssdr...**. A progress bar and status text appear below and update as the transfer proceeds. |

## Tips

- If you only want to check whether a newer version exists rather than uploading a specific file, use **Check for Update** instead of the manual browse-and-upload workflow.
- The firmware status area is empty until an upload begins. If you see no progress bar after clicking **Upload Firmware**, confirm that a file was selected with **Browse .ssdr...** first.

## Troubleshooting

- **Upload Firmware does nothing** — No `.ssdr` file has been selected. Click **Browse .ssdr...** first, select the file, then click **Upload Firmware**.
- **Radio tab controls are unpopulated or grayed out** — AetherSDR is not connected to the radio. Establish a connection via `Settings > Connect to Radio...` before opening Radio Setup.

## Related

- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)
- [Radio Setup overview](overview.md)
