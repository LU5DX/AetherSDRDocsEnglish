# Upload a new firmware .ssdr to the radio

This page explains how to load a firmware image file onto your FLEX-8600 using AetherSDR's built-in uploader. You would do this to update the radio to a specific firmware version without using SmartSDR for Windows.

## Before you start

- AetherSDR must be connected to the radio. The Radio (tab) in Radio Setup requires an active radio connection.
- Obtain the correct `.ssdr` firmware file for your FLEX-8600 and note its location on your computer.
- Do not interrupt power to the radio or close AetherSDR during the upload.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the `Radio (tab)` tab if it is not already selected.
3. Click `Browse .ssdr...` to open a file chooser.
4. Navigate to your `.ssdr` file, select it, and confirm.
5. Click `Upload Firmware`.
6. Watch the progress bar and status text below the button. Wait until the status indicates the upload is complete before doing anything else.
7. Reboot the radio when prompted or when the upload status confirms completion.

## Tips

- If you want AetherSDR to check for an available update rather than supplying your own file, click `Check for Update` instead of `Browse .ssdr...`.
- The firmware status area is blank until an upload begins. A progress bar and result text appear once `Upload Firmware` is clicked.

## Troubleshooting

- **"Browse .ssdr..." does nothing or the dialog closes immediately** — Verify you are connected to the radio. The Radio tab controls are only active with an established radio connection.
- **Upload stalls or fails partway through** — Do not close the dialog. Check that the network connection between your computer and the radio is stable. If using a VPN or remote link, a wired local connection is more reliable for firmware transfers.
- **Radio does not reboot after upload** — Power-cycle the FLEX-8600 manually from the front panel, then reconnect AetherSDR.

## Related

- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)
- [Radio Setup overview](overview.md)
