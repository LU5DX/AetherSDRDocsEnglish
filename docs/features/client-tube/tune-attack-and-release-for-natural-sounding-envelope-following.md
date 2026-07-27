# Tune Attack and Release for natural-sounding envelope following

Attack and Release set how quickly the envelope follower tracks rising and falling signal levels. They only take effect when Envelope is set to a non-zero value. Dialing these two knobs prevents the tube character from snapping on and off unnaturally during speech or audio transients.

## Before you start

- The Tube stage must be enabled on the side you want to adjust (TX or RX). See [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md).
- Envelope must be set to a non-zero value. Attack and Release have no audible effect at 0 %. See [Use Envelope to add dynamic drive on transients](use-envelope-to-add-dynamic-drive-on-transients.md).
- Open the floating editor for the side you want to adjust: double-click the TUBE stage in the CHAIN widget on the TX or RX side. The editor is titled "Aetherial Tube — TX" or "Aetherial Tube — RX".

## Steps

1. Open the floating editor by double-clicking the TUBE stage in the CHAIN widget on the TX or RX side.
2. Locate the Attack knob in the right column of the editor.
3. Adjust Attack to set how quickly the envelope follower responds when signal levels rise. Lower values make the follower react faster to transients; higher values smooth over short peaks.
4. Locate the Release knob directly below Attack in the right column.
5. Adjust Release to set how quickly the follower recovers after levels drop. Lower values return to the resting drive faster; higher values let the effect hang longer after a peak.
6. Monitor the transfer curve and the live input ball while transmitting or receiving to confirm the drive modulation looks natural.

## Inline value editing

Every knob in the Aetherial Tube editor supports direct text entry. Click the numeric value displayed below any knob to activate an inline QLineEdit overlay that replaces the painted value text. Type a number (with or without units) and press Enter, or click elsewhere, to commit. The value is clamped to the knob's valid range.

- Enter "12.5 ms", "−6 dB", or "0.75" — the editor strips trailing labels automatically.
- In locales that use a comma as decimal separator, "12,5" is parsed correctly.
- Press Escape to cancel editing and revert to the previous value.
- While the inline editor is focused, mouse-wheel events are forwarded to the knob for traditional adjustment.
- The overlay uses a subtle dark background and cyan border on focus for visibility.

## What each control does

| Control | Default | Valid range |
|---------|---------|-------------|
| Attack  | 5.00 ms | 0.1 to 30.0 ms |
| Release | 35.00 ms | 10.0 to 500.0 ms |
| RN2     | TX-only toggle (hidden in RX mode). Enables RNNoise neural denoiser on the mic input before the DSP chain. Suppresses background noise before it reaches gate/compressor/saturator. | Located in the floating StripTubePanel below the output level meter, TX side only. Voice modes only — digital modes (RADE, DAX, RTTY, FT8, FDV, CW) bypass this stage. Setting persisted via AudioEngine. |

**Attack** — Uses exponential mapping across its range. Sets how quickly the envelope follower responds to rising signal levels when Envelope ≠ 0. The label displays as "X.XX ms" below 10 ms and "X.X ms" above 10 ms. Setting key: `ClientTubeTxAttackMs` / `ClientTubeRxAttackMs`.

**Release** — Uses exponential mapping across its range. Sets how quickly the envelope follower recovers after signal levels fall when Envelope ≠ 0. The label displays as "X.XX ms" below 100 ms and "X.X ms" above 100 ms. Setting key: `ClientTubeTxReleaseMs` / `ClientTubeRxReleaseMs`.

**RN2** — TX-only toggle button located in the StripTubePanel below the output level meter. Uses the `RN2` label. See Reduce background noise with RN2 for full details.

## Tips

- Attack and Release are independent per side. Changes made in the TX editor do not affect the RX editor and vice versa.
- For natural-sounding speech on TX, start with the defaults (Attack 5.00 ms, Release 35.00 ms) and lengthen Release first. Very short Release values can produce a pumping or chattering character.
- For RX tone shaping, a longer Attack (10 ms or more) lets transient peaks pass through before the envelope follower engages, preserving initial consonants in received audio.
- The live input ball on the transfer curve moves in real time. With Envelope set, you can see the operating point shifting as levels change, which helps confirm that Attack and Release feel right before going on air.
- When the Tube stage is bypassed, the entire docked applet tile dims to approximately 55 % opacity. This visual cue applies to both the TX and RX tiles and makes it easy to confirm at a glance that the stage is not processing audio. The tile returns to full opacity as soon as the stage is re-enabled.
- Knob visual colors (background ring, arc, pointer, label, and value text) are theme-driven. They respect the per-applet container override (e.g., the amber knob foreground unique to the compression applet) by walking the widget hierarchy to `applet/tube`.

## Troubleshooting

- **Adjusting Attack or Release has no audible effect** — Envelope is likely set to 0 %. Set Envelope to a positive or negative value first; Attack and Release only apply when the envelope follower is active.
- **The effect sounds too abrupt or chattery** — Release is set too low. Increase Release toward 100 ms or higher to smooth the recovery.
- **Loud peaks cause the drive to snap on hard** — Attack is set too low. Increase Attack to 10–20 ms to slow the follower's response to transients.
- **The docked tile looks faded and the stage is not processing** — The Tube stage is bypassed. The tile dims to 55 % opacity when bypassed. Re-enable the stage to restore full opacity and resume processing. See [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md).
- **Typing a value into the inline editor has no effect** — Ensure you press Enter or click elsewhere to commit. Pressing Escape cancels the edit and reverts to the previous value.

## Related

- [Use Envelope to add dynamic drive on transients](use-envelope-to-add-dynamic-drive-on-transients.md)
- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md)
- [Monitor output clipping with the level meter in the editor](monitor-output-clipping-with-the-level-meter-in-the-editor.md)
- Reduce background noise with RN2