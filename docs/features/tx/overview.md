# TX Controls overview

The TX Controls applet gives you direct access to all transmit functions: monitoring forward power and SWR, setting output levels, selecting a TX profile, keying the transmitter, running the ATU, and enabling Adaptive Pre-Distortion. All these controls are grouped in one place in the Applet Panel.

## Before you start

- Connect to a FLEX-8600 radio. TX Controls requires an active radio connection.
- Make sure the Applet Panel is visible. If it is not, click `View > Applet Panel` to show it.

## How it works

TX Controls is always present in the Applet Panel (right sidebar). Toggle its visibility with the **TX** tray button on the right sidebar.

The applet is organized in rows from top to bottom:

1. **Meters** — real-time RF forward power and SWR readings.
2. **Power sliders** — set transmit and tune-carrier power levels before you key up.
3. **Profile and ATU status** — choose a TX profile and see the current ATU state at a glance.
4. **Action buttons** — TUNE, MOX, ATU, and MEM for transmit and tuner control.
5. **APD** — toggle Adaptive Pre-Distortion and monitor its calibration state.

None of the TX Controls settings are persisted by AetherSDR; values follow the radio's current state.

## What each control does

| Control | Kind | Default | Range / States | What it does |
|---|---|---|---|---|
| **RF Pwr** | Meter | — | 0–120 W; red above 100 W (barefoot) / 0–600 W; red above 500 W (Aurora 500W) | Displays forward power at the exciter output. The scale changes automatically based on radio model. |
| **SWR** | Meter | — | 1.0–3.0; red above 2.5 | Displays standing wave ratio at the exciter. |
| **RF Power** | Slider | 100 | 0–100 | Sets the transmit RF power level. |
| **Tune Pwr** | Slider | 10 | 0–100 | Sets the tune-carrier power level. |
| **TX Profile** | Drop-down | — | Populated from radio | Selects and loads a transmit profile from the radio's profile list. |
| **Success** | Indicator | Dim | Dim / green | Lights green when the ATU reports a successful or OK tune result. |
| **Byp** | Indicator | Dim | Dim / orange | Lights orange when the ATU is in Bypass or ManualBypass. |
| **Mem** | Indicator | Dim | Dim / green | Lights green when the ATU is recalling a saved memory. |
| **TUNE** | Button | — | TUNE / TUNING... | Starts a tune carrier. Label changes to "TUNING..." with a red background while active. Click again to stop. |
| **MOX** | Toggle button | — | Off / on (red) | Toggles manual transmit. Button turns red while the transmitter is keyed. |
| **ATU** | Button | — | — | Starts the internal ATU tuning cycle. Disabled when TGXL is in OPERATE mode. |
| **MEM** | Toggle button | — | Off / on | Toggles ATU memory recall on or off. Disabled when TGXL is in OPERATE mode. |
| **APD** | Toggle button | — | Off / on | Toggles Adaptive Pre-Distortion on the radio. |
| **Active** | Indicator | Dim | Dim / green | Lit when APD is on and the equalizer is actively applied. |
| **Cal** | Indicator | Dim | Dim / green | Lit when APD is on and still calibrating. |
| **Avail** | Indicator | Dim | Dim / green | Lit when APD is on and a calibration is available but not yet applied. |

### APD status progression

APD moves through three states in sequence: **Cal** (calibrating) → **Avail** (calibration ready, not yet applied) → **Active** (equalizer applied to the transmitted signal).

## Tips

- Keep **Tune Pwr** low (the default is 10) to avoid stressing the antenna or amplifier during ATU tuning.
- Watch the **SWR** meter after a tune cycle. The **Success** indicator confirms the ATU found a match, but the SWR meter shows you the actual result.
- The **RF Pwr** meter scale changes automatically between 0–120 W (barefoot FLEX-8600) and 0–600 W (Aurora 500W); the red threshold adjusts accordingly.

## Related

- [Set RF output power](set-rf-output-power.md)
- [Set tune-carrier power](set-tune-carrier-power.md)
- [Switch TX profiles (e.g. SSB, Digital)](switch-tx-profiles-e-g-ssb-digital.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Toggle MOX to manually key the transmitter](toggle-mox-to-manually-key-the-transmitter.md)
- [Run the internal ATU](run-the-internal-atu.md)
- [Recall an ATU memory](recall-an-atu-memory.md)
- [Enable APD to linearise the transmitter](enable-apd-to-linearise-the-transmitter.md)
- [Run a Two-Tone Tune](run-a-two-tone-tune.md)
- [Make your first QSO with AetherSDR](../../getting-started/tutorials/first-qso.md)
