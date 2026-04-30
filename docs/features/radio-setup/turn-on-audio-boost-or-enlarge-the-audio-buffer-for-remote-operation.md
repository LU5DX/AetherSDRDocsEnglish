# Turn on audio boost or enlarge the audio buffer for remote operation

Use these settings to compensate for low receive volume or audio breakup when operating AetherSDR over a VPN or SmartLink connection. Audio Boost adds extra gain on the client audio path; a larger Audio Buffer absorbs network jitter at the cost of increased latency.

## Before you start

- AetherSDR must be connected to the radio. These controls are unavailable when no radio is connected.
- Open `Settings > Radio Setup...` and select the **Audio** tab before following the steps below.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. To increase receive volume, click **Audio Boost:** to toggle it on. The button shows its active state when enabled.
4. To reduce audio breakup or dropouts, click the **Audio Buffer:** spinbox and enter a value between 50 and 1000 ms. Higher values add more buffering at the cost of latency.
5. Close the dialog. Settings take effect immediately.

## What each control does

| Control | What it does | Valid range |
|---|---|---|
| **Audio Boost:** | Enables extra gain on the client audio path. | On / Off |
| **Audio Buffer:** | Sets the client-side audio buffer to absorb network jitter. Increase this when using VPN or SmartLink connections with unstable latency. | 50–1000 ms |
| **Audio Compression (SmartLink): Auto / Uncompressed / Opus** | Selects the audio codec used over SmartLink or LAN. | Auto / Uncompressed / Opus |
| **TX Follows Active Slice** | TX follows the active slice. Mutually exclusive with Active Slice Follows TX. Disabled automatically during Split operation. | On / Off |
| **Active Slice Follows TX** | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with TX Follows Active Slice. | On / Off |
| **Voice / CW / Digital filter sharpness sliders** | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode; slider is disabled when Auto is enabled. | 0–3 |
| **Auto (Voice / CW / Digital)** | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. | On / Off |
| **Connect / Disconnect (TGXL)** | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If the IP field is empty and the radio has discovered the TGXL, the discovered IP is pre-filled. | — |
| **Connect / Disconnect (PGXL)** | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. | — |
| **Connect / Disconnect (Antenna Genius)** | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. | — |
| **Select Installer...** | Opens a file picker that accepts .msi (FlexRadio v4.2+ WiX installer), .exe (older self-extracting installer), or a pre-extracted .ssdr firmware file. The firmware stager auto-detects format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the .ssdr without external tools. This button was labelled **Browse .ssdr...** before v0.9.3. | — |
| **APD (tab)** | External Adaptive Pre-Distortion sampler configuration — per-TX-antenna selection of the feedback sample port (INTERNAL / RX_A / RX_B / XVTA / XVTB) and an equalizer reset button. Tab is hidden unless the radio reports `apd configurable=1`. Only FLEX-8x00 series with SmartSDR 4.2.18+ firmware exposes this; 6000-series and pre-4.2.18 radios keep the tab invisible. | — |
| **ANT1 / ANT2 / XVTA / XVTB sampler combos (APD)** | Selects the feedback path the radio uses to sample the outgoing RF for APD training for that TX antenna. Choose an external RX/XVTR input when driving an external linear amplifier. Options are populated live from the radio's `apd sampler` sub-object. Falls back to INTERNAL if the radio reports an unrecognised value. | INTERNAL / RX_A / RX_B / XVTA / XVTB |
| **Equalizer Reset (APD)** | Sends `apd reset` to the radio, clearing all per-antenna APD training data so adaptation starts fresh. | — |
| **Themes (tab)** | UI customization tab — currently hosts the Slice Colors section. | — |
| **Use Aether defaults / Custom colors** | Switches the slice color scheme between the built-in AetherSDR palette and a fully custom per-slice set. | Use Aether defaults / Custom colors |
| **Slice A–H color buttons** | Click any lettered button (A–H) to open a color picker and assign a custom color for that slice. Changes are visible immediately in VFO widgets, panadapter overlays, and CAT channel badges. Buttons are disabled when **Use Aether defaults** is selected. Up to 8 slices supported. | — |
| **Reset All to Defaults (Themes)** | Resets all custom slice colors to the built-in AetherSDR palette. | — |

