# Forget a pinned SmartLink certificate after a radio firmware update or hardware replacement

When you update your radio's firmware or replace the radio hardware, the SmartLink TLS certificate fingerprint changes. AetherSDR's trust-on-first-use pinning will reject the connection because the stored fingerprint no longer matches. Use the **SmartLink** tab in **Radio Setup** to forget the old certificate so the next connection re-pins the new one silently.

## Before you start

- The radio must be connected to AetherSDR.
- You need the hostname of the radio whose pinned certificate you want to remove. The table in the **SmartLink** tab shows all pinned hosts.

## Steps

1. Open **Settings > Radio Setup...**.
2. Click the **SmartLink** tab.
3. In the **Pinned SmartLink Certificates** table, click the row for the host whose certificate changed.
4. Click **Forget selected**.
5. Close the Radio Setup dialog and reconnect to the radio. The new certificate is pinned automatically.

## About the Pinned SmartLink Certificates table

The table lists every host that has been pinned on first connect (trust-on-first-use). It contains three columns:

- **Host**: The hostname of the radio.
- **SHA-256 fingerprint**: The certificate fingerprint, shown in monospace.
- **Pinned**: The date the certificate was first pinned (YYYY-MM-DD format), or "(pre-phase 2)" if pinned before the feature was introduced.

The **Forget selected** button removes the selected host's pinned certificate fingerprint. The next connection to that host silently re-pins the new certificate.

The **Forget all** button clears every pinned certificate after a confirmation prompt. The next connection to each radio silently re-pins.

## Related

- [Clear all pinned SmartLink certificates when rotating multiple radio TLS identities](clear-all-pinned-smartlink-certificates-when-rotating-multiple-radio-tls-identities.md)
- Radio Setup dialog reference