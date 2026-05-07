# Bypass the internal ATU

The ATU (automatic antenna tuner) bypass puts the tuner out of the signal path, letting the radio transmit through the antenna without any impedance matching. The TX applet's **Byp** indicator lights when bypass is active.

## Steps

1. Open the TX applet.
2. Click the **ATU** button to toggle the tuner into bypass mode. The **Byp** indicator lights to confirm bypass is active. Click the button again to return to normal tuning operation.

## What each control does

| Control | Behavior |
|---|---|
| **ATU** button | Toggles between active tuning and bypass. Each press switches state. |
| **Byp** indicator | Lit when the ATU is bypassed (signal passes through without impedance matching). |
| **Success** indicator | Lit when the ATU has completed a successful tune. Turns off when bypass is engaged. |
| **Mem** indicator | Lit when the ATU is using a recalled memory setting rather than a live tune result. |

## Tips

- Bypass is useful when you know the antenna is already matched for the current frequency, or when you want to measure raw SWR without the tuner correcting it.
- If you were previously tuned and switch to bypass, the **Success** or **Mem** indicator will clear — re-engage the ATU and press **Tune** to restore a matched state.

## Related

- [TX Applet overview](tx-applet.md)
- [Tune the antenna with the internal ATU](tune-internal-atu.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
