# ATU Pre-Tune overview

Run an automatic sweep across selected HF and 6m bands, triggering the radio's built-in ATU (Antenna Tuning Unit) at each center frequency. This ensures your tuner has a valid tuning solution stored for every band you plan to use, reducing the chance of high SWR when you change frequencies during an operating session.

## How it works

The ATU Pre-Tune feature steps the active TX slice through a calculated set of center frequencies across the bands you select. At each frequency, AetherSDR sends an `atu start` command to the radio and waits for the radio to report completion (via `atuStateChanged`) before moving to the next point. Band edges are taken from the active region's band plan so the sweep stays within legal and practical frequency limits.

## Before you start

- A radio must be connected. The Pre-Tune dialog requires an active radio connection to send ATU commands.
- The radio must have an internal or external ATU available and functional.

## Opening the dialog

- **Menu path:** `Settings > TX Band Settings...` then select the **ATU Pre-Tune** tab.
- **Alternative:** Right-click the Tuner applet in the Applet Panel and choose **ATU Pre-Tune** from the context menu.

## What each control does

| Control | Type | Behavior |
|---|---|---|
| **Band selection** | Combo box | Selects which HF/6m bands to include in the pre-tune sweep. Band edges follow the active region's band plan. |
| **Start Sweep** | Push button | Begins the ATU pre-tune sweep. Steps through each selected band's center frequencies and triggers ATU tuning at each point. |

## Troubleshooting

- **Sweep does not start** — Ensure a radio is connected and the active TX slice exists. The dialog requires an active radio connection.
- **ATU fails on some frequencies** — The radio's ATU may be unable to find a match on certain bands or antenna configurations. Verify your antenna is resonating reasonably on the chosen bands.

## Related

- [Radio Setup](Radio Setup)
- [TX Band Settings](TX Band Settings)
