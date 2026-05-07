# Understand power scale on Aurora and high-power radios

When a radio reports a new maximum allowed TX output power, AetherSDR fires the `maxPowerLevelChanged` signal to rescale the forward-power gauge and cap the RF Power slider to the radio's safe operating limit.

## Before you start

- Connect to an Aurora or other high-power radio that reports a maximum TX power value over the network link.
- Open the TX applet.

## Steps

1. Key the radio or change the output power setting. Watch the forward-power gauge — its full-scale value updates automatically to match the maximum power the radio has reported.
2. Drag the **RF Power** slider. Notice that it cannot be moved above the reported maximum; the cap is applied in real time each time `maxPowerLevelChanged` fires.

## What each control does

| Control | Behavior |
|---|---|
| Forward-power gauge | Displays current TX output power. Full-scale is set to the latest maximum power value (in watts) reported by the radio. Rescales automatically without requiring a restart. |
| RF Power slider | Sets the target TX output power. The upper limit is capped to the radio's reported maximum each time a new maximum is received, preventing the user from requesting power above the safe operating limit. |

## Tips

- If the gauge or slider cap appears lower than expected, verify the radio firmware is up to date — older firmware on some Aurora units reports a conservative default maximum until a full status exchange completes.
- The cap updates live; you do not need to disconnect and reconnect after swapping between radio profiles with different power ratings.

## Related

- [tx-applet.md](tx-applet.md)
- [aurora-setup.md](aurora-setup.md)
- [forward-power-gauge.md](forward-power-gauge.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
