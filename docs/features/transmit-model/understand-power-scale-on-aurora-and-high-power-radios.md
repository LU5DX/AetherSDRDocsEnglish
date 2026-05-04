# Understand power scale on Aurora and high-power radios

When a radio reports a new maximum allowed TX output power, AetherSDR uses that value to scale the forward-power gauge and cap the RF Power slider so you cannot exceed the radio's safe operating limit.

## Before you start

- Connect to an Aurora or other high-power radio that reports maximum TX power over the control link.

## Steps

1. Open the TX applet and locate the **RF Power** slider and the forward-power gauge.
2. Transmit or key the radio briefly. When the radio reports its maximum allowed output power, the forward-power gauge rescales its upper limit to that wattage and the RF Power slider is capped at the same value automatically — no manual adjustment is needed.

## What each control does

| Control | Behavior |
|---|---|
| RF Power slider | Capped at the maximum TX output power (in watts) reported by the connected radio. You cannot drag the slider above this limit. |
| Forward-power gauge | Upper end of the scale is set to the radio's reported maximum TX power. The scale updates each time the radio sends a new maximum power value. |

## Tips

- If the gauge or slider range looks unexpectedly low, disconnect and reconnect to the radio. A fresh connection causes the radio to resend its maximum power value, which resets both controls to the correct range.
- The cap is enforced per-connection. Switching to a different radio model will rescale both controls to match the new radio's reported limit.

## Related

- [TX Applet overview](tx-applet.md)
- [Connect to a remote radio via SmartLink](smartlink-connect.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
