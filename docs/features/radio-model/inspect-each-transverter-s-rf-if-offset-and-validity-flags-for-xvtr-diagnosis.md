# Inspect each transverter's RF/IF offset and validity flags for XVTR diagnosis

Use the `XvtrInfo` struct to read the RF/IF frequency offsets, LO error, receive gain, maximum power, and validity flags for each transverter attached to the radio. This lets you confirm whether a transverter's reported offset and validity state are correct when diagnosing unexpected frequency readouts or missing transverter entries.

## Before you start

- The radio must be connected and at least one transverter must be configured.
- You need access to the AetherSDR diagnostic or developer console where `XvtrInfo` fields are exposed.

## Steps

1. Open the transverter list in the diagnostic console and locate the entry for the transverter you want to inspect.
2. Read the `XvtrInfo` fields for that entry — check the RF offset, IF offset, LO error, receive gain, maximum power, and validity flags against the values you expect for that transverter.

## What each field contains

| Field | Description |
|---|---|
| RF offset | The frequency offset applied on the RF (antenna) side of the transverter. Compare this against the transverter's datasheet value to confirm correct configuration. |
| IF offset | The frequency offset applied on the IF (radio) side. A mismatch here causes the radio to display the wrong frequency. |
| LO error | Reported local-oscillator error for the transverter. A non-zero value indicates the transverter's LO is off by that amount. |
| Receive gain | The gain value applied during receive on this transverter. |
| Maximum power | The maximum transmit power limit for this transverter. |
| Validity flags | Boolean flags indicating whether the transverter entry is considered valid by the radio firmware. A false or unset flag means the radio is not treating this entry as active — check that the transverter is properly registered and that its configuration was accepted. |

## Tips

- If a transverter entry is missing from the list entirely, verify that the radio firmware received and acknowledged the transverter registration before re-reading `XvtrInfo`.
- If the RF or IF offset looks correct but the displayed frequency is still wrong, cross-check the LO error field — even a small non-zero value shifts the displayed frequency.
- Validity flags that remain unset after configuration often indicate a firmware rejection of the transverter parameters; re-send the configuration and inspect the flags again.

## Related

- [transverter-configuration.md](transverter-configuration.md)
- [frequency-readout-troubleshooting.md](frequency-readout-troubleshooting.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
