# AetherSDR Offline Help overview

AetherSDR includes a built-in help reader that displays bundled Markdown guides directly in the application. The help is available without an internet connection, so you can read it at the radio bench or in the field.

## How it works

Each entry in the `Help` menu opens a separate instance of the help reader, pre-loaded with the topic for that menu item. The available topics are:

| Menu item | Topic |
|---|---|
| `Help > Getting Started...` | Getting started with AetherSDR |
| `Help > AetherSDR Help...` | Full AetherSDR help document |
| `Help > Understanding Noise Cancellation...` | NR2, NR4, DFNR, and MNR noise reduction |
| `Help > Configuring AetherSDR Controls...` | AetherSDR controls reference |
| `Help > Configuring Data Modes...` | Digital mode configuration |
| `Help > Contributing to AetherSDR...` | Bug reports and contributions |

Each dialog opens independently. You can have more than one topic open at the same time.

The window opens at 760 × 680 pixels and can be resized down to a minimum of 520 × 420 pixels.

If AetherSDR cannot find the bundled file for a topic, the Markdown viewer displays a message that the help file is not available, along with instructions to reinstall the application.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| `AETHERSDR OFFLINE HELP` | Indicator (eyebrow) | Brand header displayed above the topic title. Read-only. |
| Title | Indicator | Displays the topic name passed in when the dialog was opened. Read-only. |
| Subtitle | Indicator | Fixed line: "Bundled help is available even when your station computer is offline." Read-only. |
| Markdown viewer | Scrollable text area | Renders the loaded Markdown topic. Supports internal scrolling. External links open in your default browser. |
| Hint / footer | Indicator | Displays: "Tip: The Help menu keeps each guide separate so you can reopen just the topic you need." Read-only. |
| Close | Button | Closes the help dialog. |

No settings from this dialog are persisted.

## Tips

- The `Help` menu items are independent. Open `Help > Understanding Noise Cancellation...` and `Help > Configuring Data Modes...` side by side if you need both.
- No radio connection is required to open any help topic.

## Troubleshooting

- **Markdown viewer shows "Help file not available"** — The bundled help asset is missing from the installation. Reinstall AetherSDR and try again.

## Related

- [Open bundled getting-started guide](open-bundled-getting-started-guide.md)
- [Read the full AetherSDR help document](read-the-full-aethersdr-help-document.md)
- [Learn the differences between NR2, NR4, DFNR and MNR](learn-the-differences-between-nr2-nr4-dfnr-and-mnr.md)
- [Configure digital modes step-by-step](configure-digital-modes-step-by-step.md)
- [Understand how to contribute bug reports and PRs](understand-how-to-contribute-bug-reports-and-prs.md)
