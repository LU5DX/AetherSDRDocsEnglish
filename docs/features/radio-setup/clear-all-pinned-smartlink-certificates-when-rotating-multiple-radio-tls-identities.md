# Clear all pinned SmartLink certificates when rotating multiple radio TLS identities

Removes every trusted SmartLink TLS certificate that AetherSDR has pinned on first connect, allowing you to safely re-pin certificates after rotating radio identities or replacing radio hardware.

## Before you start

- The radio must be connected to AetherSDR.
- You want to replace or rotate TLS certificates on multiple radios, and need to clear all stored trust-on-first-use pins.

## Steps

1. Open **Settings > Radio Setup...**
2. Click the **SmartLink** tab.
3. Click **Forget all**.
4. In the confirmation dialog, click **Yes** to clear every pinned certificate.

## What each control does

| Control | Behavior | Setting key |
|---|---|---|
| **Pinned SmartLink Certificates** section | Lists every host this client has pinned on first connect. Shows Host, SHA-256 fingerprint, and Pinned date. | (not persisted – managed by `WanCertCache`) |
| **Forget selected** | Removes the selected host's pinned certificate. Next connect to that host re-pins silently. | (none) |
| **Forget all** | Clears every pinned certificate after a confirmation prompt. Next connect to each radio silently re-pins. | (none) |

## Tips

- After clearing all pins, the next SmartLink connection to each radio will silently trust and re-pin the new certificate.
- Use **Forget selected** to remove a single host's pin if you are only updating one radio.

## Related

- [Forget a pinned SmartLink certificate after a radio firmware update or hardware replacement](forget-a-pinned-smartlink-certificate-after-a-radio-firmware-update-or-hardware-replacement.md)
