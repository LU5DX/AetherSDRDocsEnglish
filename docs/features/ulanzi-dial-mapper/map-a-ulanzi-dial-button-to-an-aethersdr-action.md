# Map a Ulanzi Dial button to an AetherSDR action

This page shows you how to assign functions to the Ulanzi Dial's physical buttons and rotary control. Each button and the rotary knob can trigger a different AetherSDR action, letting you control your radio without touching the software.

## Before you start

- The Ulanzi Dial must be connected and detected by AetherSDR.
- AetherSDR must be running on Linux (the Ulanzi Dial feature is Linux-only).

## Steps

1. Open **Settings > Ulanzi Dial Mapping...**.
2. Wait for the status label at the bottom of the dialog to show **Connected** (instead of **Disconnected**).
3. Find the pill for the physical control you want to map. Pills are labeled **Top Left**, **Top Middle**, **Top Right**, **Left Top**, **Left Bottom**, **Right Top**, **Right Bot**, and **Dial Press**.
4. Click the combo box next to that pill.
5. Select the action you want to assign from the drop-down list.
6. Repeat for any other buttons or the rotary control.

## What each control does

| Control | Default | Description |
| --- | --- | --- |
| **Top Left** | MOX toggle | Shortcut action bound to the physical top-left button. |
| **Top Middle** | RIT toggle | Shortcut action bound to the physical top-middle button. |
| **Top Right** | Tune toggle | Shortcut action bound to the physical top-right button. |
| **Left Top** | None | Shortcut action bound to the left top side button. |
| **Left Bottom** | None | Shortcut action bound to the left bottom side button. |
| **Right Top** | Next slice | Shortcut action bound to the right top side button. |
| **Right Bot** | None | Shortcut action bound to the right bottom side button. |
| **Dial Press** | Mute toggle | Shortcut action bound to pressing the rotary knob. |
| **Tuning:** | WheelFrequency | Drop-down to choose what the rotary knob controls. Options include tuning frequency, filter bandwidth, slice/master/headphone volume, panadapter zoom, RIT/XIT, AGC-T, RF gain, APF, CW speed, and RF power. |
| **Reset to Defaults** | — | Restores all button and rotary assignments to their default actions. |
| **Close** | — | Closes the dialog. |
| **Grant access** | Hidden | Shown only when a dial is detected but its input device can't be opened on Linux. Installs a udev rule so AetherSDR can read the dial's input. |
| **Last event:** | — | Displays the most recent physical control event received from the dial. |

## Tips

- The physical button-to-signature mapping is fixed by the dial's firmware. You can change which AetherSDR action each button triggers, but you cannot remap which physical button sends which signal.
- Use **Last event:** to verify a button is being detected before assigning an action to it.

## Troubleshooting

- **Status shows "Disconnected"** — The dial is not being detected. Check the USB connection and ensure the dial is powered on.
- **Status shows "Disconnected" but a "Grant access" button appears** — AetherSDR can't open the dial's input device. Click **Grant access** and follow the prompts to install the required udev rule. You'll need administrator approval once per machine.
- **Rotary knob doesn't work after mapping a button** — The rotary knob is configured separately with the **Tuning:** drop-down. Buttons and rotary assignments are independent.

## Related

- [Ulanzi Dial Mapping overview](overview.md)
- [Learn a Ulanzi Dial control signature](learn-a-ulanzi-dial-control-signature.md)
