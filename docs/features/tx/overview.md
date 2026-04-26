# TX Controls overview

The TX Controls applet is your primary interface for managing transmit power, tuning, and antenna matching on the FLEX-8600. It provides meters, sliders, profile selection, and keying controls in a single panel.

## How it works

The TX Controls applet is always visible in the Applet Panel (right sidebar). Click the TX tray button to show or hide it. The applet requires an active radio connection to operate.

The applet is organized into five functional areas:

**Power meters** — Two horizontal bar gauges at the top of the applet display real-time transmit readings:

- **RF Pwr** — Forward power at the exciter output. Scale is 0–120 W for standard configurations, or 0–600 W for Aurora 500W models. The bar turns red above 100 W (or above 500 W on Aurora models).
- **SWR** — Standing wave ratio at the exciter, displayed on a 1.0–3.0 scale. The bar turns red above 2.5.

**Power sliders** — Two sliders set power levels sent to the radio:

- **RF Power** — Sets the transmit RF power level. Range: 0–100. Default: 100.
- **Tune Pwr** — Sets the tune-carrier power level. Range: 0–100. Default: 10.

Both sliders display their current value as a number to the right of the slider.

**TX Profile and ATU status** — A dropdown and three indicators share a single row:

- **TX Profile** — Selects the active transmit profile. The list is populated from the profiles stored on the radio. Selecting a profile loads it immediately.
- **Success** — Lit green when the ATU reports a successful match.
- **Byp** — Lit orange when the ATU is in bypass or manual bypass.
- **Mem** — Lit green when the ATU is using a stored memory.

**Action buttons** — Four buttons control transmit and antenna tuning:

- **TUNE** — Starts a tune carrier. The button label changes to "TUNING..." with a red background while active. Click again to stop.
- **MOX** — Toggles manual transmit. The button turns red while the transmitter is keyed.
- **ATU** — Starts the internal ATU tuning cycle. Disabled when the TGXL transverter is in OPERATE mode.
- **MEM** — Toggles ATU memory recall on or off. Disabled when the TGXL transverter is in OPERATE mode.

**APD and status indicators** — The bottom row controls Adaptive Pre-Distortion:

- **APD** — Toggles adaptive pre-distortion on the radio.
- **Active** — Lit green when APD is on and the equalizer is actively applied.
- **Cal** — Lit green when APD is on and still calibrating.
- **Avail** — Lit green when APD is on and a calibration is available but not yet applied.

APD status progresses through the indicators in sequence: Cal (calibrating) → Avail (calibration ready) → Active (equalizer applied).

## Tips

- Keep **Tune Pwr** low (the default of 10 is a reasonable starting point) to avoid stressing the amplifier or antenna during ATU cycles.
- The **RF Pwr** meter scale changes automatically based on which radio model AetherSDR detects; no manual adjustment is needed.
- **ATU** and **MEM** are grayed out when the TGXL is in OPERATE mode. Switch the TGXL out of OPERATE mode before attempting ATU operations.

## Related

- [Set RF output power](set-rf-output-power.md)
- [Set tune-carrier power](set-tune-carrier-power.md)
- [Switch TX profiles (e.g. SSB, Digital)](switch-tx-profiles-e-g-ssb-digital.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [Toggle MOX to manually key the transmitter](toggle-mox-to-manually-key-the-transmitter.md)
- [Run the internal ATU](run-the-internal-atu.md)
- [Recall an ATU memory](recall-an-atu-memory.md)
- [Enable APD to linearise the transmitter](enable-apd-to-linearise-the-transmitter.md)
