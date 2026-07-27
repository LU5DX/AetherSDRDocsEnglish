# TX Controls overview

The TX Controls applet gives you direct access to all transmit functions: monitoring forward power and SWR, setting output levels, selecting a TX profile, keying the transmitter, running the ATU, and enabling Adaptive Pre-Distortion. All these controls are grouped in one place in the Applet Panel.

## Before you start

- Connect to a FLEX-8600 radio. TX Controls requires an active radio connection.
- Make sure the Applet Panel is visible. If it is not, click `View > Applet Panel` to show it.

## How it works

TX Controls is always present in the Applet Panel (right sidebar). Toggle its visibility with the **TX** tray button on the right sidebar.

The applet is organized in rows from top to bottom:

1. **Meters** — real-time RF forward power and SWR readings with peak-hold.
2. **Power sliders** — set transmit and tune-carrier power levels before you key up.
3. **Profile and ATU status** — choose a TX profile and see the current ATU state at a glance.
4. **Action buttons** — TUNE, MOX, ATU, and MEM for transmit and tuner control.
5. **APD** — toggle Adaptive Pre-Distortion and monitor its calibration state.

None of the TX Controls settings are persisted by AetherSDR; values follow the radio's current state.

## What each control does

| Control | Kind | Default | Range / States | What it does |
|---|---|---|---|---|
| **RF Pwr** | Meter | — | 0–120 W; red above 100 W (barefoot) / 0–600 W; red above 500 W (Aurora 500W) | Displays forward power at the exciter output. The scale changes automatically based on radio model. Includes a peak-hold bar that holds the highest PEP reading for 2 seconds, then decays to the current smoothed value. The peak resets to zero immediately when the transmitter un-keys. Hover the mouse over the gauge to see the exact wattage readout (e.g. "45 W"). |
| **SWR** | Meter | — | 1.0–3.0; red above 2.5 | Displays standing wave ratio at the exciter. Hover the mouse over the gauge to see the exact ratio readout (e.g. "1.42:1"). |
| **RF Power** | Slider | 100 | 0–100 | Sets the transmit RF power level as a percentage of maximum. During slider drag, a tooltip shows the current percentage (e.g. "75%"). Values are synced to the radio when you release the slider. |
| **Tune Pwr** | Slider | 10 | 0–100 | Sets the tune-carrier power level as a percentage of maximum. During slider drag, a tooltip shows the current percentage (e.g. "50%"). Values are synced to the radio when you release the slider. |
| **TX Profile** | Drop-down | — | Populated from radio | Selects and loads a transmit profile from the radio's profile list. |
| **Success** | Indicator | Dim | Dim / green | Lights green when the ATU reports a successful or OK tune result. |
| **Byp** | Indicator | Dim | Dim / orange | Lights orange when the ATU is in Bypass or ManualBypass. |
| **Mem** | Indicator | Dim | Dim / green | Lights green when the ATU is recalling a saved memory. |
| **TUNE** | Button | — | TUNE / TUNING... | Starts a tune carrier. Label changes to "TUNING..." with a red background while active. Click again to stop. Right-click to open the Tune Context Menu and select the carrier shape. |
| **MOX** | Toggle button | — | Off / on (red) | Toggles manual transmit. Button turns red while the transmitter is keyed. When idle, the button has an amber accent border and text to distinguish it from the TUNE, ATU, and MEM buttons (customizable in the Theme Editor). In v0.9.7, clicking MOX routes through the Quindar-tone coordinator so K/BK tones play on PTT engage and disengage in phone modes when Quindar is enabled in the Audio Channel Strip. See [MOX and Quindar tones](#mox-and-quindar-tones) below. |
| **ATU** | Button | — | — | Starts an ATU tune cycle or switches the tuner to bypass, depending on current state and frequency. See [ATU button behaviour](#atu-button-behaviour) below. Disabled when TGXL is in OPERATE mode. Right-click to open the ATU Context Menu. |
| **MEM** | Toggle button | — | Off / on | Toggles ATU memory recall on or off. Disabled when TGXL is in OPERATE mode. |
| **APD** | Toggle button | — | Off / on | Toggles Adaptive Pre-Distortion on the radio. |
| **Active** | Indicator | Dim | Dim / green | Lit when APD is on and the equalizer is actively applied. |
| **Cal** | Indicator | Dim | Dim / green | Lit when APD is on and still calibrating. |
| **Avail** | Indicator | Dim | Dim / green | Lit when APD is on and a calibration is available but not yet applied. |

### ATU button behaviour

The **ATU** button toggles between starting a tune cycle and bypassing the tuner, matching SmartSDR's per-frequency behaviour:

- **First click (or any click after a frequency change)** — starts a fresh ATU tune cycle.
- **Second click at the same frequency** — if the ATU reports a successful or OK match and you have not changed frequency since that tune completed, clicking **ATU** again switches the tuner to bypass.
- **After a bypass** — the tuned-frequency record is cleared. The next click always starts a fresh tune cycle.

If you change frequency between clicks, the button always starts a new tune cycle regardless of the previous ATU status.

### ATU context menu

Right-click the **ATU** button to open the ATU context menu with the following options:

- **Pre-tune bands…** — Opens the Pre-Tune Sweep dialog. This option is only available when ATU memories (MEM) are enabled. If disabled, a tooltip explains that MEM must be enabled first.
- **Clear ATU memories…** — Opens a confirmation dialog. Click **Yes** to clear all stored ATU memories on the radio.

### Tune context menu

Right-click the **TUNE** button to open the Tune context menu. This lets you choose the carrier shape for the next tune cycle. The menu offers two options:

- **Mono Tone** — A single carrier tone.
- **Two Tone** — Two simultaneous tones (typically used for IMD testing).

Selecting either option applies it immediately for the next tune cycle. This is a one-shot setting — it is not saved to AppSettings, and the radio reverts to its default tune mode across power cycles. The currently active mode is shown with a check mark.

### MOX and Quindar tones

Starting in v0.9.7, clicking **MOX** routes the PTT request through the Quindar-tone coordinator instead of keying the transmitter directly. When Quindar is enabled in the Audio Channel Strip:

- **Engage (MOX on)** — the K tone plays before the transmitter keys.
- **Disengage (MOX off)** — the BK tone plays after the transmitter unkeys.

This behaviour applies to phone modes only. On non-phone modes, or when Quindar is disabled in the Audio Channel Strip, MOX keys the transmitter immediately as before.

### APD status progression

APD moves through three states in sequence: **Cal** (calibrating) → **Avail** (calibration ready, not yet applied) → **Active** (equalizer applied to the transmitted signal).

## ShackSwitch applet

V0.9.4 adds support for the ShackSwitch device. When a ShackSwitch is detected, the Applet Panel shows its tray button (**SS**) and applet automatically. Both are hidden when no ShackSwitch device is present. No manual configuration is required to show or hide this applet.

## Tips

- Keep **Tune Pwr** low (the default is 10) to avoid stressing the antenna or amplifier during ATU tuning.
- Watch the **SWR** meter after a tune cycle. The **Success** indicator confirms the ATU found a match, but the SWR meter shows you the actual result.
- The **RF Pwr** meter scale changes automatically between 0–120 W (barefoot FLEX-8600) and 0–600 W (Aurora 500W); the red threshold adjusts accordingly.
- The **RF Pwr** meter includes a peak-hold bar that holds the highest PEP reading for 2 seconds, then gradually decays. This resets immediately when you un-key the transmitter.
- Hover the mouse over the **RF Pwr** or **SWR** gauges to see the exact numeric readout — useful when you need precise values rather than estimating from the tick marks.
- Use the right-click context menu on **TUNE** to switch between Mono Tone and Two Tone tune carriers for testing purposes.
- After a successful tune, clicking **ATU** a second time at the same frequency bypasses the tuner. To retune, change frequency or click **ATU** again after the bypass.
- Right-click **ATU** to access the Pre-tune sweep and Clear ATU memories functions.
- If you use **MOX** on a phone mode with Quindar enabled, allow the K tone to finish before speaking. The transmitter is not keyed until the tone completes.
- When dragging **RF Power** or **Tune Pwr** sliders, a tooltip displays the exact power value as a percentage (e.g. "75%"), making it easier to set precise levels. Values are sent to the radio when you release the slider.

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
- Pre-tune ATU memories
- Clear ATU memories
<!-- docmesh:llm version=v26.7.4 date=2026-06-15 -->