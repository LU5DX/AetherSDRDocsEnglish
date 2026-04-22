# UI Catalog Schema

Every catalog entry (applet, dialog, panel, menu action) follows this JSON shape.
Agents write one file per scope; each file contains an object whose top-level key is
`entries` (an array of the entries described below). All fields are strings unless
noted. Use `null` for unknowns — do not invent values.

```json
{
  "scope": "applets-core | applets-dsp | dialogs-panels | navigation",
  "entries": [
    {
      "id": "TciApplet",
      "kind": "applet",
      "display_name": "TCI",
      "applet_id_string": "TCI",
      "purpose": "1-2 sentence plain-English description of what this feature does for the user.",
      "source_files": ["src/gui/TciApplet.cpp", "src/gui/TciApplet.h"],
      "related_core_files": ["src/core/TciServer.cpp", "src/core/TciServer.h"],
      "how_to_open": "Exact navigation path from main window. Menu paths use '>' as separator (e.g. 'View > Applet Panel'). If opened via context menu, right-click, or toolbar button, describe it. If always visible, write 'Always visible in Applet Panel'.",
      "build_gate": "HAVE_WEBSOCKETS or null",
      "requires_radio_connection": true,
      "controls": [
        {
          "label": "Enable",
          "kind": "toggle_button | push_button | checkbox | slider | knob | text_field | spinbox | combo_box | radio_button | menu_action | indicator | meter | list | tab | drag_handle",
          "default": "value or null",
          "valid_range": "e.g. '1024-65535' or null",
          "setting_key": "AppSettings key that persists this control's state, or null",
          "behavior": "What happens when the user interacts with it, in one sentence.",
          "notes": "Any gotcha, validation, or side-effect users should know about."
        }
      ],
      "persisted_settings": ["TciPort", "TciRxGain1", "TciRxGain2", "TciRxGain3", "TciRxGain4", "TciTxGain"],
      "autostart_setting_key": "TciAutoStart or null",
      "indicators": [
        {"label": "Status", "states": ["(stopped)", ":<port> (N clients)", "(port in use)"], "meaning": "Server state and connected-client count."}
      ],
      "related_menu_items": ["Settings > Autostart TCI with AetherSDR"],
      "related_user_tasks": [
        "Enable TCI",
        "Change TCI port",
        "Adjust TCI RX gain per channel",
        "Auto-start TCI on launch",
        "Connect external TCI client (Log4OM, SunSDR, etc.)"
      ]
    }
  ]
}
```

## Navigation scope (only used by the navigation agent)

The navigation entry shape is different — it captures menus, toolbars, context menus,
and the applet-ID → class-name map.

```json
{
  "scope": "navigation",
  "menus": [
    {
      "title": "File",
      "mnemonic": "&F",
      "items": [
        {"label": "Quit", "shortcut": "Ctrl+Q or null", "opens": null, "action": "Closes the application."}
      ]
    }
  ],
  "toolbars": [
    {"location": "top | right | floating", "buttons": [{"label": "...", "action": "..."}]}
  ],
  "applet_panel": {
    "location": "Left/right sidebar",
    "default_order": ["RX", "TUN", "AMP", "TX", "..."],
    "applet_map": [
      {"id_string": "TCI", "class_name": "TciApplet", "display_name": "TCI", "visibility_toggle": "right-click applet title bar > enable TCI"}
    ]
  },
  "context_menus": [
    {"trigger": "right-click on applet title bar", "items": [{"label": "...", "action": "..."}]}
  ],
  "global_shortcuts": [
    {"keys": "Space", "action": "Toggle PTT"}
  ]
}
```

## Rules

- Source of truth is the code. If the .cpp file doesn't show it, don't write it.
- Never fabricate labels, default values, or menu paths.
- If a control's label is a symbol (e.g. "\u2014"), write that literal.
- Build-gated code (`#ifdef HAVE_WEBSOCKETS`, `Q_OS_WIN`, etc.) — always record the gate.
- Keep `purpose` written for *end users*, not developers. Don't say "wraps TciServer"; say "lets external software read/write the radio via TCI protocol."
