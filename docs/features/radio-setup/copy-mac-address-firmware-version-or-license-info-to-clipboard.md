# Copy MAC address, firmware version or license info to clipboard

Copy a radio's MAC address, firmware version, license subscription details, or other read-only identifiers to the system clipboard for sharing with support or documentation.

## Before you start

- AetherSDR must be connected to the radio.
- Open Radio Setup (`Settings > Radio Setup...`).

## Steps

1. Click the **Radio** tab.
2. Locate the value you want to copy:
   - **MAC Address** — on the **Network** tab, find **MAC Address**.
   - **Firmware version** — on the **Radio** tab, see **HW Version**.
   - **License Info** — on the **Radio** tab, see **Subscription**, **Expiration**, **Radio ID**, or **Licensed version**.
   - **Radio SN**, **Model**, **Options**, **IP Address**, **Mask** — each has a copy button.
3. Click the clipboard icon (two overlapping rectangles) next to the value. A "Copied" popup appears briefly.

## What each control does

| Control | Default | Behavior | Setting key |
|---|---|---|---|
| Clipboard icon (Radio SN, HW Version, Options, Model, Subscription, Expiration, Radio ID, Licensed version, IP Address, Mask, MAC Address) | — | One-click copy of the adjacent read-only value to clipboard. Button dims when value is empty or "—". | None |

## Tips

- The copy button only appears next to read-only indicator values. Editable fields like **Nickname** or **Callsign** do not have copy buttons — select the text manually.
- A screen-aligned "Copied" popup confirms the action and auto-closes after 1 second.

## Related

- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)
