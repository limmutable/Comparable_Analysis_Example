# 노타 (Nota) 밸류에이션 분석

**분석 기준일:** 2026-01-12
**데이터 출처:** 증권신고서, Peer company filings, Yahoo Finance, Stock Analysis

---

## 1. Trading Multiples 비교

### Enterprise Value Multiples

| 회사 | 티커 | 매출 ($M) | EV ($M) | EV/Revenue | 성장률 | 비고 |
|------|------|-----------|---------|------------|--------|------|
| SoundHound AI | SOUN | 84.7 | 4,520 | 53.4x | +85% | AI hype premium |
| BigBear AI | BBAI | 158.2 | 2,412 | 15.3x | +2% | M&A premium |
| C3.ai | AI | 310.6 | 1,310 | 4.2x | +25% | Enterprise AI |
| CEVA Inc | CEVA | 106.9 | 462 | 4.3x | +10% | Edge AI IP |
| Indie Semi | INDI | 216.7 | 785 | 3.6x | -3% | Automotive |
| Airship AI | AISP | 23.1 | 79 | 3.4x | +87% | Small-cap |
| Veritone | VERI | 92.6 | 200 | 2.2x | -7% | Declining |

### Multiple 통계

| 통계 | EV/Revenue | 비고 |
|------|------------|------|
| **평균** | 12.3x | SoundHound 포함 |
| **중간값** | 4.2x | 기본 적용 배수 |
| **최고** | 53.4x | SoundHound (Outlier) |
| **최저** | 2.2x | Veritone |
| **Outlier 제외 평균** | 5.5x | SOUN 제외 |
| **고성장 기업 중간값** | 9.4x | SOUN, AISP, AI |

---

## 2. Target 밸류에이션

### 노타 재무 데이터

| 항목 | KRW (백만원) | USD ($M) | 비고 |
|------|-------------|----------|------|
| FY2024 매출 | 8,437 | 6.5 | 환율 1,300 적용 |
| 매출 성장률 | +136% | +136% | YoY |
| FY2025E 매출 | 15,000~18,000 | 11.5~13.8 | 추정 |
| 현금 | 10,088 | 7.8 | H1 2025 기준 |
| 부채 | ~0 | ~0 | IPO 후 |

### 밸류에이션 방법론

노타는 Pre-profit 기업으로 EV/EBITDA, P/E 방법론 적용이 부적합합니다. **EV/Revenue** 방법론을 주요 밸류에이션 접근법으로 사용합니다.

### Multiple 선정 근거

| 시나리오 | 적용 배수 | 선정 근거 |
|----------|-----------|-----------|
| **Conservative** | 4.0x | Peer 중간값 (성숙기 기업 기준) |
| **Base Case** | 6.0x | 고성장 프리미엄 반영 (Peer 평균 대비 50% 할증) |
| **Optimistic** | 10.0x | 고성장 기업 기준 (SoundHound, Airship 참조) |

**노타 vs Peer 비교:**
- 노타 성장률 (+136%) > Peer 평균 (+27%)
- 노타는 고성장 프리미엄을 받을 자격이 있음
- 단, KOSDAQ 상장으로 유동성 할인 적용 가능

---

## 3. Implied Valuation Range

### FY2024 매출 기준

| 방법론 | 매출 ($M) | 적용 배수 | Implied EV ($M) | 조정 | Implied Equity ($M) |
|--------|-----------|-----------|-----------------|------|---------------------|
| EV/Revenue (Low) | 6.5 | 4.0x | 26.0 | +7.8 Cash | **33.8** |
| EV/Revenue (Mid) | 6.5 | 6.0x | 39.0 | +7.8 Cash | **46.8** |
| EV/Revenue (High) | 6.5 | 10.0x | 65.0 | +7.8 Cash | **72.8** |

### FY2025E 매출 기준 (Forward Multiple)

| 방법론 | 매출 ($M) | 적용 배수 | Implied EV ($M) | 조정 | Implied Equity ($M) |
|--------|-----------|-----------|-----------------|------|---------------------|
| EV/Revenue (Low) | 12.0 | 3.5x | 42.0 | +7.8 Cash | **49.8** |
| EV/Revenue (Mid) | 12.0 | 5.0x | 60.0 | +7.8 Cash | **67.8** |
| EV/Revenue (High) | 12.0 | 8.0x | 96.0 | +7.8 Cash | **103.8** |

---

## 4. 민감도 분석

### EV/Revenue 민감도 (FY2024 매출 기준)

| 매출 ($M) \ 배수 | 3.0x | 4.0x | 5.0x | 6.0x | 8.0x | 10.0x |
|------------------|------|------|------|------|------|-------|
| $5.0M | $15M | $20M | $25M | $30M | $40M | $50M |
| **$6.5M** | $20M | **$26M** | $33M | **$39M** | $52M | **$65M** |
| $8.0M | $24M | $32M | $40M | $48M | $64M | $80M |
| $10.0M | $30M | $40M | $50M | $60M | $80M | $100M |

### 성장률-배수 민감도

| 성장률 \ 적용 배수 | Conservative | Base | Optimistic |
|--------------------|--------------|------|------------|
| +100% | 3.5x | 5.0x | 8.0x |
| **+136%** (실적) | **4.0x** | **6.0x** | **10.0x** |
| +150% | 4.5x | 7.0x | 12.0x |

