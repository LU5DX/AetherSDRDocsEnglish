# Configure the external APD tab on FLEX-8x00 radios

The APD External Sampler Port Assignment controls which external sampler port is used for a given TX antenna on FLEX-8x00 radios. Use this tab in Radio Setup to select the port (such as INTERNAL, RX_A, RX_B, XVTA, or XVTB) that feeds the APD circuit.

## Before you start

- You must be connected to a FLEX-8x00 or compatible radio that supports external APD.
- Open Radio Setup from the menu bar.

## Steps

1. In Radio Setup, select the **APD** tab.
2. For each TX antenna listed, use the port selector to choose the external sampler port you want to assign (for example, **INTERNAL**, **RX_A**, **RX_B**, **XVTA**, or **XVTB**).
3. Confirm your selection. The radio applies the assignment immediately.

## What each control does

| Control | Behavior |
|---|---|
| TX Antenna row | Identifies the transmit antenna for which you are assigning a sampler port. One row appears for each available TX antenna. |
| Sampler port selector | Sets the external sampler port routed to the APD circuit for that TX antenna. Available options are INTERNAL, RX_A, RX_B, XVTA, and XVTB. Only ports supported by the connected radio are shown. |

## Tips

- If a port does not appear in the selector, the connected radio does not expose that port for APD use.
- Assigning INTERNAL uses the radio's built-in sampling path rather than an external port.

## Related

- radio-setup-overview.md
- apd-overview.md
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
