# 바로GO — 은평구 출장마사지·홈타이 안내 사이트

은평구 전지역 방문 관리(출장마사지·홈타이) 안내용 정적 사이트입니다.
상호: **바로GO** · 전화예약: **0508-202-4719**

## 구조

- 정적 HTML 사이트 — 어느 호스팅(GitHub Pages, Netlify, 일반 웹서버)에서든 그대로 서빙 가능
- `build.py` + `content/` 패키지에서 페이지를 생성하는 빌드 방식
- 생성물(각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`)도 저장소에 포함

```
build.py            # 빌드 스크립트 (레이아웃·글자수 검사·sitemap 생성)
content/
  site.py           # 상호·전화·BASE_URL·메뉴 구조·텔레그램 문의 링크
  main.py           # 메인 페이지 (+ HealthAndBeautyBusiness/FAQPage JSON-LD)
  areas.py          # 지역별: 은평구 허브 + 대표 동 11개
  stations.py       # 역세권별: 허브 + 12개 역
  zones.py          # 생활권별: 허브 + 10개 생활권
  themes.py         # 테마별: 허브 + 14개 테마
  info.py           # 홈타이 가이드·코스·예약·이용 전 확인사항·후기·고객센터·약관
  magazine.py       # 매거진
  about.py          # 운영자 소개 (E-E-A-T)
assets/             # CSS(프리미엄 팔레트·Pretendard), 모바일 내비 JS
```

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수 리포트가 출력됩니다.

## SEO 운영 원칙 (빌드에 강제됨)

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리되고 sitemap에서 제외
- 지역은 대표 동 11개만 (녹번·불광·갈현·구산·대조·응암·역촌·신사·증산·수색·진관) — 숫자 행정동(불광1·2동 등) 페이지 없음
- 역은 역 1개당 페이지 1개 — 환승역(불광·연신내·DMC)도 URL 하나, 출구별 페이지 없음
- **지역+역+테마 조합 페이지 없음** (도어웨이 방지) — 테마는 독립 페이지로만 운영
- 메뉴·URL에 "출장마사지" 키워드 반복 없음 — Title·H1·메타·첫 문단에서만 자연스럽게 사용
- 모든 페이지 본문은 페이지별 고유 작성 (지역명만 바꾼 복붙 없음)
- 본문 내부링크는 롱테일 서술형 앵커, 권위 사이트(은평구청·서울교통공사·코레일 등) 외부 링크 포함

## 배포 전 해야 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. (선택) `TELEGRAM_BUILD` / `TELEGRAM_PARTNER` 텔레그램 링크 확인
3. `python3 build.py` 재실행 (canonical·sitemap·robots.txt에 반영됨)
4. Google Search Console에 `sitemap.xml` 제출
