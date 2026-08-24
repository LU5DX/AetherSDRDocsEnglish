# Spot Settings

This page describes the Spot Settings dialog, a quick stand-alone settings window for how DX spots and memories render on the panadapter. It includes toggles, sliders, color overrides, and a clear-all action.

## Before you start

- AetherSDR must be running.
- At least one panadapter must be open.

## Opening the Spot Settings dialog

Right-click anywhere on the panadapter, then select the option that opens the Spot Settings overlay.

## Controls

### Spots

| Control | Type | Default | Description |
|---------|------|---------|-------------|
| **Spots:** | Toggle button | Enabled | Master toggle for DX spot display. When Enabled, the button label reads "Enabled"; when Disabled, it reads "Disabled". |
| **Memories:** | Toggle button | Disabled | Toggles memory channel overlays on the panadapter. When Enabled, the button label reads "Enabled"; when Disabled, it reads "Disabled". |
| **Kiwi DX:** | Toggle button | Disabled | Overlays KiwiSDR Community DX database spots (beacons, utilities, time signals) on the band plan strip. When Enabled, the button label reads "Enabled"; when Disabled, it reads "Disabled". |

### Appearance

| Control | Type | Default | Range | Description |
|---------|------|---------|-------|-------------|
| **Levels:** | Slider | 3 | 1-10 | Vertical stacking rows for spots. |
| **Position:** | Slider | 50 | 0-100 | Vertical position on the panadapter as a percentage. |
| **Font Size:** | Slider | 16 | 8-32 | Spot text size in points. |
| **Spot Lifetime:** | Slider | Varies | 10 sec – 24 hrs (non-linear steps) | How long spots remain before fading. The slider uses a non-linear scale from 10 seconds to 24 hours. The value is stored in seconds. |

### Color Overrides

| Control | Type | Default | Description |
|---------|------|---------|-------------|
| **Override Colors:** | Toggle button | Disabled | Forces a single text color for all spots. When Enabled, the button label reads "Enabled"; when Disabled, it reads "Disabled". |
| **Spot text color picker** | Push button | #FFFF00 | Opens a color picker to choose the spot text color. Only active when **Override Colors:** is Enabled. |
| **Override Background: Enabled** | Toggle button | Enabled | Draws a background under spot text. When Enabled, the button label reads "Enabled"; when Disabled, it reads "Disabled". |
| **Override Background: Auto** | Toggle button | Enabled | Auto-picks background color for contrast. |
| **Spot background color picker** | Push button | #000000 | Opens a color picker for the spot background color. Only active when **Override Background: Enabled** is Enabled and **Override Background: Auto** is Disabled. |
| **Background Opacity:** | Slider | 48 | 0-100 | Alpha of the spot background (0 = transparent, 100 = opaque). |

### Lines

| Control | Type | Default | Description |
|---------|------|---------|-------------|
| **Spot Lines:** | Toggle button | Enabled | Draws vertical lines from the spectrum baseline up to each spot label. Disable during contests to reduce visual clutter. When Enabled, the button label reads "Enabled"; when Disabled, it reads "Disabled". |

## Clear All Spots

| Control | Type | Description |
|---------|------|-------------|
| **Clear All Spots** | Push button | Clears all currently displayed spots from the panadapter. New spots will continue to arrive normally. |

## Indicator

| Indicator | Description |
|-----------|-------------|
| **Total Spots:** | Shows the count of live spots currently tracked. |

## Steps

### Clear every spot from the panadapter

1. Open the Spot Settings dialog.
2. Click **Clear All Spots**.

All spots are immediately removed from the panadapter. New spots will continue to arrive and display normally according to your current settings.

### Turn spots on or off

1. Open the Spot Settings dialog.
2. Set **Spots:** to **Enabled** or **Disabled**.

When set to **Enabled**, the button displays "Enabled" with an active background. When set to **Disabled**, the button displays "Disabled" with a dimmed background.

### Turn Kiwi DX spots on or off

1. Open the Spot Settings dialog.
2. Set **Kiwi DX:** to **Enabled** or **Disabled**.

When set to **Enabled**, KiwiSDR Community DX database spots (beacons, utilities, time signals) are overlaid on the band plan strip. When set to **Disabled**, these spots are hidden.

### Shorten or lengthen spot lifetime

1. Open the Spot Settings dialog.
2. Adjust the **Spot Lifetime:** slider to your desired duration.

Spots will remain on the panadapter for the configured time before fading.

### Change spot density and vertical position

1. Open the Spot Settings dialog.
2. Adjust **Levels:** to set the number of vertical stacking rows.
3. Adjust **Position:** to set the vertical position on the panadapter.

### Customize spot colors

1. Open the Spot Settings dialog.
2. Set **Override Colors:** to **Enabled**.
3. Click the **Spot text color picker** button to choose a text color.
4. Configure the background:
   - Set **Override Background: Enabled** to **Enabled** to show a background.
   - Set **Override Background: Auto** to **Enabled** to let the system pick a contrast color automatically, or set it to **Disabled** and click the **Spot background color picker** button to choose a custom color.
   - Adjust **Background Opacity:** to control transparency.

### Toggle spot lines

1. Open the Spot Settings dialog.
2. Set **Spot Lines:** to **Enabled** or **Disabled**.

When disabled, vertical lines from the spectrum baseline to each spot label are hidden, reducing visual clutter.

### Toggle memory display

1. Open the Spot Settings dialog.
2. Set **Memories:** to **Enabled** or **Disabled**.

## Tips

- **Clear All Spots** does not affect incoming spots from your DX cluster or other sources. Spots will reappear as new ones are received.
- The **Total Spots:** indicator at the bottom of the Spot Settings dialog shows the count of live spots currently tracked. After clearing, this count will reflect only spots received after the clear action.
- To stop spots from appearing entirely, use the **Spots:** toggle to set it to **Disabled** instead.
- The **Spot Lines:** toggle is independent of **Clear All Spots**. If the panadapter feels visually busy during a contest, set **Spot Lines:** to **Disabled** before or after clearing spots to reduce clutter without removing the spot labels themselves.
- Each toggle button (Spots, Memories, Kiwi DX, Override Colors, Override Background: Enabled, Spot Lines) now dynamically displays either "Enabled" or "Disabled" as its label to clearly indicate the current state.

## Related

- [Turn spots on or off](turn-spots-on-or-off.md)
- [Shorten or lengthen spot lifetime](shorten-or-lengthen-spot-lifetime.md)
- [Change spot density and vertical position](change-spot-density-and-vertical-position.md)