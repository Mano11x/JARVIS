# ============================================================
# brain/desktop.py — Desktop Automation
# ============================================================
# Phase 5
#
# Lets JARVIS control your Windows machine:
#   - Open applications
#   - Open folders
#   - Search for files
#   - Manage windows
#
# Dependencies (uncomment in requirements.txt):
#   pyautogui
#   psutil
# ============================================================

import os
import subprocess

# import pyautogui
# import psutil


# Map of app nicknames to their executable paths or commands.
# Add your own apps here.
APP_MAP = {
    "vs code":      "code",
    "vscode":       "code",
    "editor":       "code",
    "chrome":       "chrome",
    "browser":      "chrome",
    "notepad":      "notepad",
    "explorer":     "explorer",
    "terminal":     "wt",           # Windows Terminal
    "powershell":   "powershell",
    "spotify":      "spotify",
    "discord":      "discord",
}


def open_app(name: str) -> str:
    """
    Open an application by its nickname.

    Args:
        name (str): App name as the user said it
                    (e.g. "vs code", "browser").

    Returns:
        str: Status message for JARVIS to relay to the user.

    Example:
        msg = open_app("vs code")
        # "Opening VS Code, Bro."
    """
    key = name.lower().strip()
    command = APP_MAP.get(key)

    if not command:
        return f"I don't know how to open '{name}' yet, Sir."

    try:
        subprocess.Popen(command, shell=True)
        return f"Opening {name.title()}, Sir."
    except Exception as e:
        return f"Couldn't open {name}, Sir. Error: {str(e)}"


def open_folder(path: str) -> str:
    """
    Open a folder in Windows Explorer.

    Args:
        path (str): Full path to the folder to open.

    Returns:
        str: Status message.
    """

    if not os.path.exists(path):
        return f"That folder doesn't exist, Sir: {path}"
    subprocess.Popen(f'explorer "{path}"')
    return f"Opened {path}, Sir."



def list_running_apps() -> list[str]:
    """
    Return a list of currently running application names.

    Returns:
        list[str]: Names of running processes.
    """

    # ── Phase 5: uncomment when psutil is installed ─────────
    # return [p.name() for p in psutil.process_iter(['name'])]
    # ────────────────────────────────────────────────────────

    return []
