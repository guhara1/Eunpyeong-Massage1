#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — Bing·Naver·Yandex 등 IndexNow 참여 검색엔진에
URL 변경을 한 번의 호출로 알린다. (구글은 IndexNow 미참여 → tools/google_index.py 참고)

사용법:
  # sitemap.xml 의 모든 URL 일괄 통보 (첫 구축/전체 재색인)
  python tools/indexnow.py

  # 특정 URL만 통보 (글 한 건 올렸을 때)
  python tools/indexnow.py https://eunpyeong-massage1.pages.dev/magazine/new-post/

동작:
  - content/site.py 의 BASE_URL·INDEXNOW_KEY 를 읽는다.
  - 키 파일(https://<도메인>/<KEY>.txt)이 배포돼 있어야 검색엔진이 소유권을 검증한다.
  - IndexNow 엔드포인트(api.indexnow.org)는 참여 엔진에 자동 공유하므로 한 번만 호출하면 된다.
"""
import json
import os
import sys
import urllib.request
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

SITE = BASE_URL.rstrip("/")
HOST = urlparse(SITE).netloc
ENDPOINT = "https://api.indexnow.org/indexnow"
SITEMAP = os.path.join(ROOT, "sitemap.xml")


def sitemap_urls() -> list[str]:
    if not os.path.exists(SITEMAP):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python build.py` 를 실행하세요.")
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    tree = ET.parse(SITEMAP)
    return [loc.text.strip() for loc in tree.findall(".//sm:loc", ns) if loc.text]


def submit(urls: list[str]) -> None:
    if not urls:
        sys.exit("통보할 URL 이 없습니다.")
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{SITE}/{INDEXNOW_KEY}.txt",
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    print(f"→ {len(urls)}개 URL 을 IndexNow 로 통보합니다 (host={HOST}) …")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"✓ HTTP {resp.status} {resp.reason}")
            print("  200/202 면 정상 접수입니다. (Bing·Naver·Yandex 등에 자동 공유)")
    except urllib.error.HTTPError as e:
        print(f"✗ HTTP {e.code}: {e.read().decode('utf-8', 'ignore')}")
        print("  403 이면 키 파일 배포 여부를, 422 면 host/URL 도메인 일치를 확인하세요.")
        sys.exit(1)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a.startswith("http")]
    submit(args if args else sitemap_urls())
