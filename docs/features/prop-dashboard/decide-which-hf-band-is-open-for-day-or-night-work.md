# Decide Which HF Band Is Open for Day or Night Work

The HF Propagation Dashboard shows a band-by-band condition summary split into day and night columns, letting you choose the best band before you transmit.

## Before you start

- AetherSDR must be running. A radio connection is not required for this feature.
- The dashboard fetches data from external propagation services; an internet connection is needed for live data.

## Steps

1. Click `View > Propagation Conditions` to open the HF Propagation Dashboard.
2. Scroll to the **HF Band Conditions** section of the dialog.
3. Read the condition shown for each of the four band rows under the **Day** and **Night** columns.
4. Choose a band whose condition matches your current time of day (day or night at your location).

## What each control does

| Control | Behavior |
|---|---|
| **HF Band Conditions** | Displays a condition rating for each of four HF band rows, split into day and night columns. |
| Band condition value | Shows one of three states: **Good**, **Fair**, or **Poor**, color-coded green, amber, or orange respectively. |

## Tips

- The **Current Conditions cards** at the top of the dialog show SFI, SN, A-index, K-index, and X-ray values. Cross-reference these with the band conditions: a high SFI (120 or above) generally supports upper HF bands, while a high K-index (5 or above) indicates storm-level geomagnetic activity that degrades many paths.
- Hover over any metric card to read a plain-language tooltip explaining what that index means for HF propagation.
- If the A-index is elevated (15 or above), band conditions may remain unsettled even if the current K-index looks quiet.

## Troubleshooting

- **All band condition values appear blank or do not update** — the dashboard could not retrieve propagation data. Verify your internet connection and reopen the dialog.

## Related

- [HF Propagation Dashboard overview](overview.md)
- [Check current solar flux, sunspot number and K-index](check-current-solar-flux-sunspot-number-and-k-index.md)
- [See the 3-day Kp forecast and blackout risk](see-the-3-day-kp-forecast-and-blackout-risk.md)
- [Watch for VHF sporadic-E or auroral openings](watch-for-vhf-sporadic-e-or-auroral-openings.md)
