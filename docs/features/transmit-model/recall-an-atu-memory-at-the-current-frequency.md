# Recall an ATU memory at the current frequency

The ATU (automatic antenna tuner) can store tuning solutions in memory and reapply them instantly when you return to a previously tuned frequency. The **Mem** indicator in the TX applet lights when the radio recalls a stored memory rather than running a new tune cycle.

## Before you start

- Confirm the ATU is enabled and not in bypass mode.
- Ensure you have previously tuned on or near the target frequency so a memory entry exists.

## Steps

1. Set your operating frequency to the frequency for which a tuning memory was saved.
2. Watch the **Mem** indicator in the TX applet — it lights automatically when the radio recalls a stored ATU memory for the current frequency. No manual action is required beyond setting the frequency.

## What each control does

| Control | Behavior |
|---|---|
| **Mem** indicator | Lights when `ATUStatus` is in the memory-recall state, indicating the tuner applied a previously stored solution rather than performing a new tune. |
| **Success** indicator | Lights when the ATU completes a successful tune (new or recalled). |
| **Byp** indicator | Lights when the ATU is in bypass mode. Recall will not occur while bypass is active. |

## Tips

- If **Mem** does not light, no stored memory exists close enough to your current frequency. Use the ATU tune function to generate and store a new solution.
- Memory recall is automatic — you do not need to press any button. Simply moving to a frequency that has a stored solution triggers the recall.

## Related

- [Tune the ATU](tune-atu.md)
- [Bypass the ATU](bypass-atu.md)
- [TX Applet overview](tx-applet.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
