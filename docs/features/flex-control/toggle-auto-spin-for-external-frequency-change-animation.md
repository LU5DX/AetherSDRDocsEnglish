# Toggle Auto Spin for external frequency change animation

Enable or disable the automatic virtual wheel spin animation that plays when an external source changes the slice frequency, such as clicking on the panadapter or using CAT commands.

## Before you start

- Open the AetherControl dialog via **Settings > AetherControl...**

## Steps

1. Click **External Spin** to toggle the animation on or off.

When enabled, dragging on the panadapter or changing frequency from an external source triggers a spin-wheel tuning gesture animation on the virtual wheel. When disabled, frequency changes happen immediately without animation.

## What each control does

| Control | Label | Behavior |
|---------|-------|----------|
| Toggle button | External Spin | Enables or disables the spin animation on the virtual wheel when frequency changes originate from outside the wheel. Setting key: `FlexControlVirtualExternalSpin` |

## Related

- [Use the virtual wheel to tune the active slice](use-the-virtual-wheel-to-tune-the-active-slice.md)
- [Configure the AetherControl / FlexControl hardware controller](configure-the-aethercontrol-flexcontrol-hardware-controller.md)