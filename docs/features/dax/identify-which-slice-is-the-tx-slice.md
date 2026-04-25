# Identify which slice is the TX slice

The DAX Audio applet shows a live TX assignment indicator that tells you which slice currently holds TX privileges. Use this when you need to confirm which slice drives the DAX TX stream before transmitting digital audio.

## Before you start

- AetherSDR must be connected to the radio. The TX indicator requires an active radio connection.
- The DAX applet must be visible. If you do not see it, click the DAX tray button on the right sidebar to open it.

## Steps

1. Click the **DAX** tray button on the right sidebar to open the DAX Audio applet.
2. Look at the **TX:** row at the bottom of the applet.
3. Read the status indicator immediately to the right of the **TX:** label.
   - If a slice holds TX privileges, the indicator shows **Slice A** through **Slice H**, matching the letter assigned to that slice.
   - If no slice currently holds TX privileges, the indicator shows **—**.

## What each control does

| Control | Description | States | Persisted key |
|---|---|---|---|
| TX assignment indicator | Shows which slice currently holds TX privileges and drives the DAX TX stream. Updated automatically when TX changes between slices. | **—** (none) or **Slice A–H** | None |
| TX gain+meter | Combined level meter and gain slider for the DAX TX stream. | 0.0–1.0 (default 0.5) | `DaxTxGain` |

## Tips

- The TX indicator updates immediately whenever TX privileges transfer to a different slice. You do not need to refresh or reopen the applet.
- The RX rows above the **TX:** row show which slice is routed to each DAX channel (DAX 1 through DAX 4). Those indicators follow the same **Slice A–H** or **—** format and are independent of the TX indicator.

## Related

- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
- [Set DAX TX gain](set-dax-tx-gain.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [DAX Audio overview](overview.md)
