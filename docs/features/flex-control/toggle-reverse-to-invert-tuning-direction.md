# Toggle Reverse to invert tuning direction

This page explains how to reverse the direction of the AetherControl / FlexControl virtual wheel, so that clockwise rotation tunes downward and counter-clockwise tunes upward.

## Before you start

- Open the AetherControl dialog: **Settings > AetherControl...**

## Steps

1. In the AetherControl dialog, locate the **Reverse** toggle button.
2. Click **Reverse** to switch between normal and inverted tuning direction. The button is pressed when reverse is active.

## What each control does

| Control | Label | Behavior | Setting key |
|---------|-------|----------|-------------|
| Toggle button | **Reverse** | Reverses the wheel tuning direction. When enabled, clockwise rotation tunes to a lower frequency and counter-clockwise tunes higher. | `FlexControlInvertDir` |

## Tips

- The **Reverse** setting is independent for the virtual wheel and the physical FlexControl device; both use the same `FlexControlInvertDir` key.
- Use **Reverse** if the physical rotation of your controller feels opposite to your mental model (e.g., a left-side wheel in a go-kit might feel more natural reversed).

## Related

- [Configure the AetherControl / FlexControl hardware controller](configure-the-aethercontrol-flexcontrol-hardware-controller.md)
- [Use the virtual wheel to tune the active slice](use-the-virtual-wheel-to-tune-the-active-slice.md)
- [Adjust mouse sensitivity for the virtual wheel](adjust-mouse-sensitivity-for-the-virtual-wheel.md)
