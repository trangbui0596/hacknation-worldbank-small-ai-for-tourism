# Teranga Gambia — PRD v2 ("Record once, translate weekly")

Track: World Bank x Hack-Nation "Small AI for Development" — Tourism (Annex C).
Submission: 9:00 AM ET, Oct 4, 2026. Required: working prototype + 2–5 min video.
Status: DRAFT. Items marked **[OPEN]** are undecided or unverified.

## 1. What it is

A tourism operator in The Gambia records answers about her tour in her own language on a
feature phone, offline. Once a week a family member's smartphone gets online and the
tool transcribes, translates (English first, then German and Dutch), voices, and
publishes those pre-approved answers. Visitors scan a QR code or message WhatsApp and
get the nearest pre-approved answer as voice and text in their language.

Video one-liner (required format) — DRAFT:
> Because of Teranga, a Gambian tourism operator will turn one phone call in Wolof into answers tourists can read in English, German or Dutch, without internet. Her Google listing is drafted from those answers, and tourists can leave a review by voice. Each week she learns what tourists ask, and her community looks out for one another with shared notices and referrals. Without it, she misses or answers late the enquiries she can't read. We know because the World Bank figures above show how much tourism earns and how many Gambians are still offline.
> and Dutch with her own pre-approved words, every week, instead of losing enquiries she
> cannot read or reply to; we know because **[OPEN: cite verified UN Tourism / WDI /
> Enterprise Surveys figures with year and country]**.

## 2. Devices and people

| Who | Device | Connectivity | Role |
|---|---|---|---|
| Operator ("Noor") | Feature phone (MAIN device) | 2G voice/SMS, often none | Records answers from a printed question card; receives SMS/voice-call summaries |
| Champion (family member) | Smartphone, used ~weekly | Online only when in town | Transfers recordings (Bluetooth), runs weekly sync, reviews and approves |
| Visitor | Own smartphone | Hotel wifi / roaming | Scans QR or messages WhatsApp, gets answers |

The champion may NOT speak English. No step may rely on the champion judging English.

## 3. Core loop (P0)

