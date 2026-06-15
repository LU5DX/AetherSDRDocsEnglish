# DAX Audio overview

The DAX (Digital Audio eXchange) applet provides a software audio bridge between your FLEX-8600 and other applications running on your computer, such as digital mode software and logging programs. It gives you per-channel RX gain control and metering for four receive streams, plus a single TX stream.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio before the DAX applet is functional.
- The DAX applet is hidden by default. Click the **DAX** tray button on the right sidebar to show it.

## How it works

The DAX applet bridges audio between the radio and your operating system's audio subsystem. When you click **DAX Enable**, AetherSDR starts the DAX audio bridge, making the radio's slice audio available as virtual audio devices that other applications can select as their input or output.

The applet shows four RX channels (DAX 1–4) and one TX channel. Each RX channel can be assigned to a slice on the radio; the assignment is shown in the status indicator next to each channel. The TX channel carries audio from your computer to the radio's transmitter and shows which slice currently holds TX privileges.

Each channel has a combined meter and gain slider (a MeterSlider). The background bar displays the live audio level post-fader — the smoothed RMS level multiplied by the current gain — so the bar reflects actual output level. A draggable thumb sets the gain. Gain changes are saved immediately.

You can also configure DAX to start automatically every time AetherSDR launches via `Settings > Autostart DAX with AetherSDR`.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| **DAX Enable** | Master toggle. Starts or stops the DAX audio bridge. Button label is "Enable". | Off | On / Off | `AutoStartDAX` |
| **DAX 1 gain+meter** | Combined level meter and gain slider for DAX RX channel 1. Drag the thumb to set gain. Accessible name: "DAX RX 1 gain". | 0.5 | 0.0–1.0 | `DaxRxGain1` |
| **DAX 2 gain+meter** | Combined level meter and gain slider for DAX RX channel 2. Accessible name: "DAX RX 2 gain". | 0.5 | 0.0–1.0 | `DaxRxGain2` |
| **DAX 3 gain+meter** | Combined level meter and gain slider for DAX RX channel 3. Accessible name: "DAX RX 3 gain". | 0.5 | 0.0–1.0 | `DaxRxGain3` |
| **DAX 4 gain+meter** | Combined level meter and gain slider for DAX RX channel 4. Accessible name: "DAX RX 4 gain". | 0.5 | 0.0–1.0 | `DaxRxGain4` |
| **TX gain+meter** | Combined level meter and gain slider for the DAX TX stream. Accessible name: "DAX TX gain". | 0.5 | 0.0–1.0 | `DaxTxGain` |
| Slice-assignment status (RX, per channel) | Read-only indicator showing which slice is routed to each DAX RX channel. Displays `—` when unassigned, or a slice letter from A through H when assigned. The slice letter is rendered with rich text formatting for improved readability. | — | `—` or `Slice A`–`Slice H` | — |
| TX assignment status | Read-only indicator showing which slice currently holds TX privileges and drives the DAX TX stream. Displays `—` when no TX slice is active. The slice letter is rendered with rich text formatting. | — | `—` or `Slice A`–`Slice H` | — |

## Performance notes

On Linux, starting with AetherSDR v26.5.2.1, the DAX RX audio path uses a native PipeWire `pw_stream` source, replacing the previous PulseAudio client. This reduces DAX RX latency from approximately 400 ms to approximately 200 ms.

## Tips

- Gain settings for all channels are persisted immediately on each drag event — you do not need to click a save button.
- To have the DAX bridge start every time AetherSDR opens, use `Settings > Autostart DAX with AetherSDR` rather than clicking **Enable** manually each session.
- The slice assignment status indicators now use rich text formatting to display slice letters more clearly.
- The applet uses theme-aware styling; visual appearance adapts to your selected theme.
- Each gain slider has an accessible name set for screen reader compatibility: "DAX RX N gain" for RX channels and "DAX TX gain" for the TX channel.

## Related

- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Autostart DAX on launch](autostart-dax-on-launch.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)
- [Set DAX TX gain](set-dax-tx-gain.md)
- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
- [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)