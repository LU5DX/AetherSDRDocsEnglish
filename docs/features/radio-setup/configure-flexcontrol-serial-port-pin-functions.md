# Configure FlexControl Serial Port Pin Functions

Use this page to assign a function and polarity to the DTR and RTS output pins on the serial port connected to your FlexControl or other serial-attached device. This lets AetherSDR drive external hardware — such as PTT lines or keyer inputs — through the serial port's control signals.

## Before you start

- The radio must be connected. The Serial tab requires an active radio connection.
- The Serial tab is only present when AetherSDR was built with serial port support (`HAVE_SERIALPORT`), or on Windows (where `Q_OS_WIN` is defined). If you do not see a Serial tab or a `Settings > FlexControl...` menu item, your build does not include this feature.
- Know the device path of your serial port (for example, `/dev/ttyUSB0` on Linux or `COM3` on Windows).

## Steps

1. Open `Settings > FlexControl...` — this jumps directly to the Serial tab of Radio Setup. Alternatively, open `Settings > Radio Setup...` and click the **Serial** tab.
2. In the **Port** combo box, select your serial device from the list. Click **Refresh** to rescan if your device is not shown, or type the path directly into the **Path** field.
3. Set the serial line parameters using the **Baud**, **Data**, **Parity**, and **Stop** combo boxes to match your device's requirements.
4. For the **DTR** pin, select the desired function from the **DTR** function combo box, then select the active polarity from the adjacent **Polarity** combo box.
5. For the **RTS** pin, repeat the same two selections — function and polarity — using the **RTS** function and **Polarity** combo boxes.
6. For the **CTS** pin, select the desired input function from the **CTS** function combo box, then select the active polarity from the adjacent **Polarity** combo box. Use this to wire a foot switch, straight key, or iambic paddle dit input to CTS.
7. For the **DSR** pin, repeat the same two selections — input function and polarity — using the **DSR** function and **Polarity** combo boxes. Use this for the iambic paddle dah input or a second PTT/CW key source.
8. If your paddle connections are reversed, check **Paddle Swap (swap dit/dah)**.
9. To have AetherSDR open this port automatically each time it starts, check **Auto-open serial port on startup**.
10. If you are connecting a FlexControl tuning knob, click **Detect** under **FlexControl Tuning Knob** to identify the device. Click **Close** to release it.
11. To have AetherSDR detect the FlexControl knob automatically on startup, check **Auto-detect on startup**. To reverse the tuning direction, check **Invert tuning direction**.

## What each control does

| Control | What it does | Default | Valid range / values |
|---|---|---|---|
| **Port** | Selects or enters the serial device path. | — | System serial ports |
| **Refresh** | Rescans for available serial ports. | — | — |
| **Path** | Editable field showing the selected port path. | — | Any valid device path |
| **Baud** | Serial baud rate. | — | Per combo box options |
| **Data** | Number of data bits. | — | Per combo box options |
| **Parity** | Parity setting. | — | Per combo box options |
| **Stop** | Number of stop bits. | — | Per combo box options |
| **DTR: Function** | Assigns a signal function to the DTR output pin. | None | None, PTT, CW Key, CW PTT |
| **DTR: Polarity** | Sets active-high or active-low polarity for DTR. | — | Active High / Active Low |
| **RTS: Function** | Assigns a signal function to the RTS output pin. | None | None, PTT, CW Key, CW PTT |
| **RTS: Polarity** | Sets active-high or active-low polarity for RTS. | — | Active High / Active Low |
| **CTS: Function** | Assigns an input function to the CTS pin so a foot switch, straight key, or iambic paddle wired to CTS can control PTT or CW keying. | None | None, PTT Input, CW Key Input, CW Dit Input, CW Dah Input |
| **CTS: Polarity** | Sets active-high or active-low polarity for the CTS input. | — | Active High / Active Low |
| **DSR: Function** | Assigns an input function to the DSR pin so a foot switch, straight key, or iambic paddle wired to DSR can control PTT or CW keying. | None | None, PTT Input, CW Key Input, CW Dit Input, CW Dah Input |
| **DSR: Polarity** | Sets active-high or active-low polarity for the DSR input. | — | Active High / Active Low |
| **Paddle Swap (swap dit/dah)** | Reverses dit and dah paddle inputs. | Unchecked | Checked / Unchecked |
| **Auto-open serial port on startup** | Reopens the configured port when AetherSDR launches. | Unchecked | Checked / Unchecked |
| **FlexControl Tuning Knob: Detect** | Detects a connected FlexControl knob. | — | — |
| **FlexControl Tuning Knob: Close** | Releases the FlexControl knob connection. | — | — |
| **Auto-detect on startup** | Automatically detects the FlexControl knob at launch. | Unchecked | Checked / Unchecked |
| **Invert tuning direction** | Reverses the direction of FlexControl tuning. | Unchecked | Checked / Unchecked |

## Firmware update changes in v0.9.3

The **Radio** tab firmware update workflow has changed. The **Browse .ssdr...** button has been renamed **Select Installer...** and now accepts three file types instead of only a pre-extracted `.ssdr` file:

