# Tuner overview

The Tuner applet provides control and monitoring for the 4O3A Tuner Genius XL external antenna tuner.

## Prerequisites

- A 4O3A Tuner Genius XL must be present on your network.
- The TGXL must be detected by AetherSDR automatically or configured manually.

## Accessing the Tuner applet

Click the **TUN** button in the right sidebar to open or close the Tuner applet. The applet is hidden until a TGXL is detected.

## Applet layout

The Tuner applet contains:

- **Forward power gauge** (Fwd Pwr) — displays forward power in watts
- **SWR gauge** — displays SWR ratio (1.0–3.0)
- **Relay bars** (C1, L, C2) — show current relay bank positions
- **TUNE button** — starts an autotune cycle
- **OPERATE/BYPASS/STANDBY button** — cycles tuner mode
- **ANT 1/2/3 buttons** — antenna port selection (only visible when direct TGXL connection is active)

## Network connections

The Tuner Genius XL can connect to AetherSDR through two paths:

1. **Radio firmware path** — The TGXL communicates through the FlexRadio's network connection. This is the default.
2. **Direct connection (port 9010)** — AetherSDR connects directly to the TGXL. This enables:
   - Mousewheel adjustment of C1/L/C2 relays
   - ANT 1/2/3 antenna switch selection
   - Bypass of the radio's firmware path for autotune commands

Configure the connection in **Radio Setup → Tuner**.

## Related pages

