# RX Controls overview

The RX Controls applet gives you per-slice control over every receive parameter: mode, frequency, antenna selection, filter width, AGC, audio, squelch, RIT/XIT, and FM repeater settings. Open it whenever you need to configure how a slice receives or transmits.

## How it works

The RX applet is always present in the Applet Panel (right sidebar). Toggle its visibility with the RX tray button. When the radio supports more than one slice, a row of slice tabs (A through H) appears at the top; clicking a tab binds the applet to that slice. All controls below the tab row affect the currently selected slice only.

Filter width presets are the one setting that persists across sessions, stored under the `FilterPresets` key. Every other control reflects live radio state and is not independently saved by AetherSDR.

## What each control does

### Slice selection and identity

| Control | Default | Behavior |
|---|---|---|
| Slice tabs (A..H) | — | Select which slice the applet controls. The tab row is hidden when the radio has only one slice. Button borders and active backgrounds follow the per-slice color set in SliceColorManager. |
| Slice badge | A | Displays the letter of the active slice. Color is driven by SliceColorManager; customizable per-slice colors persist across sessions and are reflected here, in the slice tab buttons, VFO widgets, and meter strips. Read-only. |
| 🔓 / 🔒 | 🔓 (unlocked) | Toggles tune-lock. A locked slice ignores frequency changes from the panadapter and other sources. |
| TX (badge) | — | Click to designate this slice as the TX slice. |

### Frequency and mode

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| Mode combo | USB | USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, NT, RTTY (+ RADE if HAVE_RADE build flag is set) | Sets slice mode. Changing mode reshapes filter and step presets automatically. |
| Frequency label | 0.000.000 | — | Displays the current VFO frequency with dotted grouping. Click to enter edit mode. |
| Frequency edit | — | 0.001–54.000 MHz (up to 450.000 MHz on XVTR) | Type a frequency in MHz and press Enter to tune and re-center. Press Escape to cancel and restore the previous frequency. |
| STEP | 100 Hz | Per-mode list (e.g. SSB: 1, 10, 50, 100, 500, 1000, 2000, 3000 Hz) | Click the left/right triangle buttons or use the mouse wheel to cycle through step sizes. The available steps change with mode. |

### Antenna selection

| Control | Default | Behavior |
|---|---|---|
| ANT1 (RX antenna) | ANT1 | Opens a menu of available antennas from the radio's antenna list. Select to set the RX antenna for this slice. Label is blue. |
| ANT1 (TX antenna) | ANT1 | Opens a menu of TX-capable antennas. RX-only ports (names starting with `RX`) are excluded. Label is red. |

### Filter

| Control | Default / range | Setting key | Behavior |
|---|---|---|---|
| Filter width presets | USB/LSB: 1800/2100/2400/2700/2900/3300 Hz; CW: 50/100/250/400 Hz; AM/SAM: 5600–14000 Hz; DIG: 100–2000 Hz; RTTY: 250–1000 Hz | `FilterPresets` | Click a button to apply that width. Right-click to save the current filter width as a preset. Buttons are hidden in FM, NFM, and DFM modes. |
| Filter width label | 2.7K | — | Shows the current filter bandwidth. Updates when a preset is applied or the passband is dragged. Read-only. |
| Filter passband widget | — | — | Drag the low or high edge to set a custom filter passband. |

### AGC

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| AGC mode | Med | Off, Slow, Med, Fast | Sets the AGC response speed. Hidden in FM family modes. |
| AGC threshold | 65 | 0–100 | Sets the AGC threshold. When AGC mode is Off, adjusts the AGC off-level instead. |

### Audio

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| 🔊 / 🔇 (mute) | 🔊 (unmuted) | — | Mutes or unmutes the slice audio output. |
| AF gain | 70 | 0–100 | Adjusts the slice audio output level. |
| L / R pan | 50 | 0–100 | Pans audio between left (0) and right (100) channels. Double-click to reset to centre (50). |
| SQL | — | — | Enables squelch at the level set by the squelch slider. Disabled and forced off in DIGU, DIGL, NT, CW, and CWL modes. |
| Squelch level | 20 | 0–100 | Sets the squelch threshold. Takes effect only when SQL is on. |

### RIT and XIT

| Control | Default | Behavior |
|---|---|---|
| RIT | off | Toggles Receive Incremental Tuning on or off. |
| RIT 0 | — | Zeroes the RIT offset immediately. |
| RIT offset | +0 Hz | Adjust with the left/right buttons or mouse wheel in 10 Hz steps. |
| XIT | off | Toggles Transmit Incremental Tuning on or off. |
| XIT 0 | — | Zeroes the XIT offset immediately. |
| XIT offset | +0 Hz | Adjust with the left/right buttons or mouse wheel in 10 Hz steps. |

### Noise reduction and DSP filter buttons

