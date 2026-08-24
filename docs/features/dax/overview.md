# DAX Audio overview

The DAX (Digital Audio eXchange) applet provides a software audio bridge between your FLEX-8600 and other applications running on your computer, such as digital mode software and logging programs. It gives you per-channel RX gain control and metering for up to eight receive streams, plus a single TX stream.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio before the DAX applet is functional.
- The DAX applet is hidden by default. Click the **DAX** tray button on the right sidebar to show it.

## How it works

The DAX applet bridges audio between the radio and your operating system's audio subsystem. When you click **DAX Enable**, AetherSDR starts the DAX audio bridge, making the radio's slice audio available as virtual audio devices that other applications can select as their input or output.

The applet shows up to eight RX channels (DAX 1–8) and one TX channel. Each RX channel can be assigned to a slice on the radio; the assignment is shown in the status indicator next to each channel. The TX channel carries audio from your computer to the radio's transmitter and shows which slice currently holds TX privileges.

Each channel has a combined meter and gain slider (a MeterSlider). The background bar displays the live audio level post-fader — the smoothed RMS level multiplied by the current gain — so the bar reflects actual output level. RX meter levels use exponential smoothing with a fast attack and slow decay. A draggable thumb sets the gain. Gain changes are saved immediately.

You can also configure DAX to start automatically every time AetherSDR launches via `Settings > Autostart DAX with AetherSDR`.

## Platform-specific behavior

On **Windows**, AetherSDR does not include a built-in DAX audio bridge driver. The **DAX Enable** button, all per-channel and TX meters, and gain sliders are hidden. The applet displays only an informational note: "No built-in DAX driver on Windows. Use TCI, or SmartSDR DAX." DAX functionality can still be used through FlexRadio's own SmartSDR DAX drivers or via TCI. For configuration guidance, see Help > Configuring Data Modes.

On **macOS and Linux**, the full DAX applet is available as described below.

## What each control does

| Control                                   | Description                                                                                                                                                                                                                                | Default                                                                                                                              |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **DAX Enable**                            | Master toggle. Starts or stops the DAX audio bridge. Button label reads "Enabled" when active, "Disabled" when inactive.                                                                                                                   | Off                                                                                                                                  |
| **DAX 1 gain+meter**                      | Combined level meter and gain slider for DAX RX channel 1. Drag the thumb to set gain. Accessible name: "DAX RX 1 gain".                                                                                                                   | 0.5                                                                                                                                  |
| **DAX 2 gain+meter**                      | Combined level meter and gain slider for DAX RX channel 2. Accessible name: "DAX RX 2 gain".                                                                                                                                               | 0.5                                                                                                                                  |
| **DAX 3 gain+meter**                      | Combined level meter and gain slider for DAX RX channel 3. Accessible name: "DAX RX 3 gain".                                                                                                                                               | 0.5                                                                                                                                  |
| **DAX 4 gain+meter**                      | Combined level meter and gain slider for DAX RX channel 4. Accessible name: "DAX RX 4 gain".                                                                                                                                               | 0.5                                                                                                                                  |
| **TX gain+meter**                         | Combined level meter and gain slider for the DAX TX stream. Accessible name: "DAX TX gain".                                                                                                                                                | 0.5                                                                                                                                  |
| Slice-assignment status (RX, per channel) | Read-only indicator showing which slice is routed to each DAX RX channel. Displays `—` when unassigned, or a slice letter from A through H when assigned. The slice letter is rendered with rich text formatting for improved readability. | —                                                                                                                                    |
| TX assignment status                      | Read-only indicator showing which slice currently holds TX privileges and drives the DAX TX stream. Displays `—` when no TX slice is active. The slice letter is rendered with rich text formatting.                                       | —                                                                                                                                    |
| DAX 5 gain+meter                          | Combined meter/slider; drag to set RX gain on DAX channel 5.                                                                                                                                                                               | Visible only when the connected radio supports at least 5 slices.                                                                    |
| DAX 6 gain+meter                          | Combined meter/slider; drag to set RX gain on DAX channel 6.                                                                                                                                                                               | Visible only when the connected radio supports at least 6 slices.                                                                    |
| DAX 7 gain+meter                          | Combined meter/slider; drag to set RX gain on DAX channel 7.                                                                                                                                                                               | Visible only when the connected radio supports at least 7 slices.                                                                    |
| DAX 8 gain+meter                          | Combined meter/slider; drag to set RX gain on DAX channel 8.                                                                                                                                                                               | Visible only on an 8-slice-capable radio.                                                                                            |
| Windows note                              | On Windows builds the applet shows only the note 'No built-in DAX driver on Windows. Use TCI, or SmartSDR DAX.' (#4112).                                                                                                                   | Windows has no built-in DAX bridge (no kernel-mode audio driver); all other controls are omitted and their setters are null-guarded. |

## Channel visibility by radio model

The RX channel rows shown in the applet are gated to your radio's slice capacity so you never see dead gain sliders that route nowhere. The applet:

- Hides DAX rows above the connected radio's slice capacity. For example, a radio with 2 slices (e.g., a 6300/6400) shows only DAX 1–2 rows, and a 4-slice radio (e.g., a 6600/8600) shows only DAX 1–4 rows.
- Keeps the hidden rows allocated in memory — they are only hidden, not destroyed — so the same gain settings persist regardless of which radio you connect.
- Re-evaluates row visibility whenever you connect to a radio.

## Performance notes

On Linux, starting with AetherSDR v26.5.2.1, the DAX RX audio path uses a native PipeWire `pw_stream` source, replacing the previous PulseAudio client. This reduces DAX RX latency from approximately 400 ms to approximately 200 ms.

## Tips

- On Windows, DAX functionality is available via FlexRadio's SmartSDR DAX drivers or via TCI — see Help > Configuring Data Modes for setup instructions.
- Gain settings for all channels are persisted immediately on each drag event — you do not need to click a save button.
- To have the DAX bridge start every time AetherSDR opens, use `Settings > Autostart DAX with AetherSDR` rather than clicking **Enable** manually each session.
- The slice assignment status indicators now use rich text formatting to display slice letters more clearly.
- The applet uses theme-aware styling; visual appearance adapts to your selected theme.
- Each gain slider has an accessible name set for screen reader compatibility: "DAX RX N gain" for RX channels and "DAX TX gain" for the TX channel.
- RX meter levels are exponentially smoothed (fast attack, slow decay) so peak audio spikes are visible but meter motion remains readable.

## Related

- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Autostart DAX on launch](autostart-dax-on-launch.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)
- [Set DAX TX gain](set-dax-tx-gain.md)
- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
- [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)