# Antenna SWR Sweep — License Confirmation

The Antenna SWR Sweep License Confirmation is a modal dialog that appears before the first antenna SWR sweep of each session. It displays an operator-responsibility disclaimer and requires you to acknowledge your license obligations before proceeding. A "Remember my answer" checkbox lets you skip the dialog on future sweeps in the same session.

## How it works

The dialog is shown automatically when you start an Antenna SWR Sweep (via the panadapter context menu or the MainWindow SWR sweep action). If you previously ticked the "Remember my answer" checkbox and confirmed, the dialog is bypassed entirely, and the sweep starts immediately.

The static `confirm()` helper function handles the logic: it checks the persisted setting, shows the dialog if needed, saves your preference when the checkbox is ticked, and returns `true` (proceed with sweep) or `false` (cancel).

The dialog uses a one-time geometry — it does not remember its window position between appearances.

## What each control does

| Control | Kind | Behavior | Setting key |
---|---|---|---|
| *Disclaimer text* | Indicator (rich-text QLabel) | Displays the operator-responsibility warning about not interfering with other traffic, license compliance, and unattended-sweep risks. Has an orange background (`#2a1a10`). | None |
| Remember my answer | Checkbox | When checked, persists your confirmation so the dialog is skipped on subsequent sweeps in this session. | `SwrSweepLicenseConfirmed` |
| I am licensed to use this feature | Push button | Accepts the disclaimer and proceeds to the SWR sweep. Styled as the primary blue button and set as the default button (Enter key). | None |
| Cancel | Push button | Rejects the disclaimer and cancels the sweep. | None |

## Related

- [Confirm operator responsibility before running the antenna SWR sweep](confirm-operator-responsibility-before-running-the-antenna-swr-sweep.md)
- [Remembers confirmation so the dialog does not show on subsequent sweeps](remembers-confirmation-so-the-dialog-does-not-show-on-subsequent-sweeps.md)
