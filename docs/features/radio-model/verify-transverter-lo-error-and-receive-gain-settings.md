# Verify transverter LO error and receive gain settings

Use the `XvtrInfo` struct to inspect each transverter's LO error, receive gain, RF/IF frequency offsets, and validity flags so you can diagnose unexpected frequency readouts or missing transverter entries.

## Before you start

- Connect to a radio that has at least one transverter configured.
- Ensure the transverter is enabled and visible in the transverter list.

## Steps

1. Open the transverter configuration view for the attached radio and locate the entry for the transverter you want to inspect.
2. Check the **validity flag** for the entry. A valid entry will report the transverter as active; an invalid entry indicates the radio did not return a usable configuration for that slot.
3. Read the **LO error** value. A non-zero value means the transverter's local oscillator is offset from its nominal frequency by that amount. Account for this value when interpreting displayed frequencies.
4. Read the **receive gain** value. Confirm it matches the gain you configured. An unexpected value indicates the radio has overridden or not yet applied your setting.
5. Cross-check the **RF frequency offset** and **IF frequency offset** values to confirm the transverter is translating between the expected bands.
6. If any value is missing or out of range, disconnect and reconnect to the radio to force a fresh configuration pull, then repeat steps 2–5.

## What each field does

| Field | Behavior |
|---|---|
| RF frequency offset | The offset applied to convert the IF frequency to the on-air RF frequency. Used to calculate the displayed tuned frequency. |
| IF frequency offset | The intermediate frequency the radio tunes to before the transverter shifts it to RF. |
| LO error | The measured deviation of the transverter's local oscillator from its nominal value. A non-zero value causes a predictable frequency readout error equal to this offset. |
| Receive gain | The gain applied on the receive path through the transverter. Verify this matches your intended setting. |
| Maximum power | The rated maximum transmit power for the transverter. Used by the radio to cap output and protect the transverter. |
| Validity flag | Indicates whether the radio returned a complete and usable configuration for this transverter slot. An invalid entry means the transverter data should not be trusted. |

## Tips

- If the validity flag is false, the other fields in that `XvtrInfo` entry are unreliable — do not act on LO error or gain values until the entry reports valid.
- LO error is reported in the same units as the frequency fields (Hz). A small but consistent frequency offset on receive is often traced directly to a non-zero LO error value.
- Changing receive gain on the radio side does not immediately update `XvtrInfo`; reconnect or re-query the transverter list to see the updated value.

## Related

- [transverter-configuration.md](transverter-configuration.md)
- [diagnose-frequency-readout-errors.md](diagnose-frequency-readout-errors.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
