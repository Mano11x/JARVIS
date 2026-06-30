# ============================================================
# brain/search.py — Web Search + Local File Search
# ============================================================
# Phase 6
#
# Gives JARVIS the ability to search the internet and
# find files on your machine.
#
# Dependencies (uncomment in requirements.txt):
#   duckduckgo-search
#   beautifulsoup4
#   requests
# ============================================================

# from duckduckgo_search import DDGS
# import requests
# from bs4 import BeautifulSoup
import os


def web_search(query: str, max_results: int = 5) -> list[dict]:
    """
    Search the web using DuckDuckGo and return results.

    Args:
        query (str): The search query.
        max_results (int): Max number of results to return.

    Returns:
        list[dict]: Each dict has 'title', 'href', 'body'.

    Example:
        results = web_search("weather in Chennai today")
        for r in results:
            print(r['title'], r['href'])
    """

    # ── Phase 6: uncomment when duckduckgo-search is installed
    # with DDGS() as ddgs:
    #     results = list(ddgs.text(query, max_results=max_results))
    # return results
    # ────────────────────────────────────────────────────────

    return []


def fetch_page(url: str) -> str:
    """
    Fetch and extract plain text from a web page.

    Args:
        url (str): Full URL to fetch.

    Returns:
        str: Plain text content of the page body.
    """

    # ── Phase 6: uncomment ──────────────────────────────────
    # response = requests.get(url, timeout=10)
    # soup = BeautifulSoup(response.text, "html.parser")
    # return soup.get_text(separator="\n", strip=True)
    # ────────────────────────────────────────────────────────

    return ""


def find_files(name: str, search_root: str = "C:\\Users") -> list[str]:
    """
    Search for files on the local machine by name or extension.

    Args:
        name (str): Filename or pattern to look for (e.g. "resume.docx").
        search_root (str): Directory to start the search from.

    Returns:
        list[str]: List of full file paths that match.
    """
    matches = []

    # ── Phase 6: uncomment ──────────────────────────────────
    # for root, dirs, files in os.walk(search_root):
    #     dirs[:] = [d for d in dirs if not d.startswith('.')]
    #     for file in files:
    #         if name.lower() in file.lower():
    #             matches.append(os.path.join(root, file))
    # ────────────────────────────────────────────────────────

    return matches
