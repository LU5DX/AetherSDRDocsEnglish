# DX Cluster Startup Commands overview

Define custom commands that AetherSDR sends to a DX cluster or Reverse Beacon Network (RBN) immediately after each login and automatic reconnect. This lets you apply your preferred filter, announcements, or operational settings (e.g., `set/dx` or `set/wwv`) without manually typing them each time.

## How it works

When AetherSDR connects (or reconnects) to a DX cluster or RBN node, it sends every line in the corresponding command list, one per line, immediately after the login handshake completes. The same commands are replayed after every automatic reconnection triggered by a network drop.

Two independent command sets are stored and managed:

- **DX Cluster** — commands sent to the cluster configured on the DX Cluster tab in SpotHub (`DxClusterStartupCommands` AppSettings key).
- **RBN** — commands sent to the Reverse Beacon Network tab in SpotHub (`RbnStartupCommands` AppSettings key).

## What each control does

| Control | Default | Valid range / Notes | AppSettings key |
|---|---|---|---|
| **Command editor** (multi-line plain text editor) | *(empty)* | One command per line. Blank lines are ignored. No limit on number of lines. | `DxClusterStartupCommands` (main tab) / `RbnStartupCommands` (RBN tab) |

## Opening the dialog

Open `Settings > SpotHub...`, then click **Edit Startup Commands** on either:

- The **DX Cluster** tab — to edit the main cluster command set.
- The **RBN** tab — to edit the RBN command set.

## Tips

- Commands are sent in the order they appear in the editor, top to bottom.
- Typical startup commands include `set/dx` (enable DX spots), `set/announce` (enable announcements), or `set/filter` to limit spot types. Check your cluster's help (`help`) for available commands.
- If a command requires a response from the cluster (e.g., a status confirmation), AetherSDR does not wait — it sends all lines immediately. For time-sensitive sequences, keep them short.
- Changes take effect on the next connection or reconnect; they are not sent to an already-connected session.
- The dialog now uses the active theme's color palette. Backgrounds, text colors, and accent colors adapt automatically to the current UI theme selection.

## See also

- DX Cluster & RBN configuration