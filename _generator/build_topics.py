"""Phase B — derive the user-task topic list from the UI catalog.

Loads the four JSON catalog files produced in Phase A, consolidates every
`related_user_tasks` entry plus the menu-action entries that describe a
user-facing action, dedupes them, and emits `topics.json`.

Each topic has:
  - id: kebab-case identifier (also the output filename stem)
  - title: "How to …" phrased for an end user
  - category: one of the top-level doc folders
  - subcategory: feature area (applet/dialog name, or a guide group)
  - source_entries: list of catalog entry IDs that drive this topic
  - related_settings: AppSettings keys touched by the feature
  - output_path: relative md path in the docs repo

Run:  python build_topics.py
Produces:  topics.json  beside this script.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).parent
CATALOG = HERE / "catalog"
OUTPUT = HERE / "topics.json"


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def categorize(entry_kind: str, entry_id: str, task_title: str) -> tuple[str, str]:
    """Return (category, subcategory) for a task."""
    t = task_title.lower()

    # Cross-cutting guides that deserve their own category
    if any(k in t for k in ["connect", "first time", "getting started", "install"]):
        return ("getting-started", "setup")
    if any(k in t for k in ["troubleshoot", "diagnose", "slice issue", "no audio", "can't transmit"]):
        return ("troubleshooting", entry_id.replace("Applet", "").replace("Dialog", "").replace("Panel", "").lower())

    # Features bucket — one folder per applet/dialog/panel
    folder = entry_id.replace("Applet", "").replace("Dialog", "").replace("Panel", "")
    folder = re.sub(r"(?<!^)(?=[A-Z])", "-", folder).lower()  # PascalCase -> kebab
    if entry_kind == "dialog":
        return ("features", folder)
    if entry_kind == "panel":
        return ("features", folder)
    return ("features", folder)


def derive_menu_topics(nav: dict) -> list[dict]:
    """Menu items that describe a user action deserve their own docs."""
    topics = []
    for menu in nav.get("menus", []):
        for item in menu.get("items", []):
            label = item.get("label", "")
            action = item.get("action", "")
            opens = item.get("opens")

            # Skip dynamic lists and placeholders
            if label.startswith("<") or not label:
                continue

            # Skip items that just open a dialog — those get docs via the dialog itself
            # BUT keep checkable toggles and submenus, which are user actions in their own right.
            is_toggle = "Checkable" in action or "checkbox" in action.lower()
            is_submenu = "submenu" in action.lower()
            is_open_only = opens and opens.endswith("Dialog") and not is_toggle

            if is_open_only:
                continue

            # Derive a how-to title
            clean_label = label.rstrip(".").strip()
            if is_toggle:
                title = f"Enable {clean_label.replace('Autostart ', 'autostart for ')}"
            elif is_submenu:
                title = f"Configure {clean_label}"
            else:
                title = clean_label

            topics.append({
                "id": slugify(title),
                "title": title,
                "category": "reference",
                "subcategory": "menu-actions",
                "source_entries": ["MainWindow"],
                "menu_path": f"{menu['title']} > {label}",
                "description": action,
                "related_settings": [],
                "output_path": f"reference/menu-actions/{slugify(title)}.md",
            })
    return topics


def derive_entry_topics(data: dict) -> list[dict]:
    """Each entry's related_user_tasks becomes a topic."""
    topics = []
    for entry in data.get("entries", []):
        entry_id = entry.get("id", "")
        entry_kind = entry.get("kind", "")
        tasks = entry.get("related_user_tasks") or []
        settings = entry.get("persisted_settings") or []

        for task in tasks:
            category, subcategory = categorize(entry_kind, entry_id, task)
            topics.append({
                "id": slugify(task),
                "title": task if task.lower().startswith(("how ", "what ", "why ")) else task,
                "category": category,
                "subcategory": subcategory,
                "source_entries": [entry_id],
                "related_settings": settings,
                "output_path": f"{category}/{subcategory}/{slugify(task)}.md",
            })

        # Add an overview page per applet/dialog
        topics.append({
            "id": f"{slugify(entry_id)}-overview",
            "title": f"{entry.get('display_name', entry_id)} overview",
            "category": "features",
            "subcategory": re.sub(r"(?<!^)(?=[A-Z])", "-",
                                   entry_id.replace("Applet", "").replace("Dialog", "").replace("Panel", "")
                                   ).lower(),
            "source_entries": [entry_id],
            "related_settings": settings,
            "is_overview": True,
            "output_path": f"features/{re.sub(r'(?<!^)(?=[A-Z])', '-', entry_id.replace('Applet', '').replace('Dialog', '').replace('Panel', '')).lower()}/overview.md",
        })
    return topics


