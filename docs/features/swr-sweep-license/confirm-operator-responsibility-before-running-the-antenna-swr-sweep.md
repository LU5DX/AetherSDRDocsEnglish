# Confirm operator responsibility before running the antenna SWR sweep

Before the Antenna SWR Sweep transmits, you must confirm that you understand your operator responsibility. This page shows you how to accept the disclaimer or cancel the sweep.

## Before you start

- The Antenna SWR Sweep must be initiated from the panadapter context menu or the MainWindow SWR sweep action.
- You must hold a valid amateur radio license that permits the transmissions the sweep will make.

## Steps

1. Initiate the Antenna SWR Sweep from the panadapter context menu or the MainWindow SWR sweep action.
2. Read the operator-responsibility disclaimer text.
3. (Optional) Check the **Remember my answer** checkbox to skip this dialog on future sweeps.
4. Click **I am licensed to use this feature** to accept the disclaimer and proceed to the sweep.  
   — OR —  
   Click **Cancel** to reject the disclaimer and abort the sweep.

## Troubleshooting

- **The dialog does not appear on subsequent sweeps** — The **Remember my answer** checkbox was checked during a previous confirmation. The `SwrSweepLicenseConfirmed` setting is stored as `"True"`. To show the dialog again, clear the setting by editing the settings file at `~/.config/AetherSDR/AetherSDR.settings` and changing `SwrSweepLicenseConfirmed` to `"False"`.

## Related

- [Remembers confirmation so the dialog does not show on subsequent sweeps](remembers-confirmation-so-the-dialog-does-not-show-on-subsequent-sweeps.md)
