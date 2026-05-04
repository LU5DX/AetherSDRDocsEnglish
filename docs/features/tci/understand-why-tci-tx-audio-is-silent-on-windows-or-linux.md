# Understand why TCI TX audio is silent on Windows or Linux

AetherSDR's Main Window coordinates platform-aware DAX TX routing policy. On Windows and Linux, TCI TX audio can appear silent due to how the DAX TX audio path is selected for those platforms.

## Before you start

- Confirm you are running AetherSDR on Windows or Linux.
- Confirm your FlexRadio hardware is connected (LAN or SmartLink WAN) and a slice is active.
- Confirm TCI TX audio is enabled in your TCI client.

## Steps

1. Open AetherSDR. The application launches the Main Window automatically.
2. Check that the correct DAX TX audio device is selected in your system audio settings and that AetherSDR is not routing DAX TX through an external route that bypasses the TCI audio path. On Windows and Linux, AetherSDR applies a platform-specific DAX TX routing policy — if the policy selects `ExternalDax2` or `None` mode instead of `HostedDax`, TCI TX audio will produce no output.
3. If TX audio is still silent, open the audio or DAX settings in AetherSDR and verify the DAX TX mode is set to the hosted DAX bridge option rather than an external-only or disabled route.
4. Confirm the TX EQ chain is not misconfigured. As of v0.9.5.1, the EQ stage is bypassed (not removed) when disabled — audio still flows through to the radio. If you hear nothing even with EQ bypassed, the silence is in the DAX TX routing layer, not the EQ stage.

## What each control does

| Control | Behavior |
|---|---|
| DAX TX routing policy | Determines how TX audio is delivered on each platform. On Windows and Linux, the policy chooses between `HostedDax`, `ExternalDax2`, or `None`. Only `HostedDax` carries TCI TX audio to the radio. |
| TX EQ chain (CHAIN widget) | Applies parametric EQ to the TX audio before transmission. When the EQ stage is disabled (bypassed), audio passes through unmodified. The TX FFT analyzer in the EQ editor continues to display live mic input regardless of whether the EQ stage is active. |

## Tips

- If you recently upgraded to v0.9.5.1, note that the TX EQ bypass behaviour changed: audio now always flows through the pipeline even when the EQ stage is off. Silent TX is therefore not caused by a bypassed EQ — investigate the DAX TX platform routing instead.
- On Linux, verify that the correct ALSA or PipeWire/PulseAudio device is mapped to the DAX TX channel; a mismatched device will appear as silence without an error message.
- On Windows, check that no other application has exclusive control of the DAX TX audio device.

## Related

- [Configure DAX TX audio](configure-dax-tx-audio.md)
- [Set up TCI](setup-tci.md)
- [NR2 noise reduction](nr2-noise-reduction.md)
<!-- docmesh:llm version=v0.9.5.1 date=2026-05-04 -->
