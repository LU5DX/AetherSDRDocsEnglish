# Upload a new firmware .ssdr to the radio

Use this page to load a new firmware image onto your FLEX-8600. You will need a `.ssdr` firmware file on your local machine before you begin.

## Before you start

- AetherSDR must be connected to the radio. The Radio tab in Radio Setup is not available without an active connection.
- Download the target `.ssdr` firmware file and note its location on disk.
- Do not transmit during the upload.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. Click **Browse .ssdr...** to open a file chooser, then select your `.ssdr` firmware file and confirm.
4. Click **Upload Firmware**.
5. Watch the firmware status indicator below the button. It is empty until the upload begins, then shows progress and a result message when complete.
6. Close the dialog when the status indicator confirms the upload finished.

## Tips

- If you want AetherSDR to confirm which firmware version is currently on the radio before selecting a file, check **HW Version** in the Radio Information group on the same tab.
- The **Check for Update** button queries for available firmware updates if your radio has internet access configured.

## Troubleshooting

- **Browse .ssdr... opens but no file appears in the chooser** — Confirm the file has a `.ssdr` extension. The file picker filters for that type.
- **Upload Firmware is unresponsive after clicking Browse .ssdr...** — No file has been selected yet. Click **Browse .ssdr...** again and confirm a file before clicking **Upload Firmware**.
- **Status indicator shows a failure message** — Verify the radio is still connected (`Settings > Connect to Radio...`) and that no other client is holding an exclusive session. Then retry from step 3.

## Related

- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)
- [Radio Setup overview](overview.md)
