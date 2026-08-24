---
title: Supported Hardware
---

# Supported Hardware

AetherSDR works with any **FlexRadio** transceiver (the supported target) and, on
an experimental basis, with a growing list of other radio families that ride the
vendor-neutral `IRadioBackend` seam.

## Supported: FlexRadio

- FLEX-6000 series — FLEX-6300, 6400, 6400M, 6500, 6600, 6600M, 6700
- FLEX-8000 series — FLEX-8400, 8400M, 8600, 8600M
- Aurora series — AU-510, 510M, 520, 520M
- ML-, CL-, and RT-series devices

The active test target is the FLEX-8600 on firmware 4.2.18 (SmartSDR protocol
v1.4.0.0). Earlier 4.x firmware works; v3.x is unsupported.

## External devices

Outside the radio seam, AetherSDR also controls:

- **PGXL** (Power Genius XL) amplifier and **TGXL** (Tuner Genius XL) tuner
- **ACOM S-series** amplifiers (serial / ser2net)
- **SPE Expert** amplifiers — 1.3K-FA / 1.5K-FA / 2K-FA (serial / ser2net TCP)
- **VK3AMP** amplifiers — 600 W / 1000 W / 2000 W (TCP control + UDP telemetry)

## Experimental radio families

Two additional families are under active development. Neither is a *supported*
family yet, and FlexRadio remains the supported target:

- [**Hermes-Lite 2**](hermes-lite-2.md) — a low-cost open-source SDR. Four
  receivers, SSB/CW/RTTY/AX.25, hardware-filter band switching, and a host-side
  impulse noise blanker.
- [**Networked Icom**](icom.md) — CI-V over the RS-BA1 UDP transport, brought up
  on the IC-705 and completed against a live IC-7300MK2.

Both are opt-in and clearly marked in the UI: AetherSDR shows a notice banner
the first time you connect one, and they are only reachable through the manual
"Connect to Radio" flow.

## No radio at all?

**Demo mode** runs the full UI against a synthetic backend that generates its own
receive audio and spectrum — no hardware required.
