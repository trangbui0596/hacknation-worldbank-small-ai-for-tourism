# Teranga video script (target 3 to 4 minutes; limit 5)

Track: World Bank x Hack-Nation "Small AI for Development", Tourism.
Companion: `docs/DEMO_RUNBOOK.md` (exact steps and what to click). Persona Noor is fictional. All Wolof test audio is synthetic.

## Evidence (verified 2026-10-04 against the World Bank WDI API, country GMB; links on the live page)

| Fact | Value | Year | WDI indicator (data page: https://data.worldbank.org/indicator/CODE?locations=GM) |
|---|---|---|---|
| International tourism receipts | US$157 million | 2019 (last year before COVID) | ST.INT.RCPT.CD |
| Tourism receipts as share of exports | 43.6% | 2019 | ST.INT.RCPT.XP.ZS |
| International tourism arrivals | 620,000 | 2019 | ST.INT.ARVL |
| COVID year for comparison | US$53 million receipts, 246,000 arrivals | 2020 | ST.INT.RCPT.CD, ST.INT.ARVL |
| Individuals using the Internet | 49.5% of population | 2024 | IT.NET.USER.ZS |
| Mobile cellular subscriptions | 126 per 100 people (SIM subscriptions, not unique users) | 2024 | IT.CEL.SETS.P2 |
| Self-employed share of employment | 68.6% (ILO modeled estimate) | 2025 | SL.EMP.SELF.ZS |

All values live in `src/lib/evidence.ts` in the app repo; `node scripts/verify-evidence.mjs` re-checks them against the live API. Do not say a number that is not in that file.

What this shows: tourism is a large part of the economy, and about half the population is not online while mobile subscriptions outnumber people. It does NOT show that operators lose enquiries or that Teranga fixes it. Say "the gap we target", not "proof".
Not sourced (do not state as fact): language barriers, share of operators with a smartphone, lost enquiries, translation quality for Wolof.

## Required one-liner (use this wording on screen and aloud)

"Because of this tool, a Gambian tour operator will be able to answer visitors in English, German and Dutch with her own pre-approved words instead of missing enquiries she cannot read or reply to. The need: only 49.5% of people in The Gambia used the Internet in 2024, while tourism brought in 43.6% of exports in 2019, the last year before COVID. This is the gap we target, not a measured result."

## Script (full cut about 4 minutes 50 seconds; limit 5:00)

**0:00 The problem (20 s).** "Meet Noor, a fictional tour operator in The Gambia. She knows her tours. Visitors write in English, German or Dutch. She speaks Wolof and has a basic phone. Tourism earned The Gambia US$157 million in 2019, and about half of Gambians are still not online. [Show the numbers on the live page; every one links to the World Bank.]"

**0:20 Why AI, not just SMS (20 s).** "Teranga is Wolof for hospitality. Plain SMS cannot hear Wolof, cannot translate and check the meaning, and cannot speak an answer in a visitor's language. Teranga does all three, and Noor never needs the internet: she records by phone call and keeps what she needs as text messages." [On screen: the 'Works offline' and 'AI beyond SMS' tabs.]

**0:40 Scene 1, the call (30 s).** Runbook scene 1. "A simple phone call. Speech recognition turns her Wolof into text." Say that the clips are synthetic and the summary arrives on WhatsApp because SMS registration is in review.

**1:10 Scene 2, the household helper (40 s).** Runbook scene 2. "A family member reviews on WhatsApp. She sees Wolof, not English: the transcript and the numbers the AI heard, here about 1500 dalasi, so she can confirm a price without reading English. She approves. Nothing reaches a visitor without her approval."

**1:50 Scene 3, the visitor (35 s).** Runbook scene 3. "A visitor asks in English or German and gets the approved answer as text and an AI voice, labeled machine-translated. If it is not sure, it says Noor will answer. Matching is plain rules, on purpose, and we tested it on real questions from Gambian operators' FAQ pages. [Quote the measured numbers from the What's real tab.]"

**2:25 Scene 4, the Google listing (20 s).** Runbook scene 4. "From her approved answers Teranga builds a Google listing draft: description, services, meeting point, how to book. It shows what is missing and which question to record next. It never invents a phone number or hours, and it sends nothing to Google: a person publishes it."

**2:45 Scene 5, one-tap Google review (20 s).** Runbook scene 5. "After the tour the visitor speaks their review. The AI writes it down without changing a fact or the feeling. They tap the same link everyone gets, paste, and choose their own stars. We never post for them, and there is no review gating."

**3:05 Scene 6, the community champion (40 s).** Runbook scene 6. "Every operator has a household champion. A community has one too. When a road floods, the community champion sends one notice: members get an SMS in Wolof, visitors see it under every answer in their language, fixed wording, never machine-translated in an emergency, always labeled a community notice, not an official warning. And when a household helper is unsure about a translation, a bilingual person in the community checks it." [One sourced line: almost a fifth of the country's land is less than 5 metres above sea level, World Bank, 2015.]

**3:45 Scene 7, no internet needed (20 s).** Runbook scene 7. "Noor texts COACH from her phone and gets her coaching as a plain message she can keep all week. Today the text arrives on WhatsApp because US carrier registration is still in review. Say so."

**4:05 Scene 8, coaching (20 s).** Runbook scene 8. "From real public Google Maps reviews, a small sample, Noor gets plain advice in Wolof. If there is not enough data, it says so."

**4:25 Limits and what is next (25 s).** Read the limits from the runbook section 10 plainly: synthetic audio, unverified Wolof, SMS pending registration, simulated parts labeled, features not yet tried by real users. "Next: a native Wolof speaker to test recognition and wording, real partner operators, and community champions in real circles."

**Short cut (about 3 minutes 30 seconds):** problem, why AI, scene 1, scene 2, scene 3, scene 6, limits.

## Model and data notes for the submission text

- Speech to text and text to speech: ElevenLabs (Scribe for Wolof; voice for English, German, Dutch). Translation and coaching summaries: Lovable AI. Matching: keyword rules (no AI).
- Messaging: Twilio (WhatsApp sandbox, voice calls; SMS pending A2P registration). Backend: Lovable Cloud.
- Reviews: Google Maps Places data, a few reviews per place, no raw review text stored.
- The 20-question matching test is agent-written test data, tuned on its misses; not real-visitor accuracy.
