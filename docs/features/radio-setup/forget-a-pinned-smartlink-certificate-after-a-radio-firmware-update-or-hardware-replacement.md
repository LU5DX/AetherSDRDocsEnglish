# Forget a pinned SmartLink certificate after a radio firmware update or hardware replacement

When you update your radio's firmware or replace the radio hardware, the SmartLink TLS certificate fingerprint changes. AetherSDR's trust-on-first-use pinning will reject the connection because the stored fingerprint no longer matches. Use the SmartLink tab in Radio Setup to forget the old certificate so the next connection re-pins the new one silently.

## Before you start

- The radio must be connected to AetherSDR.
- You need the hostname of the radio whose pinned certificate you want to remove. The table in the SmartLink tab shows all pinned hosts.

## Steps

1. Open **Settings > Radio Setup...**.
2. Click the **SmartLink** tab.
3. In the **Pinned SmartLink Certificates** table, click the row for the host whose certificate changed.
4. Click **Forget selected**.
5. Close the Radio Setup dialog and reconnect to the radio. The new certificate is pinned automatically.

## Related

- [Clear all pinned SmartLink certificates when rotating multiple radio TLS identities](clear-all-pinned-smartlink-certificates-when-rotating-multiple-radio-tls-identities.md)
