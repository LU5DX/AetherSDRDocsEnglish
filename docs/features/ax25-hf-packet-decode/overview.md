# HF Packet Decode overview

The HF Packet Decode feature decodes AX.25 amateur radio packet data transmitted over HF. It provides a real-time view of decoded frames, signal activity, and connection status for monitoring packet communications on the FLEX-8600. The decoder uses a shim layer over libmodem for physical-layer packet demodulation and integrates with the audio engine for live decode.

## Before you start

- Ensure AetherSDR is connected to a FLEX-8600 radio
- The radio must be tuned to an active HF packet frequency

## How it works

HF Packet Decode pulls demodulated audio from the radio's audio stream and passes it through an AX.25 decoder. Decoded frames appear in a scrollable text area as they are received, showing source, destination, and payload information. A signal activity indicator provides real-time visual feedback of packet detection and decode status.

The feature is opened from the digital modes area when HF packet decode is active, or from a related menu entry.

## What each control does

| Control | Kind | Behavior |
|---------|------|----------|
| Decoded frames | text_area | Scrollable display of decoded AX.25 frames showing source, destination, and payload information. New in v26.5.2.1. |
| Signal activity | widget | Real-time signal activity indicator showing packet detection and decode status. Provided by PacketActivityWidget. |

## Tips

- The decoded frames area scrolls automatically as new frames are received. Use the scrollbar to review older frames.
- For best decode results, tune the radio to a clear frequency with active HF packet activity. Typical HF packet frequencies are in the 14.100-14.110 MHz range on 20 meters and corresponding allocations on other bands.

## Troubleshooting

- **No frames decoded** — Verify the radio is connected and tuned to a frequency with active AX.25 packet activity. Check that the audio level is sufficient; the decoder needs a clean signal to demodulate.
- **Garbled or partial frames** — Weak signals, interference, or incorrect tuning can cause decode errors. Try adjusting the receiver bandwidth or retuning to center the signal within the passband.
