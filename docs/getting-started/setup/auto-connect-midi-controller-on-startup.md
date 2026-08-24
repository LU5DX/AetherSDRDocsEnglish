# Auto-connect MIDI controller on startup

When AetherSDR launches, it can automatically reopen the last-used MIDI port so your controller is ready without manual intervention each session.

## Before you start

- AetherSDR must have been built with MIDI support (`Settings > MIDI Mapping...` must appear in the Settings menu).
- Your MIDI controller must be physically connected and recognized by the operating system.
- You must have connected to the port at least once manually so that AetherSDR has a device to reopen. See [Connect a MIDI controller](connect-a-midi-controller.md).

## Steps

1. Go to `Settings > MIDI Mapping...`.
2. In the **Port:** combo box, select your MIDI controller.
3. Click **Connect**. The port status changes to show the connected device name.
4. Check **Auto-connect on startup**.

AetherSDR saves both `MidiPort` and `MidiAutoConnect` immediately. On the next launch, the port reopens automatically without any further action.

## What each control does

| Control | Kind | Behavior | Persisted setting |
|---|---|---|---|
| **Port:** | Combo box | Selects the MIDI input device to use | `MidiPort` |
| **Refresh** | Button | Rescans available MIDI ports | — |
| **Connect** | Button | Opens or closes the selected MIDI port | — |
| **Auto-connect on startup** | Checkbox | Reopens the saved MIDI port each time AetherSDR launches | `MidiAutoConnect` |

## Using the MIDI Mapping dialog

The **MIDI Controller Mapping** dialog lets you configure a MIDI controller. Use the **Category** combo box to filter the **Parameter** list. Available categories include:

- All
- RX
- TX
- Phone/CW
- EQ
- Global
- Mode
- Band
- Filter
- Slice
- Display
- Frequency

Select a **Parameter** to assign, then click **Learn** to record a binding from your MIDI controller. In the Phone/CW category, three momentary (Gate) actions are available: **Trigger straight key**, **Trigger CW Left Paddle**, and **Trigger CW Right Paddle**. Legacy dotted IDs (`cw.key`, `cw.dit`, `cw.dah`) are automatically migrated on read.

You can also create a binding without using **Learn**: click **Manual…** to open a dialog where you type the binding's channel, message type, and number. This is useful when you know the exact MIDI message your controller sends but cannot or do not want to trigger it through Learn mode. Each row in the **Bindings table** also has an edit (✎) button that opens the same manual editor to correct that row's channel, message type, and number.

The **Bindings table** shows existing bindings with per-row **Invert**, **Relative**, edit (✎), and delete (**×**) controls. Columns: Parameter, MIDI Source, Channel, Invert, Relative, (edit), (delete).

Use the **Profile:** combo box, **Save**, and **Load** buttons to manage named mapping profiles. You can also transfer profiles between systems:

- Click **Import...** to import a profile file from disk. Both AetherSDR profile XML files and SmartSDR `.map` files are accepted. After importing, AetherSDR reports how many bindings were imported; click **Load** to apply them.
- Click **Export...** to write the current bindings to an AetherSDR profile XML file. The file dialog opens in the same directory you last used for imports or exports; the directory is remembered in the `MidiImportExportPath` setting.

## Tips

- If you unplug and replug the controller, click **Refresh** to repopulate the **Port:** list before clicking **Connect**.
- The port status and activity indicator update in real time. Confirm the activity indicator shows incoming messages before closing the dialog.
- The dialog remembers its size and position between sessions.
- Use **Manual…** when you need a binding for a MIDI message you cannot easily generate with the physical controller (for example, a pitch-bend event from a virtual device).
- When importing a profile, the bindings are not applied until you click **Load**. This lets you review the import summary before making changes to your current setup.

## Troubleshooting

- **Port list is empty after plugging in the controller** — Click **Refresh** to rescan. If the port still does not appear, verify the operating system recognizes the device.
- **Auto-connect does not work on the next launch** — Confirm you clicked **Connect** and saw a connected status before checking **Auto-connect on startup**. The setting saves the most recently opened port name; if the device name changed (for example, on a different USB port on some systems), select the correct port manually, connect again, and re-check **Auto-connect on startup**.
- **An imported profile does not appear in the table** — Click **Load** after importing. The import only stages the bindings; it does not apply them automatically.
- **Manual… opened the editor but the binding is wrong** — Use the per-row ✎ button in the **Bindings table** to correct the channel, message type, and number for that specific binding without recreating it.

## Related

- [Connect a MIDI controller](connect-a-midi-controller.md)
- [MIDI Controller Mapping overview](../../features/midi-mapping/overview.md)
- [Record a new binding with Learn mode](../../features/midi-mapping/record-a-new-binding-with-learn-mode.md)
- [Save the current mapping as a named profile](../../features/midi-mapping/save-the-current-mapping-as-a-named-profile.md)
- Import and export mapping profiles
- Triggers for CW straight key and paddles