The following DSP filter buttons are visible in non-FM modes. Button availability depends on the radio series.

| Button | Availability | Behavior |
|---|---|---|
| NR | All series | Enables noise reduction. Hidden in FM family modes. |
| NR2 | All series | Enables noise reduction mode 2. Hidden in FM family modes. |
| NB | All series | Enables noise blanker. Hidden in FM family modes. |
| NRL | All series (including 6000-series) | Enables noise reduction (NRL algorithm). Hidden in FM family modes. Available on 6000-series radios as of V0.9.4; previously required 8000-series firmware. |
| NRS | 8000-series only | Enables NRS noise reduction. Hidden in FM family modes. |
| RNN | 8000-series only | Enables RNN noise reduction. Hidden in CW and FM family modes. |
| NRF | 8000-series only | Enables NRF noise reduction. Hidden in FM family modes. |

### Indicators

| Indicator | States | Meaning |
|---|---|---|
| QSK | Grey / amber | Lights amber when CW full break-in is active. Controlled from the CW applet; read-only here. |

### FM repeater controls

These controls are visible only when the slice mode is FM, NFM, or DFM.

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| Tone mode (FM) | Off | Off, CTCSS TX | Selects whether a CTCSS tone is sent on transmit. |
| CTCSS tone value | — | 67.0–254.1 Hz (41 standard EIA/TIA-603 tones) | Selects the CTCSS tone frequency. Active only when Tone mode is CTCSS TX. |
| Offset (FM) | 0.0 MHz | 0.0–100.0 MHz (step 0.1) | Sets the FM repeater offset frequency. |
| − (offset down) | — | — | Sets the TX frequency below the RX frequency by the offset amount. |
| Simplex | checked | — | Sets TX and RX to the same frequency (no offset). |
| + (offset up) | — | — | Sets the TX frequency above the RX frequency by the offset amount. |
| REV | — | — | Inverts the offset direction to work a reversed repeater pair. |

## Peripherals tab — manual IP connect

The Peripherals tab in the Radio Setup dialog lets you manually connect to external devices by IP address. The following rows are available.

### Antenna Genius (AG) — row 3

Connects to an Antenna Genius device at the specified IP and port. The "Connected" status is shown only when the connected device is an Antenna Genius proper. If the connection is actually to a ShackSwitch, the AG row shows as disconnected and the ShackSwitch row shows as connected instead.

### ShackSwitch — row 4 (added in V0.9.4)

| Control | Setting key | Default | Behavior |
|---|---|---|---|
| IP address field | `SS_ManualIp` | — | Enter the IP address of the ShackSwitch. |
| Port field | `SS_ControlPort` | 9007 | Port used for the AG control protocol. Always connects on port 9007 regardless of the value entered. |
| Connect button | — | — | Connects to the ShackSwitch at the specified IP on port 9007 using the AG control protocol. |
| Disconnect button | — | — | Disconnects from the ShackSwitch. |
| Connected status | — | — | Shows "Connected" only when the active connection is to a ShackSwitch device. |
| ⚙ Web UI button | `SS_ManualIp`, `SS_WebPort` | port 5000 | Opens the ShackSwitch web interface in your browser. Uses the live peer address if a ShackSwitch is currently connected. Uses `SS_WebPort` from settings if set and greater than 1024, otherwise falls back to the device's advertised `webPort` if valid (>1024), then defaults to port 5000. Does nothing if no IP address can be determined. |

Both the AG and ShackSwitch rows share the underlying `AntennaGeniusModel` connection. Connecting to one will reflect as disconnected in the other.

## AppletPanel accessors and visibility methods

The following accessor methods and visibility helpers are available on `AppletPanel`. They are used internally and by code that coordinates device presence with applet state.

### Applet accessors

| Method | Returns | Description |
|---|---|---|
| `tciApplet()` | `TciApplet*` | Returns the TCI applet instance. |
| `daxIqApplet()` | `DaxIqApplet*` | Returns the DAX IQ applet instance. |
| `agApplet()` | `AntennaGeniusApplet*` | Returns the Antenna Genius applet instance. |
| `ssApplet()` | `ShackSwitchApplet*` | Returns the ShackSwitch applet instance. Added in V0.9.4. |
| `meterApplet()` | `MeterApplet*` | Returns the meter applet instance. |
| `mqttApplet()` | `MqttApplet*` | Returns the MQTT applet instance. Available only in HAVE_MQTT builds. |

### Visibility helpers

| Method | Description |
|---|---|
| `setAgVisible(bool visible)` | Shows or hides the Antenna Genius button and applet based on device presence. |
| `setShackSwitchVisible(bool visible)` | Shows or hides the ShackSwitch applet based on device presence. Added in V0.9.4. |
| `resetOrder()` | Resets applet order to the default arrangement. |

## Tips

- The L
<!-- docmesh:llm version=v0.9.4 date=2026-05-01 -->