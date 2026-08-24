# Load a noise scene preset for realistic band simulation

This page explains how to load a one-click noise scene preset in Demo Mode, instantly shaping synthetic RF noise to simulate a specific band condition.

## Before you start

- The built-in Demo radio must be connected (see [Start the built-in demo radio](start-the-built-in-demo-radio.md))
- The Demo Mode applet must be visible in the Applet Panel

## Steps

1. Locate the Demo Mode applet in the Applet Panel tray (look for the "DEMO" label).
2. Find the **Scene presets** section containing preset buttons. The buttons wrap to multiple lines if the applet panel is narrow, so all labels remain fully visible.
3. Click the preset that matches the desired band scenario (e.g., **storm**, **night-40m**, **contest pileup**, **quiet band**, etc.).

The noise scene updates immediately: all noise channels (pink noise, white noise, QRM bursts, birdies, etc.) and their levels are set to match the selected preset.

## What each control does

| Control | Behavior |
|---------|----------|
| **Noise channel toggles** (checkboxes) | Enable or disable individual noise sources (pink noise, white noise, QRM bursts, birdies, etc.) |
| **Noise level sliders** | Adjust the per-channel level for each noise source |
| **Scene presets** (push buttons) | One-click buttons that configure all channels to match a specific scenario (storm, night-40m, contest pileup, quiet band, etc.) |

## Tips

- Scene presets override any manual channel toggles and level sliders you may have set.
- After loading a preset, you can still fine-tune individual noise channels using the toggles and sliders.
- Hover over any noise channel toggle or level slider to see a one-line explanation of what that noise source sounds like on a real HF band.
- If the preset buttons appear clipped, widen the applet panel — the buttons now wrap instead of compressing, so every label stays readable.

## Related

- [Demo Mode overview](overview.md)
- [Shape synthetic RF noise with per-channel controls](shape-synthetic-rf-noise-with-per-channel-controls.md)