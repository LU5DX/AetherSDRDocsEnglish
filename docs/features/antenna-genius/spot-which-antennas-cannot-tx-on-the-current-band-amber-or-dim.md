# Spot which antennas cannot TX on the current band (amber or dim)

The antenna buttons in the Antenna Genius applet are colour-coded to show TX and RX permission on the current band. This lets you see at a glance which antennas are available for transmit before you click one.

## Before you start

- The Antenna Genius applet must be open. Click the "AG" tray button on the right sidebar to show it.
- The applet must be connected to a device. The status label must read "Connected — \<name\> v\<version\>".
- The radio must be on the band you want to check. Button colours update automatically when the band changes.

## Steps

1. Look at the antenna buttons in the Port A or Port B section.
2. Read the button colour:
   - **Blue (checked)** — the selected antenna has TX and RX permission on the current band.
   - **Amber (checked)** — the selected antenna has RX-only permission on the current band; transmit is not available on this antenna.
   - **Dim (unchecked, visually muted)** — the antenna has no permission on the current band for either TX or RX.
3. If you need a TX-capable antenna, click a button that is not dim. After selection, confirm it lights blue rather than amber.

## What each control does

| Control | Colour / State | Meaning |
|---|---|---|
| Port A antenna buttons | Blue | Antenna selected; TX and RX permitted on the current band. |
| Port A antenna buttons | Amber | Antenna selected; RX only on the current band — no TX. |
| Port A antenna buttons | Dim | No permission on the current band. |
| Port B antenna buttons | Blue | Antenna selected; TX and RX permitted on the current band. |
| Port B antenna buttons | Amber | Antenna selected; RX only on the current band — no TX. |
| Port B antenna buttons | Dim | No permission on the current band. |

Buttons are also disabled and dim when the same antenna is already selected on the other port. See [Swap radios that share the AG (antennas in use by the other port are locked out)](swap-radios-that-share-the-ag-antennas-in-use-by-the-other-port-are-locked-out.md) for details on that case.

## Tips

- Button colours refresh automatically when the radio changes band, so you do not need to reopen the applet after a band change.
- If you use AUTO mode, the applet selects antennas based on band-follow rules. The same colour coding applies to the automatically selected antenna. See [Enable AUTO mode so the AG follows radio band changes](enable-auto-mode-so-the-ag-follows-radio-band-changes.md).

## Troubleshooting

- **All buttons are dim after connecting** — The applet may not yet have received band information from the radio. Confirm the radio is tuned to a valid band and that the status label shows "Connected". If the applet was opened before the radio was on a band, change bands once to trigger a refresh.
- **Colours do not update when changing bands** — The band-follow update requires an active connection to the Antenna Genius device. Verify the status label still reads "Connected — \<name\> v\<version\>" and that no error is displayed.

## Related

- [Antenna Genius overview](overview.md)
- [Select an antenna for Port A or Port B](select-an-antenna-for-port-a-or-port-b.md)
- [Enable AUTO mode so the AG follows radio band changes](enable-auto-mode-so-the-ag-follows-radio-band-changes.md)
- [Swap radios that share the AG (antennas in use by the other port are locked out)](swap-radios-that-share-the-ag-antennas-in-use-by-the-other-port-are-locked-out.md)
