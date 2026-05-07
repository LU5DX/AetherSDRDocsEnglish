# Assign an external APD sampler port for a TX antenna

The APD External Sampler Port Assignment determines which external sampler port is used for a given TX antenna on radios that support external APD. This setting is available on FLEX-8x00 and compatible radios.

## Before you start

- Confirm your radio is a FLEX-8x00 or a compatible model that supports external APD.
- Connect to the radio in AetherSDR before opening Radio Setup.

## Steps

1. Open **Radio Setup** and select the **APD** tab.
2. Locate the TX antenna you want to configure, then select the desired sampler port from the **External Sampler Port** dropdown. Available options are **INTERNAL**, **RX_A**, **RX_B**, **XVTA**, and **XVTB**.

## What each control does

| Control | Behavior |
|---|---|
| **External Sampler Port** | Sets which hardware port is used to sample the TX signal for APD on the selected TX antenna. Only ports supported by the connected radio are shown. Select **INTERNAL** to use the radio's built-in sampler. Select **RX_A**, **RX_B**, **XVTA**, or **XVTB** to route APD sampling through the corresponding external port. |

## Tips

- If a port does not appear in the dropdown, the connected radio does not expose that port for APD sampling.
- Changing the sampler port takes effect immediately; no restart is required.
- Use an external port (for example, **XVTA** or **XVTB**) when a transverter or external preamplifier is in the signal path and you need accurate APD measurements beyond the radio's internal coupler.

## Related

- [Radio Setup overview](radio-setup.md)
- [APD tab reference](radio-setup-apd.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
