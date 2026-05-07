# Run the internal ATU to tune the antenna

The ATU Tune Status tracks the automatic antenna tuner through each stage of its cycle — idle, in-progress, success, bypass, failure, or memory recall — and reflects the result in the TX applet's **Success**, **Byp**, and **Mem** indicators.

## Before you start

- Ensure the radio is not currently transmitting (MOX is off).
- Connect an antenna to the antenna port before tuning.

## Steps

1. Open the **TX** applet from the main toolbar.
2. Click the **ATU** button to start the tuning cycle. The radio transmits a low-power carrier and the tuner steps through its matching network.
3. Watch the **Success**, **Byp**, and **Mem** indicators in the TX applet:
   - **Success** lights when the tuner finds an acceptable match.
   - **Byp** lights when the tuner is bypassed (no match attempted or ATU disabled).
   - **Mem** lights when the tuner recalled a previously stored match for the current frequency.
4. If the tuner fails to find a match, the **Success** indicator remains unlit. Try lowering TX power, checking your antenna connection, and clicking **ATU** again.

## What each control does

| Control | Behavior |
|---------|----------|
| **ATU** button | Toggles between starting a tune cycle and bypassing the tuner. Calls `startTune()` on the transmit model when activated. |
| **Success** indicator | Lit when the ATU completed tuning and found a valid match (`ATUStatus` = success). |
| **Byp** indicator | Lit when the ATU is in bypass mode — the tuner is in-line but not matching (`ATUStatus` = bypass). |
| **Mem** indicator | Lit when the ATU applied a match from memory rather than running a new tune cycle (`ATUStatus` = memory recall). |

## Tips

- The tuner runs at reduced power. If your radio has a separate tune-power setting, set it to the lowest effective level (typically 10 W) before clicking **ATU** to reduce wear on the tuner relay.
- Memory recall (**Mem** lit) is the fastest outcome — the tuner skips a new sweep and reuses the stored L/C values for that frequency. No action is needed; tuning is complete.
- If **Byp** lights immediately without a tune attempt, check that the ATU is enabled in your radio's antenna settings.

## Related

- [tx-applet.md](tx-applet.md)
- [transmit-power.md](transmit-power.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
