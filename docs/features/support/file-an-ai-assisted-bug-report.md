# File an AI-assisted bug report

Use the AI-assisted bug report flow to get help writing a clear, complete GitHub issue. AetherSDR copies a pre-filled diagnostic prompt — including your version, OS, and connected radio — to your clipboard, then guides you through an AI assistant and the GitHub issue form.

## Before you start

- Reproduce the problem at least once so you can describe what happened.
- If you want diagnostic logs attached, clear the log and reproduce the issue first so the log contains only relevant output. See [Clear the log before reproducing a bug](clear-the-log-before-reproducing-a-bug.md).
- A radio connection is not required, but if you are connected the bundle will include radio model, firmware, and serial information automatically.

## Steps

1. Click `Help > Support...` to open the Support & Diagnostics dialog.
2. Click `File an Issue`.
   AetherSDR creates a support bundle (logs and settings) and copies a diagnostic prompt to your clipboard. The prompt includes your AetherSDR version, Qt version, OS, and radio information if connected.
3. In the AI-Assisted Bug Report dialog that appears, click the AI service you want to use: `Claude`, `ChatGPT`, `Gemini`, `Grok`, or `Perplexity`.
   Your default browser opens to that service.
4. In the AI chat, paste the clipboard contents.
5. At the end of the prompt, replace the placeholder text with a plain description of what went wrong. For example: "The waterfall freezes after about 10 minutes" or "Audio cuts out when I switch bands."
6. Send the prompt and wait for the AI to produce a formatted bug report.
7. Copy the AI's output.
8. Return to AetherSDR. If the dialog is still open, click `Submit Bug Report`.
   Your browser opens the GitHub new-issue form with the `bug` label pre-selected, and the folder containing your support bundle opens in the OS file browser.
9. Paste the AI's bug report into the GitHub issue form.
10. Drag the support bundle file from the folder that opened into the GitHub issue form to attach it.
11. Submit the issue on GitHub.

## What each control does

| Control | What it does |
|---|---|
| `Claude` | Opens `https://claude.ai/new` in your browser. |
| `ChatGPT` | Opens `https://chat.openai.com/` in your browser. |
| `Gemini` | Opens `https://gemini.google.com/` in your browser. |
| `Grok` | Opens `https://grok.x.ai/` in your browser. |
| `Perplexity` | Opens `https://www.perplexity.ai/` in your browser. |
| `Submit Bug Report` | Opens the GitHub new-issue form (pre-tagged `bug`) and opens the support bundle folder for drag-and-drop attachment. |

## Tips

- The diagnostic prompt instructs the AI to write the full bug report in one response without asking follow-up questions. You only need to add your description at the bottom of the pasted prompt.
- The support bundle is created when you click `File an Issue`, before you interact with any AI. If you reproduce the issue after opening the dialog, click `Close`, clear the log, reproduce the bug, then start the flow again so the bundle contains fresh logs.
- If you close the AI-Assisted Bug Report dialog and need to file the issue later, click `Submit Bug Report` from a new `File an Issue` session to reopen the GitHub form and the bundle folder.

## Troubleshooting

- **"Failed to create support bundle" warning appears** — AetherSDR could not write the bundle to disk. Check that you have write permission to your home directory and that there is available disk space, then try again.
- **The browser does not open when you click an AI button** — Verify that a default browser is configured on your OS. On Linux, check that `xdg-open` is installed and associated with an HTTP handler.
- **Radio information shows "not connected" in the prompt** — The radio was not connected when you clicked `File an Issue`. Add the radio model and firmware version manually in the AI chat after pasting the prompt.

## Related

- [Clear the log before reproducing a bug](clear-the-log-before-reproducing-a-bug.md)
- [Enable verbose logging for a specific subsystem](enable-verbose-logging-for-a-specific-subsystem.md)
- [Open the log folder to grab multiple files](open-the-log-folder-to-grab-multiple-files.md)
