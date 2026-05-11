# Read the SW ALC meter (post-software-ALC SSB peak) on the Phone or CW panel

This page shows you how to monitor the software Automatic Level Control (ALC) meter, which reads the post-software-ALC SSB peak in dBFS. This meter helps you set your microphone gain or CW keying envelope so you transmit at an appropriate level without overdriving the audio chain.

## Before you start

- Ensure your FLEX-8600 is connected and the active slice is in a voice mode (Phone) or CW mode.
- The Phone/CW applet must be visible in the right sidebar — toggle it on using the **P/CW** tray button if needed.

## Steps

1. Locate the **ALC** gauge on either the Phone or CW sub-panel. It reads **-20 to 0 dBFS**, filling from right to left.
2. Key the transmitter (or, for CW, begin sending).
3. Watch the ALC gauge needle while you adjust your microphone gain with the **Mic gain** slider:
   - The meter is empty (at **-20 dBFS**) when no ALC is applied.
   - The gauge fills toward **0 dBFS** as ALC increases.
   - The red zone begins at **-3 dBFS** (marked on the gauge).
4. For CW, the same ALC gauge appears on the CW sub-panel — it is identical and driven by the same meter source.

## What each control does

| Control | Label | Behavior | Valid range | Default | Setting key |
|---------|-------|----------|-------------|---------|-------------|
| ALC gauge (Phone panel) | **ALC** | Shows automatic level control reading from the software ALC meter (post-software-ALC SSB peak in dBFS). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. Red zone above -3 dBFS. | -20 to 0 dBFS | — | None |
| ALC gauge (CW panel) | **ALC** | Mirrors the Phone-panel ALC gauge; both read from the same software ALC meter for consistent readings across voice and CW. | -20 to 0 dBFS | — | None |

## Related

- [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md)
- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
