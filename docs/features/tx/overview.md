# TX Controls overview

The TX Controls applet gives you direct access to all transmit functions from a single panel: power metering, output level adjustment, profile selection, antenna tuning, and signal linearisation. Open it whenever you need to adjust transmit settings or monitor output during a QSO.

## Before you start

- Connect to a FLEX-8600 radio. TX Controls requires an active radio connection.
- Confirm the Applet Panel is visible. If it is not, click `View > Applet Panel` to show it.

## How it works

The TX Controls applet is always present in the right-side Applet Panel. Toggle its visibility with the TX tray button on the right sidebar. The applet is divided into five functional areas:

**Power meters** — two horizontal bar gauges at the top of the applet display live transmitter output.

- **RF Pwr** shows forward power at the exciter output. The scale is 0–120 W on standard FLEX-8600 hardware (red zone above 100 W) or 0–600 W on Aurora 500 W hardware (red zone above 500 W). The scale switches automatically based on the connected radio model.
- **SWR** shows standing wave ratio at the exciter. The scale runs from 1.0 to 3.0; the bar turns red above 2.5.

**Power sliders** — two sliders let you set output levels before keying.

- **RF Power** sets the transmit RF power level. Range is 0–100, default 100.
- **Tune Pwr** sets the tune-carrier power level. Range is 0–100, default 10. Keep this low to protect the final amplifier and antenna during tuning.

A numeric readout to the right of each slider shows the current value.

**TX Profile** — a drop-down selector populated with the profiles stored on the radio. Selecting a profile immediately loads it on the radio. Use this to switch between configurations such as SSB, digital, or contest modes.

**ATU status indicators** — three small indicators sit alongside the TX Profile selector and report the state of the internal antenna tuner:

| Indicator | Lights when |
|-----------|-------------|
| Success | ATU tune completed successfully (dim otherwise) |
| Byp | ATU is in bypass or manual bypass (orange) |
| Mem | ATU is operating from a stored memory (green) |

**Action buttons** — a row of four buttons controls transmit and tuning operations:

| Button | Type | Behavior |
|--------|------|----------|
| TUNE | Push | Starts a tune carrier. Label changes to "TUNING..." with a red background while active. Click again to stop. |
| MOX | Toggle | Keys the transmitter manually. Turns red while TX is active. |
| ATU | Push | Starts the internal ATU tuning cycle. Disabled when TGXL is in OPERATE mode. |
| MEM | Toggle | Enables or disables ATU memory recall. Disabled when TGXL is in OPERATE mode. |

**APD (Adaptive Pre-Distortion)** — the bottom row contains the APD toggle and its status cluster.

- **APD** toggles adaptive pre-distortion on the radio. When enabled, the button lights green.
- Three indicators in the inset panel to the right of APD show the progression of the APD process:

| Indicator | Meaning |
|-----------|---------|
| Cal | APD is on and currently calibrating |
| Avail | APD is on and a calibration is available but not yet applied |
| Active | APD is on and the equaliser is actively applied |

The normal progression after enabling APD is Cal → Avail → Active.

## Tips

- Set **Tune Pwr** to a low value (10 is the default) before running the ATU or checking SWR. Tuning at high power can stress an unmatched antenna system.
- The **TUNE** button sends a continuous carrier on the current frequency and mode. Ensure you are within your licensed band before activating it.
- **MOX** does not depend on any mode or PTT input — it keys the transmitter unconditionally. Use it with care.
- The ATU and MEM buttons are disabled when the TGXL amplifier is in OPERATE mode to prevent interference with the amplifier's own tuning state.

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
