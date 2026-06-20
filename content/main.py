# 은평구 메인 페이지 — 허브 역할. 모든 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY
from .pricing import PRICING

_JSONLD = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "HealthAndBeautyBusiness",
  "name": "{BRAND}",
  "telephone": "{PHONE}",
  "url": "{BASE_URL}/",
  "image": "{BASE_URL}/assets/og-image.png",
  "description": "은평구 전지역 방문형 출장마사지·홈타이 예약 안내",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "서울특별시 은평구"
  }},
  "openingHours": "Mo-Su 00:00-24:00",
  "priceRange": "₩90,000 - ₩180,000"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "은평구 전지역으로 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "연신내·불광·응암·녹번·은평뉴타운을 포함한 은평구 대표 11개 동을 안내하고 있습니다. 정확한 가능 여부는 예약 시간, 방문 위치, 배정 상황에 따라 달라지므로 지역별 안내 페이지에서 생활권을 먼저 확인하신 뒤 전화로 확정하시길 권장합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "연신내역·불광역·구파발역 근처도 안내가 되나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "은평구를 지나는 3호선과 6호선 주요 역세권은 역 상세 페이지에서 인접 생활권과 함께 정리해 두었습니다. 환승역도 페이지는 하나로 운영하며, 실제 가능 여부는 예약 시 위치를 기준으로 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "불광1동·응암3동처럼 번호 동은 왜 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "불광1·2동, 응암1·2·3동, 갈현1·2동, 신사1·2동처럼 번호로 나뉜 행정동은 대표 동 페이지 안에서 세부 생활권으로 통합 안내합니다. 비슷한 내용을 반복하는 중복 페이지를 만들지 않기 위한 운영 기준입니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "은평뉴타운이나 진관동도 방문 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "구파발역·은평뉴타운·북한산 인접 생활권은 진관동 대표 페이지와 은평뉴타운·진관 생활권 안내에서 다룹니다. 대단지 아파트가 많은 지역인 만큼 동·호수와 공동현관 출입 방법을 예약 시 함께 알려주시면 도착이 빨라집니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "홈타이와 출장마사지는 어디에서 비교하나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "홈타이 이용 가이드 페이지에서 두 방식의 차이, 은평구 이용 기준, 코스 선택 방법을 정리했습니다. 처음 이용하시는 분은 이 안내를 먼저 읽으신 뒤 예약하시면 도움이 됩니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Spa · 은평구 전지역</p>
    <h1>은평구 출장마사지 · 은평구 홈타이 지역별 예약 안내</h1>
    <p class="hero-lead">연신내·불광·응암·은평뉴타운까지, 샵을 찾아갈 필요 없이 계신 곳에서 받는 방문형 관리.<br>자택·오피스텔·숙소 어디든 전화 한 통으로 가능 지역을 확인해 드립니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/courses/">코스 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>11개</strong><span>대표 동</span></li>
      <li><strong>12개</strong><span>역세권</span></li>
      <li><strong>10개</strong><span>생활권</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<p class="lead">은평구에서 출장마사지와 홈타이 예약을 알아보실 때 가장 먼저 막히는 부분은 "우리 동네에 정말 오는지, 얼마인지, 처음인데 무엇을 준비해야 하는지"입니다. 이 페이지는 연신내, 불광, 응암, 녹번, 은평뉴타운 생활권을 한눈에 보고 자신에게 맞는 안내 페이지로 바로 이동할 수 있도록 만든 은평구 전체 허브입니다. {BRAND}는 키워드를 반복해 페이지를 늘리는 대신, 대표 동·역세권·생활권을 기준으로 실제 방문 조건이 다른 지역만 고유하게 정리했습니다.</p>

