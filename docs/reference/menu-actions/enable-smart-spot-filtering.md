# Enable Smart Spot Filtering

Smart Spot Filtering dims SSB spots in the panadapter when no detected voice signal is present within ±1 kHz of the spot frequency, helping you focus on active conversations. CW and digital spots are unaffected. This feature requires Signal History to be enabled.

## Before you start

- Ensure Signal History is enabled in AetherSDR.
- Verify you have an active connection to a FLEX-8600 radio.

## Steps

1. Open the **View** menu.
2. Click **Smart Spot Filtering** to toggle it on (a checkmark appears when enabled).

## What each control does

| Control | Behavior |
|---------|----------|
| Smart Spot Filtering (menu item) | Checkable; default off. When enabled, SSB spots with no detected voice signal within ±1 kHz are dimmed. Persisted setting key: `SmartSpotFilterEnabled`. |

## Tips

- Smart Spot Filtering works best during busy band conditions where many SSB spots are displayed.
- The filter is applied in real-time as Signal History updates.

## Related

- [Configure Band Plan](configure-band-plan.md)
- [Enable Propagation Conditions](enable-propagation-conditions.md)
