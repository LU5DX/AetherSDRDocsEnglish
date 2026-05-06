# Cancel an active or stuck transmission with the status bar TX badge

The status bar TX badge gives you a single click to drop the transmitter out of TX — useful when MOX is stuck on, a tune carrier is still running, or any other condition has left the radio keyed and the TX Controls applet is not immediately to hand.

## Before you start

- AetherSDR must be connected to the radio. The TX badge only appears in the status bar when a radio connection is active.
- The radio must currently be in a transmitting state (MOX keyed or tune carrier active) for the badge to be actionable.

## Steps

1. Locate the TX badge in the AetherSDR status bar at the bottom of the main window. The badge is visible and lit when the radio is transmitting.
2. Click the TX badge once.
3. Confirm the radio has returned to receive: the RF Pwr gauge in the TX Controls applet drops to zero, the MOX button returns to its unlit state (blue), and the TUNE button label returns to "TUNE" if a tune carrier was running.

## Tips

- If the TX Controls applet is visible, you can also click MOX to toggle transmit off, or click TUNE to stop an active tune carrier (the button reads "TUNING..." while active). The status bar TX badge is the fastest path when the applet is collapsed or out of view.
- If MOX was engaged by an external CAT or TCI command, clicking the TX badge sends the same unkey command. The source of the original PTT does not matter.

## Troubleshooting

- **Clicking the TX badge does not stop transmission** — The radio may be keyed by hardware PTT (footswitch or microphone PTT line). Release the hardware PTT first; software commands cannot override a held hardware PTT line.
- **TX badge is not visible during transmission** — The status bar may be hidden. Check that the main window is not in Minimal Mode (`View > Minimal Mode`). Disabling Minimal Mode restores the status bar.

## Related

- [Toggle MOX to manually key the transmitter](toggle-mox-to-manually-key-the-transmitter.md)
- [Start a tune carrier to check SWR](start-a-tune-carrier-to-check-swr.md)
- [TX Controls overview](overview.md)
