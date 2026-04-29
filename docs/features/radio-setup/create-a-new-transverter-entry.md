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
| Connect / Disconnect (Antenna Genius) | Button | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. |

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

## Related

- [Radio Setup overview](overview.md)
- [Set per-band TX max power and tune mode](set-per-band-tx-max-power-and-tune-mode.md)