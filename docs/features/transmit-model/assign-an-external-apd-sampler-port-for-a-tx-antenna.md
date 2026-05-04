# Assign an external APD sampler port for a TX antenna

The APD External Sampler Port Assignment controls which external sampler port is used for a given TX antenna when performing Automatic Power Distortion (APD) calibration. This setting applies only to radios that support external APD, such as the FLEX-8x00 and compatible models.

## Before you start

- Confirm your radio supports external APD (FLEX-8x00 or compatible).
- Connect to the radio before opening Radio Setup.

## Steps

1. Open **Radio Setup** and select the **APD** tab.
2. Locate the TX antenna you want to configure.
3. In the **Sampler Port** selector for that antenna, choose the port you want to assign: `INTERNAL`, `RX_A`, `RX_B`, `XVTA`, or `XVTB`.
4. Confirm the selector shows only the ports that are available for your hardware configuration — unavailable ports appear grayed out.

## What each control does

| Control | Behavior |
|---|---|
| Sampler Port selector | Sets the external sampler port assigned to the TX antenna. Options are `INTERNAL`, `RX_A`, `RX_B`, `XVTA`, and `XVTB`. Only ports supported by the connected radio are selectable. |

## Tips

- If a port you expect to see is missing or grayed out, verify your radio model and any connected transverter hardware — available ports depend on the physical configuration reported by the radio.
- Each TX antenna can be assigned a different sampler port; assignments are independent per antenna.

## Related

- [radio-setup-apd.md](radio-setup-apd.md)
- [flex-8x00-overview.md](flex-8x00-overview.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