1. **Record (offline, feature phone).** Noor answers ~10 standard questions in order from a
   printed card (price, meeting point, duration, what to bring, children, food, safety,
   what's included, how to book, cancellation) plus optional free "tour stop" recordings.
   Order identifies the question; no tagging needed.
2. **Transfer.** Bluetooth/file copy to the smartphone. No network needed.
3. **Weekly sync (smartphone online).**
   - Speech-to-text in the Gambian language **[OPEN: language and ASR chosen after support test]**.
   - Translate to English (pivot), then English to German and Dutch.
   - Round-trip check: translate English back to the source language, compare with the
     original transcript; divergence = flagged, not published.
   - Text-to-speech in English/German/Dutch for approved answers.
4. **Review (champion).** Sees which answers are flagged and which are machine-translated;
   approves, re-records, or marks "needs a bilingual reviewer". Numbers, prices and place
   names are always highlighted for confirmation.
5. **Publish.** Approved answers join the answer library.
6. **Visitor Q&A.** QR code or WhatsApp. The visitor's question (any supported language) is
   matched to the nearest library answer by a small intent classifier. Reply = pre-approved
   voice + text, labeled "machine-translated". Low-confidence match = "not sure — Noor will
   answer" (never a guess).
7. **No library answer.** Visitor gets an honest holding message. The question is added to
   Noor's next recording round (answer arrives after the next weekly sync).

## 4. Safeguards (pass/fail — design in)

- Fixed list of answers: the tool only says what Noor recorded and approved.
- Human in the loop: champion approves every library entry; the tool never acts alone.
- Translation safeguard (no assumed English-speaking human): round-trip consistency check,
  low-confidence flags, a "bilingual reviewer" role in the design, and a visitor
  "was this clear?" prompt that sends low-scored answers back to review.
- Honest labeling: every visitor-facing answer says it is machine-translated; translations
  of the Gambian language are **unverified** until a bilingual reviewer checks them.
- Voice cloning: OPTIONAL, only after Noor gives recorded, explicit consent; output labeled
  AI-generated; default is a neutral stock voice.
- Consent and data: visitor feedback shared with the operator only after opt-in; voice
  recordings deletable on request; state the retention policy in the video; note that EU
  visitors' data goes to non-EU services.
- Reviews: the review link is offered neutrally to every visitor regardless of rating. No
  review gating. Complaints also feed private coaching.

## 5. Secondary features

- **P1 Weekly digest.** On the same sync: counts of visitor questions by topic, unanswered
  questions, visitor feedback themes. Delivered to Noor by SMS or an outbound voice call.
  Fixed recommendation templates (pre-translated, flagged "needs native review"), no free
  generation.
- **P2 Pricing range.** A labeled market range with an "ask a person" flag. No pricing
  engine, no auto-changes. Source and gaps stated.
- **P2 Cross-recommendation ledger.** Opt-in, tourist-fit matching, scripted rotation, no
  cash, champion mediates. Scripted demo.
- **P2 Google review bridge.** Neutral link offered to every visitor. Scripted demo.

## 6. AI components ("why not a spreadsheet")

1. Speech recognition in a low-resource language (no spreadsheet hears).
2. Machine translation (Gambian language to English; English to German/Dutch).
3. Speech synthesis in the visitor's language.
4. Intent matching of free-form visitor questions to library answers.
5. Round-trip translation consistency check (hallucination guard).

Models **[OPEN: confirm each]**: ASR — ElevenLabs Scribe if the language is supported,
else Meta MMS; MT — NLLB-200 distilled; TTS — ElevenLabs for English/German/Dutch;
intent — small multilingual sentence-embedding model + nearest-neighbor with a threshold.

## 7. Data layer (cite source, year, country; state the gaps)

| Dataset | Job | License | Gap to state |
|---|---|---|---|
| UN Tourism statistics | Problem evidence (arrivals, receipts) | **[OPEN: check]** | Annual granularity |
| WDI tourism series | Second source, tourism vs GDP/jobs | World Bank | Annual |
| Enterprise Surveys | Small-firm constraints | World Bank | **[OPEN: Gambia coverage]** |
| FLORES-200 / NLLB-200 | Translation + evaluation | Open | Low-resource quality varies |
| Common Voice / MMS / FLEURS | ASR baseline / benchmark | CC0 / mixed | Few hours of the language |
| MASSIVE | Intent templates | **[OPEN: check]** | No Gambian-language intents |
| Yelp Open Dataset | Question/theme categories only | Academic — **[OPEN: check]** | US-centric, no Gambian coverage |
| Wikivoyage | Tour description tone | CC BY-SA | Pageviews are a proxy |
| OpenStreetMap | Findability diagnostic | ODbL | Sparse in rural Gambia |
| GSMA Gender Gap, Global Findex | Device and mobile money evidence | **[OPEN: pull Gambia]** | Regional |

No TripAdvisor scraping. Real Gambian visitor reviews: **[OPEN: search once network is
open; if none are usable, synthetic reviews are used ONLY with user approval and labeled
synthetic everywhere]**.

## 8. Stated limits (go in the video)

- Demo assumes a relatively quiet recording environment.
- The Gambian-language translation is unverified by a native reviewer.
- Parts of the demo may be simulated (WhatsApp, SMS) and will be labeled as such.
- Library answers cover standard questions only; novel questions wait for the next sync.

## 9. Priorities for the weekend

- **P0:** record, transfer, weekly sync, round-trip check, review screen, answer library,
  visitor Q&A with intent matching, honest fallbacks, evaluation (FLORES translation score,
  intent accuracy).
- **P1:** voice output, real SMS/WhatsApp, weekly digest, polished UI (Lovable), video.
- **P2:** pricing range, ledger, Google bridge, voice cloning.

## 10. Open items

- Which Gambian language (Wolof vs Mandinka) — decided after support test.
- Sandbox network access (HuggingFace, ElevenLabs, World Bank, Kaggle) and
  `ELEVENLABS_API_KEY` as an environment secret.
- Real review data vs approved synthetic data.
- Verified evidence figures for the one-liner.
