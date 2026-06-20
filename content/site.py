# 사이트 공통 설정
# 배포 도메인 확정 후 BASE_URL 을 실제 도메인으로 변경하세요.
BASE_URL = "https://www.barogo-eunpyeong.example.com"

BRAND = "바로GO"
BRAND_MARK = "바"          # 헤더 로고 원형 마크 글자
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 제작·제휴 문의(텔레그램)
TELEGRAM_BUILD = "https://t.me/googleseolab"   # 웹사이트 제작문의
TELEGRAM_PARTNER = "https://t.me/googleseolab" # 제휴문의

# 상단 메뉴 — 메뉴명과 URL에는 "출장마사지"를 반복하지 않는다(지시서 1·14항).
# 하위 메뉴에는 지역명·역명·생활권명만 표시한다.
NAV = [
    ("홈", "/", []),
    ("지역별 안내", "/seoul/eunpyeong-gu/", [
        ("은평구 전체", "/seoul/eunpyeong-gu/"),
        ("녹번동", "/seoul/eunpyeong-gu/nokbeon-dong/"),
        ("불광동", "/seoul/eunpyeong-gu/bulgwang-dong/"),
        ("갈현동", "/seoul/eunpyeong-gu/galhyeon-dong/"),
        ("구산동", "/seoul/eunpyeong-gu/gusan-dong/"),
        ("대조동", "/seoul/eunpyeong-gu/daejo-dong/"),
        ("응암동", "/seoul/eunpyeong-gu/eungam-dong/"),
        ("역촌동", "/seoul/eunpyeong-gu/yeokchon-dong/"),
        ("신사동", "/seoul/eunpyeong-gu/sinsa-dong/"),
        ("증산동", "/seoul/eunpyeong-gu/jeungsan-dong/"),
        ("수색동", "/seoul/eunpyeong-gu/susaek-dong/"),
        ("진관동", "/seoul/eunpyeong-gu/jingwan-dong/"),
    ]),
    ("역세권 안내", "/seoul/eunpyeong-gu/station/", [
        ("역 전체", "/seoul/eunpyeong-gu/station/"),
        ("녹번역", "/seoul/eunpyeong-gu/station/nokbeon-station/"),
        ("불광역", "/seoul/eunpyeong-gu/station/bulgwang-station/"),
        ("독바위역", "/seoul/eunpyeong-gu/station/dokbawi-station/"),
        ("연신내역", "/seoul/eunpyeong-gu/station/yeonsinnae-station/"),
        ("구산역", "/seoul/eunpyeong-gu/station/gusan-station/"),
        ("역촌역", "/seoul/eunpyeong-gu/station/yeokchon-station/"),
        ("응암역", "/seoul/eunpyeong-gu/station/eungam-station/"),
        ("새절역", "/seoul/eunpyeong-gu/station/saejeol-station/"),
        ("증산역", "/seoul/eunpyeong-gu/station/jeungsan-station/"),
        ("디지털미디어시티역", "/seoul/eunpyeong-gu/station/digital-media-city-station/"),
        ("수색역", "/seoul/eunpyeong-gu/station/susaek-station/"),
        ("구파발역", "/seoul/eunpyeong-gu/station/gupabal-station/"),
    ]),
    ("생활권 안내", "/seoul/eunpyeong-gu/area/", [
        ("생활권 전체", "/seoul/eunpyeong-gu/area/"),
        ("연신내 상권 생활권", "/seoul/eunpyeong-gu/area/yeonsinnae-commercial/"),
        ("불광·북한산 생활권", "/seoul/eunpyeong-gu/area/bulgwang-bukhansan/"),
        ("녹번·은평구청 생활권", "/seoul/eunpyeong-gu/area/nokbeon-eunpyeong-office/"),
        ("은평뉴타운·진관 생활권", "/seoul/eunpyeong-gu/area/eunpyeong-newtown-jingwan/"),
        ("구파발·진관 생활권", "/seoul/eunpyeong-gu/area/gupabal-jingwan/"),
        ("응암·불광천 생활권", "/seoul/eunpyeong-gu/area/eungam-bulgwangcheon/"),
        ("새절·신사 생활권", "/seoul/eunpyeong-gu/area/saejeol-sinsa/"),
        ("증산·수색 DMC 생활권", "/seoul/eunpyeong-gu/area/jeungsan-susaek-dmc/"),
        ("구산·역촌 생활권", "/seoul/eunpyeong-gu/area/gusan-yeokchon/"),
        ("대조·연신내 인접 생활권", "/seoul/eunpyeong-gu/area/daejo-yeonsinnae/"),
    ]),
    ("예약 안내", "/reservation/", [
        ("예약 방법", "/reservation/#how"),
        ("예약 가능 시간", "/reservation/#hours"),
        ("예약 가능 지역 확인", "/reservation/#place"),
        ("추가 이동비 안내", "/reservation/#move"),
        ("결제 방식 안내", "/reservation/#payment"),
        ("예약 변경·취소 안내", "/reservation/#change"),
    ]),
    ("이용 전 확인사항", "/guide/", [
        ("처음 이용하시는 분", "/guide/#first"),
        ("방문 가능 주소 확인", "/guide/#prepare"),
        ("자택·숙소·사무실 이용 안내", "/guide/#place"),
        ("위생 및 안전 기준", "/guide/#hygiene"),
        ("개인정보 처리 기준", "/guide/#privacy"),
        ("불법·선정적 서비스 불가 안내", "/guide/#prohibited"),
    ]),
    ("홈타이 이용 가이드", "/massage/", [
        ("홈타이란?", "/massage/#hometai"),
        ("출장마사지와 홈타이 차이", "/massage/#diff"),
        ("은평구 홈타이 이용 기준", "/massage/#standard"),
        ("지역별 이동 기준", "/massage/#move"),
        ("코스 선택 안내", "/massage/#course"),
        ("처음 이용 고객 안내", "/massage/#first"),
    ]),
    ("고객센터", "/support/", [
        ("문의하기", "/support/#contact"),
        ("자주 묻는 질문", "/support/#faq"),
        ("운영 기준", "/support/#notice"),
        ("제휴·기업 문의", "/support/#biz"),
        ("개인정보처리방침", "/support/privacy/"),
        ("이용약관", "/support/terms/"),
    ]),
]

# 보조 콘텐츠(테마·코스·매거진·후기·운영자 소개) — 푸터에서 연결한다.
