# Select iambic mode A or B for the radio keyer

Choose between Curtis iambic mode A and mode B for the FLEX-8600's built-in keyer. The setting applies to both the radio hardware keyer and AetherSDR's local software keyer, which mirrors the radio's state for low-latency sidetone.

## Before you start

- AetherSDR must be connected to the radio. The Phone/CW tab is unavailable when no radio is connected.
- A paddle must be wired to the radio's key jack for the iambic keyer to function.

## Steps

1. Click `Settings > Radio Setup...` to open the Radio Setup dialog.
2. Click the **Phone/CW** tab.
3. Confirm that **Iambic:** is set to **Enabled**. If it reads **Disabled**, click it once to enable the iambic keyer.
4. Click **A** or **B** to select the desired Curtis iambic mode.

## What each control does

| Control | Kind | Default | Valid values | Behavior |
|---|---|---|---|---|
| **Iambic:** | Toggle button | — | Enabled / Disabled | Enables or disables the iambic keyer on the radio. Must be enabled before mode selection has effect. |
| **Iambic Mode: A / B** | Push button (mutually exclusive pair) | A | A / B | Selects Curtis iambic mode A or mode B for both the radio keyer and the local software keyer. |
| **Swap:** | Toggle button | — | Enabled / Disabled | Swaps the dit and dah paddle inputs. |

## Tips

- Mode A (Curtis A) releases the last element when both paddles are released mid-squeeze. Mode B (Curtis B) completes the last element before stopping. Choose based on your sending style.
- The local software keyer mirrors whichever mode you select here, providing sub-5 ms sidetone response independent of network latency.

## Related

- [Radio Setup overview](overview.md)
- [Configure FlexControl serial port pin functions](configure-flexcontrol-serial-port-pin-functions.md)
