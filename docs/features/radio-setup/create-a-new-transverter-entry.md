The diff contains only internal implementation changes (adding `QDesktopServices`/`QUrl` includes, blank lines, internal `isRealAg` lambda refactor, `webPort` parsing from the discovery datagram, and late-enrichment logic in `AntennaGeniusModel`). None of these alter any user-visible control, behavior, setting key, or documented feature — the ShackSwitch row, ⚙ Web UI button, and all related documentation were already present in the current document. The Serial tab note about v0.9.4 deferred builder and CTS/DSR input assignment is also already documented. No user-facing documentation change is warranted.

# Create a new transverter entry

Use this page to add a transverter definition to your FLEX-8600 so AetherSDR knows the IF-to-RF frequency offset and operating parameters for your transverter band.

## Before you start

- The radio must be connected. Radio Setup requires an active radio connection.
- Know the IF frequency range your transverter uses and the RF frequency offset you want to display.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **XVTR** tab.
3. Click **Create New Transverter**.
4. A new nested tab appears. Configure the fields for the new entry on that tab.
5. To restrict the entry to receive only, set **RX Only:** to the enabled state.
6. To delete an entry you no longer need, click **Remove** on that entry's tab.
7. Close the dialog with **Close**.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Create New Transverter** | Button | Adds a new transverter entry and opens its configuration tab. |
| **RX Only:** | Toggle button | Forces the transverter to receive-only, preventing TX through it. |
| **Remove** | Button | Permanently deletes the selected transverter definition. |
| TX Follows Active Slice | Button | TX follows the active slice. Mutually exclusive with Active Slice Follows TX. Disabled automatically during Split operation. |
| Active Slice Follows TX | Button | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with TX Follows Active Slice. |
| Voice / CW / Digital filter sharpness sliders | Slider | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode; slider is disabled when Auto is enabled. Commands sent as `radio filter_sharpness <mode> level=<N>`. |
| Auto (Voice / CW / Digital) | Toggle button | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. Commands sent as `radio filter_sharpness <mode> auto_level=1`. |
| Connect / Disconnect (TGXL) | Button | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side `tgxl autotune handle=<H>` path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If the IP field is empty and the radio has discovered the TGXL, the discovered IP is pre-filled. |
| Connect / Disconnect (PGXL) | Button | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. |
| Connect / Disconnect (Antenna Genius) | Button | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. The row is hidden from the Connected state if a ShackSwitch (rather than a standard Antenna Genius) is the connected device. |
| Connect / Disconnect (ShackSwitch) | Button | Opens/closes connection to a ShackSwitch antenna switch via the AG UDP/TCP protocol on port 9007. Saves IP to `SS_ManualIp` and port to `SS_ControlPort`. ShackSwitch is detected by the 'ShackSwitch' field in the AG broadcast beacon. Auto-discovery via UDP also works without this row. Row hidden from Connected status if Antenna Genius (non-ShackSwitch) is the connected device. |
| ⚙ Web UI (ShackSwitch) | Button | Opens the ShackSwitch device's local web configuration interface in the system browser. Uses the beacon's `webPort` if greater than 1024, otherwise falls back to `SS_WebPort` or port 5000. |
| Select Installer... | Button | Opens a file picker that accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` firmware file. The firmware stager auto-detects format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the `.ssdr` without external tools. When an update is available, the status label instructs you to download the SmartSDR installer from flexradio.com and then use this button to stage it. Label changed from **Browse .ssdr...** in v0.9.3. |
| APD (tab) | Tab | External Adaptive Pre-Distortion sampler configuration — per-TX-antenna selection of the feedback sample port (INTERNAL / RX_A / RX_B / XVTA / XVTB) and an equalizer reset button. Tab is hidden unless the radio reports `apd configurable=1`. Only FLEX-8x00 series with SmartSDR 4.2.18+ firmware exposes this; 6000-series and pre-4.2.18 radios keep the tab invisible. |
| ANT1 / ANT2 / XVTA / XVTB sampler combos (APD) | Combo box | Selects the feedback path the radio uses to sample the outgoing RF for APD training for that TX antenna. Choose an external RX/XVTR input when driving an external linear amplifier. Options are populated live from the radio's `apd sampler` sub-object. Falls back to INTERNAL if the radio reports an unrecognised value. Default: INTERNAL. |
| Equalizer Reset (APD) | Button | Sends `apd reset` to the radio, clearing all per-antenna APD training data so adaptation starts fresh. |
| Themes (tab) | Tab | UI customization tab — currently hosts the Slice Colors section. |
| Use Aether defaults / Custom colors | Radio button | Switches the slice color scheme between the built-in AetherSDR palette and a fully custom per-slice set. |
| Slice A–H color buttons | Button | Click any lettered button (A–H) to open a color picker and assign a custom color for that slice. Changes are visible immediately in VFO widgets, panadapter overlays, and CAT channel badges. Buttons are disabled when **Use Aether defaults** is selected. Up to 8 slices supported. |
| Reset All to Defaults (Themes) | Button | Resets all custom slice colors to the built-in AetherSDR palette. |

## Firmware update (Radio tab)

Use the controls in the **Radio** tab to check for and apply firmware updates.

1. Click **Check for Update**. AetherSDR queries the FlexRadio update server.
   - If firmware is up to date, the status label shows the current version in green.
   - If an update is available, the status label shows the version number and instructs you to download the SmartSDR installer from flexradio.com.
2. Download the SmartSDR installer from flexradio.com (`.msi` for v4.2+, `.exe` for older releases).
3. Click **Select Installer...** and choose the downloaded installer or a pre-extracted `.ssdr` file. The stager detects the file format automatically and extracts the firmware without external tools. A progress indicator appears while staging completes.
4. Click **Upload Firmware** to transfer the staged firmware to the radio.

## Frequency calibration (RX tab)

In v0.9.2.1 the calibration controls on the **RX** tab are available regardless of whether a GPSDO is installed. Previously, **Cal Frequency (MHz):**, **Start**, and **Freq Offset (ppb):** were hidden when a GPSDO was detected. The status label at the top of the group now reads:

- **GPSDO installed. Manual frequency offset calibration available.** (green) — GPSDO present.
- **Manual frequency offset calibration available.** (amber) — no GPSDO.

### How calibration works in v0.9.2.1

The **Start** button now validates the cal frequency field before sending any commands, resets the frequency error to zero (`radio set freq_error_ppb=0`), then triggers the PLL sweep. While the sweep runs, **Start** is disabled and labeled **Busy**. A status label next to the button shows progress text. The button and label return to their normal states when the sweep completes or fails.

| Control | Behavior |
|---|---|
| **Cal Frequency (MHz):** | Enter the reference frequency in MHz used for calibration. Must not be empty before clicking Start. |
| **Start** | Validates the field, resets `freq_error_ppb` to 0, and starts the calibration sweep. Disabled and labeled **Busy** while a sweep is in progress. |
| **Freq Offset (ppb):** | Manual frequency offset in parts per billion. Applied directly without running a sweep. |
| Status label | Shows current calibration state: Starting, progress text, or error. Updates live during the sweep. |

## Tips

- Each transverter gets its own nested tab inside the XVTR tab. If you have multiple transverters, use those tabs to switch between entries.
- If you need to return to this dialog later to adjust a transverter, reopen `Settings > Radio Setup...` and go directly to the **XVTR** tab.
- On the **RX** tab, always enter a known accurate reference frequency in **Cal Frequency (MHz):** before clicking **Start**. Leaving the field empty cancels the sweep.
- When **Check for Update** reports a new firmware version, download the SmartSDR installer from flexradio.com before clicking **Select Installer...**. AetherSDR no longer downloads the installer automatically.
- The **APD** tab appears only on FLEX-8x00 radios running SmartSDR 4.2.18 or later. If you do not see it, your radio model or firmware version does not support configurable APD.
- Custom slice colors set on the **Themes** tab apply immediately to VFO widgets, panadapter overlays, and CAT channel badges. Select **Use Aether defaults** and click **Reset All to Defaults** to return to the standard palette.
- To open the ShackSwitch web interface, click **⚙ Web UI** in the ShackSwitch row of the **Peripherals** tab. The button uses the device's advertised web port when available; if the beacon does not supply a valid port, it falls back to `SS_WebPort` or port 5000.
- The **Antenna Genius** row hides its Connected status when a ShackSwitch is the active device. Use the **ShackSwitch** row to manage that connection instead.

## Related

- [Radio Setup overview](overview.md)
- [Set per-band TX max power and tune mode](set-per-band-tx-max-power-and-tune-mode.md)
<!-- docmesh:llm version=v0.9.4 date=2026-05-02 -->