<section id="criteria">
<h2>은평구에서 출장마사지를 찾을 때 먼저 확인할 기준</h2>
<p>방문형 관리는 매장을 직접 찾아가는 방식이 아니라 관리사가 자택·오피스텔·숙소로 이동해 진행하는 서비스이기 때문에, 매장 위치보다 "내가 있는 곳까지 정해진 시간 안에 도착할 수 있는가"가 가장 중요한 기준이 됩니다. 그래서 은평구를 알아보실 때는 광고 문구보다 다음 네 가지를 먼저 확인하시는 편이 안전합니다.</p>
<p>첫째, 방문 가능 지역이 구체적으로 적혀 있는지 보세요. 막연히 "서울 전지역"이라고만 적힌 곳보다, 녹번·불광·응암·진관처럼 동 단위로 생활권을 나눠 설명하는 안내가 실제 도착 시간 예측에 유리합니다. 둘째, 요금이 코스별로 공개되어 있는지 확인하세요. {BRAND}는 60·90·120분 기준 요금을 화면에 그대로 공개하며, 이동 거리나 예약 시간대에 따른 추가 비용은 상담 단계에서 미리 확인해 드립니다. 셋째, 예약 절차가 명확한지 보세요. 위치 확인, 시간 확인, 코스 선택, 가능 여부 안내, 예약 확정으로 이어지는 단계가 정리되어 있어야 처음 이용하시는 분도 혼선이 없습니다. 넷째, 위생·개인정보·금지행위 기준이 분명한지 확인하세요. 자세한 비교는 <a href="/massage/">출장마사지와 홈타이의 차이부터 은평구 이용 기준까지 정리한 홈타이 이용 가이드</a>에서 단계별로 확인하실 수 있습니다.</p>
<p>은평구는 행정 구역상 <a href="https://www.ep.go.kr/" target="_blank" rel="noopener nofollow">은평구청 공식 홈페이지</a> 기준 11개 행정동권으로 나뉘고, 3호선과 6호선이 구를 가로지르며 연신내·불광·구파발 같은 핵심 환승·상권 거점이 분포해 있습니다. 같은 은평구라도 북한산 자락의 진관동과 불광천을 낀 응암동, DMC와 가까운 수색동은 도로 사정과 방문 동선이 서로 다르기 때문에, 생활권별로 나눠 보는 것이 정확합니다.</p>
</section>

<section id="lifezone">
<h2>연신내·불광·응암·진관 생활권 차이</h2>
<p>은평구를 크게 보면 성격이 다른 네 개의 축으로 이해하면 편합니다. 연신내 축은 은평구 최대 상권으로, 연신내역을 중심으로 음식점·숙박·오피스가 밀집해 저녁과 심야 시간대 문의가 많은 지역입니다. 머무시는 곳이 상권 한가운데라면 주변 도로 혼잡과 주차 여건을 함께 알려주시면 도착 예측이 정확해집니다. 자세한 내용은 <a href="/seoul/eunpyeong-gu/area/yeonsinnae-commercial/">연신내 상권을 중심으로 한 생활권 방문 관리 안내</a>에서 다룹니다.</p>
<p>불광 축은 불광역·독바위역과 북한산 입구를 끼고 있어 주거와 등산·여가 수요가 겹치는 지역입니다. 단독·다세대 주택과 아파트가 섞여 있어 공동현관 출입 방법을 미리 확인해 두면 좋습니다. 자세한 안내는 <a href="/seoul/eunpyeong-gu/area/bulgwang-bukhansan/">불광·북한산 인접 생활권 방문 안내</a>에서 확인하세요. 응암 축은 응암역·새절역과 불광천을 따라 형성된 주거 밀집 지역으로, 6호선 라인을 따라 신사동·증산동까지 생활권이 이어집니다. <a href="/seoul/eunpyeong-gu/area/eungam-bulgwangcheon/">응암·불광천을 따라 이어지는 생활권 안내</a>에서 더 자세히 설명합니다.</p>
<p>진관 축은 구파발역과 은평뉴타운, 북한산을 끼고 있는 대단지 신도시 생활권입니다. 대규모 아파트 단지가 많아 동·호수와 단지 출입 정보를 정확히 주시면 도착이 빨라집니다. 자세한 내용은 <a href="/seoul/eunpyeong-gu/area/eunpyeong-newtown-jingwan/">은평뉴타운·진관 생활권의 방문 동선 안내</a>에서 확인하실 수 있습니다. 이렇게 네 축의 성격이 다르기 때문에, 같은 은평구 안에서도 예약 전 확인해야 할 항목이 조금씩 달라집니다.</p>
</section>

