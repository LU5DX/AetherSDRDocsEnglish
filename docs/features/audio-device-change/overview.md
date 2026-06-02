# Audio Device Change overview

The Audio Device Change feature automatically detects when system audio devices are added or removed while AetherSDR is running and prompts you to confirm or change the audio routing before audio breaks.

## How it works

AetherSDR monitors the system for audio device changes while running. When a device is added or removed — for example, when a USB audio interface is unplugged or replugged — the Audio Device Change dialog appears automatically. The dialog displays the current and available audio devices side-by-side so you can verify the routing or select a different device before audio is disrupted.

The dialog uses a themed container for visual consistency with the rest of the application interface.

The selected devices are persisted to AppSettings, so your choices are remembered for future sessions.

## What each control does

| Control                      | Behavior                                                                                                                                                      | Notes                                         |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| **Available Input Devices**  | Lists all detected input audio devices. The currently-selected device is highlighted.                                                                         | New in v26.5.2.1.                             |
| **Available Output Devices** | Lists all detected output audio devices. The currently-selected device is highlighted.                                                                        |                                               |
| **Apply**                    | Applies the selected audio devices and closes the dialog. Persists the choice to AppSettings. Styled as the primary action button.                            |                                               |
| **Cancel**                   | Closes the dialog without changing audio devices.                                                                                                             |                                               |
| Don't ask me again           | When checked and Apply is clicked, persists the suppression flag so the dialog is not shown on future hotplug events while the current selection still works. | New in v26.5.3 (#2926).                       |

## Tips

- The dialog appears automatically — you don't need to open it manually. If you need to change audio devices at other times, use **Settings > Radio Setup...** and navigate to the audio configuration section.
- Changes are saved to AppSettings immediately when you click **Apply**.

## Troubleshooting

- **The Audio Device Change dialog doesn't appear when I plug in a new USB audio device** — Ensure the device is properly connected and recognized by your operating system. Some devices may require driver installation before AetherSDR can detect them.
- **Audio is lost after changing a device** — Click **Apply** to confirm the new device selection; the dialog will not apply changes until you explicitly do so.