# Zoom the panadapter bandwidth with the scroll wheel

The Spectrum / Waterfall widget renders the live FFT spectrum and scrolling waterfall for one panadapter. Use the scroll wheel directly on the widget to zoom the displayed bandwidth in or out.

## Steps

1. Open the Panadapter applet. The Spectrum / Waterfall widget is always visible inside it.
2. Hover your mouse pointer over the spectrum or waterfall area.
3. Scroll up to zoom in (narrow the displayed bandwidth) or scroll down to zoom out (widen it).

## What each control does

| Control | Behavior |
|---|---|
| Waterfall colour scheme | Changes the gradient palette used to map signal intensity to waterfall colour. Persisted per-panadapter. Valid values: `0` = Default, `1` = Grayscale, `2` = Blue-Green, `3` = Fire, `4` = Plasma. Default: `0` (Default). |

## Tips

- Zoom in to get a closer look at a narrow signal, then scroll back out to survey a wider portion of the band.
- The waterfall colour scheme does not affect zoom behaviour — change it independently via the **Waterfall colour scheme** selector to improve signal visibility at any zoom level.

## Related

- [spectrum-waterfall.md](spectrum-waterfall.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
