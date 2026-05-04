# Recall an ATU memory at the current frequency

The ATU Tune Status (`ATUStatus`) tracks every state of the automatic antenna tuner, including when a stored memory match is applied at the current frequency. The **Mem** indicator in the TX applet lights when a memory recall is active.

## Before you start

- The radio must be connected and a slice must be active.
- A previous tune cycle must have stored a memory for the target frequency.

## Steps

1. Set your transmit frequency to the frequency for which a tuner memory exists.
2. Click the **MEM** button in the TX applet. The radio retrieves the stored ATU settings for that frequency and the **Mem** indicator illuminates.

## What each control does

| Control | Behavior |
|---|---|
| **MEM button** | Toggles ATU memory recall. Sends a recall command to the radio, which applies previously stored tuner settings for the current frequency. |
| **Mem indicator** | Lights when `ATUStatus` is in a memory-recall state, confirming the tuner is using stored settings rather than a live tune result. |
| **Success indicator** | Lights green when `ATUStatus` is `Successful` or `OK`. Remains off during a memory recall. |
| **Byp indicator** | Lights when `ATUStatus` is `Bypass` or `ManualBypass`. Off during memory recall. |

## Tips

- If no memory exists for the current frequency, the radio will not recall one — use the **ATU** button to run a fresh tune cycle and store a new result.
- After recalling a memory, clicking the **ATU** button starts a new tune cycle rather than bypassing, because the tuned-frequency pin is not set by a memory recall.

## Related

- [Start an ATU tune cycle](atu-tune-start.md)
- [Bypass the ATU](atu-bypass.md)
- [TX Applet overview](tx-applet.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
