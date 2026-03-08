# /// script
# requires-python = ">=3.10"
# dependencies = ["playwright>=1.44.0"]
# ///

from __future__ import annotations

import pathlib
import sys
from typing import Iterable

from playwright.sync_api import sync_playwright


PAGES: dict[str, str] = {
    "home": "/",
    "my-story": "/my-story/",
    "services": "/services/",
    "resources": "/helpful-links/",
}

VIEWPORTS = [
    ("desktop", {"width": 1440, "height": 900}),
    ("ipad", {"width": 1024, "height": 1366}),
    ("phone", {"width": 390, "height": 844}),
]


def iter_pages(base_url: str, page_map: dict[str, str]) -> Iterable[tuple[str, str]]:
    for name, path in page_map.items():
        url = base_url.rstrip("/") + path
        yield name, url


def main() -> int:
    base_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:1313"
    out_dir = pathlib.Path("designs/renders")
    out_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()

        for label, viewport in VIEWPORTS:
            page = browser.new_page(viewport=viewport)
            for name, url in iter_pages(base_url, PAGES):
                page.goto(url, wait_until="networkidle")
                page.wait_for_timeout(500)
                target = out_dir / f"{name}-{label}.png"
                page.screenshot(path=str(target), full_page=True)
                print(f"Wrote {target}")
            page.close()

        browser.close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
