# Change CW pitch / sidetone frequency

The CW pitch controls set the tone frequency used for sidetone monitoring and CW decode. Two independent pitch settings exist: the radio's pitch (sent to the FLEX-8600) and the local sidetone pitch (generated client-side by AetherSDR).

## Before you start

- Connect to a FLEX-8600 radio. The Phone/CW applet requires an active radio connection.
- Set the active slice to a CW mode. The CW sub-panel is only visible when the active slice is in CW mode; the Phone sub-panel is shown otherwise.
- Open the Phone/CW applet by clicking the **P/CW** tray button in the right sidebar if it is not already visible.

## Steps

### Change the radio CW pitch

1. Locate **Pitch < / >** in the CW sub-panel. It is a spinbox with two arrow buttons.
2. Click **<** to decrease the pitch by 10 Hz, or **>** to increase it by 10 Hz.
3. The new pitch is sent to the radio immediately. Valid range: 100–6000 Hz, step 10 Hz. Default: 600 Hz.

### Change the local sidetone pitch

The local sidetone has its own pitch control, which by default follows the radio pitch automatically.

1. Check whether **Follow (local pitch)** is enabled (button appears highlighted/checked). If it is on, the local sidetone pitch tracks the radio pitch automatically — no further action is needed.
2. To set a manual pitch, click **Follow (local pitch)** to turn it off.
3. Adjust the **Local sidetone pitch** slider to the desired frequency. Valid range: 100–2000 Hz. Default: 600 Hz. The setting is persisted as `CwLocalSidetonePitchHz`.
4. To restore automatic tracking, click **Follow (local pitch)** again to turn it back on. The setting is persisted as `CwLocalSidetonePitchFollow`.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| **Pitch < / >** | 600 Hz | 100–6000 Hz (step 10) | — | Steps the radio CW sidetone/decode pitch by 10 Hz per click; sent to the FLEX-8600. |
| **Follow (local pitch)** | On | On / Off | `CwLocalSidetonePitchFollow` | When on, local sidetone pitch mirrors the radio pitch. When off, the **Local sidetone pitch** slider is enabled for manual control. |
| **Local sidetone pitch** | 600 Hz | 100–2000 Hz | `CwLocalSidetonePitchHz` | Sets the client-side sidetone tone frequency in Hz. Only active when **Follow (local pitch)** is off. |

## Tips

- The **Pitch < / >** control affects both the audible sidetone on the radio and the frequency used by the CW decoder. Adjust it to match your personal pitch preference.
- When **Follow (local pitch)** is on, you only need to change the radio pitch with **Pitch < / >** — the local sidetone updates automatically.
- The local sidetone (**Local STn**) operates at approximately 10 ms latency and works with paddle, straight key, and CWX-generated transmissions. If you are not hearing a local sidetone at all, verify that **Local STn** is enabled.

## Troubleshooting

- **Local sidetone pitch slider is greyed out** — **Follow (local pitch)** is on. Click **Follow (local pitch)** to turn it off before adjusting the slider.
- **Pitch < / > has no effect on the local sidetone pitch** — **Follow (local pitch)** is off. Either turn **Follow (local pitch)** back on, or manually update **Local sidetone pitch** to match.
- **CW sub-panel is not visible** — The active slice is not in a CW mode. Switch the slice to CW; the applet switches automatically.

## Related

- [Enable the low-latency local CW sidetone (Local STn) for fast paddle / straight-key / CWX work](enable-the-low-latency-local-cw-sidetone-local-stn-for-fast-paddle-straight-key-cwx-work.md)
- [Make the local sidetone pitch follow the radio's CW pitch, or set it manually with the slider](make-the-local-sidetone-pitch-follow-the-radio-s-cw-pitch-or-set-it-manually-with-the-slider.md)
- [Set the local sidetone volume independently of the radio monitor](set-the-local-sidetone-volume-independently-of-the-radio-monitor.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
