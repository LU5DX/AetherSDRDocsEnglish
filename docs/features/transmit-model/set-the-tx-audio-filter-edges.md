# Set the TX audio filter edges

The TX audio filter edges define the low- and high-frequency boundaries of the transmitted audio signal. Adjusting these cutoffs shapes the transmitted audio bandwidth sent to the radio.

## Steps

1. Open the Transmit panel.
2. Set the **Low Cut** spinbox to the desired low-frequency cutoff in Hz. Step buttons snap to the nearest 50 Hz multiple.
3. Set the **High Cut** spinbox to the desired high-frequency cutoff in Hz. Step buttons snap to the nearest 50 Hz multiple.

> Both filter edges are sent to the radio together in a single command whenever either value changes.

## What each control does

| Control | Default | Valid Range |
|---|---|---|
| **Low Cut** | 50 Hz | 0–10000 Hz |
| **High Cut** | 3300 Hz | 0–10000 Hz |
## Tips

- Keep **Low Cut** below **High Cut**; reversing the values produces no usable audio passband.
- A typical SSB voice passband is 100–2800 Hz or 100–3000 Hz. Widening the high cut to 3300 Hz or beyond increases audio fidelity but also increases occupied bandwidth.
- EQ applets update their guide lines automatically when the filter edges change.

## Related

- [transmit-model.md](transmit-model.md)
- [tx-profile.md](tx-profile.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->
