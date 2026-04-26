# Listen to a TX sidetone monitor

The TX sidetone monitor lets you hear your own transmitted audio in your headphones while on phone modes. Use it to confirm your audio is clean and at the right level without relying on a separate receiver.

## Before you start

- AetherSDR must be connected to the radio.
- The active slice must be in a phone mode (SSB, AM, FM). The Phone/CW applet displays phone controls only when a phone mode is active; switching to CW shows the CW panel instead.
- Open the Phone/CW applet in the Applet Panel. If it is not visible, click the **P/CW** tray button on the right sidebar.

## Steps

1. In the Phone/CW applet, locate the **MON** toggle button.
2. Click **MON** to enable the sidetone monitor. The button lights up when active.
3. Adjust the **Monitor volume** slider (0–100) to set the monitor level in your headphones.
4. To disable the monitor, click **MON** again.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| MON | Enables or disables the TX sidetone monitor. | Off | On / Off | — |
| Monitor volume | Sets the sideband monitor playback volume. | — | 0–100 | — |

## Tips

- The monitor plays back what the radio is actually transmitting, so it reflects any speech processing or compression applied by the **PROC** control.
- If you are using **PC** as the mic source, the mic gain value is stored client-side as `PcMicGain` (default 50, range 0–100) rather than reported by the radio.

## Related

- [Phone/CW overview](overview.md)
- [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md)
- [Enable speech processor at NOR, DX, or DX+ level](enable-speech-processor-at-nor-dx-or-dx-level.md)
- [Pick a mic source (MIC, BAL, LINE, ACC, PC)](pick-a-mic-source-mic-bal-line-acc-pc.md)
