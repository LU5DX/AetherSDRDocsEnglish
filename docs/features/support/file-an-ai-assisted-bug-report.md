# File an AI-assisted bug report

AetherSDR can prepare a diagnostic prompt — pre-filled with your version, OS, and radio info — that you paste into an AI assistant to produce a well-structured GitHub bug report. Use this when you need help describing a problem clearly before filing it on GitHub.

## Before you start

- Reproduce or note the details of the problem you want to report.
- Optionally, clear and re-capture the log immediately before filing so it contains only relevant data. See [Clear the log before reproducing a bug](clear-the-log-before-reproducing-a-bug.md).
- A radio connection is not required, but if you are connected the bundle will include your radio model, firmware version, and callsign automatically.

## Steps

1. Click `Help > Support...` to open the **Support & Diagnostics** dialog.
2. Click **File an Issue**.
   AetherSDR creates a support bundle (logs and settings) and copies a diagnostic prompt to your clipboard. The prompt is pre-filled with your AetherSDR version, Qt version, OS, and radio information.
3. In the **AI-Assisted Bug Report** dialog that appears, click the AI service you want to use: **Claude**, **ChatGPT**, **Gemini**, **Grok**, or **Perplexity**. Your default browser opens that service.
4. In the AI chat window, paste the clipboard contents (the prompt is already there from step 2).
5. At the end of the prompt, replace the placeholder text with a description of what went wrong — for example, what you were doing, what happened, and what you expected instead.
6. Send the message and wait for the AI to produce a formatted GitHub bug report.
7. Copy the AI's output.
8. Return to the **AI-Assisted Bug Report** dialog (still open in AetherSDR) and click **Submit Bug Report**. AetherSDR opens the GitHub new-issue form in your browser and opens the folder containing your support bundle.
9. Paste the AI's output into the GitHub issue form.
10. Drag your support bundle file from the folder that opened into the GitHub issue form to attach it.

## What each control does

| Control | Behavior |
|---|---|
| **Claude** | Opens `https://claude.ai/new` in your browser. |
| **ChatGPT** | Opens `https://chat.openai.com/` in your browser. |
| **Gemini** | Opens `https://gemini.google.com/` in your browser. |
| **Grok** | Opens `https://grok.x.ai/` in your browser. |
| **Perplexity** | Opens `https://www.perplexity.ai/` in your browser. |
| **Submit Bug Report** | Opens the GitHub new-issue form (pre-tagged `bug`) and opens the support bundle folder for drag-and-drop attachment. |
| **Close** | Dismisses the dialog without filing. |

## Tips

- The diagnostic prompt instructs the AI to write the full report in one response without asking follow-up questions. Give the AI as much detail as you can in your description — the more specific, the better the output.
- If you clicked an AI button and then closed the **AI-Assisted Bug Report** dialog before submitting, click **File an Issue** again to re-open it and use **Submit Bug Report**. A new support bundle will be created.
- If you are connected to your radio when you click **File an Issue**, the bundle automatically includes your radio model, serial number, firmware version, and IP address. If you are not connected, connect first and then click **File an Issue** to include that data.
- Enable verbose logging for the relevant subsystem before reproducing the bug so the support bundle contains useful detail. See [Enable verbose logging for a specific subsystem](enable-verbose-logging-for-a-specific-subsystem.md).

## Troubleshooting

- **"Failed to create support bundle." warning appears** — AetherSDR could not write the bundle to disk. Check that you have write permission to your user data directory. The diagnostic prompt is still copied to your clipboard, so you can proceed with the AI steps and file the issue manually without the attachment.
- **No browser opens after clicking an AI button** — Verify that your OS has a default browser configured and that it can open external URLs. On Linux, ensure `xdg-open` is functional.
- **Radio information shows "not connected" in the prompt** — AetherSDR was not connected to the radio when you clicked **File an Issue**. Connect via `Settings > Connect to Radio...` and click **File an Issue** again if the radio details are relevant to your report.

## Related

- [Clear the log before reproducing a bug](clear-the-log-before-reproducing-a-bug.md)
- [Enable verbose logging for a specific subsystem](enable-verbose-logging-for-a-specific-subsystem.md)
- [Open the log folder to grab multiple files](open-the-log-folder-to-grab-multiple-files.md)
- [Support & Diagnostics overview](overview.md)
