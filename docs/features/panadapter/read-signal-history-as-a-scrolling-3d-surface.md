# Read signal history as a scrolling 3D surface

Enable the 3D FFT spectrum view to see signal history rendered as a forward-scrolling 3D surface instead of the traditional 2D waterfall. The surface shows elevation shadows from slice flags and resynchronizes its floor after bandwidth zoom.

## Before you start

- Your AetherSDR must be connected to a FLEX-8600 radio (see [Radio Setup...] in the Settings menu).
- A panadapter must be visible in the main window showing spectrum and waterfall data.

## Steps

1. Locate the **3D FFT view** toggle button on the panadapter — it is labeled with the 3D FFT icon and sits with the other spectrum controls in the SpectrumWidget area.
2. Click the **3D FFT view** toggle button once to enable the 3D surface view. The spectrum display switches from the flat 2D waterfall to a scrolling 3D surface.
3. To return to the standard 2D view, click the same **3D FFT view** toggle button again to disable it.

## What each control does

| Control | Default | Behavior | Setting key |
|---------|---------|----------|-------------|
| 3D FFT view toggle | Disabled | Enables/disables the 3D FFT spectrum view showing signal history as a forward-scrolling surface with elevation shadows and smooth-scroll boundaries. | None |

## Tips

- Slice flags cast cached elevation shadows on the 3D surface, making active slice positions easier to identify at a glance.
- The 3D surface floor resynchronizes automatically after you change the bandwidth zoom level, preventing a flat or misaligned baseline.
- The 3D FFT view shares the same panadapter freeze behavior as the 2D waterfall — during transmit (from any client), the display freezes and resumes when transmission ends.

## Related

- [Toggle the 3D FFT spectrum view](toggle-the-3d-fft-spectrum-view.md)
- [Panadapter overview](overview.md)
