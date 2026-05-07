# Drag a filter edge to reshape the passband

The Spectrum / Waterfall widget renders a live FFT spectrum and scrolling waterfall for each panadapter. You can drag either edge of the filter overlay directly on the spectrum to reshape the passband without opening any dialog.

## Steps

1. Open the Panadapter applet. The Spectrum / Waterfall widget is always visible inside it.
2. Move your pointer over the left or right edge of the shaded filter region on the spectrum display. The cursor changes to a resize cursor when you are over a draggable edge.
3. Click and drag the edge left or right to set the desired passband boundary. Release the mouse button to confirm.

## What each control does

| Control | Behavior |
|---|---|
| Waterfall colour scheme | Changes the gradient palette used to map signal intensity to waterfall colour. Does not affect filter edge dragging. |

## Tips

- If the filter edges are hard to grab, zoom in on the spectrum first by scrolling the mouse wheel over the waterfall to widen the Hz-per-pixel scale.
- Drag the body of the filter overlay (the shaded area between the two edges) to shift the entire passband without changing its width.

## Related

- [spectrum-waterfall-overview.md](spectrum-waterfall-overview.md)
- [tune-by-clicking-the-spectrum.md](tune-by-clicking-the-spectrum.md)
- [zoom-the-spectrum.md](zoom-the-spectrum.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->
