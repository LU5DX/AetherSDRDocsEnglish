# Demo Mode overview

Demo Mode is a built-in simulation feature that lets you explore AetherSDR without a physical radio. It generates synthetic RF noise across multiple configurable channels, allowing you to practice tuning, filtering, and operating in realistic band conditions.

## How it works

Demo Mode creates a virtual "radio" that behaves like a physical FLEX-8600 but generates artificial RF noise instead of receiving real signals. The noise scene is fully configurable, making it useful for training, demonstrations, or testing AetherSDR features when no radio is available.

The simulation operates through the Demo Mode applet, which becomes visible only when the built-in Demo radio is connected.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| Noise channel toggles | checkbox | Enable or disable individual noise sources: pink noise, white noise, QRM bursts, birdies, and others. Hover over a toggle or its level slider to see a one-line description of what that noise source sounds like on a real HF rig and what causes it. |
| Noise level sliders | slider | Adjust the level of each enabled noise source independently. Hover over a slider to see the same descriptive tooltip as its channel toggle. |
| Scene presets | push button | Apply a one-click preset that configures all noise channels to match a specific simulated band condition, such as storm, night-40m, or contest pileup. |

## Noise source reference

Each noise channel toggle and level slider shows a tooltip explaining what that sound is, what causes it on a real receiver, and how to deal with it. Playing with the demo doubles as an HF primer:

| Channel | What it is | Practical note |
|---|---|---|
| CW tone | A Morse code signal — a wanted signal | Your filters and notch should spare this one. |
| Voice (speech) | An SSB voice signal | The wanted audio that noise reduction must preserve, not scrub. |
| White / AWGN | Flat thermal noise from the receiver itself | The baseline hiss that sets how weak a signal you can hear. |
| Pink / hiss | Atmospheric band noise, strongest on the low bands | The ever-present hiss behind every HF signal. |
| QRN crackle | Lightning static from distant thunderstorms | Worse in summer and on 160/80/40 m. A noise blanker helps. |
| Power-line | Mains buzz (50/60 Hz plus harmonics) | Typically caused by proximity to power lines or arcing insulators. |
| Static crash | Loud crashes from a nearby storm front | The bursts that ride over everything when weather is close. |
| Birdie carrier | A steady unwanted carrier (heterodyne) | Often a spur from nearby electronics — the classic notch-filter target. |
| SMPS hash | Broadband hash from switch-mode power supplies | Phone chargers, LED lamps, solar inverters near the antenna. |
| Woodpecker | A pulsed rasp from over-the-horizon radar | Named for the Cold-War Russian "Woodpecker" heard worldwide. |

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
- The preset and fault-injection button rows wrap onto multiple lines when the applet is docked in a narrow tray, so every button label stays fully visible at any width.

## Related

- [Start the built-in demo radio](start-the-built-in-demo-radio.md)
- [Shape synthetic RF noise with per-channel controls](shape-synthetic-rf-noise-with-per-channel-controls.md)
- [Load a noise scene preset for realistic band simulation](load-a-noise-scene-preset-for-realistic-band-simulation.md)