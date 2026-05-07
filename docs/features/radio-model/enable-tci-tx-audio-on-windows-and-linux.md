# Enable TCI TX audio on Windows and Linux

TCI TX audio allows a TCI client to send transmit audio directly to the radio as VITA-49 packets, bypassing the Windows and Linux audio device layer entirely. This works regardless of whether SmartSDR DAX2 owns the system audio devices.

## Before you start

- AetherSDR V0.9.7 or later is required.
- A TCI client capable of sending TX audio must be connected to the radio.

## Steps

1. In your TCI client, enable TX audio output and point it at the AetherSDR TCI server address and port.
2. Key the radio through your TCI client. AetherSDR registers its own DAX TX stream slot on the radio and routes the incoming TCI audio directly as VITA-49 packets — no additional audio device configuration is needed on the AetherSDR side.

## What each control does

| Control | Behavior |
|---|---|
| TCI TX audio (TCI client side) | Sends encoded TX audio to AetherSDR over the TCI connection. AetherSDR forwards it to the radio's DAX TX stream as VITA-49 packets, independent of any Windows or Linux audio device. |
| DAX TX stream slot | Claimed automatically by AetherSDR when TCI TX audio is active. SmartSDR DAX2 owning the system audio layer does not block this claim. |

## Tips

- Because TCI TX audio never touches Windows or Linux audio devices, you do not need to configure or release any system audio devices before transmitting.
- If SmartSDR DAX2 is also running, TCI TX audio will still work — the two use separate stream slots.

## Related

- [Per-Band TX Settings](tx-band-info.md)
- [DAX TX policy](dax-tx-policy.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
