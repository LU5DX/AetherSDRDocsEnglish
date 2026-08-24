# DAX Audio Applet

## Windows note

On Windows, AetherSDR does not include a built-in DAX audio driver. The DAX applet displays only the following informational message, and no controls are available:

> No built-in DAX driver on Windows. Use TCI, or SmartSDR DAX.

DAX audio routing on Windows is supported through FlexRadio's own SmartSDR DAX drivers or through TCI. See **Help > Configuring Data Modes** for setup instructions.

On macOS and Linux, the full DAX applet is available as described below.

## DAX channels and radio slice capacity

The DAX applet shows RX gain/meter rows for DAX channels 1 through 8. Rows above the connected radio's slice capacity are hidden, so a radio with fewer slices does not show dead gain sliders that route nowhere. For example:

- FLEX-6300 / FLEX-6400 (2 slices): DAX 1-2 are shown, DAX 3-8 are hidden.
- FLEX-6600 / FLEX-8600 (4 slices): DAX 1-4 are shown, DAX 5-8 are hidden.
- FLEX-6700 (8 slices): all DAX 1-8 rows are shown.

The hidden rows are not destroyed — they are only hidden, and their gain values are still persisted so they are restored when you connect to a larger radio.

## Autostart DAX on Launch

Enable the `AutoStartDAX` setting so that the DAX audio bridge starts automatically every time AetherSDR opens, without requiring a manual click of Enable each session.

### Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The DAX applet requires an active radio connection.
- The DAX applet must be visible. If it is not, click the **DAX** tray button on the right sidebar to show it.

### Steps

1. Open the DAX applet by clicking the **DAX** tray button on the right sidebar if it is not already visible.
2. Click **Settings > Autostart DAX with AetherSDR** to place a check mark next to the item. This persists `AutoStartDAX` as `True`.
3. Confirm the **Enable** button in the DAX applet shows **Enabled** (lit green). If it shows **Disabled**, click it to start the bridge for the current session.

On the next launch, AetherSDR will read `AutoStartDAX` and activate the bridge automatically, reflecting the enabled state on the **Enable** button (showing **Enabled**).

To turn autostart off, click **Settings > Autostart DAX with AetherSDR** again to remove the check mark.

## What each control does

| Control                                     | What it does                                                                                                                                                   | Default                                                                                                                              |
|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **Enable** button in the DAX applet         | Master toggle. Starts or stops the DAX audio bridge for the current session and persists the state. Shows **Enabled** when active, **Disabled** when inactive. | Disabled                                                                                                                             |
| **Settings > Autostart DAX with AetherSDR** | Checkable menu item. When checked, AetherSDR starts the DAX bridge on every launch.                                                                            | Off (unchecked)                                                                                                                      |
| DAX 1 gain+meter                            | Combined level meter and gain slider for DAX RX channel 1. Drag to adjust. Accessible name: "DAX RX 1 gain".                                                   | 0.5                                                                                                                                  |
| DAX 2 gain+meter                            | Combined level meter and gain slider for DAX RX channel 2. Drag to adjust. Accessible name: "DAX RX 2 gain".                                                   | 0.5                                                                                                                                  |
| DAX 3 gain+meter                            | Combined level meter and gain slider for DAX RX channel 3. Drag to adjust. Accessible name: "DAX RX 3 gain".                                                   | 0.5                                                                                                                                  |
| DAX 4 gain+meter                            | Combined level meter and gain slider for DAX RX channel 4. Drag to adjust. Accessible name: "DAX RX 4 gain".                                                   | 0.5                                                                                                                                  |
| DAX 5 gain+meter                            | Combined meter/slider; drag to set RX gain on DAX channel 5.                                                                                                   | Visible only when the connected radio supports at least 5 slices.                                                                    |
| DAX 6 gain+meter                            | Combined meter/slider; drag to set RX gain on DAX channel 6.                                                                                                   | Visible only when the connected radio supports at least 6 slices.                                                                    |
| DAX 7 gain+meter                            | Combined meter/slider; drag to set RX gain on DAX channel 7.                                                                                                   | Visible only when the connected radio supports at least 7 slices.                                                                    |
| DAX 8 gain+meter                            | Combined meter/slider; drag to set RX gain on DAX channel 8.                                                                                                   | Visible only on an 8-slice-capable radio.                                                                                            |
| TX gain+meter                               | Combined level meter and gain slider for the DAX TX stream. Drag to adjust. Accessible name: "DAX TX gain".                                                    | 0.5                                                                                                                                  |
| Windows note                                | On Windows builds the applet shows only the note 'No built-in DAX driver on Windows. Use TCI, or SmartSDR DAX.' (#4112).                                       | Windows has no built-in DAX bridge (no kernel-mode audio driver); all other controls are omitted and their setters are null-guarded. |

## Indicator meanings

| Indicator | States | Meaning |
|---|---|---|
| DAX 1..8 assignment | — or Slice A..H | The slice (if any) currently assigned to this DAX channel. Displays the slice letter in the active radio model's color. |
| TX assignment | — or Slice A..H | The slice currently holding TX privileges (drives DAX TX). Displays the slice letter in the active radio model's color. |

## Tips

- The **Enable** button and **Settings > Autostart DAX with AetherSDR** both write the same `AutoStartDAX` key. Clicking either one updates the shared setting.
- Gain values for all RX channels and the TX channel are saved independently. Adjusting them before enabling autostart means they will be restored at the same levels on the next launch.
- Slice assignment indicators display the slice letter in the active radio model's color (rich text format) for improved visibility. This affects both DAX RX channel assignments and TX assignment indicators.
- On Linux, DAX audio uses PipeWire native streams (`pw_stream`) for lower latency, reducing RX latency from approximately 400 ms to approximately 200 ms. This applies to all DAX RX channels.
- Each gain slider has an accessible name set for screen reader compatibility: "DAX RX N gain" for channels 1-8 and "DAX TX gain" for the transmit channel.
- The **Enable** button now dynamically updates its text to show **Enabled** or **Disabled** based on the current state, providing clearer visual feedback.
- RX meter levels are exponentially smoothed with fast attack and slow decay for stable, readable metering.

## Troubleshooting

- **The DAX applet is not visible** — Click the **DAX** tray button on the right sidebar to show it.
- **Enable is checked but the bridge does not start on the next launch** — Verify that **Settings > Autostart DAX with AetherSDR** has a check mark. Clicking **Enable** in the applet alone sets the bridge state for the current session and persists `AutoStartDAX`, but confirming the menu item is checked ensures the autostart path runs at launch.
- **The Enable button shows Disabled after launch despite autostart being on** — This can occur if AetherSDR launches before a radio connection is established. The DAX applet requires a connected radio. Connect to the radio and click **Enable** manually, or allow AetherSDR to connect before checking the bridge state.
- **Some DAX gain sliders are missing** — This is expected when the connected radio supports fewer slices than 8. For example, a FLEX-6600 shows only DAX 1-4. The gain sliders reappear when you connect to a radio with more slice capacity.
- **On Windows, the DAX applet shows only a note** — This is expected. AetherSDR does not include a built-in DAX audio driver on Windows. Use FlexRadio's SmartSDR DAX drivers or TCI instead. See **Help > Configuring Data Modes** for details.

## Related

- [DAX Audio overview](overview.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)
- [Set DAX TX gain](set-dax-tx-gain.md)
- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)