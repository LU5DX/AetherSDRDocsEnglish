# Blend the Body enhancement with Mix

The "Body / Mix" knob controls how much of the processed low-frequency signal is blended back with the dry audio. Use it to dial in the amount of Body enhancement without overwhelming the original signal.

## Before you start

- PUDU must be enabled on the side you want to adjust. If the Body group is not visible, the PUDU stage may be bypassed — see [Bypass PUDU from either chain](bypass-pudu-from-either-chain.md).
- Open the relevant applet: "Aetherial TX Voice Processor" for transmit, or "Aetherial RX Poodoo™" for receive. Double-click the PUDU stage in the CHAIN widget on the matching side to open the frameless editor if the applet is not already visible.
- When the PUDU stage is bypassed, the entire applet tile dims to approximately 55 % opacity. Full opacity is restored as soon as the stage is re-enabled.

## Steps

1. Locate the **Body** group bracket in the applet. It contains three knobs: **Drive**, **Tune**, and **Mix**.
2. Turn the **Mix** knob under the **Body** bracket to the desired blend level.
   - Turning toward 0 % passes the dry signal with no low-frequency enhancement.
   - Turning toward 100 % blends the full processed signal in.
3. The value is saved automatically. No additional confirmation is needed.

## Inline value editing

v26.5.2.1 adds direct keyboard entry for knob values.

1. Click the value text below a knob to activate the inline editor. The text area gains a thin cyan border to indicate edit mode.
2. Type a new value. The editor accepts:
   - Plain numbers (e.g., `30`, `8500`)
   - Decimal values (e.g., `15.5`)
   - Locale-aware formatting (e.g., `12,5` in comma-decimal locales)
   - Numbers with trailing unit text (e.g., `30 %`, `5.0 kHz`, `100 Hz`)
3. Press **Enter** or click outside the editor to commit the value. The knob updates to the new setting, clamped to its valid range.
4. Press **Escape** to cancel the edit without changing the value.
5. While the editor is active, the mouse wheel adjusts the knob as usual — wheel events are forwarded to the knob.

The inline editor uses the same formatting as the normal knob display (for example, percentage values appear as `30 %`, frequency values as `100 Hz` or `5.0 kHz`).

## What each control does

| Control            | Default                                                                                      | Valid range                               |
|--------------------|----------------------------------------------------------------------------------------------|-------------------------------------------|
| **Even**           | Not selected by default                                                                      | N/A (radio button exclusive with Odd)     |
| **Odd**            | Not selected by default                                                                      | N/A (radio button exclusive with Even)    |
| **Poo / Drive** (TX) | 6.0 dB                                                                                     | 0.0 to 24.0 dB                             |
| **Poo / Tune** (TX)  | 100 Hz                                                                                      | 50 to 160 Hz                               |
| **Poo / Mix** (TX)   | 30 %                                                                                        | 0 % to 100 % (stored as 0.0 to 1.0)       |
| **Poo / Drive** (RX) | 6.0 dB                                                                                     | 0.0 to 24.0 dB                             |
| **Poo / Tune** (RX)  | 100 Hz                                                                                      | 50 to 160 Hz                               |
| **Poo / Mix** (RX)   | 30 %                                                                                        | 0 % to 100 % (stored as 0.0 to 1.0)       |
| **Doo / Tune** (TX)  | 5000 Hz                                                                                     | 1000 to 10000 Hz                           |
| **Doo / Air** (TX)   | 6.0 dB                                                                                     | 0.0 to 24.0 dB                             |
| **Doo / Mix** (TX)   | 30 %                                                                                        | 0 % to 100 % (stored as 0.0 to 1.0)       |
| **Doo / Tune** (RX)  | 5000 Hz                                                                                     | 1000 to 10000 Hz                           |
| **Doo / Air** (RX)   | 6.0 dB                                                                                     | 0.0 to 24.0 dB                             |
| **Doo / Mix** (RX)   | 30 %                                                                                        | 0 % to 100 % (stored as 0.0 to 1.0)       |
| AetherVoice logo   | Animated branded logo that pulses with the wet-signal RMS. Displays 'AetherVoice™' wordmark. | PooDooLogo widget — 40 px minimum height. |

The knob display shows the value as a whole-number percentage (for example, "30 %"). Internally the value is stored as a linear fraction between 0.0 and 1.0.

## Tips

- The TX and RX sides have fully independent Mix values. Adjusting one does not affect the other.
- Watch the PooDoo logo — its brightness pulses with the wet (processed) signal RMS. A noticeable increase in pulse intensity as you raise Mix confirms the low-frequency processing is audible in the blend.
- Start at the default of 30 % and increase gradually. Heavy Mix values can thicken the low end to the point of muddiness, especially if **Poo / Drive** is also high.
- Use the inline edit feature to type exact values instead of fine-tuning with the mouse wheel — for example, type `45` to set exactly 45 % Mix.
- The **Even** and **Odd** radio buttons select the processing mode. Even mode uses Aphex-style asymmetric shaping with Big Bottom LF saturation. Odd mode uses Behringer-style symmetric tanh shaping with a feed-forward bass compressor.
- The **Body** group bracket contains the low-frequency processor controls: **Drive**, **Tune**, and **Mix**.
- The **Clarity** group bracket contains the high-frequency processor controls: **Tune**, **Air**, and **Mix**.

## Related

- [Dial Poo / Drive for LF thickness](dial-poo-drive-for-lf-thickness.md)
- [Tune Poo to the fundamental of your voice (TX) or to bring out RX program lows](tune-poo-to-the-fundamental-of-your-voice-tx-or-to-bring-out-rx-program-lows.md)
- Blend the Clarity excitement with Mix
- [Aetherial TX Voice Processor / Aetherial RX Poodoo overview](overview.md)