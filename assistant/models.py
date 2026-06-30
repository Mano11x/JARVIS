# ============================================================
# assistant/models.py — Database Models
# ============================================================
# Defines what JARVIS stores in SQLite.
#
# Phase 2: Conversation — chat history
# Phase 4: Memory      — long-term facts about the user
# ============================================================

from django.db import models


# ── Phase 2 ──────────────────────────────────────────────────

class Conversation(models.Model):
    """
    A single message exchange — one user message
    and one JARVIS response, stored together.

    Activate in Phase 2:
        python manage.py makemigrations
        python manage.py migrate
    """
    user_message  = models.TextField()
    jarvis_reply  = models.TextField()
    created_at    = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        preview = self.user_message[:40]
        return f"[{self.created_at:%Y-%m-%d %H:%M}] {preview}"


# ── Phase 4 ──────────────────────────────────────────────────

class Memory(models.Model):
    """
    A single fact JARVIS has learned about the user.

    Examples:
        key="favorite_editor"   value="VS Code"
        key="name"              value="Mano"
        key="location"          value="Chennai"
    """
    key        = models.CharField(max_length=100, unique=True)
    value      = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["key"]
        verbose_name_plural = "Memories"

    def __str__(self):
        return f"{self.key}: {self.value}"
