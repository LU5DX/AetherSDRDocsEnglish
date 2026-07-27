# Demo Mode overview

Demo Mode is a built-in simulation feature that lets you explore AetherSDR without a physical radio. It generates synthetic RF noise across multiple configurable channels, allowing you to practice tuning, filtering, and operating in realistic band conditions.

## How it works

Demo Mode creates a virtual "radio" that behaves like a physical FLEX-8600 but generates artificial RF noise instead of receiving real signals. The noise scene is fully configurable, making it useful for training, demonstrations, or testing AetherSDR features when no radio is available.

The simulation operates through the Demo Mode applet, which becomes visible only when the built-in Demo radio is connected.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| Noise channel toggles | checkbox | Enable or disable individual noise sources: pink noise, white noise, QRM bursts, birdies, and others. |
| Noise level sliders | slider | Adjust the level of each enabled noise source independently. |
| Scene presets | push button | Apply a one-click preset that configures all noise channels to match a specific simulated band condition, such as storm, night-40m, or contest pileup. |

## Before you start

- AetherSDR must be running and no physical radio connected (or you must intentionally use the Demo radio).

## Getting started

1. Open the **Connect** panel.
2. Select the **Demo** radio from the available radio list.
3. Click **Connect**.
4. The Demo Mode applet appears in the Applet Panel tray.

## Tips

- The Demo Mode applet only appears while the Demo radio is connected — if you don't see it, verify you're connected to the Demo radio, not a physical FLEX-8600.
- Scene presets are a quick way to simulate realistic band conditions without manually adjusting each noise channel.

## Related

- [Start the built-in demo radio](start-the-built-in-demo-radio.md)
- [Shape synthetic RF noise with per-channel controls](shape-synthetic-rf-noise-with-per-channel-controls.md)
- [Load a noise scene preset for realistic band simulation](load-a-noise-scene-preset-for-realistic-band-simulation.md)
