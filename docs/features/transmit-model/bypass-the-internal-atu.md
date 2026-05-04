# Bypass the internal ATU

The ATU (automatic antenna tuner) can be bypassed after a successful tune at a given frequency. The TX applet tracks tune state through the `ATUStatus` enum, which drives the **Success**, **Byp**, and **Mem** indicators.

## Before you start

- The ATU must have already completed a successful tune cycle at the current transmit frequency. The **Success** indicator must be lit (green).
- Do not change the transmit frequency before bypassing. A frequency change resets the tuner state and a second click will start a new tune cycle instead of bypassing.

## Steps

1. In the TX applet, click the **ATU** button once.
   - If the tuner holds a successful match at the current frequency, clicking **ATU** a second time switches the tuner to bypass mode. The **Byp** indicator lights up to confirm bypass is active.
   - If the transmit frequency has changed since the last tune, clicking **ATU** starts a fresh tune cycle instead.

## What each control does

| Control | Behavior |
|---|---|
| **ATU** button | First click starts a tune cycle. Second click — only when the tuner shows a successful match at the same frequency — activates bypass. Any frequency change resets this toggle so the next click always starts a new tune. |
| **Success** indicator | Lit (green) when `ATUStatus` is `Successful` or `OK`. Indicates a valid match is held at the current frequency. |
| **Byp** indicator | Lit when `ATUStatus` is `Bypass` or `ManualBypass`. Confirms the tuner is bypassed. Clearing bypass state resets the tuned-frequency pin, so the next **ATU** click starts a fresh tune. |
| **Mem** indicator | Lit when a recalled ATU memory is active. |

## Tips

- If you change frequency after a successful tune, clicking **ATU** always starts a new tune cycle — never bypass — regardless of the previous status indicator state.
- To return to normal tuning from bypass, click **ATU** once. The tuner starts a fresh cycle at the current frequency.

## Related

- [Start an ATU tune cycle](start-atu-tune.md)
- [TX Applet overview](tx-applet.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
