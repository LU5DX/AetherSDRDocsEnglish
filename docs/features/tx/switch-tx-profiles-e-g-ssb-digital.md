# Switch TX Profiles (e.g. SSB, Digital)

Use the TX Profile selector to load a named transmit profile from the radio. Profiles store microphone settings, equalizer values, and other transmit parameters, letting you switch quickly between modes such as SSB and Digital.

## Before you start

- AetherSDR must be connected to the radio. The TX Controls applet requires an active radio connection.
- At least one transmit profile must already exist on the radio. Create or manage profiles via `Profiles > Profile Manager...`.

## Steps

1. Click the **TX** tray button in the right sidebar to open the TX Controls applet.
2. Locate the **TX Profile** drop-down near the middle of the applet.
3. Click the drop-down and select the profile name you want to load (for example, "SSB" or "Digital").

The radio loads the selected profile immediately. No confirmation step is required.

## What each control does

| Control        | Kind      | Behavior                                                                                 |
|----------------|-----------|------------------------------------------------------------------------------------------|
| **TX Profile** | Drop-down | Selects and loads a transmit profile from the radio. The list is populated by the radio. |

## Tips

- You can also load a profile from the menu bar without opening the TX Controls applet. Go to `Profiles` and click the profile name in the checkable list below the separator.
- To create, edit, or delete profiles, go to `Profiles > Profile Manager...`.

## Troubleshooting

- **TX Profile drop-down is empty** — No transmit profiles exist on the radio. Open `Profiles > Profile Manager...` to create one.
- **TX Profile drop-down is not responding** — AetherSDR is not connected to the radio. Connect first via `Settings > Connect to Radio...`.

## ATU button behavior (v0.9.5.1)

Starting with v0.9.5.1, the **ATU** button works as a per-frequency toggle that mirrors the behavior of SmartSDR:

| Situation | What the ATU button does |
|---|---|
| No previous successful tune, or frequency has changed since the last tune | Starts a new ATU tuning cycle. |
| ATU status is **Success** (or **OK**) and the transmit frequency has not changed since the last tune | Switches the tuner to bypass. |
| ATU is in bypass | The next click starts a fresh tuning cycle. |

In practice this means:

1. Click **ATU** on a new frequency — the tuner runs a full tune cycle.
2. When the **Success** indicator lights green, click **ATU** again on the same frequency — the tuner switches to bypass.
3. Change frequency and click **ATU** — the tuner always starts a fresh cycle, even if the previous status was successful.

The **Byp** indicator lights orange whenever the tuner is in bypass. The **Success** indicator lights green when the tune was successful and the tuner is holding that match.

> **Note:** The **ATU** and **MEM** buttons are disabled when the TGXL amplifier is in OPERATE mode.

## Right-click ATU menu (v26.5.2.1)

Right-click the **ATU** button to open a context menu with two advanced options.

| Menu Item | Action |
|---|---|
| **Pre-tune bands…** | Opens the Pre-Tune dialog to sweep antenna tuner settings across a range of frequencies. Enabled only when **MEM** is active. |
| **Clear ATU memories…** | Prompts for confirmation and then clears all stored ATU tune memories on the radio. |

> **Note:** **Pre-tune bands…** is disabled when the **MEM** button is off. Enable **MEM** first to use this feature.

## Right-click TUNE menu (v26.5.2.1)

Right-click the **TUNE** button to choose the carrier shape for the next tune cycle. This is a one-shot selection — the choice is not saved in AetherSDR settings.

| Menu Item | Action |
|---|---|
| **Mono Tone** | Produces a single-tone carrier. This is the default behavior. |
| **Two Tone** | Produces a two-tone carrier used for testing intermodulation distortion. |

The radio's tune mode also resets to single-tone after a power cycle.

## MOX button and Quindar tones (v0.9.7)

Starting with v0.9.7, clicking **MOX** routes the PTT request through the Quindar-tone coordinator rather than keying the transmitter directly. The practical effect is:

- When Quindar is enabled in the Audio Channel Strip and the active TX slice is on a phone mode (SSB, AM, FM, and so on), the K tone plays when **MOX** is clicked on and the BK tone plays when **MOX** is clicked off.
- When Quindar is disabled, or the active TX slice is not on a phone mode, behavior is identical to previous versions — the transmitter keys and unkeys immediately.

The **MOX** button appearance is unchanged: it turns red while TX is keyed and returns to its default color on release.

> **Note:** Quindar tones are a feature of the Audio Channel Strip. Enable the **QUIN** control there before expecting tones to play on PTT.

## RF Power meter peak-hold (v26.5.2.1)

The **RF Pwr** meter includes a peak-hold feature that captures and holds the peak envelope power (PEP) reading:

- The peak value holds steady for 2 seconds after the most recent peak.
- After the hold period, the peak value decays back toward the current reading at a rate that takes approximately 2.5 seconds from peak to zero.
- When you stop transmitting, the peak-hold value resets to zero immediately — a held PEP reading does not linger across overs.

The decay rate scales automatically depending on the radio model: 48 W/s for a barefoot radio (120 W scale) and 240 W/s when an Aurora 500 W exciter is connected (600 W scale).

## APD status indicators

The **Active**, **Cal**, and **Avail** indicators show the current state of the adaptive pre-distortion (APD) system:

| State | Meaning |
|---|---|
| **Cal** (green) | APD is calibrating. |
| **Avail** (green) | Calibration is complete and available but not yet applied. |
| **Active** (green) | APD is on and the equalizer is actively applied. |
| All dim | APD is off. |

## Related

- [TX Controls overview](overview.md)
- [Set RF output power](set-rf-output-power.md)
- [Run a Two-Tone Tune](run-a-two-tone-tune.md)