<section id="dongs">
<h2>대표동별 방문 가능 지역 안내</h2>
<p>지역별 안내는 은평구 11개 대표 동을 기준으로 구성되어 있습니다. 불광1·2동, 응암1·2·3동, 갈현1·2동, 신사1·2동처럼 번호로 나뉜 행정동은 별도 페이지를 만들지 않고 각 대표 동 페이지 안에서 세부 생활권으로 묶어 안내합니다. 아래에서 거주하시거나 머무시는 동을 선택해 주세요.</p>
<ul class="card-grid">
<li><a href="/seoul/eunpyeong-gu/nokbeon-dong/">녹번동</a></li>
<li><a href="/seoul/eunpyeong-gu/bulgwang-dong/">불광동</a></li>
<li><a href="/seoul/eunpyeong-gu/galhyeon-dong/">갈현동</a></li>
<li><a href="/seoul/eunpyeong-gu/gusan-dong/">구산동</a></li>
<li><a href="/seoul/eunpyeong-gu/daejo-dong/">대조동</a></li>
<li><a href="/seoul/eunpyeong-gu/eungam-dong/">응암동</a></li>
<li><a href="/seoul/eunpyeong-gu/yeokchon-dong/">역촌동</a></li>
<li><a href="/seoul/eunpyeong-gu/sinsa-dong/">신사동</a></li>
<li><a href="/seoul/eunpyeong-gu/jeungsan-dong/">증산동</a></li>
<li><a href="/seoul/eunpyeong-gu/susaek-dong/">수색동</a></li>
<li><a href="/seoul/eunpyeong-gu/jingwan-dong/">진관동</a></li>
</ul>
<p>각 동 페이지에서는 해당 생활권의 특징, 가까운 역세권, 방문 전 확인사항, 예약 가능 시간대를 동마다 다른 관점으로 설명합니다. 예를 들어 <a href="/seoul/eunpyeong-gu/nokbeon-dong/">녹번역·은평구청 생활권을 다루는 녹번동 방문 안내</a>는 관공서·업무 동선을 중심으로, <a href="/seoul/eunpyeong-gu/jingwan-dong/">구파발역·은평뉴타운 인접 진관동 방문 안내</a>는 대단지 출입 동선을 중심으로 작성되어 있습니다. 은평구 전체 구조가 궁금하시면 <a href="/seoul/eunpyeong-gu/">은평구 지역별 안내 허브</a>에서 한눈에 확인하실 수 있습니다.</p>
</section>

