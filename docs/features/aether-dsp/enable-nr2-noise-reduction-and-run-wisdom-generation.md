# Enable NR2 noise reduction and run wisdom generation

AetherSDR's Main Window coordinates NR2 noise reduction and runs background wisdom generation to optimize its filter coefficients for your hardware.

## Before you start

- Confirm you are connected to a FlexRadio (LAN or SmartLink WAN) — NR2 controls are unavailable while disconnected.

## Steps

1. Open the Main Window (launched automatically on application start).
2. Locate the **NR2** noise reduction control in the receiver settings area and enable it.
3. Allow wisdom generation to run in the background — AetherSDR automatically starts the wisdom generation process after NR2 is enabled. Wait until the status indicator shows generation is complete before adjusting NR2 parameters.

## What each control does

| Control | Behavior |
|---|---|
| NR2 Enable | Turns on the NR2 noise-reduction DSP stage for the active receive slice. Triggers background wisdom generation on first use or when hardware configuration changes. |
| Wisdom generation (background process) | Computes optimized filter coefficients for NR2 on the current platform. Runs automatically; no manual start required. Application remains fully usable during generation. |

## Tips

- Wisdom generation only needs to run once per hardware configuration. Subsequent launches reuse the stored wisdom file unless hardware changes.
- If wisdom generation appears stalled, restart the application — generation resumes automatically.

## Related

- [main-window.md](main-window.md)
- [noise-reduction.md](noise-reduction.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
