# Select the PGXL fan speed (Standard, Contest, Broadcast)

Choose between the three cooling profiles of a direct-connected Power Genius XL amplifier from the Amplifier applet, so the fan runs at the appropriate level for your operating style.

## Before you start

- Connect to a FLEX-8600 radio running firmware 4.1.5.
- The PGXL amplifier must be physically connected directly to the computer, not proxied through the radio.
- The Amplifier applet must be visible — toggle it with the AMP tray button on the right sidebar.
- Wait for the first fan mode status from the amplifier; the fan speed selector is hidden until that arrives.

## Steps

1. Click the AMP tray button on the right sidebar to open the Amplifier applet.
2. Confirm the source label reads "● DIRECT" (fan speed is only available on a direct connection).
3. Click the fan speed selector (labeled "Fan: Std", "Fan: Contest", or "Fan: Bcast").
4. Select **STANDARD**, **CONTEST**, or **BROADCAST** from the dropdown.

The amplifier switches to the chosen fan mode immediately. The selector's label updates to reflect the current mode.

## What each control does

- **Fan speed selector** — Dropdown listing the three modes. Hidden until a direct PGXL connection delivers the first fan mode status. The selector ignores mouse-wheel scroll unless the dropdown is open, preventing accidental changes while hovering.

## Tips

- The fan speed selector only appears when the telemetry source is DIRECT. If you see "● RADIO", the amplifier is proxied through the radio and the selector stays hidden.
- The three modes map to labels "Fan: Std", "Fan: Contest", and "Fan: Bcast" in the closed selector.

## Troubleshooting

- **The fan speed selector is missing** — The amplifier is connected through the radio proxy, not directly. Check the source label; if it reads "● RADIO", connect the PGXL directly to the computer. The selector also needs at least one fan mode status from the direct connection before it appears.
- **The fan mode changed unintentionally** — The selector ignores mouse-wheel scroll when the dropdown is closed. If the mode still changes, you likely clicked the selector and scrolled while the dropdown was open.

## Related

- [Confirm whether PGXL telemetry is direct or proxied through the radio](confirm-whether-pgxl-telemetry-is-direct-or-proxied-through-the-radio.md)
- [Put the PGXL amplifier in OPERATE](put-the-pgxl-amplifier-in-operate.md)
- [Put the PGXL amplifier in STANDBY](put-the-pgxl-amplifier-in-standby.md)
