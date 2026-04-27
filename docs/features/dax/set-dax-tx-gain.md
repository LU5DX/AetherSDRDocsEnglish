# Set DAX TX gain

Adjust the DAX TX gain slider to control how much audio from your transmit slice is sent through the DAX TX stream to connected software.

## Before you start

- The radio must be connected. The DAX Audio applet requires an active radio connection.
- DAX must be enabled. Click `Enable` in the DAX Audio applet if it is not already active.

## Steps

1. Click the `DAX` tray button on the right sidebar to open the DAX Audio applet.
2. Locate the `TX:` row at the bottom of the applet. The slider to the right of the TX status indicator is the TX gain control.
3. Drag the thumb on the `TX gain+meter` slider left or right to decrease or increase TX gain. The value is saved immediately and persists as `DaxTxGain`.

## What each control does

| Control | Default | Range | Persisted key |
|---|---|---|---|
| `TX gain+meter` slider | 0.5 | 0.0 – 1.0 | `DaxTxGain` |
| TX status indicator | — | — or Slice A–H | *(none)* |

The TX status indicator shows which slice currently holds TX privileges. It updates automatically as the TX slice changes. The meter bar behind the slider displays the live TX audio level scaled by the current gain setting.

## Tips

- The meter bar reflects post-fader level: it shows the actual output level after your gain setting is applied. Moving the slider gives immediate visual feedback even before you transmit.
- A gain of 0.5 is the default starting point. If your digital mode software reports overdriven or weak audio, adjust from there in small increments.

## Related

- [DAX Audio overview](overview.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Set DAX RX gain per channel](set-dax-rx-gain-per-channel.md)
- [Identify which slice is the TX slice](identify-which-slice-is-the-tx-slice.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)
