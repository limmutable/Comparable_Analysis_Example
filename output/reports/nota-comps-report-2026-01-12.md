# 노타 (Nota) Comparable Analysis Report

**회사:** 노타 (Nota Inc.)
**분석일:** 2026-01-12
**분석가:** Claude AI (Financial Analysis Skill)
**버전:** v1.0

---

## Executive Summary

### 핵심 결론

1. **밸류에이션 범위:** $42M - $88M (550억원 - 1,140억원), Base Case $57M (740억원)
2. **적용 방법론:** EV/Revenue 4.0x - 10.0x (Pre-profit 기업으로 수익 기반 멀티플 부적합)
3. **고성장 프리미엄:** +136% YoY 성장률은 Peer 평균(+27%) 대비 5배, 프리미엄 적용 타당
4. **주요 리스크:** 소규모 매출($6.5M), 고객 집중, KOSDAQ 유동성 할인

### 밸류에이션 요약

| 시나리오 | Equity Value (USD) | Equity Value (KRW) | 적용 EV/Revenue |
|----------|-------------------|-------------------|-----------------|
| Conservative | $42M | ~550억원 | 4.0x |
| **Base Case** | **$57M** | **~740억원** | **6.0x** |
| Optimistic | $88M | ~1,140억원 | 10.0x |

### Investment Highlights

| 구분 | 내용 |
|------|------|
| **Upside** | 매출 성장 지속, 대형 계약 체결, 글로벌 확장 |
| **Downside** | 경쟁 심화, 수익성 달성 지연, 고객 집중 리스크 |
| **Catalyst** | 삼성/Arm 계약 확대, 흑자 전환, On-Device LLM 시장 성장 |

---

## 1. 회사 개요

### 사업 요약

노타는 AI 모델 경량화 및 최적화 기술을 기반으로 온디바이스 AI 솔루션을 제공하는 기업입니다.

| 구분 | 내용 |
|------|------|
| **산업** | AI 소프트웨어 / 온디바이스 AI / 엣지 AI |
| **제품** | NetsPresso Platform (AI 모델 최적화), NetsPresso Solution (맞춤형 솔루션) |
| **수익 모델** | B2B 플랫폼 라이선싱, 프로젝트 기반 공급, Revenue Sharing |
| **타겟 시장** | 반도체, 전자기기, IoT, 자동차 |
| **상장 시장** | 코스닥 (KOSDAQ) |

### 핵심 기술

- **모델 경량화:** Pruning, Knowledge Distillation, Filter Decomposition
- **양자화:** FP32 → Int8, Mixed Precision
- **On-Device LLM:** 모바일/엣지 디바이스용 LLM 최적화

### 주요 고객

- 삼성전자 (반도체)
- Arm (반도체 IP)
- Renesas (자동차 반도체)
- 대전시 (스마트시티)

### 경쟁 우위

| 구분 | 내용 |
|------|------|
| **기술 차별화** | Hardware-Aware AI 최적화 (다양한 HW 지원) |
| **지적재산권** | 119건 (국내 82, 미국 12, 일본 10, 상표 15) |
| **선점 효과** | 2019년 시장 진입, 국내 최초 AI 최적화 전문 기업 |

---

## 2. 재무 현황

### 손익계산서 (KRW Million)

| Metric | FY2024 | FY2023 | FY2022 | YoY Growth |
|--------|-------:|-------:|-------:|-----------:|
| Revenue | 8,437 | 3,581 | 2,005 | +136% |
| Operating Loss | (12,019) | (11,324) | (9,548) | - |
| Net Loss | (24,852) | (13,135) | (7,895) | - |

### 재무상태표 (KRW Million)

| Metric | H1 2025 | FY2024 |
|--------|--------:|-------:|
| Total Assets | 23,066 | 27,420 |
| Cash | 10,088 | 6,676 |
| Total Debt | ~0 | N/A |
| Equity | 7,857 | (70,517)* |

*FY2024 부채에는 RCPS 및 파생상품부채 포함, IPO 후 자본전환됨

### 매출 성장 추이

```
Revenue (KRW Billion)
10 ┤
 8 ┤                    ████ 8.4B (+136%)
 6 ┤
 4 ┤          ████ 3.6B (+79%)
 2 ┤████ 2.0B
 0 └──────────────────────────────
      2022     2023     2024
```

---

## 3. Peer Group 분석

### 선정 기준

| 단계 | 기준 | 결과 |
|------|------|------|
| 1 | 산업: AI 소프트웨어 / Edge AI | 50+ |
| 2 | 비즈니스 모델: B2B 플랫폼/라이선싱 | 25 |
| 3 | 상장 여부: 공개 상장사 | 15 |
| 4 | 성장 단계: High-growth / Pre-profit | 10 |
| 5 | 데이터 가용성 | **7** |

