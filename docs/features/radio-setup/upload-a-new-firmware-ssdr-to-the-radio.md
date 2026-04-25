# Upload a new firmware .ssdr to the radio

This page explains how to load a firmware image file onto your FLEX-8600 using AetherSDR's built-in uploader. Use this procedure when FlexRadio releases a new `.ssdr` firmware package and you want to update the radio without leaving AetherSDR.

## Before you start

- The radio must be connected. The Radio tab of Radio Setup is only functional when AetherSDR has an active radio connection.
- Download the `.ssdr` firmware file from FlexRadio to your computer before opening the dialog.
- Do not transmit during the upload.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the `Radio` tab.
3. Click `Browse .ssdr...` to open a file-chooser dialog.
4. Navigate to the `.ssdr` file you downloaded and select it. The filename will be shown next to the button.
5. Click `Upload Firmware`.
6. Watch the progress bar and status text below the button. The upload is complete when the status text indicates success.
7. Reboot the radio as instructed by the firmware release notes to apply the new firmware.

## Tips

- If you want to check whether a newer firmware version is available before obtaining the file manually, click `Check for Update`. AetherSDR will query for available firmware updates and report the result in the status area.
- The `Radio SN`, `HW Version`, and `Model` fields on the same tab confirm you are looking at the correct radio before uploading.

## Troubleshooting

- **Upload Firmware is unresponsive** — No `.ssdr` file has been selected yet. Click `Browse .ssdr...` first, confirm the file appears, then click `Upload Firmware`.
- **Progress bar stalls or status shows an error** — Verify the radio is still connected and reachable on the network. Check `Settings > Network...` for connectivity issues, then retry the upload from step 3.
- **Wrong radio updated** — Confirm the `Radio SN` and `Model` indicators on the Radio tab match your intended radio before clicking `Upload Firmware`.

## Related

- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)
- [Switch the radio between DHCP and static IP](switch-the-radio-between-dhcp-and-static-ip.md)
