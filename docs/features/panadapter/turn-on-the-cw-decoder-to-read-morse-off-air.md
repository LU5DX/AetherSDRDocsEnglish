# Turn on the CW decoder to read Morse off-air

The CW decode panel appears beneath the panadapter and displays incoming Morse code as readable text in real time. Use it to copy off-air CW without a separate decoding program. In v26.5.2.1, the decoder also renders your own transmitted keying in a distinct cyan color so you can visually separate your sending from incoming CW when both directions feed the same panel (#2417).

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- PC audio must be routed to AetherSDR. The panel itself shows the reminder "(requires PC Audio)" — decoding will not work without it.
- Tune to a CW signal and set the mode to CW on the active slice.

## Steps

1. In the panadapter title bar, confirm the correct slice is shown in the "Slice" title label (for example, "Slice A").
2. Open the CW decode panel. The panel appears below the spectrum/waterfall area and is hidden by default — look for a CW control or mode button that exposes it for the active slice. Once visible, the panel shows the label **CW** in blue alongside the hint **(requires PC Audio)**.
3. Watch the **CW decode text** area at the bottom of the panel. As the decoder tracks the signal, decoded characters roll in and are coloured by confidence: green (high), yellow, orange, or red (low). Characters decoded from your own transmitted keying appear in cyan (#5fc8ff) and are separated from incoming text by a space.
4. Check the **CW stats label** above the text area. It shows the detected pitch and speed in the format `<Hz>  <WPM>`, for example `600 Hz  20 WPM`. Confirm these match the signal you are listening to before relying on the decode.

## What each control does

| Control                    | What it does                                                                                                                                                                | Default |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| **Sens** slider            | Filters low-confidence characters. Higher values reject more uncertain decodes.                                                                                             | 30      |
| **🔒P (Lock Pitch)** toggle | Locks the decoder to the current detected pitch so it stops searching.                                                                                                      | Off     |
| **🔒S (Lock Speed)** toggle | Locks the decoder to the current detected speed (WPM).                                                                                                                      | Off     |
| **Pitch** range slider     | Sets the minimum and maximum pitch the decoder searches. A single double-handle slider replaces the previous separate Lo/Hi sliders. Range: 300–1200 Hz.                     | 500–700 Hz |
| **WPM** range slider       | Sets the minimum and maximum speed the decoder searches. A single double-handle slider. Range: 5–60 WPM.                                                                   | 15–40 WPM |
| **A-** button              | Decreases the decoded-text font size by 1 pixel (persisted across sessions).                                                                                               | —       |
| **A+** button              | Increases the decoded-text font size by 1 pixel (persisted across sessions).                                                                                               | —       |
| **CPY ALL**                | Copies the entire decoded text buffer to the clipboard.                                                                                                                     | —       |
| **CPY VIS**                | Copies only the text currently visible in the scroll area to the clipboard.                                                                                                 | —       |
| **CLR**                    | Clears the CW decode buffer.                                                                                                                                                | —       |
| **× (close CW)**           | Hides the CW decode panel.                                                                                                                                                  | —       |
| **Drag-grip (top edge)**   | A thin horizontal strip above the panel controls. Drag up or down with the vertical resize cursor to adjust the panel height (60–600 px) and reveal more decoded-text history. Persisted across sessions. | 80 px (default) |
| **CW stats label**         | Indicator showing detected pitch and speed. Read-only.                                                                                                                      | —       |
| **CW decode text**         | Rolling read-only display of decoded characters, coloured by confidence. Right-click opens a context menu with a **Clear** option in addition to the standard text actions. The font size is controlled by the A- / A+ buttons. | 13 px (default) |

## How TX decode appears

When you transmit CW, the decoder captures your keying and displays it in cyan text. This lets you verify your own sending alongside incoming signals. The decoder applies the same confidence filter as the RX path — low-confidence characters are suppressed. A space is inserted when switching between TX and RX decode to prevent the coloured runs from visually merging.

## Waterfall freeze during transmit

In v26.6.1, the waterfall now freezes when any client (not just this radio) starts transmitting. The freeze is driven by the radio's interlock TRANSMITTING state instead of the local MOX edge, eliminating the 10–23 second TX-trail artifact that previously appeared after unkeying.

When the radio reconnects, the desired panadapter FPS and waterfall line duration are reasserted (via internal reconciliation) to prevent silently dropping to the radio's 10 Hz default.

## Persisted panel preferences

In v26.7.4, the CW decode panel height and font size are now saved and restored across sessions, eliminating the need to re-adjust them each time you open the panel. The settings are stored in `CwDecodeSettings::panelHeight` and `CwDecodeSettings::fontPx`.

- Panel height: 60–600 px. Drag the resize grip (thin horizontal strip at the top of the panel) to adjust.
- Font size: 8–32 px. Use the **A-** and **A+** buttons to change.

## Tips

- If the text area fills with low-confidence (orange or red) characters, increase **Sens** to filter them out. Start around 50 and raise until noise characters disappear.
- Narrow the pitch search range with the **Pitch** slider to match the sidetone of the station you are copying. This reduces false triggers from nearby signals.
- Narrow the speed range with the **WPM** slider to match the sending speed of the station you are copying. This improves decoding accuracy.
- Once the **CW stats label** settles on a stable pitch and speed, enable **🔒P (Lock Pitch)** and **🔒S (Lock Speed)** to prevent the decoder from drifting to another signal.
- Use **CLR** before a new QSO to keep the text area readable. You can also right-click the **CW decode text** area and choose **Clear** from the context menu.
- Adjust the **A- / A+** buttons to a font size comfortable for your monitor resolution and viewing distance. The setting persists automatically.
- Drag the **resize grip** at the top of the panel to show more or less decoded history. The new height is saved when you close the panel or restart AetherSDR.

## Troubleshooting

- **No text appears in the decode area** — Verify PC audio is routed to AetherSDR. The panel shows "(requires PC Audio)" as a reminder. Without it the decoder receives no audio and produces no output.
- **Decode text is mostly red or orange** — The signal confidence is low. Increase **Sens**, or narrow the **Pitch** range to match the actual sidetone frequency shown in the **CW stats label**. Also narrow the **WPM** range to match the sending speed.
- **Wrong pitch or speed shown in CW stats label** — Do not engage **🔒P (Lock Pitch)** or **🔒S (Lock Speed)** until the stats label has stabilised on the target signal.
- **Waterfall has long TX trail after unkeying** — In v26.6.1, this is fixed. If you still see artifact trails, ensure you are running the latest version. A radio reconnect reasserts the correct FPS and waterfall line duration.
- **Panel height or font size resets after restart** — Ensure you have v26.7.4 or later. In v26.7.4, these preferences persist automatically. If they still reset, check that `CwDecodeSettings` values are being written to your configuration file.

## Related

- [Tune CW decoder sensitivity to reject noise](tune-cw-decoder-sensitivity-to-reject-noise.md)
- [Lock CW decoder pitch or speed once tracking is good](lock-cw-decoder-pitch-or-speed-once-tracking-is-good.md)
- [Copy decoded CW text to the clipboard](copy-decoded-cw-text-to-the-clipboard.md)
- [Panadapter overview](overview.md)