# Configure the external APD tab on FLEX-8x00 radios

The external APD tab lets you assign which sampler port (such as INTERNAL, RX_A, RX_B, XVTA, or XVTB) is used for Automatic Power Detection on each TX antenna. This setting is available on FLEX-8x00 radios and compatible hardware.

## Before you start

- Confirm your radio is a FLEX-8x00 or a compatible model. The external APD tab does not appear on unsupported hardware.
- Connect the radio and verify it is online in AetherSDR.

## Steps

1. Open **Radio Setup** from the main menu.
2. Select the **APD** tab.
3. For each TX antenna listed, use the **Sampler Port** selector to choose the external sampler port you want to assign (INTERNAL, RX_A, RX_B, XVTA, or XVTB).
4. Confirm your selections. Changes take effect immediately; no separate Save step is required.

## What each control does

| Control | Behavior |
|---|---|
| Sampler Port | Selects which external sampler port is used for APD on the corresponding TX antenna. Options are INTERNAL, RX_A, RX_B, XVTA, and XVTB. Only ports available on the connected hardware appear as selectable options. |

## Tips

- If a port does not appear in the list, the hardware does not expose that port on your specific FLEX-8x00 variant. Check your radio's rear-panel connections and firmware version.
- Set INTERNAL if you are not using an external sampler and want the radio to use its built-in APD reference.

## Related

- [radio-setup-overview.md](radio-setup-overview.md)
- [flex-8x00-hardware-guide.md](flex-8x00-hardware-guide.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