### 최종 Peer Group

| # | 회사명 | 티커 | 매출 ($M) | 시총 ($M) | 성장률 | 적합도 |
|---|--------|------|----------:|----------:|-------:|--------|
| 1 | CEVA Inc | CEVA | 106.9 | 620 | +10% | ★★★★★ |
| 2 | SoundHound AI | SOUN | 84.7 | 4,720 | +85% | ★★★★☆ |
| 3 | C3.ai | AI | 310.6 | 2,040 | +25% | ★★★☆☆ |
| 4 | BigBear AI | BBAI | 158.2 | 2,500 | +2% | ★★★☆☆ |
| 5 | Indie Semi | INDI | 216.7 | 800 | -3% | ★★★☆☆ |
| 6 | Airship AI | AISP | 23.1 | 90 | +87% | ★★★☆☆ |
| 7 | Veritone | VERI | 92.6 | 180 | -7% | ★★☆☆☆ |

### Peer Group 특성

| 지표 | 값 |
|------|-----|
| 평균 매출 | $149M |
| 매출 범위 | $23M - $311M |
| 평균 성장률 | +27% |
| 평균 시가총액 | $1,564M |
| 수익성 | 6/7 기업 Pre-profit |

### 제외 기업

| 회사명 | 제외 사유 |
|--------|-----------|
| Deci AI | NVIDIA에 인수됨 (2024) |
| Neural Magic | IBM/Red Hat에 인수됨 |
| NVIDIA, Intel, AMD | 규모 과다, 다각화된 사업 |
| UiPath, Palantir | 비즈니스 모델 차이 |

---

## 4. Trading Multiples 분석

### EV/Revenue Multiples

| Company | Revenue ($M) | EV ($M) | EV/Revenue | Growth | Note |
|---------|-------------:|--------:|-----------:|-------:|------|
| SoundHound | 84.7 | 4,520 | **53.4x** | +85% | Outlier |
| BigBear | 158.2 | 2,412 | **15.3x** | +2% | M&A premium |
| C3.ai | 310.6 | 1,310 | **4.2x** | +25% | |
| CEVA | 106.9 | 462 | **4.3x** | +10% | |
| Indie Semi | 216.7 | 785 | **3.6x** | -3% | |
| Airship | 23.1 | 79 | **3.4x** | +87% | |
| Veritone | 92.6 | 200 | **2.2x** | -7% | |

### Multiple 통계

| Statistic | EV/Revenue | Notes |
|-----------|:----------:|-------|
| Mean | 12.3x | SoundHound skews |
| **Median** | **4.2x** | Primary reference |
| High | 53.4x | SoundHound |
| Low | 2.2x | Veritone |
| Ex-Outlier Mean | 5.5x | Excluding SOUN |

---

## 5. 밸류에이션 분석

### 방법론 선정

노타는 **Pre-profit 기업**으로 EV/EBITDA, P/E 방법론이 부적합합니다.
**EV/Revenue** 방법론을 주요 접근법으로 사용합니다.

### Multiple 선정

| 시나리오 | 적용 배수 | 선정 근거 |
|----------|:---------:|-----------|
| Conservative | 4.0x | Peer 중간값 |
| **Base Case** | **6.0x** | 고성장 프리미엄 50% 반영 |
| Optimistic | 10.0x | 고성장 기업 참조 |

### Implied Valuation (FY2024 기준)

| 시나리오 | 매출 | 배수 | Implied EV | Cash | Implied Equity |
|----------|-----:|-----:|-----------:|-----:|---------------:|
| Conservative | $6.5M | 4.0x | $26.0M | $7.8M | **$33.8M** |
| Base Case | $6.5M | 6.0x | $39.0M | $7.8M | **$46.8M** |
| Optimistic | $6.5M | 10.0x | $65.0M | $7.8M | **$72.8M** |

### Implied Valuation (FY2025E Forward)

| 시나리오 | 매출 | 배수 | Implied EV | Cash | Implied Equity |
|----------|-----:|-----:|-----------:|-----:|---------------:|
| Conservative | $12.0M | 3.5x | $42.0M | $7.8M | **$49.8M** |
| Base Case | $12.0M | 5.0x | $60.0M | $7.8M | **$67.8M** |
| Optimistic | $12.0M | 8.0x | $96.0M | $7.8M | **$103.8M** |

### 가중 평균 밸류에이션

| 시나리오 | FY2024 | FY2025E | 가중 평균 (50/50) |
|----------|-------:|--------:|------------------:|
| Conservative | $33.8M | $49.8M | **$42M (~550억원)** |
| Base Case | $46.8M | $67.8M | **$57M (~740억원)** |
| Optimistic | $72.8M | $103.8M | **$88M (~1,140억원)** |

---

## 6. 민감도 분석

