# What the World Bank data told us (and what it did not)

All figures are World Bank WDI, country GMB, retrieved 2026-10-04, and each is linked from the live page (`src/lib/evidence.ts` in the code repo).
"Derived" numbers are our arithmetic on those figures, not separate World Bank indicators.

| Finding | Figures | Design decision it supports |
| --- | --- | --- |
| **Phones outnumber internet users by a wide margin** | 126 mobile subscriptions per 100 people (2024; SIMs, not unique people) vs 49.5% of people using the Internet (2024) | Voice and SMS first for the operator; the internet is only needed by tourists and once a week by a household champion |
| **Tourism is large and fragile** | Receipts US$157M (2019), 43.6% of exports; fell to US$53M in 2020 (derived: down 66%). Arrivals 620,000 to 246,000 (derived: down 60%) | An operator's income can vanish quickly, so answering every enquiry well matters; supports community resilience and fair referrals |
| **Most workers run their own business** | 68.6% of employed people are self-employed (2025, ILO modeled estimate) | Built for one-person operators like Noor, with no staff to read or translate enquiries |
| **Low-lying land** | 18.9% of land is below 5 m above sea level (2015) | One community champion can warn a whole river or road at once (flood notices) |
| **Spend per visitor** (derived) | About US$253 per arrival in 2019 and US$215 in 2020 | Each missed enquiry is worth real money, but we claim no number for how many are missed |

## What it did not show
- It does not show that operators lose enquiries, or that Teranga fixes anything. We did not measure lost enquiries and claim no number.
- No World Bank language or speech dataset was used to build or tune the system. The language data we could use is listed as next steps in
  `docs/eval/WOLOF_TRANSLATION_CHECK.md` (FLEURS, Common Voice, FLORES-200, MMS).
- The brief's other datasets (enterprise surveys, financial inclusion) were not pulled for Gambia in this prototype.
