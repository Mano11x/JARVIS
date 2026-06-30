import json
import os
import urllib.error
import urllib.request

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST


def chat(request):
    return render(request, "chat.html")


def _fetch_openai_response(prompt):
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return None, "OpenAI API key is not configured. Set OPENAI_API_KEY in your environment."

    model = os.environ.get("OPENAI_MODEL", "gpt-3.5-turbo")
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are Jarvis, a helpful personal assistant."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.7,
        "max_tokens": 800,
    }

    request = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers=headers,
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            choices = data.get("choices")
            if not choices:
                return None, "OpenAI returned an empty response."
            return choices[0]["message"]["content"].strip(), None
    except urllib.error.HTTPError as exc:
        payload = exc.read().decode("utf-8")
        try:
            error_data = json.loads(payload)
            detail = error_data.get("error", {}).get("message", payload)
        except Exception:
            detail = payload
        return None, f"OpenAI request failed: {detail}"
    except Exception as exc:
        return None, f"Unable to contact OpenAI: {exc}"


from brain.core import handle_message

@require_POST
def chat_api(request):
    try:
        payload = json.loads(request.body.decode("utf-8"))
        prompt = payload.get("prompt", "").strip()
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({"error": "Invalid request payload."}, status=400)

    if not prompt:
        return JsonResponse({"error": "Prompt is required."}, status=400)

    # Route through the JARVIS brain core router
    reply = handle_message(prompt)
    return JsonResponse({"reply": reply})