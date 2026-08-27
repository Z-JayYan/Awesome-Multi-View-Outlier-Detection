#!/usr/bin/env python3
"""Best-effort external-link audit for scheduled, non-blocking CI."""

from __future__ import annotations

import argparse
import ssl
import urllib.error
import urllib.request
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def urls(value):
    if isinstance(value, dict):
        for item in value.values():
            yield from urls(item)
    elif isinstance(value, list):
        for item in value:
            yield from urls(item)
    elif isinstance(value, str) and value.startswith(("http://", "https://")):
        yield value


def check(url: str, timeout: float) -> tuple[str, str]:
    headers = {"User-Agent": "Awesome-MVOD-metadata-audit/0.2 (+https://github.com/Z-JayYan/Awesome-Multi-View-Outlier-Detection)"}
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, headers=headers, method=method)
        if method == "GET":
            request.add_header("Range", "bytes=0-1023")
        try:
            with urllib.request.urlopen(request, timeout=timeout, context=ssl.create_default_context()) as response:
                return "ok", str(response.status)
        except urllib.error.HTTPError as error:
            if method == "HEAD" and error.code in {403, 405, 429, 501}:
                continue
            # Publisher anti-bot/rate-limit responses are reported but not treated as proof of a broken link.
            if error.code in {401, 403, 429}:
                return "blocked", str(error.code)
            return "failed", str(error.code)
        except Exception as error:  # scheduled audit must retain the exact network failure
            if method == "HEAD":
                continue
            return "failed", f"{type(error).__name__}: {error}"
    return "failed", "no response"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="fail for confirmed non-blocked link errors")
    parser.add_argument("--timeout", type=float, default=12.0)
    args = parser.parse_args()

    all_urls: set[str] = set()
    for path in sorted((ROOT / "data").glob("*.yaml")):
        all_urls.update(urls(yaml.safe_load(path.read_text(encoding="utf-8"))))

    counts = {"ok": 0, "blocked": 0, "failed": 0}
    for url in sorted(all_urls):
        status, detail = check(url, args.timeout)
        counts[status] += 1
        print(f"{status.upper():7} {detail:20} {url}")
    print(f"SUMMARY {counts}")
    return 1 if args.strict and counts["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
