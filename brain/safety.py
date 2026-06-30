# ============================================================
# brain/safety.py — Input / Output Safety Filtering
# ============================================================
# Runs before every request and after every response.
# Keeps JARVIS from doing things it shouldn't.
#
# Used by: brain/core.py
# ============================================================

# Words and phrases that JARVIS will refuse to act on
BLOCKED_INPUTS = [
    "rm -rf",
    "format c:",
    "delete system",
    "drop table",
    "shutdown /s",
]


def is_safe(text: str) -> bool:
    """
    Check whether a user input is safe to process.

    Args:
        text (str): Raw user input.

    Returns:
        bool: True if safe, False if blocked.
    """
    lowered = text.lower()
    for phrase in BLOCKED_INPUTS:
        if phrase in lowered:
            return False
    return True


def sanitize_output(text: str) -> str:
    """
    Clean up JARVIS's response before sending it to the user.
    Strips leading/trailing whitespace, normalizes line breaks.

    Args:
        text (str): Raw model output.

    Returns:
        str: Cleaned response string.
    """
    return text.strip()


def is_harmful(text: str) -> bool:
    """
    Inverse of is_safe() — convenience alias.

    Args:
        text (str): Raw user input.

    Returns:
        bool: True if harmful, False if safe.
    """
    return not is_safe(text)
