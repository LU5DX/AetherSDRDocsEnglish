---
title: Hermes-Lite 2
---

# Hermes-Lite 2

!!! warning "Experimental"
    Hermes-Lite 2 support is **experimental** — it is not a supported radio
    family yet. Core receive and transmit work, but some controls, meters and
    radio-specific features are still incomplete. FlexRadio remains the
    supported target.

The Hermes-Lite 2 (HL2) is a low-cost, open-source SDR transceiver. It speaks
HPSDR **Protocol 1** (Metis) over Ethernet and, unlike a FlexRadio, ships raw IQ
and runs **no firmware DSP** — all filtering, noise reduction and demodulation
happen on your computer.

## Connecting

1. Open **Connect to Radio**.
2. Choose the manual radio type **Hermes-Lite 2**.
3. The HL2 answers an HPSDR Protocol 1 discovery datagram on UDP/1024, so it is
   discovered automatically on the local network.

## What works

- **Four independent receivers**, each with its own slice.
- **SSB voice**, **CW/RTTY decoding**, and **AX.25 packet**.
- **Band switching with hardware filters**.
- **Manual notch filters**.
- **Noise blanking** — the HL2 has no radio-side DSP, so the impulse blanker runs
  on the host, ahead of the demodulator, on the raw IQ.
- **A real CW BFO** — the passband skirt is centred on the CW pitch, so the
  receiver listens where the radio actually transmits.
- **Host frequency calibration** and **per-radio state restore** (including AGC
  mode and threshold, which survive a restart).
- **Client-timed CW transmit** with restart persistence.
- **TX level control** — the client's audio level (e.g. WSJT-X's `Pwr` slider)
  is honoured; the host speech ALC no longer overrides it.

## How it differs from FlexRadio

- **Host-modulated:** the HL2 transmits whatever audio you send it, so the host
  does the modulation. This is the opposite of the networked Icom backend, which
  lets the radio modulate.
- **No radio-side DSP:** NR/ANF are not offered; the noise blanker and other
  processing run on the host.
- **Raw IQ:** there is no radio-generated spectrum; the panadapter is drawn from
  the IQ stream on your machine.

## Limitations

- Experimental: not all meters, controls and radio-specific features are wired.
- The host does more work per slice than on a FlexRadio (IQ is processed
  locally).

See [Supported Hardware](index.md) for the full picture.