---

## 5. 밸류에이션 범위 요약

### Equity Value Range (USD)

| 시나리오 | FY2024 기준 | FY2025E 기준 | 가중 평균 |
|----------|-------------|--------------|-----------|
| **Conservative** | $33.8M | $49.8M | **$42M** |
| **Base Case** | $46.8M | $67.8M | **$57M** |
| **Optimistic** | $72.8M | $103.8M | **$88M** |

### Equity Value Range (KRW, 환율 1,300 적용)

| 시나리오 | Equity Value (억원) | 비고 |
|----------|---------------------|------|
| **Conservative** | **~550억원** | Peer 중간값 적용 |
| **Base Case** | **~740억원** | 고성장 프리미엄 반영 |
| **Optimistic** | **~1,140억원** | 고성장 기업 기준 |

---

## 6. 밸류에이션 조정 요인

### Premium 요인 (상향 조정)

| 요인 | 영향 | 근거 |
|------|------|------|
| 고성장 (+136%) | +20~40% | Peer 평균 대비 5배 성장률 |
| 시장 포지션 | +10% | 국내 최초/선두 AI 최적화 기업 |
| 글로벌 고객 | +10% | 삼성전자, Arm, Renesas 등 |
| IP 포트폴리오 | +5% | 119건 특허/상표권 |

### Discount 요인 (하향 조정)

| 요인 | 영향 | 근거 |
|------|------|------|
| KOSDAQ 상장 | -15~20% | 글로벌 시장 대비 유동성 할인 |
| Pre-profit | -10% | 수익성 미검증 |
| 소규모 매출 | -10% | 매출 $6.5M은 Peer 최소치 미만 |
| 고객 집중 | -5% | 소수 대형 고객 의존 |

### 순 조정

**Net Premium/Discount: 0% ~ +15%**

Base Case 배수 (6.0x)는 이미 프리미엄을 반영했으므로 추가 조정 불필요.

---

## 7. Peer 대비 포지션

```
EV/Revenue Multiple Map
│
│  SoundHound ●                                      53.4x (Outlier)
│              │
│              │
│  BigBear    ●                                      15.3x
│              │
│              │
│  Nota       ●──────● (Implied Range: 4.0x - 10.0x)
│              │
│  C3.ai      ●                                       4.2x
│  CEVA       ●                                       4.3x
│  Indie      ●                                       3.6x
│  Airship    ●                                       3.4x
│  Veritone   ●                                       2.2x
└────────────────────────────────────────────────────────────
```

---

## 8. 주요 가정 및 제한사항

### 주요 가정

1. **환율:** KRW/USD = 1,300 (시장 환율 참조)
2. **FY2025 매출:** 기존 성장률 유지 시 ~$12M 추정
3. **부채:** IPO 이후 순부채 ~$0 가정
4. **시장 환경:** AI 섹터 밸류에이션 프리미엄 지속 가정

### 제한사항

1. **직접 비교 기업 부족:** Deci AI, Neural Magic 등 직접 경쟁사는 인수됨
2. **규모 차이:** Nota 매출($6.5M)은 Peer 최소(Airship $23M)보다 작음
3. **시장 변동성:** AI 섹터 밸류에이션은 높은 변동성 보유
4. **수익성 미검증:** Pre-profit 기업으로 수익 모델 검증 필요

---

## 9. 결론 및 권고

### 밸류에이션 결론

| 지표 | 값 |
|------|-----|
| **Implied Equity Value (Base)** | **$57M (약 740억원)** |
| **Implied Equity Value Range** | **$42M - $88M (550억원 - 1,140억원)** |
| **적용 EV/Revenue** | **4.0x - 10.0x (Base: 6.0x)** |

### 밸류에이션 근거

1. **고성장 프리미엄:** +136% 성장률은 Peer 중 최고 수준
2. **기술 차별화:** Hardware-Aware AI 최적화 기술로 글로벌 반도체 기업과 협력
3. **시장 성장:** On-Device AI 시장 CAGR 38%+ 전망
4. **KOSDAQ 할인:** 글로벌 상장 대비 유동성 할인 적용

### 투자 고려사항

- **Upside:** 매출 성장 지속 시 고성장 프리미엄 확대 가능
- **Downside:** 경쟁 심화, 고객 집중 리스크, 수익성 달성 지연
- **Catalyst:** 대형 계약 체결, 흑자 전환, 글로벌 확장

---

## 10. 다음 단계

- [ ] `05-output-format.md` - 최종 보고서 작성 및 CSV 내보내기
- [ ] 분기별 실적 업데이트 시 밸류에이션 재검토
- [ ] 추가 Peer 발굴 (신규 상장 AI 기업)

---

**데이터 출처:**
- [SoundHound AI Statistics](https://stockanalysis.com/stocks/soun/statistics/)
- [CEVA Financial Results](https://www.ceva-ip.com/press/)
- [BigBear AI IR](https://ir.bigbear.ai/)
- [C3.ai Statistics](https://stockanalysis.com/stocks/ai/statistics/)
- [AI Valuation Multiples 2025](https://aventis-advisors.com/ai-valuation-multiples/)
- [Software Valuation Multiples](https://multiples.vc/reports/software-saas-valuation-multiples)

---

*본 분석은 교육 목적으로 작성되었으며, 투자 권유가 아닙니다.*