<section id="stations">
<h2>연신내역·불광역·구파발역·응암역 역세권 안내</h2>
<p>역세권 안내는 은평구를 지나는 3호선과 6호선 주요 역을 기준으로 구성합니다. 각 역 페이지에서는 인근 생활권, 주변 대표 동, 예약 가능 시간대, 방문 전 준비사항을 설명하며, 출구별 페이지나 역과 테마를 조합한 페이지는 만들지 않습니다. 환승역도 노선이 여러 개라도 페이지는 하나로 운영합니다.</p>
<ul class="card-grid">
<li><a href="/seoul/eunpyeong-gu/station/yeonsinnae-station/">연신내역</a></li>
<li><a href="/seoul/eunpyeong-gu/station/bulgwang-station/">불광역</a></li>
<li><a href="/seoul/eunpyeong-gu/station/gupabal-station/">구파발역</a></li>
<li><a href="/seoul/eunpyeong-gu/station/eungam-station/">응암역</a></li>
<li><a href="/seoul/eunpyeong-gu/station/nokbeon-station/">녹번역</a></li>
<li><a href="/seoul/eunpyeong-gu/station/dokbawi-station/">독바위역</a></li>
<li><a href="/seoul/eunpyeong-gu/station/saejeol-station/">새절역</a></li>
<li><a href="/seoul/eunpyeong-gu/station/digital-media-city-station/">디지털미디어시티역</a></li>
</ul>
<p>가장 문의가 많은 곳은 3호선과 6호선이 만나는 환승 거점입니다. <a href="/seoul/eunpyeong-gu/station/yeonsinnae-station/">연신내역 인근 상권·생활권을 함께 다루는 방문 안내</a>는 심야 시간대 도착 동선을, <a href="/seoul/eunpyeong-gu/station/gupabal-station/">구파발역·은평뉴타운 인접 역세권 안내</a>는 대단지 진입 동선을 중심으로 정리했습니다. 노선·운행 시간 등 교통 정보는 <a href="http://www.seoulmetro.co.kr/" target="_blank" rel="noopener nofollow">서울교통공사 공식 홈페이지</a>에서 확인하실 수 있고, 역 전체 목록은 <a href="/seoul/eunpyeong-gu/station/">은평구 역세권 안내 허브</a>에 정리되어 있습니다.</p>
</section>

<section id="hometai-check">
<h2>은평구 홈타이 예약 전 확인사항</h2>
<p>원활한 방문 관리를 위해 예약 전에 몇 가지를 미리 정리해 두시면 좋습니다. 정확한 주소와 동·호수, 공동현관 출입 방법, 주차 가능 여부, 그리고 관리받을 조용한 공간이 확보되는지를 확인해 주세요. 특히 은평뉴타운이나 연신내 오피스텔처럼 출입 절차가 있는 건물은 예약 시간대에 연락이 가능한지 함께 알려주시면 도착이 지연되지 않습니다.</p>
<p>처음 이용하시는 분이라면 코스 선택이 가장 고민될 수 있습니다. 누적된 피로를 풀고 싶은 분, 편안한 휴식이 필요한 분, 운동 후 근육 이완이 필요한 분, 커플이 함께 받고 싶은 분 등 상황에 따라 권장 코스가 달라집니다. 선택이 어려우시면 <a href="/reservation/">예약 시간과 가능 지역 확인 절차를 정리한 예약 안내</a>를 참고하시거나, 예약 전화에서 컨디션을 말씀해 주시면 함께 정해 드립니다. 방문 전 준비사항 전체는 <a href="/guide/">자택·숙소·사무실 이용 시 확인해야 할 사항을 정리한 이용 전 확인사항</a>에 단계별로 정리되어 있습니다.</p>
</section>

<section id="dedup">
<h2>은평구 페이지 중복 방지 운영 기준</h2>
<p>{BRAND}는 검색 노출용 페이지를 무작정 늘리지 않습니다. 지역명과 역명만 바꿔 같은 문장을 반복하는 페이지는 이용자에게 도움이 되지 않을 뿐 아니라 정보의 신뢰도를 떨어뜨리기 때문입니다. 그래서 첫째, 번호로 나뉜 행정동은 대표 동 안에서 통합 안내하고, 둘째, 출구별·노선별로 역 페이지를 쪼개지 않으며, 셋째, 지역과 테마를 조합한 페이지(예: "○○동 스웨디시")는 만들지 않습니다.</p>
<p>대신 각 페이지는 실제로 다른 생활권·이동 기준·방문 동선을 기준으로 고유하게 작성합니다. 연신내 상권의 심야 동선, 진관동 대단지의 출입 절차, 수색·증산 DMC 방면의 도로 사정처럼 지역마다 다른 조건을 페이지마다 다르게 설명하는 것이 이 사이트의 운영 원칙입니다. 누가 어떤 기준으로 이 콘텐츠를 만드는지는 <a href="/about/">운영자 소개와 콘텐츠 원칙</a> 페이지에서 공개하고 있습니다.</p>
</section>

