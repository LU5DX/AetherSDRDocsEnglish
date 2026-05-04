# Run the internal ATU to tune the antenna

The internal automatic antenna tuner (ATU) finds the best impedance match for your antenna on the current transmit frequency. The TX applet's **Success**, **Byp**, and **Mem** indicators reflect the tuner's progress and outcome in real time.

## Before you start

- The radio must be connected and a transmit slice must be active.
- Set your transmit frequency before starting a tune cycle. Changing frequency after a successful tune clears the match and requires a new tune.

## Steps

1. In the TX applet, click the **ATU** button to start a tune cycle. The tuner transmits a brief carrier and searches for a match.
2. Watch the indicators:
   - **Success** (green) lights when the tune completes successfully.
   - If **Success** is already lit and you are on the **same frequency** as the last tune, clicking **ATU** again switches the tuner to bypass mode and **Byp** lights instead.
   - If you have changed frequency since the last tune, clicking **ATU** always starts a fresh tune cycle regardless of the previous status.

## What each control does

| Control | Behavior |
|---|---|
| **ATU** button | Starts a tune cycle on first click. On a subsequent click at the same frequency where a successful tune was completed, switches the tuner to bypass instead. Any frequency change resets this toggle and a click always starts a new tune. |
| **Success** indicator | Lights green when the tuner reports a successful match (`Successful` or `OK` status). |
| **Byp** indicator | Lights when the tuner is in bypass mode (`Bypass` or `ManualBypass` status). Bypass also clears the stored tuned frequency so the next ATU button click will start a fresh tune. |
| **Mem** indicator | Lights when the tuner recalls a match from memory rather than running a new tune cycle. |

## Tips

- If the band or antenna changes, move to the new frequency first, then click **ATU** — the frequency-change detection ensures a fresh tune rather than an inadvertent bypass.
- A successful tune is stored per frequency. If you return to a previously tuned frequency the **Mem** indicator may light, indicating the radio is applying a recalled match without a full tune cycle.

## Related

- [tx-applet-overview.md](tx-applet-overview.md)
- [atu-status-indicators.md](atu-status-indicators.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