- [Put the tuner in OPERATE, BYPASS, or STANDBY](#)
- [Monitor forward power and SWR on the Tuner applet](#)
- [Run an autotune on the external TGXL](run-an-autotune-on-the-external-tgxl.md)
- [Read SWR immediately after a tune](read-swr-immediately-after-a-tune.md)
- [Fine-tune the C1/L/C2 relays with the mousewheel](fine-tune-the-c1-l-c2-relays-with-the-mousewheel.md)

---

# Put the tuner in OPERATE, BYPASS, or STANDBY

Use the OPERATE button in the Tuner applet to cycle the 4O3A Tuner Genius XL through its three relay states: OPERATE, BYPASS, and STANDBY.

## Before you start

- AetherSDR must be connected to the radio. The Tuner applet is hidden until a Tuner Genius XL is detected.
- The TUN tray button must be available in the right sidebar, indicating the TGXL has been detected.

## Steps

1. Click the TUN tray button on the right sidebar to open the Tuner applet.
2. Locate the OPERATE button in the lower-right area of the applet.
3. Click OPERATE to advance to the next state. Each click cycles one step forward:
   - OPERATE → BYPASS
   - BYPASS → STANDBY
   - STANDBY → OPERATE

## What each control does

| Button | Color when active | Meaning |
|---|---|---|
| OPERATE | Green | Tuner relays are in circuit and active. |
| BYPASS | Orange | Tuner is energized but the matching network is bypassed. |
| STANDBY | Default (theme-dependent) | Tuner is not operating. |

The button label and color update immediately when the TGXL acknowledges the state change.

## Tips

- The button always shows the **current** state, not the next state. A green OPERATE label means the tuner is already in OPERATE.
- Clicking once from STANDBY returns the tuner to OPERATE and restores the green color. You do not need to pass through BYPASS to get back to OPERATE.

## Troubleshooting

- **The TUN tray button is not visible** — The Tuner applet is hidden until a Tuner Genius XL is detected on the network. Verify the TGXL is powered on and connected. See [Tuner overview](overview.md).
- **The button label does not change after clicking** — The label updates only when the TGXL confirms the new state. If the label stays the same, check the connection between AetherSDR and the TGXL.

## Related

- [Tuner overview](overview.md)
- [Run an autotune on the external TGXL](run-an-autotune-on-the-external-tgxl.md)
- [Read SWR immediately after a tune](read-swr-immediately-after-a-tune.md)
- [Fine-tune the C1/L/C2 relays with the mousewheel](fine-tune-the-c1-l-c2-relays-with-the-mousewheel.md)

---

# Monitor forward power and SWR on the Tuner applet

The Tuner applet displays forward power and SWR gauges reported by the 4O3A Tuner Genius XL.

## Before you start

- AetherSDR must be connected to the radio and the TGXL must be detected on the network.

## Steps

1. Click the TUN tray button on the right sidebar to open the Tuner applet.
2. Locate the **Fwd Pwr** gauge at the top of the applet. It displays forward power in watts.
3. Locate the **SWR** gauge below it. It displays the SWR ratio.

## Gauge scaling

The forward power gauge scale depends on your hardware configuration:

| Configuration | Scale range |
|---|---|
| Barefoot (no amplifier) | 0–200 W |
| Aurora amplifier | 0–600 W |
| PGXL amplifier | 0–2000 W |

The SWR gauge ranges from 1.0 to 3.0. Values above 2.5 display in red to indicate a high SWR condition.

## Gauge performance improvements in v26.8.4

The forward power gauge scale is now only updated when the hardware configuration actually changes (for example, when you connect or disconnect a PGXL). Previously, the gauge scale was reapplied on every radio status update, which could cause unnecessary screen repaints and visible flicker. This change improves UI responsiveness, especially during rapid status updates while transmitting.

## Important behavior changes in v26.6.3

- **SWR gauge now resets to 1.0 when forward power is below 5 W.** The TGXL reports an SWR of 99.9 at idle when no incident signal is present. To prevent this from pegging the gauge, the SWR bar resets to 1.0 whenever forward power drops below 5 W. This matches the threshold used for the SWR label display.
- **Accessible names added** for screen reader support: "Forward power", "SWR", "Tuner capacitor C1", "Tuner inductor L", "Tuner capacitor C2".

## Troubleshooting

- **The SWR gauge shows 1.0 even when transmitting** — Check that forward power exceeds 5 W. The SWR gauge only displays the measured value when forward power is at least 5 W.
- **The forward power gauge flickers during status updates** — If you are running a version before v26.8.4, upgrade to v26.8.4 or later. The gauge scale is now only recalculated when your hardware configuration changes.

## Related

- [Put the tuner in OPERATE, BYPASS, or STANDBY](#)
- [Run an autotune on the external TGXL](run-an-autotune-on-the-external-tgxl.md)

---

# Run an autotune on the external TGXL

Use the TUNE button in the Tuner applet to start an automatic tuning cycle on the 4O3A Tuner Genius XL.

## Before you start

- The Tuner applet must be open. The TGXL must be detected on the network.
- Ensure your radio is transmitting at a suitable power level for tuning (typically 5–100 W).
- The tuner must be in OPERATE mode. The TUNE button will not respond in BYPASS or STANDBY mode.

## Steps

1. Click the **TUNE** button in the Tuner applet.
2. The button label changes to **TUNING...** and turns red while the tuning cycle is in progress.
3. When tuning completes, the button label flashes **SWR x.xx** for approximately 2.5 seconds, showing the post-tune SWR.
4. After the flash, the button returns to its default **TUNE** label.

## Direct connection behavior (v0.9.2.1 and later)

When a direct TGXL connection is configured (port 9010) in Radio Setup → Tuner, the autotune command is sent directly to the TGXL, bypassing the radio's firmware path. This resolves tuning issues that some users experienced with FlexRadio firmware 4.2.

When no direct connection is configured, the autotune command routes through the radio's firmware path.

Configure the direct connection in **Radio Setup → Tuner**.

## Tips

- The TUNE button will not respond if the tuner is in BYPASS or STANDBY mode. Set the tuner to OPERATE first.
- The post-tune SWR flash allows you to read the final SWR immediately after tuning without having to watch a separate meter.

## Troubleshooting

- **The TUNE button remains red and does not return to TUNE** — The tuning cycle may have been interrupted. Click TUNE again or check the connection to the TGXL.
- **TUNE is grayed out or unresponsive** — Verify the tuner is in OPERATE mode and the TGXL is detected.
- **Tuning fails or is slow** — If you are running firmware 4.2 and experience tuning issues with the radio firmware path, configure a direct TGXL connection (port 9010) in Radio Setup → Tuner. This bypasses the radio's firmware path for the autotune command.

## Related

- [Read SWR immediately after a tune](read-swr-immediately-after-a-tune.md)
- [Put the tuner in OPERATE, BYPASS, or STANDBY](#)

---

# Fine-tune the C1/L/C2 relays with the mousewheel

Adjust individual relay bank positions on the 4O3A Tuner Genius XL using the mousewheel over the C1, L, and C2 relay bars.

## Before you start

- A direct TGXL connection (port 9010) must be active. The relay bars can only be adjusted when AetherSDR has a direct connection to the TGXL.
- The Tuner applet must be open.

## Steps

1. Position your mouse cursor over the **C1**, **L**, or **C2** relay bar in the Tuner applet.
2. Scroll the mousewheel up to increase the relay position, or down to decrease it.
3. The relay bar updates immediately to show the new position.

## Relay ranges

| Relay | Range | Description |
|---|---|---|
| C1 | 0–255 | Capacitor bank 1 |
| L | 0–255 | Inductor bank |
| C2 | 0–255 | Capacitor bank 2 |

## When scrolling is disabled

The mousewheel scrolling is only enabled when a direct TGXL connection is active. If you are using the radio's firmware path to communicate with the tuner, the relay bars display the current values but cannot be adjusted with the mousewheel.

## Tips

- Fine-tuning relays is useful for optimizing a match after an autotune, or for manually adjusting the tuner to a specific impedance.
- The relay values are sent immediately to the TGXL on each scroll event.

## Related

- [Tuner overview](overview.md)
- [Run an autotune on the external TGXL](run-an-autotune-on-the-external-tgxl.md)

---

# Select an antenna with the ANT 1/2/3 switch

When a direct TGXL connection is active, the Tuner applet shows a 3x1 antenna switch. Use the ANT 1, ANT 2, and ANT 3 buttons to select which antenna port the TGXL routes RF to.

## Before you start

- A direct TGXL connection (port 9010) must be active. The antenna switch row is only visible when AetherSDR has a direct connection to the TGXL.
- The Tuner applet must be open.

## Steps

1. Click the **ANT 1**, **ANT 2**, or **ANT 3** button in the Tuner applet.
2. The selected button highlights to indicate it is active.
3. The TGXL immediately routes the RF signal to the selected antenna port.

## When the antenna switch is hidden

The ANT 1/2/3 buttons are only visible when a direct TGXL connection is active. If you are using the radio's firmware path to communicate with the tuner, the antenna switch row is hidden.

## Tips

- Use the antenna switch to quickly switch between antennas without leaving the Tuner applet.
- The current antenna selection is shown by the highlighted button.

## Related

- [Tuner overview](overview.md)
- [Fine-tune the C1/L/C2 relays with the mousewheel](fine-tune-the-c1-l-c2-relays-with-the-mousewheel.md)