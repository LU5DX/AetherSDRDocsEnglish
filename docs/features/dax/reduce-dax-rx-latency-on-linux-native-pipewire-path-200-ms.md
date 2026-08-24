# DAX Audio Applet

The DAX Audio applet provides the digital audio bridge between your FLEX-8600 radio and computer audio system. It shows per-channel RX meters and gain sliders for DAX channels 1–8 plus a single TX meter, with a master Enable toggle.

## Before you start

- AetherSDR v26.8.4 or later installed.
- A connected FLEX-8600 radio (DAX requires an active radio connection).
- At least one slice assigned to a DAX channel in the radio.

Rows above the connected radio's slice capacity are hidden, so a radio with fewer slices (for example, a 2-slice or 4-slice model) does not show dead gain sliders.

## Platform support

| Platform | DAX driver | Notes |
|---|---|---|
| Linux | Built-in (PipeWire `pw_stream` source) | Native PipeWire path since v0.9.7, ~200 ms latency. No PulseAudio fallback. |
| macOS | Built-in | Shipped as part of AetherSDR. |
| Windows | **Not shipped with AetherSDR** | DAX Enable button and all meters are inert on Windows. Use FlexRadio's own SmartSDR DAX drivers or TCI instead. |

On Windows, the DAX Audio applet displays only a notice: *"No built-in DAX driver on Windows. Use TCI, or SmartSDR DAX."* No controls are built, and no meters update. For setup instructions on Windows, see **Help > Configuring Data Modes**.

## How to use (Linux / macOS)

1. Click the **DAX** tray button on the right sidebar to open the DAX Audio applet.
2. Click **Enable** to start the DAX audio bridge. The button turns green and shows "Enabled" when active.
3. Confirm that the `AutoStartDAX` setting is saved: the Enable button remains checked and shows "Enabled" after you reopen the applet.
4. In your digital mode software (WSJT-X, fldigi, or similar), select the audio source corresponding to the DAX channel you assigned.

On Linux, audio arrives with approximately 200 ms latency rather than ~400 ms. No additional configuration is required; the PipeWire path is used automatically.

## What each control does

| Control                               | Default                                                                                                                  | Valid range                                                                                                                          |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| DAX Enable                            | Starts the DAX audio bridge; emits daxToggled.                                                                           | Button label is 'Enable'/'Disabled'; master switch for all DAX RX and TX streams. Not built on Windows (#4112).                      |
| DAX 1 gain+meter                      | 0.5                                                                                                                      | 0.0 – 1.0                                                                                                                            |
| DAX 2 gain+meter                      | 0.5                                                                                                                      | 0.0 – 1.0                                                                                                                            |
| DAX 3 gain+meter                      | 0.5                                                                                                                      | 0.0 – 1.0                                                                                                                            |
| DAX 4 gain+meter                      | 0.5                                                                                                                      | 0.0 – 1.0                                                                                                                            |
| DAX 5 gain+meter                      | 0.5                                                                                                                      | 0.0 – 1.0. Visible only when the connected radio supports at least 5 slices.                                                         |
| DAX 6 gain+meter                      | 0.5                                                                                                                      | 0.0 – 1.0. Visible only when the connected radio supports at least 6 slices.                                                         |
| DAX 7 gain+meter                      | 0.5                                                                                                                      | 0.0 – 1.0. Visible only when the connected radio supports at least 7 slices.                                                         |
| DAX 8 gain+meter                      | 0.5                                                                                                                      | 0.0 – 1.0. Visible only on an 8-slice-capable radio.                                                                                 |
| TX gain+meter                         | 0.5                                                                                                                      | 0.0 – 1.0                                                                                                                            |
| Slice-assignment status (per channel) | Shows which slice is currently routed to each DAX channel.                                                               | Slice letters render as rich text identifiers.                                                                                       |
| Windows note                          | On Windows builds the applet shows only the note 'No built-in DAX driver on Windows. Use TCI, or SmartSDR DAX.' (#4112). | Windows has no built-in DAX bridge (no kernel-mode audio driver); all other controls are omitted and their setters are null-guarded. |
## Tips

- If the meter bars on DAX 1–8 are not moving after you click **Enable**, check that the slice-assignment status indicator shows a slice letter rather than —. A — means no slice is currently routed to that channel; assign the slice to the DAX channel from the radio's slice controls.
- To have DAX start automatically at every launch, check **Settings > Autostart DAX with AetherSDR**. This sets `AutoStartDAX` to True without requiring you to click Enable manually each session.
- The level meter uses fast attack (α = 0.4) and slow decay (α = 0.08) ballistics. A brief absence of signal will not immediately blank the meter.

## Troubleshooting

- **Enable button is greyed out or does not respond** — On Windows, this is expected behavior (see Platform support above). On Linux and macOS, DAX requires an active radio connection. Connect to the FLEX-8600 first via **Settings > Connect to Radio...**, then click Enable.
- **Latency is still ~400 ms after upgrading** — Verify that PipeWire is the active audio server on your Linux system. If your system still uses PulseAudio without PipeWire, the native PipeWire path is not available and latency will remain at the higher figure.
- **No audio from the DAX source in WSJT-X or fldigi** — Confirm Enable is checked (shows "Enabled") in the DAX applet and that the slice-assignment indicator for the relevant channel shows a slice letter, not —.
- **On Windows, which DAX driver should I use?** — Use the official FlexRadio SmartSDR DAX drivers, or configure your digital software to use TCI instead of DAX audio.

## Related

- [DAX Audio overview](overview.md)
- [Autostart DAX on launch](autostart-dax-on-launch.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)
- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)