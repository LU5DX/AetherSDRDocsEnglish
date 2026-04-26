# DAX Audio overview

The DAX (Digital Audio eXchange) applet bridges audio between the FLEX-8600 and other software on your computer — for example, digital mode programs such as WSJT-X or fldigi. It provides per-channel RX gain sliders and metering for DAX channels 1–4, a single TX gain slider and meter, and slice-assignment indicators showing which slice is routed to each channel.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The DAX applet requires an active radio connection.
- The DAX applet is hidden by default. Click the **DAX** tray button on the right sidebar to show it.

## How it works

When you click **Enable**, AetherSDR starts the DAX audio bridge and persists your choice in `AutoStartDAX`. The bridge exposes up to four RX audio streams (one per slice assignment) and one TX audio stream to the host operating system.

Each RX channel (DAX 1–4) has a combined meter and gain slider. The meter shows the smoothed RMS level of the incoming audio post-fader — the displayed level reflects gain multiplied by the raw signal, so dragging the thumb gives immediate visual feedback. The TX channel works the same way for outbound audio.

Slice-assignment indicators next to each channel show which slice (A–H) is currently routed there. If no slice is assigned, the indicator shows —. The TX indicator shows which slice currently holds TX privileges; it is not user-editable here.

To start DAX automatically every time AetherSDR launches, use `Settings > Autostart DAX with AetherSDR`.

## What each control does

| Control | What it does | Default | Range | Setting key |
|---|---|---|---|---|
| **Enable** | Starts or stops the DAX audio bridge. Master switch for all RX and TX streams. | Off | On / Off | `AutoStartDAX` |
| **DAX 1** gain+meter | Sets RX gain and shows audio level for DAX channel 1. | 0.5 | 0.0–1.0 | `DaxRxGain1` |
| **DAX 2** gain+meter | Sets RX gain and shows audio level for DAX channel 2. | 0.5 | 0.0–1.0 | `DaxRxGain2` |
| **DAX 3** gain+meter | Sets RX gain and shows audio level for DAX channel 3. | 0.5 | 0.0–1.0 | `DaxRxGain3` |
| **DAX 4** gain+meter | Sets RX gain and shows audio level for DAX channel 4. | 0.5 | 0.0–1.0 | `DaxRxGain4` |
| **TX** gain+meter | Sets TX gain and shows audio level for the DAX TX stream. | 0.5 | 0.0–1.0 | `DaxTxGain` |
| Slice-assignment indicator (per RX channel) | Shows which slice (e.g. Slice A) is routed to this DAX channel, or — if unassigned. | — | — or Slice A–H | — |
| TX assignment indicator | Shows which slice currently holds TX privileges and drives the DAX TX stream. | — | — or Slice A–H | — |

## Tips

- Gain and meter values are saved immediately when you drag a slider. They persist across restarts.
- The meter ballistics use a fast attack and slow decay, matching the metering behaviour elsewhere in AetherSDR.

## Related

- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)
- [Set DAX TX gain](set-dax-tx-gain.md)
- [Autostart DAX on launch](autostart-dax-on-launch.md)
- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
- [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)
