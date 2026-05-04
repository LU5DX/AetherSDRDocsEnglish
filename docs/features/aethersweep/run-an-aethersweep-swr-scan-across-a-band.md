# Run an AetherSweep SWR scan across a band

AetherSDR's AetherSweep feature lets you run an SWR sweep directly inside the panadapter display. Use it to check antenna match across a band without leaving the application.

## Before you start

- Confirm your FlexRadio hardware is connected (LAN or SmartLink WAN) and visible in the main window.
- Ensure no active transmission is in progress before starting the sweep.

## Steps

1. Open the AetherSDR Main Window (opens automatically on launch).
2. In the panadapter, set the displayed frequency range to the band segment you want to sweep.
3. Locate the **AetherSweep** controls in the main window toolbar or panadapter context menu.
4. Set **SWR Sweep Power** to the desired transmit power level in watts. This value is saved between sessions.
5. Start the sweep. AetherSweep transmits a stepped signal across the displayed band and plots the SWR result in the panadapter.
6. When the sweep completes, read the SWR curve overlaid on the panadapter. Peaks indicate frequency ranges with poor antenna match.

## What each control does

| Control | Behavior |
|---|---|
| SWR Sweep Power (Watts) | Sets the transmit power used during the sweep. Persisted across sessions. Lower values reduce stress on the final amplifier during testing. |

## Tips

- Keep sweep power at the minimum level needed for a reliable reading, especially when sweeping near other active stations.
- The SWR overlay remains visible after the sweep completes so you can compare it against the noise floor or signal activity in the panadapter. Retune or zoom in and run another sweep to examine a narrower segment in detail.
- Do not transmit into an unconnected or open antenna port; connect a proper load or antenna before sweeping.

## Related

- [Connect to a FlexRadio over LAN or SmartLink](connect-flexradio.md)
- [Panadapter layout and slice management](panadapter-layout.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
