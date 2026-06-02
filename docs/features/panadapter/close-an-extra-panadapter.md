# Close an extra panadapter

When you have multiple panadapters open in a multi-slice layout, you can close any extra one to reclaim screen space. This page explains how to close a panadapter you no longer need.

## Before you start

- Your radio must be connected. The × (close) button is only available when AetherSDR is connected to a FLEX-8600.
- You must have more than one panadapter open. The × (close) button is hidden in single-pan mode.

## Steps

1. Locate the title bar of the panadapter you want to close. It sits at the top of the panadapter and shows a label such as "Slice A" or "Slice B".
2. Click the × button at the right end of that title bar.

The panadapter closes immediately. The remaining panadapters expand to fill the available space.

## Tips

- If you cannot see the × button, you are in single-pan mode — only one panadapter is open, and closing it is not permitted.
- If the panadapter has been popped out into a floating window, the × button is still in the floating window's title bar at the top right. Click it there.

## Troubleshooting

- **The × button is not visible** — The radio is either disconnected or only one panadapter is open. AetherSDR hides the × button in both cases. Connect to the radio and add a second panadapter before trying again.

## CW decode text context menu

Right-clicking anywhere inside the CW decode text area opens a context menu. In addition to the standard text editing commands (Select All, Copy, and so on), the menu includes a **Clear** item. Choosing **Clear** erases the entire CW decode buffer immediately. This is equivalent to clicking the **CLR** button in the CW panel toolbar.

## CW decode TX/RX coloring

In the CW decode panel, received text and transmitted (self-sent) text are rendered in different colors so you can distinguish your own sending from incoming CW. The colors are:

- **Green**: Confidence cost < 0.15 (high confidence)
- **Yellow**: Confidence cost < 0.35
- **Orange**: Confidence cost < 0.60
- **Red**: Confidence cost >= 0.60 (low confidence)
- **Cyan** (`#5fc8ff`): Text decoded from your own transmitted keying

When switching between transmit and receive, a space is automatically inserted to prevent the colored text runs from merging together.

## Slice title with Multi-Flex

In Multi-Flex sessions, the slice title shown in the panadapter title bar uses the radio-provided index letter so the title matches the slice badge. This ensures consistency when multiple clients are connected to the same radio.

## Panadapter theming (v26.6.1)

In v26.6.1, the panadapter and its CW decode panel now use theme-aware styling instead of hardcoded colors. The title bar gradient, drag grip dots, slice title, stats labels, and CW panel background all reference theme color tokens. This means the panadapter automatically adapts to light and dark themes without requiring manual color overrides. The theme system replaces the previous fixed-color stylesheets with token-based values such as `{{color.background.1}}`, `{{color.text.secondary}}`, and `{{color.accent}}`.

## Related

- [Panadapter overview](overview.md)
- [Click the spectrum to activate a panadapter (multi-slice mode)](click-the-spectrum-to-activate-a-panadapter-multi-slice-mode.md)
- [Pop a panadapter out into its own window](pop-a-panadapter-out-into-its-own-window.md)
- [Maximize one panadapter to fill the main area](maximize-one-panadapter-to-fill-the-main-area.md)