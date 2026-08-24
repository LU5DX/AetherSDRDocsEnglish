# Ulanzi Dial Mapping overview

The Ulanzi Dial Mapping dialog lets you visually map the physical buttons and rotary control of your Ulanzi Dial to AetherSDR actions. A stylized dial with callout pills shows each control's current binding; you can reassign any control to a different action from a list, or learn a new control signature by pressing the physical control.

## How it works

The dialog displays a stylized image of the Ulanzi Dial with color-coded callout pills anchored to each physical control. Each pill corresponds to a specific hardware control — the three top buttons, the dial press, the four side tabs, and the rotary knob. The signature-to-pill mapping is a fixed property of the dial firmware and cannot be changed; only the action bound to each control is configurable.

For each pill, select an action from the dropdown to bind that physical control to an AetherSDR function. Clicking a pill without a bound action enters Learn mode, where you press the corresponding physical control to capture its signature and bind it. The rotary control has its own dedicated dropdown for tuning-related actions.

The dialog shows connection status, the last input event received, and lets you reset all bindings to their defaults.

## Controls

| Control | Description |
|---------|-------------|
| **Callout pills** | Click a pill to enter Learn mode for that control, then press the physical dial button or knob to bind it. |
| **Tuning dropdown** | Assigns the rotary knob to one of 15 actions: Frequency (Tune Slice), Filter Bandwidth, Slice Audio Volume, Master Volume, Headphone Volume, Panadapter Zoom, Band Zoom, Segment Zoom, RIT, XIT, AGC-T, RF Gain, APF, CW Speed, or RF Power. Default: Frequency (Tune Slice). |
| **Reset to Defaults** | Restores every pill and the rotary dropdown to their default actions. |
| **Grant access** (Linux only) | Appears when a dial is detected but its input node cannot be opened. Installs a udev rule (with administrator approval) so AetherSDR can read the dial's input. Required once per machine. |
| **Last event** | Shows the most recent input event captured from the dial. |
| **Close** | Closes the dialog. |

## Default button bindings

| Physical control | Default action |
|---|---|
| Top Left | MOX toggle |
| Top Middle | RIT toggle |
| Top Right | Tune toggle |
| Left Top | None |
| Left Bottom | None |
| Right Top | Next slice |
| Right Bottom | None |
| Dial Press | Mute toggle |

## Related

- [Learn a Ulanzi Dial control signature](learn-a-ulanzi-dial-control-signature.md)
- [Map a Ulanzi Dial button to an AetherSDR action](map-a-ulanzi-dial-button-to-an-aethersdr-action.md)
