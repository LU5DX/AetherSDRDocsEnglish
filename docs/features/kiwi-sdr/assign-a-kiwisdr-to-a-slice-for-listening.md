# Assign a KiwiSDR to a slice for listening

After browsing the public KiwiSDR directory and connecting to a receiver, assign it to an active slice so you can tune and listen through the selected remote KiwiSDR.

## Before you start

- You must have a KiwiSDR receiver connected (status indicator shows "Connected").
- A slice must be active in the panadapter.

## Steps

1. Open the **Applet panel** and click the **KiwiSDR** tile to open the KiwiSDR applet.
2. In the **Receiver list**, select the KiwiSDR receiver you want to use.
3. Click **Assign to slice**.

The slice now tunes the selected KiwiSDR receiver. The **Status indicator** shows connection details.

## What each control does

| Control | Behavior |
|---------|----------|
| Receiver list | Searchable, scrollable list of public KiwiSDR receivers with name, location, band and status. |
| Assign to slice | Assigns the selected KiwiSDR receiver to the active slice for tuning and listening. |
| Status indicator | Shows connection state (`Disconnected` / `Connecting` / `Connected` / `Error`) with detail text. |

## Related

- [KiwiSDR overview](overview.md)
- [Browse the public KiwiSDR directory](browse-the-public-kiwisdr-directory.md)
- [Connect to a KiwiSDR receiver](../../getting-started/setup/connect-to-a-kiwisdr-receiver.md)
