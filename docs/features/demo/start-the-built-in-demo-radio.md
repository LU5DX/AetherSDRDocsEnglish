# Start the built-in demo radio

The built-in demo radio simulates a FLEX-8600 with synthetic RF noise, allowing you to explore AetherSDR's features without a physical radio connected. This is useful for learning the interface, testing configurations, or demonstrating the software.

## Before you start

- AetherSDR must be installed and running.
- No physical FlexRadio needs to be connected.

## Steps

1. Open **Settings > Connect to Radio...** from the menu bar.
2. In the connection dialog, select **Demo** from the radio list.
3. Click **Connect**.

The main window now shows a panadapter and spectrum display with synthetic noise. The Demo Mode applet panel becomes available in the tray at the bottom of the window.

## What each control does

The Demo Mode applet panel appears only when the demo radio is connected. It contains the following controls:

| Control | Type | Behavior |
|---------|------|----------|
| Noise channel toggles | Checkbox | Enable or disable individual noise sources (pink noise, white noise, QRM bursts, birdies). |
| Noise level sliders | Slider | Adjust the amplitude of each enabled noise source independently. |
| Scene presets | Push button | One-click buttons that set all noise channels to match a specific scenario (storm, night-40m, contest pileup, quiet band, etc.). |

## Tips

- The demo radio does not support transmit operations.

## Related

- [Demo Mode overview](overview.md)
- [Shape synthetic RF noise with per-channel controls](shape-synthetic-rf-noise-with-per-channel-controls.md)
- [Load a noise scene preset for realistic band simulation](load-a-noise-scene-preset-for-realistic-band-simulation.md)
