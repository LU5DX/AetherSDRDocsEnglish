# Toggle the 3D FFT spectrum view

Switch the spectrum display from the default 2D FFT waterfall to a 3D surface view that shows signal history scrolling forward in time, with elevation shadows for slice markers.

## Before you start

- Your radio must be connected and the panadapter visible in the main window.
- The panadapter must be in a normal (docked) state — the 3D toggle is part of the SpectrumWidget embedded in each Panadapter.

## Steps

1. Locate the panadapter's spectrum display area (the FFT / waterfall region).
2. Click the **3D FFT view** toggle button on the panadapter. This button is a toggle that switches between the default 2D spectrum and the 3D surface view.
   - The button label reads **3D FFT view** (a toggle button in the SpectrumWidget).
   - The default state is **Disabled**.
3. To return to the 2D view, click the **3D FFT view** toggle again.

## What each control does

| Control | Behavior |
|---|---|
| **3D FFT view** toggle button | Switches between 2D spectrum/waterfall and the 3D surface view. When enabled, signal history displays as a forward-scrolling 3D surface with elevation shadows cast by slice flags. The floor resynchronizes after bandwidth zoom. |

## Tips

- The 3D FFT view includes smooth-scroll history boundaries and cached elevation shadows for slice markers.
- Bandwidth zoom works normally — the floor resynchronizes automatically.
- This feature is new in v26.7.x and is part of the SpectrumWidget.

## Related

- [Read signal history as a scrolling 3D surface](read-signal-history-as-a-scrolling-3d-surface.md)