## Firmware update — selecting an installer (v0.9.3 change)

In v0.9.3 the firmware staging workflow changed. The button previously labelled **Browse .ssdr...** is now labelled **Select Installer...**. The file picker now accepts the full SmartSDR installer package in addition to a pre-extracted .ssdr file.

When **Check for Update** detects a newer firmware version, AetherSDR no longer downloads it automatically. Instead, the status label instructs you to download the SmartSDR installer from flexradio.com yourself, then use **Select Installer...** to stage it.

### How to stage and upload firmware

1. Click `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. Click **Check for Update**. If an update is available, the status label displays the version number and instructs you to download the installer from flexradio.com.
4. Download the SmartSDR installer from flexradio.com to your computer (.msi for v4.2+, .exe for older releases).
5. Click **Select Installer...**. In the file picker, select the downloaded .msi, .exe, or .ssdr file and click **Open**. The status label shows **Preparing firmware from \<filename\>...** and a progress bar appears while the stager extracts the firmware.
6. When staging completes, click **Upload Firmware** to transfer the firmware to the radio. A progress bar and status label track the upload.

> **Note:** If you already have a pre-extracted .ssdr file, you can select it directly in step 5. The stager detects the format automatically.

## RX tab — frequency calibration

In v0.9.2.1 the RX tab calibration section was revised. The **Cal Frequency (MHz):** field and **Start** button are now always visible regardless of whether a GPSDO is installed. When a GPSDO is present, the status label confirms it in green; when no GPSDO is installed, the label appears in amber. Both cases allow manual frequency offset calibration.

### Calibration controls

| Control | What it does |
|---|---|
| **Cal Frequency (MHz):** | Enter the known-accurate reference frequency in MHz to use for calibration. The field must not be empty before clicking Start. |
| **Start** | Begins the frequency calibration sequence. AetherSDR resets the frequency error to 0 ppb, then sends `radio pll_start` to the radio. The button is disabled and labelled **Busy** while calibration is running. A status label beside the button reports progress (Starting…, and subsequent states). |
| **Freq Offset (ppb):** | Displays or manually sets the current frequency offset in parts per billion. |
| **10 MHz Reference Source:** | Selects the oscillator reference: Auto, TCXO, GPSDO, or External. Options shown depend on installed hardware. Lock status (Locked / Unlocked) updates live beside the control. |

### How to run a frequency calibration

1. Click `Settings > Radio Setup...`.
2. Click the **RX** tab.
3. Enter a known-accurate reference frequency in **Cal Frequency (MHz):**.
4. Click **Start**. The button changes to **Busy** and the status label shows **Starting…**.
5. Wait for the status label to indicate completion. The button re-enables automatically.
6. If needed, review the resulting value in **Freq Offset (ppb):**.

> **Note:** If you leave **Cal Frequency (MHz):** empty and click **Start**, the status label shows **Enter cal frequency** and the sequence does not run.

## Tips

- Start with a modest buffer increase (200–300 ms) before going higher. Very large values make the audio noticeably sluggish during QSOs.
- If audio quality is poor over SmartLink, also review the codec setting (**Audio Compression (SmartLink):**). Switching from Auto to Opus can reduce bandwidth and improve stability on slow connections.

## Troubleshooting

- **Audio Boost and Audio Buffer controls are greyed out or missing** — These controls are on the **Audio** tab. Confirm you have selected that tab, not another tab such as **RX** or **Phone/CW**.
- **Increasing Audio Buffer has no effect on dropouts** — The buffer absorbs jitter but cannot compensate for sustained packet loss. Check your network path; also see [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md).
- **Start button stays disabled after calibration** — If the radio does not respond to `radio pll_start`, check that the radio is connected and not transmitting, then try again.
- **Select Installer... shows a progress bar but never enables Upload Firmware** — The stager was unable to extract a valid .ssdr from the selected file. Confirm you downloaded the correct SmartSDR installer for your radio family and try again.

## Related

- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md)