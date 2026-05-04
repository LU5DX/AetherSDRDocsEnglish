# Enable NR2 noise reduction and run wisdom generation

AetherSDR's NR2 spectral noise reduction requires pre-generated FFTW wisdom data before it can run efficiently. The main window handles this automatically through its `enableNr2WithWisdom()` flow, which checks for valid wisdom, regenerates it in the background if needed, then activates NR2.

## Before you start

- AetherSDR must be connected to a FlexRadio (LAN or SmartLink WAN).
- If the application was built without FFTW3 support (`HAVE_FFTW3` not defined), NR2 is unavailable and wisdom generation is skipped automatically.
- Wisdom generation can take several minutes on first run. Do not close the application during this process.

## Steps

1. Launch AetherSDR. The main window opens automatically on application start.
2. In the noise reduction controls, enable **NR2**. If valid FFTW wisdom does not exist or cannot be imported, the application starts background wisdom generation before activating NR2. A progress indicator appears while generation runs.
3. Wait for wisdom generation to complete. NR2 activates automatically once wisdom is ready. You do not need to re-enable it manually.

> **Note:** Enabling NR2 disables any active DFNR or MNR noise reduction, as these modes are mutually exclusive.

## What each control does

| Control | Behavior |
|---|---|
| **NR2** (enable toggle) | Activates spectral noise reduction. Disables DFNR and MNR if either is on. Triggers background wisdom generation if no valid wisdom file exists or the existing file cannot be imported. |
| Wisdom generation progress | Displays progress during background FFTW wisdom generation. Generation runs off the audio worker thread to prevent audio interruption. |

## Tips

- Wisdom is stored on disk and reused across sessions. Generation only runs again if the wisdom file is missing or found to be unreadable at startup.
- If wisdom generation was interrupted in a previous session, AetherSDR detects the corrupt or missing file and regenerates it automatically on the next NR2 enable.
- If wisdom cannot be loaded when NR2 is enabled, AetherSDR falls back to runtime `FFTW_MEASURE` plans, which are slower to initialize. Check the application log for a warning if this occurs.

## Related

- [Noise reduction overview](noise-reduction-overview.md)
- [Connect to FlexRadio](connect-to-flexradio.md)
<!-- docmesh:llm version=v0.9.5.1 date=2026-05-04 -->
