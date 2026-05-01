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
| **10 MHz Reference Source:** | Combo box | Selects the oscillator reference source. Valid values: `Auto` \| `TCXO` \| `GPSDO` \| `External`. Options shown depend on hardware installed. Lock status (Locked / Unlocked) is displayed alongside the combo box and updates live. |
| **TX Follows Active Slice** | Push button | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. |
| **Active Slice Follows TX** | Push button | Switches the active slice when TX moves externally (for example, from WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. |
| **Voice / CW / Digital filter sharpness sliders** | Slider | Sets filter sharpness (0 = lowest latency to 3 = sharpest) per mode. The slider is disabled when **Auto** is enabled for that mode. Commands sent as `radio filter_sharpness <mode> level=<N>`. |
| **Auto (Voice / CW / Digital)** | Toggle button | Enables automatic filter-level selection for that mode and disables the manual sharpness slider. Commands sent as `radio filter_sharpness <mode> auto_level=1`. |
| **Connect / Disconnect (TGXL)** | Push button | Opens or closes a direct TCP connection to the TGXL on port 9010. Saves the IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If the IP field is empty and the radio has already discovered the TGXL, the discovered IP is pre-filled. |
| **Connect / Disconnect (PGXL)** | Push button | Opens or closes a direct TCP connection to the Power Genius XL (default port 9008). Saves the IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. |
| **Connect / Disconnect (Antenna Genius)** | Push button | Opens or closes a connection to the Antenna Genius (default port 9007). Saves the IP and port to `AG_ManualIp` and `AG_ManualPort`. The row is hidden from the Connected status if a ShackSwitch (rather than an Antenna Genius) is the connected device. |
| **Connect / Disconnect (ShackSwitch)** | Push button | Opens or closes a connection to a ShackSwitch antenna switch via the AG UDP/TCP protocol on port 9007. Saves the IP to `SS_ManualIp` and the port to `SS_ControlPort`. ShackSwitch is detected by the `ShackSwitch` field in the AG broadcast beacon. Auto-discovery via UDP also works without this row. The row is hidden from the Connected status if an Antenna Genius (non-ShackSwitch) is the connected device. |
| **⚙ Web UI (ShackSwitch)** | Push button | Opens the ShackSwitch device's local web configuration interface in the system browser. Uses the beacon's `webPort` if greater than 1024, otherwise falls back to `SS_WebPort` or port 5000. |
| **Select Installer...** | Push button | Opens a file picker that accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` firmware file. The firmware stager auto-detects the format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the `.ssdr` without external tools. When an update is available, the status label instructs you to download the SmartSDR installer from flexradio.com and then click **Select Installer...** to stage it. Label changed from **Browse .ssdr...** in v0.9.3. |
| **APD (tab)** | Tab | External Adaptive Pre-Distortion sampler configuration — per-TX-antenna selection of the feedback sample port (`INTERNAL` / `RX_A` / `RX_B` / `XVTA` / `XVTB`) and an equalizer reset button. Tab is hidden unless the radio reports `apd configurable=1`. Only FLEX-8x00 series with SmartSDR 4.2.18+ firmware exposes this; 6000-series and pre-4.2.18 radios keep the tab invisible. |
| **ANT1 / ANT2 / XVTA / XVTB sampler combos (APD)** | Combo box | Selects the feedback path the radio uses to sample the outgoing RF for APD training for that TX antenna. Choose an external RX/XVTR input when driving an external linear amplifier. Options are populated live from the radio's `apd sampler` sub-object. Falls back to `INTERNAL` if the radio reports an unrecognised value. |
| **Equalizer Reset (APD)** | Push button | Sends `apd reset` to the radio, clearing all per-antenna APD training data so adaptation starts fresh. |
| **Themes (tab)** | Tab | UI customization tab — currently hosts the Slice Colors section. |
| **Use Aether defaults / Custom colors** | Radio button | Switches the slice color scheme between the built-in AetherSDR palette and a fully custom per-slice set. |
| **Slice A–H color buttons** | Push button | Click any lettered button (A–H) to open a color picker and assign a custom color for that slice. Changes are visible immediately in VFO widgets, panadapter overlays, and CAT channel badges. Buttons are disabled when **Use Aether defaults** is selected. Up to 8 slices supported. |
| **Reset All to Defaults (Themes)** | Push button | Resets all custom slice colors to the built-in AetherSDR palette. |

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

## Firmware update workflow (v0.9.3)

In v0.9.3 the firmware update flow changed. AetherSDR no longer downloads and stages firmware automatically when an update is detected. Instead:

1. Click **Check for Update** on the **Radio** tab. If an update is available, the status label displays the version number and instructs you to download the SmartSDR installer from flexradio.com.
2. Download the installer from flexradio.com (`.msi` for SmartSDR 4.2+, `.exe` for older releases).
3. Click **Select Installer...** (previously labelled **Browse .ssdr...**) and choose the downloaded file. AetherSDR accepts `.msi`, `.exe`, or a pre-extracted `.ssdr` file and stages the firmware automatically, detecting the format from the file header.
4. Once staging completes, click **Upload Firmware** to transfer the firmware to the radio.

The **Check for Update** button no longer relabels itself as a download trigger after detecting an available update.

## ShackSwitch web interface (v0.9.4)

In v0.9.4, a **⚙ Web UI** button was added to the ShackSwitch row in the **Peripherals** tab. Click it to open the ShackSwitch device's local configuration page in your default system browser.

Port resolution order:

1. If the ShackSwitch beacon advertises a `webPort` greater than 1024, that port is used.
2. Otherwise, the value stored in `SS_WebPort` is used.
3. If neither is available, port 5000 is used as a fallback.

The button reads the IP from `SS_ManualIp`. If that setting is empty and a ShackSwitch is currently connected, the live peer address is used instead. If no IP can be determined, the button does nothing.

Also in v0.9.4, the **Antenna Genius** row in the **Peripherals** tab now correctly hides its Connected status when a ShackSwitch (rather than a true Antenna Genius) is the device actually connected through the AG protocol stack.

## Tips

- If you intend to use an external 10 MHz reference instead of the GPSDO, set **10 MHz Reference Source:** to `External` before calibrating, so the offset applies to the correct source.
- The sweep resets `freq_error_ppb` to zero before starting. If you have a manually entered offset that you want to preserve, note it down before clicking **Start**.

## Related

- [Switch to an external 10 MHz reference](switch-to-an-external-10-mhz-reference.md)
- [Radio Setup overview](overview.md)