# File an AI-assisted bug report

Use the AI-assisted bug report flow to get help writing a clear, complete GitHub issue. AetherSDR copies a pre-filled diagnostic prompt — including your version, OS, and connected radio — to your clipboard, then guides you through an AI assistant and the GitHub issue form.

## Before you start

- Reproduce the problem at least once so you can describe what happened. You can enable logging categories first to capture more detail. See [Enable verbose logging for a specific subsystem](enable-verbose-logging-for-a-specific-subsystem.md).
- If you want diagnostic logs attached, clear the log and reproduce the issue first so the log contains only relevant output. See [Clear the log before reproducing a bug](clear-the-log-before-reproducing-a-bug.md).
- A radio connection is not required, but if you are connected the bundle will include radio model, firmware, and serial information automatically.

## Steps

1. Click `Help > File an Issue` to open the AI-Assisted Bug Report dialog and start the flow.
   AetherSDR creates a support bundle (logs and settings) and copies a diagnostic prompt to your clipboard. The prompt includes your AetherSDR version, Qt version, OS, and radio information if connected.
2. In the AI-Assisted Bug Report dialog, click the AI service you want to use: `Claude`, `ChatGPT`, `Gemini`, `Grok`, or `Perplexity`.
   Your default browser opens to that service.
3. In the AI chat, paste the clipboard contents.
4. At the end of the prompt, replace the placeholder text with a plain description of what went wrong. For example: "The waterfall freezes after about 10 minutes" or "Audio cuts out when I switch bands."
5. Send the prompt and wait for the AI to produce a formatted bug report.
6. Copy the AI's output.
7. Return to AetherSDR. If the dialog is still open, click `Submit Bug Report`.
   Your browser opens the GitHub new-issue form with the `bug` label pre-selected, and the folder containing your support bundle opens in the OS file browser.
8. Paste the AI's bug report into the GitHub issue form.
9. Drag the support bundle file from the folder that opened into the GitHub issue form to attach it.
10. Submit the issue on GitHub.

## What each control does

| Control                               | What it does                                                                                                                                                    | Notes                                                                                                                                     |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| `Claude`                              | Opens `https://claude.ai/new` in your browser.                                                                                                                  |                                                                                                                                           |
| `ChatGPT`                             | Opens `https://chat.openai.com/` in your browser.                                                                                                               |                                                                                                                                           |
| `Gemini`                              | Opens `https://gemini.google.com/` in your browser.                                                                                                             |                                                                                                                                           |
| `Grok`                                | Opens `https://grok.x.ai/` in your browser.                                                                                                                     |                                                                                                                                           |
| `Perplexity`                          | Opens `https://www.perplexity.ai/` in your browser.                                                                                                             |                                                                                                                                           |
| `Submit Bug Report`                   | Opens the GitHub new-issue form (pre-tagged `bug`) and opens the support bundle folder for drag-and-drop attachment.                                            |                                                                                                                                           |
| Instructions (report-an-issue how-to) | Rich-text block pointing the user to Help > File an Issue for bug reporting once the relevant logging categories have been enabled and the problem reproduced. | New in v26.8.4: the 'Reset Settings' and 'File an Issue' buttons were removed from this dialog (they now live directly on the Help menu). |
| Close                                 | Closes the dialog.                                                                                                                                              |                                                                                                                                           |

## Tips

- The diagnostic prompt instructs the AI to write the full bug report in one response without asking follow-up questions. You only need to add your description at the bottom of the pasted prompt.
- The support bundle is created when you start the `File an Issue` flow, before you interact with any AI. If you reproduce the issue after starting the flow, close the dialog, clear the log, reproduce the bug, then start the flow again so the bundle contains fresh logs.
- If you close the AI-Assisted Bug Report dialog and need to file the issue later, start a new `File an Issue` flow and click `Submit Bug Report` to reopen the GitHub form and the bundle folder.

## Troubleshooting

- **"Failed to create support bundle" warning appears** — AetherSDR could not write the bundle to disk. Check that you have write permission to your home directory and that there is available disk space, then try again.
- **The browser does not open when you click an AI button** — Verify that a default browser is configured on your OS. On Linux, check that `xdg-open` is installed and associated with an HTTP handler.
- **Radio information shows "not connected" in the prompt** — The radio was not connected when you started the `File an Issue` flow. Add the radio model and firmware version manually in the AI chat after pasting the prompt.

## Related

- [Clear the log before reproducing a bug](clear-the-log-before-reproducing-a-bug.md)
- [Enable verbose logging for a specific subsystem](enable-verbose-logging-for-a-specific-subsystem.md)
- [Open the log folder to grab multiple files](open-the-log-folder-to-grab-multiple-files.md)

---

# Support & Diagnostics reference

The Support & Diagnostics dialog (`Help > Support...`) provides log viewing, logging category control, and access to support tools. The dialog remembers its size and position between sessions.

## Logging controls

| Control | What it does |
|---|---|
| Category checkboxes | Enable or disable logging per category. One checkbox per logging category. |
| Enable All | Turns on every logging category. |
| Disable All | Turns off every logging category. |
| Log path label | Shows the current log file path. |
| Log viewer | Scrollable view of the most recent log text. |
| Refresh | Reloads the log file. |
| Clear Log | Truncates the current log file. |
| Open Log Folder | Opens the log directory in the OS file browser. |

## Support tools

| Control | What it does |
|---|---|
| Instructions (report-an-issue how-to) | Rich-text block pointing the user to Help > File an Issue for bug reporting once the relevant logging categories have been enabled and the problem reproduced. |
| Close | Closes the dialog. |

## Indicators

| Indicator | What it shows |
|---|---|
| Log file size | Current size of the active log file. |

## Related menu items

| Menu item | What it does |
|---|---|
| `Help > File an Issue` | Launches the AI-Assisted Bug Report flow. |
| `Help > Reset Settings` | Removes AetherSDR's app-specific settings, writes a backup, and closes the application immediately. |