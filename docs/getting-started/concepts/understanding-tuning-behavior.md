# How tuning works: the five ways to change frequency

AetherSDR treats different tuning actions differently — on purpose. When you scroll the panadapter, click a spot, type a frequency into the VFO, or recall a memory, each action produces a subtly different result. This page explains what to expect from each.

## The quick version

| Action | What happens |
|---|---|
| Mouse-wheel or trackpad scroll, VFO knob, VFO drag in the spectrum, arrow keys, FlexControl, USB encoder, MIDI | Frequency changes. Panadapter only nudges if the slice drifts near the edge of the visible range. |
| Click the spectrum, click an ordinary DX spot, pick a band-stack entry | Frequency jumps to the target. Panadapter *reveals* the target if it was off-screen; otherwise stays put. |
| Type a frequency in the VFO, **Go To Frequency** dialog, recall a memory, click a memory spot | Frequency jumps. Panadapter always recenters on the new frequency. |
| Zoom buttons, pinch-to-zoom, bandwidth slider, `+` / `-` zoom shortcut, pan drag | Panadapter zooms or pans only. Frequency does not change. |
| Active-slice change lands off-screen | Panadapter brings the slice into view without hard-centering. |

## Incremental tuning — small adjustments

When you *adjust* the frequency — mouse-wheel scroll, VFO knob, dragging the VFO marker in the spectrum, arrow keys, a FlexControl or USB encoder, MIDI relative controls, the Zero Beat function — AetherSDR assumes you're making small, continuous changes. It tunes the radio but doesn't recenter the panadapter. As long as the slice stays inside the middle region of the visible range, the display stays put.

If the slice drifts far enough toward the edge (about 12% from either side), the panadapter nudges step-by-step to keep the slice in view. It won't snap to center; it just shuffles along quietly behind you. This is what makes wheel-tuning feel smooth instead of jumpy.

If you have **View > Pan Follows VFO** disabled, the panadapter stays completely stationary even when the slice drifts off the edge. Useful when you're tuning on one panadapter while watching another.

## Absolute jumps — target-based tuning

Click a frequency on the spectrum, click a DX cluster spot, pick an entry from the band stack — AetherSDR jumps straight to that target. The panadapter then *reveals* the new frequency if it was off-screen or close to the edge (within about 18%), but if your target was already comfortably visible, the display doesn't move at all.

This avoids the "jumps to center every time I click" behavior that older SDR clients exhibit. If you want to peek at a spot without losing the view of the signals around it, clicking it tunes there without shuffling your context.

## Commanded target center — precise recalls

When you know exactly where you want to be — typing a frequency into the VFO and pressing Enter, using the **Go To Frequency** dialog, recalling a memory, clicking a *memory* spot (not an ordinary cluster spot) — AetherSDR treats that as a command to land precisely on that frequency and hard-centers the panadapter on it.

The distinction matters: an ordinary DX cluster spot might be near where you're already tuned, so clicking it just nudges the view over. But recalling a memory is an explicit "take me there" action, so the display always snaps to center.

## Explicit pan and zoom — no tuning

The zoom buttons, pinch-to-zoom on a touchpad or touchscreen, dragging the bandwidth slider, `+` / `-` keyboard zoom, or dragging the panadapter sideways — these change only the display, not the frequency. The radio keeps receiving on the same slice; you're just changing how much spectrum you see and where it's centered.

Center and bandwidth changes are sent to the radio as a single combined command, so the waterfall and spectrum stay in sync while you zoom. You won't see the waterfall edge-loss or zoom drift that could happen in older releases.

## Reveal off-screen — switching between slices

When you make a different slice active and that slice is off-screen, AetherSDR brings it into view without hard-centering on it. It drifts the panadapter until the slice is visible — usually keeping the slice toward the side of the display rather than snapping to the middle. That preserves whatever you were looking at while still showing you the active slice.

If you want the active slice dead-center, use the explicit **Center Slice** action (right-click the slice letter, or the keyboard shortcut if you've configured one). That uses a true hard-center.

## Actions that always recenter

A few actions always hard-center regardless of the rules above:

- **Band buttons and the band menu** — switching bands recenters.
- **Restoring per-band state** (loading a saved per-band config) — recenters.
- **The explicit Center Slice action** — recenters on demand.

These are command-style actions where you're asking for a clean reset, so they're deliberately more assertive than contextual tuning.

## Tips

- **Feels jumpy when scrolling?** Make sure you're using wheel or trackpad scroll, not click-tune. Scroll is incremental; clicks are jumps.
- **Want the display to follow your VFO tightly?** Increase panadapter zoom so the slice bumps into the trigger window more often. That way small VFO changes already cross the 12% threshold and nudge the display.
- **Tuning remotely and don't want any automatic display movement?** Turn off `View > Pan Follows VFO`. All wheel and encoder input will then leave the panadapter alone.
- **Animation feels off?** Small center shifts animate smoothly over ~110 ms. Large shifts or bandwidth changes snap instantly — there's no animation for them because it'd look sluggish.

## Troubleshooting

- **The panadapter keeps recentering after I type a frequency.** That's by design — VFO entry is a commanded target, so the display always hard-centers. Use the mouse wheel or VFO knob if you want drift-only behavior instead.
- **Clicking a spot sometimes recenters and sometimes doesn't.** Ordinary cluster spots only recenter if the target was off-screen. Memory spots always recenter. If the behavior surprises you, check whether the spot is a memory spot or a regular cluster/band-stack entry.
- **My off-screen active slice is showing but not centered.** That's the reveal-off-screen policy. Use **Center Slice** explicitly to snap to it.
- **Cross-panadapter clicks feel stuttery.** The active-slice switch is deliberately deferred to prevent UI churn mid-gesture. If you want to work on a specific panadapter, click once to activate its slice, then tune.

## Related

- [Understanding slices and VFOs](understanding-slices.md)
- [Understanding the AetherSDR applet panel](understanding-applets.md)
