# Switch to an External 10 MHz Reference

This page explains how to select an external 10 MHz reference clock on a connected FLEX-8600. Use an external reference when you have a GPS-disciplined oscillator or other precision 10 MHz source and want the radio to lock to it instead of its internal oscillator.

## Before you start

- AetherSDR must be connected to the radio. The Radio Setup dialog requires an active radio connection.
- Your external 10 MHz reference signal must be connected to the rear-panel REF IN port on the FLEX-8600 before switching the source.

## Steps

1. Click `Settings > Radio Setup...` to open the Radio Setup dialog.
2. Click the `RX` tab.
3. Locate the `10 MHz Reference Source:` combo box.
4. Select `External` from the combo box. To return to the built-in oscillator, select `Internal`.

## What each control does

| Control | Kind | Valid range |
|---|---|---|
| `10 MHz Reference Source:` | Combo box | `Auto` \| `TCXO` \| `GPSDO` \| `External`. Options shown depend on hardware installed. Lock status (Locked / Unlocked) is shown alongside the combo and updates live. |
| TX Follows Active Slice | Push button | TX follows the active slice. Mutually exclusive with Active Slice Follows TX. Disabled automatically during Split operation. |
| Active Slice Follows TX | Push button | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with TX Follows Active Slice. |
| Voice / CW / Digital filter sharpness sliders | Slider (0–3) | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode; slider is disabled when Auto is enabled. Commands sent as `radio filter_sharpness <mode> level=<N>`. |
| Auto (Voice / CW / Digital) | Toggle button | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. Commands sent as `radio filter_sharpness <mode> auto_level=1`. |
| Connect / Disconnect (TGXL) | Push button | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side path broken in firmware 4.2. If the IP field is empty and the radio has discovered the TGXL, the discovered IP is pre-filled. |
| Connect / Disconnect (PGXL) | Push button | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. |
| Connect / Disconnect (Antenna Genius) | Push button | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. |

## Frequency calibration (RX tab)

As of v0.9.2.1, the frequency calibration controls on the RX tab are always visible, regardless of whether a GPSDO is installed. When a GPSDO is present, the status label reads "GPSDO installed. Manual frequency offset calibration available." (shown in green). When no GPSDO is present, the label reads "Manual frequency offset calibration available." (shown in amber). In previous versions, the calibration controls were hidden when a GPSDO was detected.

### Calibration controls

| Control | Kind | Behavior |
|---|---|---|
| `Cal Frequency (MHz):` | Text field | Frequency used for manual calibration. Enter the exact frequency of your reference signal in MHz. |
| `Start` | Push button | Sets the calibration frequency, resets `freq_error_ppb` to 0, then starts the calibration sweep. The button is disabled and shows "Busy" while calibration is in progress. A status label beside the button shows the current state (Starting…, progress text, or result). The field must not be empty; if it is, the status label prompts you to enter a frequency before proceeding. |
| `Freq Offset (ppb):` | Spinbox | Manual frequency offset in parts per billion. Adjust if you need to apply a known offset without running the automated calibration sweep. |

### How to run a calibration sweep

1. Click `Settings > Radio Setup...` to open the Radio Setup dialog.
2. Click the `RX` tab.
3. Enter the exact frequency of your reference signal in the `Cal Frequency (MHz):` field.
4. Click `Start`. The button becomes disabled and shows "Busy". Watch the status label for progress.
5. When the sweep finishes, the status label reports the result and the `Start` button re-enables.

## Tips

- The `RX` tab also contains the `10 MHz Reference Source:` combo box. If you are using a GPS-disciplined oscillator, switch the reference source to `GPSDO` or `External` as appropriate before running calibration.
- If the `Cal Frequency (MHz):` field is empty when you click `Start`, the status label will prompt you to enter a frequency. No commands are sent to the radio in that case.

## Troubleshooting

- **Radio frequency appears unstable or offset after switching to External** — The REF IN signal may be absent, too low in level, or not exactly 10 MHz. Verify the external source is running and properly connected before selecting `External`. Switch back to `Internal` while diagnosing.
- **Start button remains disabled / shows "Busy" indefinitely** — This can occur if the radio does not respond to the `radio pll_start` command. Disconnect and reconnect to the radio, then try again.

## Related

- [Calibrate the GPSDO frequency offset](calibrate-the-gpsdo-frequency-offset.md)