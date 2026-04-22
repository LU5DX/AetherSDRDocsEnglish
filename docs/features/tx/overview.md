# TX Controls overview

The TX Controls applet gives you access to all transmit functions in one panel: power metering, RF and tune power adjustment, TX profile selection, manual transmit keying, ATU control, and adaptive pre-distortion. Open it whenever you need to monitor or adjust your station's transmit chain.

## How it works

The TX Controls applet lives in the Applet Panel (right sidebar) and is always accessible. Toggle its visibility with the TX tray button on the right sidebar. The applet requires an active radio connection to operate.

The applet is organized into five functional areas:

**Power meters** — Two horizontal bar gauges at the top show live transmit readings. "RF Pwr" displays forward power at the exciter output in watts; the scale is 0–120 W for standard operation, with the red zone starting above 100 W. On an Aurora 500W-capable radio the scale extends to 0–600 W, red above 500 W. "SWR" shows the standing wave ratio on a 1.0–3.0 scale, with red above 2.5.

**Power sliders** — "RF Power" sets the transmit RF power level from 0 to 100 (default 100). "Tune Pwr" sets the tune-carrier power level from 0 to 100 (default 10). A numeric readout to the right of each slider shows the current value.

**TX Profile** — The "TX Profile" drop-down lists the transmit profiles available on the connected radio. Selecting a profile loads it immediately. The three small indicators next to the drop-down ("Success", "Byp", "Mem") reflect ATU state:

| Indicator | Color when lit | Meaning |
|-----------|---------------|---------|
| Success | Green | ATU tuned successfully or status is OK |
| Byp | Orange | ATU is in Bypass or ManualBypass |
| Mem | Green | ATU is using a stored memory |

**TUNE / MOX / ATU / MEM buttons** — Four buttons control transmit keying and antenna tuning:

| Button | Type | Behavior |
|--------|------|----------|
| TUNE | Push button | Starts or stops a tune carrier. Label changes to "TUNING..." with a red background while the carrier is active. |
| MOX | Toggle button | Manually keys the transmitter. Button turns red while TX is keyed. |
| ATU | Push button | Starts the internal ATU tuning cycle. Disabled when the TGXL is in OPERATE mode. |
| MEM | Toggle button | Enables or disables ATU memory recall. Disabled when the TGXL is in OPERATE mode. |

**APD** — The "APD" toggle button enables Adaptive Pre-Distortion on the radio, which linearises the transmitter. Three indicators show APD progression:

| Indicator | Color when lit | Meaning |
|-----------|---------------|---------|
| Cal | Green | APD is on and calibrating |
| Avail | Green | APD is on and a calibration is available but not yet applied |
| Active | Green | APD is on and the equalizer is actively applied |

The normal progression after enabling APD is Cal → Avail → Active.

## Related

- [Set RF output power](set-rf-output-power.md)
- [Set tune-carrier power](set-tune-carrier-power.md)
- [Switch TX profiles (e.g. SSB, Digital)](switch-tx-profiles-e-g-ssb-digital.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Toggle MOX to manually key the transmitter](toggle-mox-to-manually-key-the-transmitter.md)
- [Run the internal ATU](run-the-internal-atu.md)
- [Recall an ATU memory](recall-an-atu-memory.md)
- [Enable APD to linearise the transmitter](enable-apd-to-linearise-the-transmitter.md)
- [Make your first QSO with AetherSDR](../../getting-started/tutorials/first-qso.md)
