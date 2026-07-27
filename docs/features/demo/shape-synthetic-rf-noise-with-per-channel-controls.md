# Shape synthetic RF noise with per-channel controls

Shape the simulated RF environment when using the built-in Demo radio by enabling or disabling individual noise sources and adjusting their levels.

## Before you start

- Connect to the built-in Demo radio from the **Settings > Connect to Radio...** dialog or the Connect panel

## Steps

1. Open the Demo Mode applet from the Applet Panel tray (the DEMO tray button appears only when the Demo radio is connected).
2. In the applet, find the **Noise channel toggles** section. Each checkbox controls a separate noise source: pink noise, white noise, QRM bursts, birdies, and others.
3. Check a checkbox to enable that noise source; uncheck it to disable.
4. For each enabled noise source, adjust its **Noise level slider** to set the intensity.
5. Optionally, click a **Scene presets** button to set all channels at once for a specific scenario (storm, night-40m, contest pileup, quiet band, etc.).

## What each control does

| Control | Action |
|---------|--------|
| Noise channel toggles (checkboxes) | Enable or disable individual noise sources. Sources available: pink noise, white noise, QRM bursts, birdies, and others. |
| Noise level sliders | Adjust the level of each enabled noise source independently. |
| Scene presets (buttons) | Apply a pre-configured combination of noise channels and levels to simulate a specific band condition. |

## Tips

- Start with all noise sources disabled (all checkboxes unchecked) to hear the cleanest simulation, then enable sources one at a time to understand their character.
- Use scene presets as a quick starting point, then fine-tune individual sliders.

## Related

- [Start the built-in demo radio](start-the-built-in-demo-radio.md)
- [Load a noise scene preset for realistic band simulation](load-a-noise-scene-preset-for-realistic-band-simulation.md)
- [Demo Mode overview](overview.md)