- `.msi` — the WiX-based SmartSDR installer used by FlexRadio for firmware 4.2 and later.
- `.exe` — the older self-extracting SmartSDR installer.
- `.ssdr` — a pre-extracted firmware file (accepted as before).

The firmware stager detects the file format automatically from the first 8 bytes (OLE/MSI magic for `.msi`, PE/COFF MZ header for `.exe`) and extracts the `.ssdr` payload without requiring any external tools. A progress bar and status label update while the extraction runs.

In addition, the **Check for Update** button no longer changes into a **Download** button when a newer firmware version is found. Instead, when an update is available the status label instructs you to download the SmartSDR installer from flexradio.com yourself and then click **Select Installer...** to stage it.

### Updated Radio tab firmware controls

| Control | What it does | Notes |
|---|---|---|
| **Check for Update** | Queries for available firmware updates and reports the result in the status label. | When an update is found, the label directs you to download the installer from flexradio.com. The button label no longer changes to **Download**. |
| **Select Installer...** | Opens a file picker. Select a `.msi`, `.exe`, or `.ssdr` file. The stager extracts and stages the firmware automatically. | Renamed from **Browse .ssdr...** in v0.9.3. |
| **Upload Firmware** | Starts the firmware upload to the radio with a progress bar. | Enabled only after the stager completes extraction successfully. |

## Frequency calibration changes in v0.9.2.1

The **RX** tab frequency calibration section has been revised. Previously, the **Cal Frequency (MHz)** field and **Start** button were only shown when no GPSDO was detected. Starting in v0.9.2.1, those controls are always visible regardless of whether a GPSDO is installed.

The status message at the top of the calibration group changes depending on hardware:

- GPSDO installed — shown in green: *GPSDO installed. Manual frequency offset calibration available.*
- No GPSDO — shown in amber: *Manual frequency offset calibration available.*

The **Start** button now provides inline status feedback next to the button. While a calibration is in progress the button is disabled and its label changes to **Busy**. The status label shows the current stage (for example, *Starting…*) and updates as the calibration proceeds. The button is re-enabled when the calibration completes or fails.

Before starting calibration, AetherSDR now resets the stored frequency error to zero (`radio set freq_error_ppb=0`) before sending `radio pll_start`. If the **Cal Frequency (MHz)** field is empty when you click **Start**, the status label shows *Enter cal frequency* in amber and the calibration does not start.

### Updated RX tab calibration controls

| Control | What it does | Notes |
|---|---|---|
| **Cal Frequency (MHz):** | Frequency used for manual calibration. | Now always shown, with or without GPSDO. |
| **Start** | Starts the frequency calibration sweep. | Disabled and labelled **Busy** while active. Validates that a cal frequency has been entered before proceeding. |
| **Freq Offset (ppb):** | Manual frequency offset in parts per billion. | Reset to 0 automatically when **Start** is clicked. |

## Slice color themes (Themes tab)

The **Themes** tab was added in v0.9.3 under Radio Setup. It hosts the **Slice Colors** section, which lets you replace the built-in AetherSDR slice colors with a fully custom per-slice palette.

### Steps

1. Open `Settings > Radio Setup...` and click the **Themes** tab.
2. Select **Custom colors** to enable per-slice color assignment. Select **Use Aether defaults** to revert to the built-in palette.
3. When **Custom colors** is selected, click any lettered button (**A** through **H**) to open a color picker for that slice. The color takes effect immediately in VFO widgets, panadapter overlays, and CAT channel badges.
4. To revert all slices to the built-in colors, click **Reset All to Defaults**.

### Themes tab controls

| Control | What it does | Default | Notes |
|---|---|---|---|
| **Use Aether defaults** | Uses the built-in AetherSDR slice color palette. | Selected | Slice color buttons are disabled when this is active. |
| **Custom colors** | Enables per-slice color assignment. | — | Activates the A–H color buttons. |
| **Slice A–H color buttons** | Click a lettered button to open a color picker for that slice. Changes apply immediately. | — | Up to 8 slices supported. Buttons disabled when **Use Aether defaults** is selected. |
| **Reset All to Defaults** | Resets all custom slice colors to the built-in AetherSDR palette. | — | — |

## External APD tab (FLEX-8x00 only)

The **APD** tab configures the External Adaptive Pre-Distortion sampler. It is only visible when the connected radio reports `apd configurable=1`, which requires a FLEX-8x00 series radio running SmartSDR 4.2.18 or later firmware. The tab is hidden automatically for 6000-series radios and for any radio running firmware earlier than 4.2.18.

The APD system samples the outgoing RF signal and uses the feedback to train a pre-distortion model that linearises the transmitter. When driving an external linear amplifier, you can select an external receive input as the feedback path instead of the radio's internal coupler.

### Steps

1. Open `Settings > Radio Setup...`. If the **APD** tab is not visible, your radio or firmware does not support configurable APD.
2. For each TX antenna (**ANT1**, **ANT2**, **XVTA**, **XVTB**), select the feedback sample port from the corresponding combo box. Choose **INTERNAL** when transmitting directly into the radio's own load or antenna. Choose **RX_A**, **RX_B**, **XVTA**, or **XVT
<!-- docmesh:llm version=v0.9.4 date=2026-05-02 -->