def add_hand_crafted_topics() -> list[dict]:
    """Top-level guides that don't correspond to a single UI element."""
    return [
        {
            "id": "installation-linux",
            "title": "Install AetherSDR on Linux",
            "category": "getting-started",
            "subcategory": "install",
            "source_entries": [],
            "related_settings": [],
            "output_path": "getting-started/install/installation-linux.md",
        },
        {
            "id": "installation-macos",
            "title": "Install AetherSDR on macOS",
            "category": "getting-started",
            "subcategory": "install",
            "source_entries": [],
            "related_settings": [],
            "output_path": "getting-started/install/installation-macos.md",
        },
        {
            "id": "installation-windows",
            "title": "Install AetherSDR on Windows",
            "category": "getting-started",
            "subcategory": "install",
            "source_entries": [],
            "related_settings": [],
            "output_path": "getting-started/install/installation-windows.md",
        },
        {
            "id": "first-qso",
            "title": "Make your first QSO with AetherSDR",
            "category": "getting-started",
            "subcategory": "tutorials",
            "source_entries": ["ConnectionPanel", "RxApplet", "TxApplet"],
            "related_settings": [],
            "output_path": "getting-started/tutorials/first-qso.md",
        },
        {
            "id": "understanding-applets",
            "title": "Understanding the AetherSDR applet panel",
            "category": "getting-started",
            "subcategory": "concepts",
            "source_entries": ["MainWindow"],
            "related_settings": [],
            "output_path": "getting-started/concepts/understanding-applets.md",
        },
        {
            "id": "understanding-slices",
            "title": "Understanding slices and VFOs",
            "category": "getting-started",
            "subcategory": "concepts",
            "source_entries": ["RxApplet", "PanadapterApplet"],
            "related_settings": [],
            "output_path": "getting-started/concepts/understanding-slices.md",
        },
        {
            "id": "noise-reduction-overview",
            "title": "Choosing the right noise reduction: NR2, NR4, DFNR, MNR",
            "category": "operating",
            "subcategory": "dsp",
            "source_entries": ["AetherDspDialog"],
            "related_settings": [],
            "output_path": "operating/dsp/noise-reduction-overview.md",
        },
        {
            "id": "digital-modes-setup",
            "title": "Setting up digital modes (FT8, WSJT-X, fldigi)",
            "category": "operating",
            "subcategory": "digital-modes",
            "source_entries": ["DaxApplet", "CatControlApplet", "DxClusterDialog"],
            "related_settings": [],
            "output_path": "operating/digital-modes/digital-modes-setup.md",
        },
        {
            "id": "remote-operation-smartlink",
            "title": "Operating remotely over SmartLink",
            "category": "operating",
            "subcategory": "remote",
            "source_entries": ["ConnectionPanel"],
            "related_settings": [],
            "output_path": "operating/remote/remote-operation-smartlink.md",
        },
        {
            "id": "settings-reference",
            "title": "Full AppSettings key reference",
            "category": "reference",
            "subcategory": "settings",
            "source_entries": [],
            "related_settings": [],
            "output_path": "reference/settings/settings-reference.md",
        },
    ]


def main():
    nav = json.loads((CATALOG / "00-navigation.json").read_text(encoding="utf-8"))
    core = json.loads((CATALOG / "01-applets-core.json").read_text(encoding="utf-8"))
    dsp = json.loads((CATALOG / "02-applets-dsp.json").read_text(encoding="utf-8"))
    dialogs = json.loads((CATALOG / "03-dialogs-panels.json").read_text(encoding="utf-8"))

    all_topics: list[dict] = []
    all_topics += add_hand_crafted_topics()
    all_topics += derive_menu_topics(nav)
    all_topics += derive_entry_topics(core)
    all_topics += derive_entry_topics(dsp)
    all_topics += derive_entry_topics(dialogs)

    # Dedupe by id, merging source_entries
    by_id: dict[str, dict] = {}
    for t in all_topics:
        tid = t["id"]
        if tid in by_id:
            by_id[tid]["source_entries"] = sorted(set(by_id[tid]["source_entries"] + t["source_entries"]))
        else:
            by_id[tid] = t

    topics = sorted(by_id.values(), key=lambda t: (t["category"], t["subcategory"], t["title"]))

    # Stats by category
    by_cat: dict[str, int] = {}
    for t in topics:
        by_cat[t["category"]] = by_cat.get(t["category"], 0) + 1

    output = {
        "topic_count": len(topics),
        "by_category": by_cat,
        "topics": topics,
    }
    OUTPUT.write_text(json.dumps(output, indent=2), encoding="utf-8")

    print(f"Wrote {OUTPUT} with {len(topics)} topics")
    for cat, n in sorted(by_cat.items()):
        print(f"  {cat}: {n}")


if __name__ == "__main__":
    main()
