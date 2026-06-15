# HF Packet Decode overview

The HF Packet Decode feature decodes AX.25 amateur radio packet data transmitted over HF and VHF. It provides a real-time view of decoded frames, signal activity, and connection status for monitoring packet communications on the FLEX-8600. The decoder uses a shim layer over libmodem for physical-layer packet demodulation and integrates with the audio engine for live decode.

## Before you start

- Ensure AetherSDR is connected to a FLEX-8600 radio
- The radio must be tuned to an active packet frequency (HF or VHF)

## How it works

HF Packet Decode pulls demodulated audio from the radio's audio stream and passes it through an AX.25 decoder. Decoded frames appear in a scrollable text area as they are received, showing source, destination, and payload information. A signal activity indicator provides real-time visual feedback of packet detection and decode status.

The decoder supports two modem profiles:
- **HF 300** (300 baud, AFSK): Uses free-running phase-diversity lanes (PLL alpha 0) spread evenly across the symbol period for robust decoding. TX preamble is 80 flags (~2.13 seconds).
- **VHF 1200** (1200 baud, Bell 202/APRS): Uses a bank of demodulator lanes with multiple space-gain multipliers. Nine lanes use the exact Direwolf A+ space-gain values (MIN_G=0.5, MAX_G=4.0) in a geometric series. Duplicate suppression collapses identical frames seen by multiple lanes into a single emission, similar to Direwolf's multi_modem.c. The TX preamble is 64 flags (~0.43 seconds) for VHF 1200 to reduce dead air and slot time.

Both profiles use an abstract demodulator interface (`IAfskDemod`) that allows VHF (Direwolf-derived) and HF (libmodem) demod types to coexist in the same lane vector. The HF 300 profile uses `LibmodemAfskDemod` wrapping the libmodem sinc_corr_afsk_demodulator, while VHF 1200 uses `DirewolfAfskDemod` wrapping the AetherAFSKDemod.

Duplicate suppression collapses the same frame seen by multiple lanes into one emission, like a multi-decoder TNC (e.g. Dire Wolf).

The feature is opened from the digital modes area when HF packet decode is active, or from a related menu entry.

## What each control does

| Control | Kind | Behavior |
|---------|------|----------|
| Decoded frames | text_area | Scrollable display of decoded AX.25 frames showing source, destination, and payload information. New in v26.5.2.1. |
| Signal activity | widget | Real-time signal activity indicator showing packet detection and decode status. Provided by PacketActivityWidget. |

## Tips

- The decoded frames area scrolls automatically as new frames are received. Use the scrollbar to review older frames.
- For best decode results, tune the radio to a clear frequency with active packet activity. Typical HF packet frequencies are in the 14.100-14.110 MHz range on 20 meters and corresponding allocations on other bands. For VHF 1200, standard APRS frequencies apply (144.390 MHz in North America, 144.800 MHz in Europe, etc.).
- The VHF 1200 profile adjusts TX preamble automatically based on the selected profile. If using a transverter, the VHF 1200 preamble may need adjustment for T/R switching lead-in time. Set `kVhf1200TxPreambleFlags` in the configuration to tune this value.

## Troubleshooting

- **No frames decoded** — Verify the radio is connected and tuned to a frequency with active AX.25 packet activity. Check that the audio level is sufficient; the decoder needs a clean signal to demodulate.
- **Garbled or partial frames** — Weak signals, interference, or incorrect tuning can cause decode errors. Try adjusting the receiver bandwidth or retuning to center the signal within the passband.
- **VHF 1200 decode issues** — Ensure the correct profile is selected. If using a transverter, verify that the TX preamble provides enough lead-in time for T/R switching.