<section id="howto">
<h2>은평구 출장마사지 사이트 이용 방법</h2>
<p>이 사이트는 다음 순서로 이용하시면 가장 편합니다. 먼저 위 대표동 또는 역세권 카드에서 머무시는 곳과 가까운 페이지로 이동해 방문 가능 생활권과 어울리는 코스를 확인합니다. 다음으로 코스가 고민되면 <a href="/courses/">코스 안내</a>에서 60·90·120분 구성과 추천 대상을 비교합니다. 그다음 <a href="/reservation/">예약 안내</a>에서 가능 시간과 절차를 확인한 뒤, 마지막으로 전화로 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<p>홈타이가 처음이거나 출장마사지와의 차이가 궁금하시면 <a href="/massage/">홈타이 이용 가이드</a>를, 위생·개인정보·환불 같은 기준이 궁금하시면 <a href="/support/">고객센터</a>를 먼저 보시길 권합니다. 은평구의 행정·생활권 정보는 <a href="https://www.ep.go.kr/" target="_blank" rel="noopener nofollow">은평구청</a>에서, 지하철 운행 정보는 <a href="http://www.seoulmetro.co.kr/" target="_blank" rel="noopener nofollow">서울교통공사</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>은평구 전지역으로 방문이 가능한가요?</h3>
<p>연신내·불광·응암·녹번·은평뉴타운을 포함한 은평구 대표 11개 동을 안내하고 있습니다. 정확한 가능 여부는 예약 시간, 방문 위치, 배정 상황에 따라 달라지므로 지역별 안내 페이지에서 생활권을 먼저 확인하신 뒤 전화로 확정하시길 권장합니다.</p>
</div>
<div class="faq-item">
<h3>연신내역·불광역·구파발역 근처도 안내가 되나요?</h3>
<p>은평구를 지나는 3호선과 6호선 주요 역세권은 역 상세 페이지에서 인접 생활권과 함께 정리해 두었습니다. 환승역도 페이지는 하나로 운영하며, 실제 가능 여부는 예약 시 위치를 기준으로 확인합니다.</p>
</div>
<div class="faq-item">
<h3>불광1동·응암3동처럼 번호 동은 왜 따로 없나요?</h3>
<p>불광1·2동, 응암1·2·3동, 갈현1·2동, 신사1·2동처럼 번호로 나뉜 행정동은 대표 동 페이지 안에서 세부 생활권으로 통합 안내합니다. 비슷한 내용을 반복하는 중복 페이지를 만들지 않기 위한 운영 기준입니다.</p>
</div>
<div class="faq-item">
<h3>은평뉴타운이나 진관동도 방문 가능한가요?</h3>
<p>구파발역·은평뉴타운·북한산 인접 생활권은 진관동 대표 페이지와 은평뉴타운·진관 생활권 안내에서 다룹니다. 대단지 아파트가 많은 지역인 만큼 동·호수와 공동현관 출입 방법을 예약 시 함께 알려주시면 도착이 빨라집니다.</p>
</div>
<div class="faq-item">
<h3>홈타이와 출장마사지는 어디에서 비교하나요?</h3>
<p>홈타이 이용 가이드 페이지에서 두 방식의 차이, 은평구 이용 기준, 코스 선택 방법을 정리했습니다. 처음 이용하시는 분은 이 안내를 먼저 읽으신 뒤 예약하시면 도움이 됩니다.</p>
</div>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>은평구 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 머무시는 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "은평구 출장마사지｜연신내·불광·응암·은평뉴타운 홈타이 지역 안내",
    "desc": "은평구 출장마사지·홈타이 예약 전 연신내, 불광, 응암, 녹번, 은평뉴타운 생활권을 확인하세요.",
    "h1": "은평구 출장마사지 · 은평구 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
