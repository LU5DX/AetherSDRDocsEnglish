# Reduce DAX RX Latency on Linux (Native PipeWire Path, ~200 ms)

AetherSDR v0.9.7 on Linux routes DAX RX audio through a native PipeWire `pw_stream` source, cutting receive latency from ~400 ms to ~200 ms. This page explains what changed and how to confirm DAX is running with the lower-latency path.

## Before you start

- AetherSDR v0.9.7 or later installed on Linux with PipeWire running as the system audio server.
- A connected FLEX-8600 radio (DAX requires an active radio connection).
- At least one slice assigned to a DAX channel in the radio.

## Steps

1. Click the DAX tray button on the right sidebar to open the DAX Audio applet.
2. Click Enable to start the DAX audio bridge. The button turns green when active.
3. Confirm that the `AutoStartDAX` setting is saved: the Enable button remains checked after you reopen the applet.
4. In your digital mode software (WSJT-X, fldigi, or similar), select the PipeWire source corresponding to the DAX channel you assigned. Audio now arrives with approximately 200 ms of latency rather than ~400 ms.

No additional configuration is required. The PipeWire path is used automatically on Linux in v0.9.7 and later; there is no toggle to switch between the old PulseAudio path and the new one.

## What each control does

| Control | Default | Valid range | Persisted key | Description |
|---|---|---|---|---|
| DAX Enable | Off | On / Off | `AutoStartDAX` | Master switch. Starts all DAX RX and TX streams. Must be on for audio to flow. |
| DAX 1 gain+meter | 0.5 | 0.0 – 1.0 | `DaxRxGain1` | Combined level meter and gain slider for DAX channel 1. Drag to adjust RX gain. Accessible name: "DAX RX 1 gain". |
| DAX 2 gain+meter | 0.5 | 0.0 – 1.0 | `DaxRxGain2` | Combined level meter and gain slider for DAX channel 2. Accessible name: "DAX RX 2 gain". |
| DAX 3 gain+meter | 0.5 | 0.0 – 1.0 | `DaxRxGain3` | Combined level meter and gain slider for DAX channel 3. Accessible name: "DAX RX 3 gain". |
| DAX 4 gain+meter | 0.5 | 0.0 – 1.0 | `DaxRxGain4` | Combined level meter and gain slider for DAX channel 4. Accessible name: "DAX RX 4 gain". |
| TX gain+meter | 0.5 | 0.0 – 1.0 | `DaxTxGain` | Combined level meter and gain slider for the DAX TX stream. Accessible name: "DAX TX gain". |
| Slice-assignment status (per channel) | — | — or Slice A–H | *(none)* | Read-only indicator showing which slice is routed to each DAX channel. |

## Tips

- If the meter bars on DAX 1–4 are not moving after you click Enable, check that the slice-assignment status indicator shows a slice letter rather than —. A — means no slice is currently routed to that channel; assign the slice to the DAX channel from the radio's slice controls.
- To have DAX start automatically at every launch, check `Settings > Autostart DAX with AetherSDR`. This sets `AutoStartDAX` to True without requiring you to click Enable manually each session.
- The level meter uses fast attack (α = 0.4) and slow decay (α = 0.08) ballistics. A brief absence of signal will not immediately blank the meter.

## Troubleshooting

- **Enable button is greyed out or does not respond** — DAX requires an active radio connection. Connect to the FLEX-8600 first via `Settings > Connect to Radio...`, then click Enable.
- **Latency is still ~400 ms after upgrading to v0.9.7** — Verify that PipeWire is the active audio server on your system. If your system still uses PulseAudio without PipeWire, the native PipeWire path is not available and latency will remain at the higher figure.
- **No audio from the PipeWire source in WSJT-X or fldigi** — Confirm Enable is checked (green) in the DAX applet and that the slice-assignment indicator for the relevant channel shows a slice letter, not —.

## Related

- [DAX Audio overview](overview.md)
- [Autostart DAX on launch](autostart-dax-on-launch.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)
- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)