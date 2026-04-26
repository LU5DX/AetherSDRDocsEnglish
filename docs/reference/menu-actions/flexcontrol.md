# FlexControl

`Settings > FlexControl...` opens the serial port configuration for the FlexControl hardware interface, allowing you to assign and configure the serial port AetherSDR uses to communicate with a FlexControl knob controller.

## Before you start

- A FlexControl hardware device must be physically connected to your computer via serial or USB-serial adapter.
- AetherSDR must have been built with serial port support (`HAVE_SERIALPORT`). If `FlexControl...` does not appear in the `Settings` menu, your build does not include this feature.
- AetherSDR must be running.

## Steps

1. Click `Settings` in the menu bar.
2. Click `FlexControl...`.
3. In the dialog that opens, select the serial port your FlexControl device is connected to.
4. Adjust any additional serial port parameters as needed.
5. Click the confirmation control to apply the settings.

## Related

- [USB Cables](usb-cables.md)
- [Configuring AetherSDR Controls](configuring-aethersdr-controls.md)
- [Getting Started](getting-started.md)
