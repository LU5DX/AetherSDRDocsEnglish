# Calibrate the GPSDO frequency offset

Use this page to correct the frequency reference of your FLEX-8600 using the built-in calibration controls. Accurate frequency calibration reduces dial error across all bands.

## Before you start

- AetherSDR must be connected to the radio. The RX tab in Radio Setup is only available when a radio connection is active.
- If a GPSDO is installed, the calibration controls are still available. Without a GPSDO, a yellow status message is shown instead of the green GPSDO confirmation.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **RX** tab.
3. In **Cal Frequency (MHz):**, enter the frequency of a known-accurate reference signal.
4. Click **Start** to begin the calibration sweep. The button label changes to **Busy** and a status message appears while the sweep runs. The **Start** button is disabled until the sweep completes or fails.
5. When the sweep completes, review the measured offset shown in **Freq Offset (ppb):**.
6. If you prefer to set the offset manually rather than using the sweep result, edit **Freq Offset (ppb):** directly.

## What each control does

| Control | Kind | Description |
|---|---|---|
| **Cal Frequency (MHz):** | Spinbox | The reference frequency used during the calibration sweep. Set this to a known-accurate signal — for example, a broadcast standard-frequency station. The field must not be empty before clicking **Start**; if it is empty, a warning is shown and the sweep does not start. |
| **Start** | Push button | Initiates the calibration sweep at the frequency entered in **Cal Frequency (MHz):**. Before starting, AetherSDR resets the current frequency error to zero (`freq_error_ppb=0`) so the sweep begins from a clean baseline. The button is disabled and shows **Busy** while the sweep is in progress. |
| **Freq Offset (ppb):** | Spinbox | The frequency offset applied to the radio's reference oscillator, in parts per billion. Can be set by the sweep or entered manually. |
| **10 MHz Reference Source:** | Combo box | Selects the oscillator reference source. Valid values: `Auto` \| `TCXO` \| `GPSDO` \| `External`. Options shown depend on the hardware installed. A live lock status indicator (Locked / Unlocked) appears alongside the combo box. |
| **TX Follows Active Slice** | Push button | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. |
| **Active Slice Follows TX** | Push button | Switches the active slice when TX moves externally (for example, from WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. |
| **Voice / CW / Digital filter sharpness sliders** | Slider | Sets filter sharpness (0 = lowest latency to 3 = sharpest) per mode. The slider is disabled when **Auto** is enabled for that mode. Commands sent as `radio filter_sharpness <mode> level=<N>`. |
| **Auto (Voice / CW / Digital)** | Toggle button | Enables automatic filter-level selection for that mode and disables the manual sharpness slider. Commands sent as `radio filter_sharpness <mode> auto_level=1`. |
| **Connect / Disconnect (TGXL)** | Push button | Opens or closes a direct TCP connection to the TGXL on port 9010. Saves the IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If the IP field is empty and the radio has already discovered the TGXL, the discovered IP is pre-filled. |
| **Connect / Disconnect (PGXL)** | Push button | Opens or closes a direct TCP connection to the Power Genius XL (default port 9008). Saves the IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. |
| **Connect / Disconnect (Antenna Genius)** | Push button | Opens or closes a connection to the Antenna Genius (default port 9007). Saves the IP and port to `AG_ManualIp` and `AG_ManualPort`. |

## Calibration status messages

Starting with v0.9.2.1, a status label appears next to the **Start** button and updates throughout the sweep.

| Message | Colour | Meaning |
|---|---|---|
| Starting... | Blue-grey | The calibration command sequence has been sent to the radio. |
| Enter cal frequency | Amber | **Cal Frequency (MHz):** was empty when **Start** was clicked. Enter a frequency and try again. |
| Busy | — | Shown on the **Start** button itself while a sweep is in progress. |

## GPSDO status banner

The banner at the top of the calibration group reflects whether a GPSDO is installed:

- **Green banner** — GPSDO is installed. Manual frequency offset calibration is still available.
- **Amber banner** — No GPSDO installed. Manual frequency offset calibration is available.

In v0.9.2.1 the green banner wording changed. Previously it read "GPSDO is installed. Frequency error correction is not required." It now reads "GPSDO installed. Manual frequency offset calibration available." This makes the behaviour consistent: the calibration controls are always shown regardless of GPSDO presence.

## Tips

- If you intend to use an external 10 MHz reference instead of the GPSDO, set **10 MHz Reference Source:** to `External` before calibrating, so the offset applies to the correct source.
- The sweep resets `freq_error_ppb` to zero before starting. If you have a manually entered offset that you want to preserve, note it down before clicking **Start**.

## Related

- [Switch to an external 10 MHz reference](switch-to-an-external-10-mhz-reference.md)
- [Radio Setup overview](overview.md)