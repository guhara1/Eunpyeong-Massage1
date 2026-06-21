#!/usr/bin/env python3
"""구글 Indexing API 색인 통보 — 구글은 IndexNow에 참여하지 않으므로 별도 경로가 필요하다.

⚠ 참고
  - 구글은 sitemap "ping" 엔드포인트(/ping?sitemap=)를 2023년에 폐지했다.
    따라서 구글에는 (1) Search Console에 sitemap.xml·rss.xml 등록,
    (2) 아래 Indexing API 호출 두 가지가 실질적인 통보 수단이다.
  - Indexing API는 공식적으로 JobPosting/BroadcastEvent 용도지만 URL 단건
    색인 요청에도 널리 쓰인다. 일반 콘텐츠는 효과가 보장되지 않으니
    sitemap·rss + Search Console 제출을 기본으로 두고 보조로 사용한다.

사전 준비 (1회)
  1) Google Cloud 프로젝트에서 "Indexing API" 사용 설정.
  2) 서비스 계정 생성 → JSON 키 다운로드.
  3) Search Console 속성에 그 서비스 계정 이메일을 "소유자"로 추가.
  4) pip install google-auth requests

사용법
  export GOOGLE_APPLICATION_CREDENTIALS=/path/service-account.json
  python tools/google_index.py                 # sitemap.xml 전체
  python tools/google_index.py https://eunpyeong-massage1.pages.dev/magazine/new-post/
"""
import os
import sys
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITEMAP = os.path.join(ROOT, "sitemap.xml")
SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"


def sitemap_urls() -> list[str]:
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    tree = ET.parse(SITEMAP)
    return [loc.text.strip() for loc in tree.findall(".//sm:loc", ns) if loc.text]


def main(urls: list[str]) -> None:
    try:
        import requests
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        sys.exit("의존성 필요: pip install google-auth requests")

    cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        sys.exit("GOOGLE_APPLICATION_CREDENTIALS 환경변수에 서비스 계정 JSON 경로를 지정하세요.")

    creds = service_account.Credentials.from_service_account_file(cred_path, scopes=SCOPES)
    session = AuthorizedSession(creds)

    for url in urls:
        body = {"url": url, "type": "URL_UPDATED"}
        r = session.post(ENDPOINT, json=body, timeout=30)
        flag = "✓" if r.status_code == 200 else "✗"
        print(f"{flag} {r.status_code}  {url}")
        if r.status_code != 200:
            print("   " + r.text[:300])


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a.startswith("http")]
    if not args and not os.path.exists(SITEMAP):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python build.py` 를 실행하세요.")
    main(args if args else sitemap_urls())
