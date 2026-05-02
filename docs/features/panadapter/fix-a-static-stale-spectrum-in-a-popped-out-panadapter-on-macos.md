# Fix a static/stale spectrum in a popped-out panadapter on macOS

On macOS, popping a panadapter out into a floating window can leave the spectrum frozen — the FFT and waterfall stop updating even though the radio is still connected. This is a known Metal/GPU surface issue that AetherSDR resolves automatically as of v0.9.5.1.

## Before you start

- AetherSDR v0.9.5.1 or later is installed. Earlier versions do not contain the fix.
- You are running macOS with a FLEX-8600 connected.
- You have more than one panadapter open (the ⬈ / ↩ pop-out button is hidden in single-pan mode).

## Steps

1. In the panadapter title bar, click ↩ to dock the floating panadapter back into the main window.
2. Click ⬈ to pop it out again.

AetherSDR resets the GPU resources and re-binds the Metal rendering surface to the new window during each float/dock cycle. After step 2 the spectrum should be live.

## Tips

- If the spectrum is still static after one dock/pop cycle, repeat the cycle once more. A stale WAN disconnect state can occasionally require a second reset.
- Quitting and relaunching AetherSDR also clears the condition. The application releases GPU resources during shutdown specifically to prevent a Metal teardown crash in this scenario.

## Troubleshooting

- **The ⬈ pop-out button is not visible** — You are in single-pan mode. Add a second panadapter to enable multi-pan mode; the title bar buttons appear only when more than one panadapter is present.
- **Spectrum is still frozen after dock/undock** — Confirm you are on v0.9.5.1 or later. Earlier builds do not call the GPU resource reset on float/dock cycles.

## Related

- [Pop a panadapter out into its own window](pop-a-panadapter-out-into-its-own-window.md)
- [Panadapter overview](overview.md)
