# Configure FlexControl Serial Port Pin Functions

Use this page to assign a function and polarity to the DTR and RTS output pins on the serial port connected to your FlexControl or other serial-attached device. This lets AetherSDR drive external hardware — such as PTT lines or keyer inputs — through the serial port's control signals.

## Before you start

- The radio must be connected. The Serial tab requires an active radio connection.
- The Serial tab is only present when AetherSDR was built with serial port support (`HAVE_SERIALPORT`). If you do not see a Serial tab or a `Settings > FlexControl...` menu item, your build does not include this feature.
- Know the device path of your serial port (for example, `/dev/ttyUSB0` on Linux or `COM3` on Windows).

## Steps

1. Open `Settings > FlexControl...` — this jumps directly to the Serial tab of Radio Setup. Alternatively, open `Settings > Radio Setup...` and click the **Serial** tab.
2. In the **Port** combo box, select your serial device from the list. Click **Refresh** to rescan if your device is not shown, or type the path directly into the **Path** field.
3. Set the serial line parameters using the **Baud**, **Data**, **Parity**, and **Stop** combo boxes to match your device's requirements.
4. For the **DTR** pin, select the desired function from the **DTR** function combo box, then select the active polarity from the adjacent **Polarity** combo box.
5. For the **RTS** pin, repeat the same two selections — function and polarity — using the **RTS** function and **Polarity** combo boxes.
6. If your paddle connections are reversed, check **Paddle Swap (swap dit/dah)**.
7. To have AetherSDR open this port automatically each time it starts, check **Auto-open serial port on startup**.
8. If you are connecting a FlexControl tuning knob, click **Detect** under **FlexControl Tuning Knob** to identify the device. Click **Close** to release it.
9. To have AetherSDR detect the FlexControl knob automatically on startup, check **Auto-detect on startup**. To reverse the tuning direction, check **Invert tuning direction**.

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
| **DTR: Function** | Assigns a signal function to the DTR output pin. | — | Per combo box options |
| **DTR: Polarity** | Sets active-high or active-low polarity for DTR. | — | Per combo box options |
| **RTS: Function** | Assigns a signal function to the RTS output pin. | — | Per combo box options |
| **RTS: Polarity** | Sets active-high or active-low polarity for RTS. | — | Per combo box options |
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

## 10 MHz reference source changes in v0.9.7

The **10 MHz Reference Source:** combo box on the **RX** tab has been updated to populate and display more accurately based on detected hardware and live oscillator state.

Previously, the combo box listed only the options corresponding to hardware detected at the time the dialog opened (TCXO, GPSDO, External), and the lock status label showed only the raw oscillator state string followed by "Locked" or "Unlocked". Starting in v0.9.7, the combo box and status label behave as follows.

### Combo box population

The combo box is rebuilt dynamically. **Auto** is always present. Additional entries appear when any of the following is true for that source:

- The radio has reported any oscillator status (the state field is non-empty) — in this case **TCXO** and **External 10 MHz** are always included.
- The corresponding hardware is detected (`tcxoPresent`, `gpsdoPresent`, `extPresent`).
- The source matches the current setting or the current oscillator state.

The entry for an external reference is now labelled **External 10 MHz** instead of **External**.

The combo box selects the entry matching the radio's current oscillator setting. If that setting is not in the list, it falls back to the current combo selection, then to **Auto**.

### Lock status label

The lock status label beside the combo box now shows a richer description:

- When oscillator status has not yet been received: *Waiting for oscillator status* (shown in grey/blue).
- When **Auto** is selected and the radio has resolved to a specific source: *Auto -> \<resolved source\>* (for example, *Auto -> GPSDO*).
- When the setting and active state differ: *\<setting\> -> \<active state\>* (for example, *TCXO -> External 10 MHz*).
- Otherwise: the active source name alone.

In all cases the lock state is appended: *Locked* (shown in green) or *Unlocked* (shown in red). If the active source is **External 10 MHz** but no external reference is detected, *(not detected)* is appended after the lock state.

The label color is green (`#00c040`) when locked, red (`#c04040`) when unlocked, and grey-blue (`#8aa8c0`) while waiting for status.

### Updated RX tab reference source controls

| Control | What it does | Notes |
|---|---|---|
| **10 MHz Reference Source:** | Selects the oscillator reference source. Sends `radio oscillator <value>` to the radio when changed. | **Auto**, **TCXO**, **GPSDO**, and **External 10 MHz** entries. Options shown depend on hardware detected and live oscillator state. The value `ext` reported by the radio is treated as equivalent to `external`. |
| Lock status label | Shows the active source, resolution of Auto, and lock state. Updates live as the radio reports oscillator state changes. | Green = Locked; Red = Unlocked; Grey-blue = waiting for status. Appends *(not detected)* when External 10 MHz is active but no external reference signal is present. |

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
| **Slice A–H color buttons** | Open a color picker for each slice letter. | — | Changes apply immediately. |

## Radio Setup dialog changes in v26.5.1

The Radio Setup dialog now uses a `PersistentDialog` base class that saves and restores its geometry automatically. The dialog no longer uses a frameless window with a custom title bar — it returns to a standard operating system window frame. The `PersistentDialog` saves the window geometry to the `RadioSetupDialogGeometry` setting on close and restores it on open. No manual saving or restoring of geometry is performed in the `closeEvent` or constructor.

### Peripherals tab IP clearing

The **Peripherals** tab now properly handles clearing a saved manual IP address for TGXL, PGXL, and Antenna Genius devices. When the **Connect** / **Disconnect** button is clicked, the following logic applies:

- If connected and the IP field has been cleared, the saved manual IP and port are removed from settings before disconnecting. This ensures downstream handlers (for example, SmartSDR button visibility) see the cleared settings immediately.
- If disconnected and the IP field is empty with a previously saved manual IP present, clicking the button clears the saved manual IP and port from settings so the device stops auto-connecting.
- If disconnected and the IP field is empty with no saved manual IP, the button does nothing.

### Save-on-close for peripheral IP fields

When you close the Radio Setup dialog, the **closeEvent** persists any uncommitted "user cleared IP" edits from the Peripherals tab before the base class flushes