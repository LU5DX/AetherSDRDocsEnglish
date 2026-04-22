# Spot which antennas cannot TX on the current band (amber or dim)

The Antenna Genius applet colour-codes every antenna button to show whether that antenna can transmit on the current band. Checking button colours before you transmit tells you immediately which antennas are TX-capable and which are receive-only or have no permission at all on that band.

## Before you start

- The Antenna Genius applet must be open and connected. The status label should read "Connected — \<name\> v\<version\>".
- The radio must be tuned to the band you want to check; button colours update automatically when the band changes.

## Steps

1. Click the "AG" tray button on the right sidebar to open the Antenna Genius applet.
2. Look at the antenna buttons in the Port A (and Port B, if visible) grid.
3. Read the colour of each button:
   - **Blue** — antenna has TX and RX permission on the current band.
   - **Amber** — antenna has RX permission only on the current band; transmitting on this antenna is not permitted.
   - **Dim (unlit)** — antenna has no permission at all on the current band.
4. Choose a blue button for normal TX+RX operation. Avoid amber and dim buttons if you intend to transmit.

## What each control does

| Control | Colour / state | Meaning |
|---|---|---|
| Port A antenna buttons | Blue (checked) | Selected; TX and RX allowed on current band |
| Port A antenna buttons | Amber (checked) | Selected; RX only on current band |
| Port A antenna buttons | Dim | Not selected or no permission on current band |
| Port B antenna buttons | Same three states | Same meaning for Port B |
| Port A band / Port B band labels | Band name or "—" | Shows the band AetherSDR is currently evaluating permissions against |

## Tips

- Button colours update in real time whenever the radio changes band, so you do not need to reopen the applet after tuning.
- If Port B is hidden, the connected Antenna Genius reports only one radio port; all antenna buttons are on Port A.
- An antenna button that is dim because it is already selected on the other port is a separate lockout condition. See [Swap radios that share the AG (antennas in use by the other port are locked out)](swap-radios-that-share-the-ag-antennas-in-use-by-the-other-port-are-locked-out.md) for details.

## Troubleshooting

- **All buttons appear dim and the band label shows "—"** — AetherSDR cannot determine the current band. Confirm the radio is connected and tuned to a recognised amateur band.
- **Colours do not change after tuning** — Verify the status label still reads "Connected — \<name\> v\<version\>". If the connection dropped, click "Disconnect" then "Connect" to re-establish it.

## Related

- [Antenna Genius overview](overview.md)
- [Select an antenna for Port A or Port B](select-an-antenna-for-port-a-or-port-b.md)
- [Enable AUTO mode so the AG follows radio band changes](enable-auto-mode-so-the-ag-follows-radio-band-changes.md)
- [Swap radios that share the AG (antennas in use by the other port are locked out)](swap-radios-that-share-the-ag-antennas-in-use-by-the-other-port-are-locked-out.md)
