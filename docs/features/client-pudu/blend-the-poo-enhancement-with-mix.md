# Blend the Poo enhancement with Mix

The "Poo / Mix" knob controls how much of the processed low-frequency signal is blended back with the dry audio. Use it to dial in the amount of Poo enhancement without overwhelming the original signal.

## Before you start

- PUDU must be enabled on the side you want to adjust. If the Poo group is not visible, the PUDU stage may be bypassed — see [Bypass PUDU from either chain](bypass-pudu-from-either-chain.md).
- Open the relevant applet: "Aetherial TX Poodoo™" for transmit, or "Aetherial RX Poodoo™" for receive. Double-click the PUDU stage in the CHAIN widget on the matching side to open the frameless editor if the applet is not already visible.

## Steps

1. Locate the **Poo** group bracket in the applet. It contains three knobs: **Drive**, **Tune**, and **Mix**.
2. Turn the **Mix** knob under the **Poo** bracket to the desired blend level.
   - Turning toward 0 % passes the dry signal with no low-frequency enhancement.
   - Turning toward 100 % blends the full processed signal in.
3. The value is saved automatically. No additional confirmation is needed.

## What each control does

| Control | Default | Valid range | Persisted setting |
|---|---|---|---|
| **Poo / Mix** (TX) | 30 % | 0 % to 100 % (stored as 0.0 to 1.0) | `ClientPuduTxPooMix` |
| **Poo / Mix** (RX) | 30 % | 0 % to 100 % (stored as 0.0 to 1.0) | `ClientPuduRxPooMix` |

The knob display shows the value as a whole-number percentage (for example, "30 %"). Internally the value is stored as a linear fraction between 0.0 and 1.0.

## Tips

- The TX and RX sides have fully independent Mix values. Adjusting one does not affect the other.
- Watch the PooDoo logo — its brightness pulses with the wet (processed) signal RMS. A noticeable increase in pulse intensity as you raise Mix confirms the low-frequency processing is audible in the blend.
- Start at the default of 30 % and increase gradually. Heavy Mix values can thicken the low end to the point of muddiness, especially if **Poo / Drive** is also high.

## Related

- [Dial Poo Drive for LF thickness](dial-poo-drive-for-lf-thickness.md)
- [Tune Poo to the fundamental of your voice (TX) or to bring out RX program lows](tune-poo-to-the-fundamental-of-your-voice-tx-or-to-bring-out-rx-program-lows.md)
- [Blend the Doo excitement with Mix](blend-the-doo-excitement-with-mix.md)
- [Aetherial TX Poodoo / Aetherial RX Poodoo overview](overview.md)
