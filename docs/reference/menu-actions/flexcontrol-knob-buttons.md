# FlexControl Knob & Buttons

Opens the FlexControl Tuning Knob settings inside the Serial & Controllers page of Radio Setup, so you can adjust knob and button behavior without first opening AetherControl.

## Before you start

- A FLEX-8600 radio with the FlexControl hardware connected via USB.
- AetherSDR built with serial port support (the menu item is hidden otherwise).

## Steps

1. Click **Settings > FlexControl Knob & Buttons...**.
2. The Radio Setup dialog opens on the **Serial & Controllers** page, with the **FlexControl Tuning Knob** group in focus.
3. Adjust the knob and button settings as needed.
4. Click **Close** (or the dialog's equivalent) to apply your changes.

## Tips

- This menu item is a shortcut — the same settings are reachable from **Settings > AetherControl...** followed by the controller's settings button.
- If the FlexControl is not detected, check the USB cable and confirm the device appears in the Serial & Controllers page before adjusting settings.

## Troubleshooting

- **The menu item is grayed out or missing** — AetherSDR was built without serial port support (`HAVE_SERIALPORT` build gate). Rebuild with serial port support or use the AetherControl window if available.

## Related

- [Configuring AetherSDR Controls](configuring-aethersdr-controls.md)
- [USB Cables](usb-cables.md)
- [Getting Started](getting-started.md)
