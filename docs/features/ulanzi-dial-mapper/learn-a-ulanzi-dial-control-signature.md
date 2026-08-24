# Learn a Ulanzi Dial control signature

Learn what physical button or knob event AetherSDR receives from your Ulanzi Dial, so you can verify a control works or diagnose why a binding isn't triggering.

## Before you start

- A Ulanzi Dial connected to your machine (Linux only).
- AetherSDR running and able to read the dial's input. The status label at the bottom of the dialog shows `Connected` or `Disconnected`.

## Steps

1. Open **Settings > Ulanzi Dial Mapping...**.
2. Look at the **Last event:** label at the bottom of the dialog — it shows the most recent kernel event signature the dial sent.
3. Press the physical button or turn the rotary knob whose signature you want to learn.
4. Read the signature from the **Last event:** label. For example, pressing the Top Left button shows `Last event: KEY_PREVIOUSSONG`.

## What each control does

| Control | Behavior |
| --- | --- |
| **Last event:** | Displays the most recent kernel event signature received from the dial (e.g. `KEY_PLAYPAUSE`, `Ctrl+V`). The signature is immutable firmware behavior, not user-configurable. |
| **Status label** (bottom left) | Shows `Connected` or `Disconnected`, plus the device name when a dial is detected. |
| **Grant access** | Appears only when a dial is detected but its evdev node can't be opened. Installs a udev rule (with administrator approval) so AetherSDR can read the dial's input. Required once per machine. |
| Callout pills | Visual map of the dial's physical controls with their current action bindings. This dialog does not support entering Learn mode via pills — use **Last event:** to learn a signature. |

## Tips

- The signature-to-pill mapping is a property of the dial firmware (v1.x), not user-configurable. Changing it requires re-flashing the dial.
- The rotary control's tuning event is routed by MainWindow directly and does not appear as a button signature. Use the **Tuning:** combo at the bottom of the dialog to change what the knob does.
- If the status label reads `Disconnected`, check that the dial is plugged in before trying to learn a signature.

## Troubleshooting

- **Last event:** stays `—` when pressing buttons — the dial isn't connected or AetherSDR can't read its input. Check the connection status label; if **Grant access** appears, click it to install the udev rule, then try again.
- **The signature I see doesn't match what I expect** — Signatures are fixed by the dial firmware. Refer to the callout pills to see which physical control maps to which action.

## Related

- [Ulanzi Dial Mapping overview](overview.md)
- [Map a Ulanzi Dial button to an AetherSDR action](map-a-ulanzi-dial-button-to-an-aethersdr-action.md)