### EV/Revenue 민감도 Matrix (EV, $M)

| 매출 \ 배수 | 3.0x | 4.0x | 5.0x | 6.0x | 8.0x | 10.0x |
|------------:|-----:|-----:|-----:|-----:|-----:|------:|
| $5.0M | $15 | $20 | $25 | $30 | $40 | $50 |
| **$6.5M** | $20 | **$26** | $33 | **$39** | $52 | **$65** |
| $8.0M | $24 | $32 | $40 | $48 | $64 | $80 |
| $10.0M | $30 | $40 | $50 | $60 | $80 | $100 |
| $12.0M | $36 | $48 | $60 | $72 | $96 | $120 |

### 성장률-배수 관계

| 성장률 | Conservative | Base | Optimistic |
|-------:|:------------:|:----:|:----------:|
| +100% | 3.5x | 5.0x | 8.0x |
| **+136%** | **4.0x** | **6.0x** | **10.0x** |
| +150% | 4.5x | 7.0x | 12.0x |

---

## 7. 리스크 및 제한사항

### 분석 제한사항

| 제한사항 | 설명 |
|----------|------|
| **직접 비교 기업 부족** | Deci AI, Neural Magic 등 직접 경쟁사는 인수됨 |
| **규모 차이** | Nota 매출($6.5M)은 Peer 최소(Airship $23M)보다 작음 |
| **시장 변동성** | AI 섹터 밸류에이션은 높은 변동성 보유 |
| **수익성 미검증** | Pre-profit 기업으로 수익 모델 검증 필요 |

### 주요 리스크

| 리스크 | 영향 | 완화 요인 |
|--------|------|-----------|
| **수익성 리스크** | 지속적인 영업손실 | 매출 성장으로 레버리지 개선 가능 |
| **고객 집중** | 소수 대형 고객 의존 | 신규 고객 파이프라인 확보 중 |
| **기술 리스크** | AI 모델 트렌드 변화 | 지속적 R&D 투자, 학술 역량 |
| **경쟁 리스크** | 빅테크 자체 도구 개발 | HW-Agnostic 플랫폼 차별화 |
| **KOSDAQ 할인** | 글로벌 대비 유동성 할인 | 해외 상장 검토 가능 |

### Premium/Discount 요인

**Premium (+):**
- 고성장 (+136%): +20~40%
- 시장 포지션 (국내 선두): +10%
- 글로벌 고객: +10%
- IP 포트폴리오: +5%

**Discount (-):**
- KOSDAQ 상장: -15~20%
- Pre-profit: -10%
- 소규모 매출: -10%
- 고객 집중: -5%

---

## 8. 시장 환경

### 시장 규모 전망

| 시장 | 2023 | 2027-2030 | CAGR |
|------|-----:|----------:|-----:|
| On-Device AI (TAM) | $3.8B | $50.5B | 38.2% |
| On-Device AI SW (SAM) | $260M | $1.1B | 32.7% |
| Edge AI (TAM) | $18.5B | $173.9B | 37.7% |

### AI 밸류에이션 트렌드 (2025)

| 카테고리 | 일반적인 EV/Revenue |
|----------|:-------------------:|
| AI Startups (Fundraising) | 25-30x |
| Public SaaS | ~6x |
| Hardware/Semiconductor | ~1.4x |
| High-Growth AI Software | 10-30x+ |

---

## Appendix

### A. 데이터 출처

| 데이터 | 출처 | 날짜 |
|--------|------|------|
| Nota 재무 | 증권신고서 (nota-sec.pdf) | 2025 H1 |
| SoundHound | Stock Analysis | 2026-01 |
| CEVA | PR Newswire, 10-K | 2025-02 |
| BigBear | Company IR | 2025-03 |
| C3.ai | Stock Analysis | 2026-01 |
| Indie Semi | Business Wire | 2025-02 |
| Airship AI | Globe Newswire | 2025-03 |
| 환율 | Market Reference | 2026-01-12 |

### B. 용어 정의

| 용어 | 정의 |
|------|------|
| EV | Enterprise Value = Market Cap + Debt - Cash |
| EBITDA | Earnings Before Interest, Taxes, Depreciation & Amortization |
| LTM | Last Twelve Months (최근 12개월) |
| NTM | Next Twelve Months (향후 12개월) |
| Pre-profit | 영업이익/순이익이 음수인 기업 |

### C. 첨부 파일

- [재무 데이터 (CSV)](../nota/03-financial-data.csv)
- [Comps Table (CSV)](../nota/04-comps-table.csv)

---

**Disclaimer:** 본 분석은 교육 목적으로 작성되었으며, 투자 권유가 아닙니다. 실제 투자 결정 시 전문가 상담을 권장합니다.

---

Generated by Claude AI (Financial Analysis Skill) | 2026-01-12
