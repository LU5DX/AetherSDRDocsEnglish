# Bypass the VK3AMP amplifier

Take the VK3AMP amplifier out of the transmit signal path so you can operate barefoot (without the amp) or troubleshoot an issue.

## Before you start

- AetherSDR must be connected to your FLEX-8600 radio.
- The VK3AMP amplifier must be reachable over TCP with UDP telemetry enabled.

## Steps

1. Open the Applet panel and click the **VKAMP** tile.
2. Locate the **BYPASS** button. The label shows the current state — "BYPASS" in amber means the amp is bypassed; "BYPASS" in green means the amp is in-line.
3. Click **BYPASS** to toggle between bypass and in-line operation.

## What each control does

| Control | Behavior |
|---|---|
| **BYPASS** | Toggles the amplifier between bypass and in-line. The button label displays the current state, not the action you're about to take. Amber border = bypassed; green border = in-line. |
| **COOLING** | Toggles the cooling override. Active state is shown with a normal text color. |

## Tips

- The **BYPASS** button label tells you the current state, not what clicking it will do. If the button shows "BYPASS" in amber, the amp is already bypassed.
- When the radio connection is lost, the app clears the bypass state and resets the button — the amp returns to its default state, not necessarily to bypass.

## Troubleshooting

- **The amp doesn't bypass when I click BYPASS** — Verify the amplifier connection is active (check the status pill at the top of the applet). If the connection is down, the button is disabled and won't respond.
- **The button shows in-line but the amp is actually bypassed** — The button reflects the last known state from the amplifier. If the amp was changed externally, wait for the next telemetry update — the display mirrors live status, not your last click.

## Related

- [VK3AMP Amplifier overview](overview.md)
- [Monitor forward and reflected power on the VK3AMP amplifier](monitor-forward-and-reflected-power-on-the-vk3amp-amplifier.md)
- [Select the VK3AMP antenna port](select-the-vk3amp-antenna-port.md)
