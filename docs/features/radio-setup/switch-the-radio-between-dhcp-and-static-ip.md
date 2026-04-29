# Switch the Radio Between DHCP and Static IP

Use this page to change how the FLEX-8600 obtains its network address — either automatically via DHCP or with a fixed static IP, subnet mask, and gateway you specify.

## Before you start

- AetherSDR must be connected to the radio. The Network tab is only available when a radio connection is active.
- If you are switching to static IP, have the IP address, subnet mask, and gateway values ready before you begin.
- Changing the network configuration will cause the radio to move to a new address. You will need to reconnect after applying.

## Steps

1. Click `Settings > Radio Setup...` to open the Radio Setup dialog.
2. Click the **Network** tab.
3. Note the current **IP Address**, **Mask**, and **MAC Address** shown as read-only indicators.
4. Click the **DHCP / Static** toggle button to switch modes. The button reflects the current mode; clicking it switches to the other.
5. If you selected static mode, fill in the **IP Address:**, **Mask:**, and **Gateway:** text fields with the values for your network.
6. Click **Apply** to push the network configuration to the radio.
7. Reconnect to the radio at its new address using `Settings > Connect to Radio...`.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **IP Address / Mask / MAC Address** | Indicators (read-only) | Displays the radio's current network addresses. |
| **DHCP / Static** | Toggle button | Switches the radio between DHCP and static IP modes. |
| **IP Address:** | Text field | Static IP address to assign to the radio. Active only in static mode. |
| **Mask:** | Text field | Subnet mask for the static configuration. Active only in static mode. |
| **Gateway:** | Text field | Default gateway for the static configuration. Active only in static mode. |
| **Apply** | Push button | Sends the network configuration to the radio. |
| **TX Follows Active Slice** | Push button | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. |
| **Active Slice Follows TX** | Push button | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. |
| **Voice / CW / Digital filter sharpness sliders** | Sliders (0–3) | Sets filter sharpness (0 = lowest latency to 3 = sharpest) per mode. Slider is disabled when Auto is enabled. Commands sent as `radio filter_sharpness <mode> level=<N>`. |
| **Auto (Voice / CW / Digital)** | Toggle button | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. Commands sent as `radio filter_sharpness <mode> auto_level=1`. |
| **Connect / Disconnect (TGXL)** | Push button | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If the IP field is empty and the radio has discovered the TGXL, the discovered IP is pre-filled. |
| **Connect / Disconnect (PGXL)** | Push button | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. |
| **Connect / Disconnect (Antenna Genius)** | Push button | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. |

## Frequency calibration (RX tab)

The **RX** tab provides manual frequency offset calibration and 10 MHz reference source selection. In v0.9.2.1 the calibration controls are always shown regardless of whether a GPSDO is installed. A status label at the top of the group indicates the GPSDO state:

- **GPSDO installed** — label shown in green: *GPSDO installed. Manual frequency offset calibration available.*
- **No GPSDO** — label shown in amber: *Manual frequency offset calibration available.*

### Calibration controls

| Control | Kind | Behavior |
|---|---|---|
| **Cal Frequency (MHz):** | Spinbox / text field | Frequency used for calibration. Must not be empty before starting. |
| **Start** | Push button | Starts the frequency calibration sequence. Sets `cal_freq`, resets `freq_error_ppb` to 0, then triggers the radio PLL calibration. The button is disabled and shows **Busy** while calibration is running. A status label beside the button reports progress (Starting… / running / result). |
| **Freq Offset (ppb):** | Spinbox | Manual frequency offset in parts per billion. Set to 0 automatically at the start of a calibration run. |
| **10 MHz Reference Source:** | Combo box | Selects oscillator reference source: Auto, TCXO, GPSDO, or External. Options shown depend on installed hardware. Live lock status (Locked / Unlocked) is displayed alongside the combo. |

### How calibration works in v0.9.2.1

1. Enter the known reference frequency in **Cal Frequency (MHz):**.
2. Click **Start**. AetherSDR sends `radio set cal_freq=<value>` and `radio set freq_error_ppb=0` to the radio, then issues `radio pll_start` to begin the sweep.
3. The **Start** button is disabled and labeled **Busy** until the sequence completes or fails.
4. The status label beside the button updates in real time. When calibration finishes the button re-enables and the label shows the result.

If the **Cal Frequency (MHz):** field is empty when you click **Start**, the status label shows *Enter cal frequency* in amber and calibration does not start.

> **Note:** Prior to v0.9.2.1, the calibration controls were hidden when a GPSDO was detected. They are now always available.

## Tips

- The **IP Address / Mask / MAC Address** indicators show what the radio is currently using. Record these values before making changes so you can revert if needed.
- The **Enforce Private IP Connections:** toggle on the same tab rejects connections from non-RFC1918 addresses. If you assign a static IP, confirm it falls within a private range (e.g. 192.168.x.x, 10.x.x.x) if that toggle is enabled.

## Troubleshooting

- **Cannot find the radio after clicking Apply** — The radio has moved to its new address. Use `Settings > Connect to Radio...` to discover and reconnect to it on the updated address.
- **IP Address:, Mask:, and Gateway: fields are not editable** — The toggle is set to DHCP. Click **DHCP / Static** to switch to static mode first.
- **Start button stays disabled after calibration** — If the dialog is closed or the radio disconnects while calibration is running, the button state is discarded. Reopen Radio Setup and try again.
- **Status label shows "Enter cal frequency"** — Type a valid frequency in MHz in the **Cal Frequency (MHz):** field before clicking **Start**.

## Related

- [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md)
- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)