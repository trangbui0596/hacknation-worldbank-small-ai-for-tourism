# Teranga video script

**Submission cut: 59.4 s (limit 60 s). The long-form 3 to 4 minute script further down is kept as a reference for a longer cut.**
Track: World Bank x Hack-Nation "Small AI for Development", Tourism. Companion: `docs/DEMO_RUNBOOK.md` (exact steps for filming the clips) and `docs/VIDEO_PRODUCTION.md` (how the cut is built).
Persona Noor is fictional. All Wolof test audio is synthetic. All paper-collage art is AI-generated.

## Current 60-second cut

Style: layered paper-collage storybook, one idea per screen, one short caption at a time with the key word highlighted. Screen recordings are filmed on WhatsApp and mirror the SMS commands (footer: "Shown on WhatsApp, same commands by SMS").

| Time | Visual | Narration (verbatim) |
| --- | --- | --- |
| 0:00-0:08 | Three paper pages tear in: tourist writing "Guten Tag!", Noor with an unread message, the unread phone; then a stamp bridge and the Teranga logo card (evidence strip: US$157M tourism receipts 2019, about half of Gambians offline, World Bank WDI) | "A tourist writes in German. Noor speaks Wolof. The message goes unread." |
| 0:08-0:30 | **1 Noor.** Card of AI-suggested questions (price, meeting point, duration, what is included, how to book, cancellation); she answers by voice; tags "SMS + voice, no internet" then "WhatsApp, weekly sync only"; approval with one digit; Google listing drafted; **AI COACHING** card: latest reviews + tourist questions, AI analyses the data, Wolof SMS tips to improve her service | "AI suggests questions about her business. Noor answers each by voice. It all runs on SMS, offline. WhatsApp is only a weekly sync. She approves each answer with one digit. Nothing goes out without her. Teranga drafts her Google listing. Each week, AI analyses fresh reviews and questions, then coaches Noor by SMS, in Wolof." |
| 0:30-0:42 | **2 The tourist.** Question in her own language, the approved answer as text and an AI voice note (labelled), a voice review cleaned up, she pastes it into Google herself | "The tourist asks. Teranga answers in Noor's words." (voice note: "The price is fifteen hundred dalasi per adult.") "Later she speaks a review. Teranga cleans it up, and she posts it herself." |
| 0:42-0:55 | **3 The community.** One flood notice to the community, shown under every answer, a neighbour suggested | "One flood notice reaches the whole community. Every tourist sees it under their next answer. A visitor wants something else? A neighbour is suggested, and a person connects them." |
| 0:55-1:00 | Logo, closing line, links, stamp bridge joining tourist and Noor | "Teranga gives Noor her voice, and her community its champion." |

Claim check for the cut (checked against the code on 2026-10-04; updated after the AI question-card step was built):
- **"AI suggests questions about her business":** true once the step in `docs/` NEXT_STEPS update 21 is live. The 10 starting cards are fixed. Each week the AI reads the questions visitors asked that Teranga could not answer and proposes up to three new cards; code checks every claim against the visitors' own words and counts the visitors (at least two); the household champion approves with `IDEA 1` on WhatsApp (`IDEAS` lists them, `IDEA NO 1` skips). If the database table is not migrated or the AI is down there are no suggestions and nothing else changes. To show it on camera, film `IDEAS` after at least two unclear tourist questions on the same topic (for example wheelchair access), then `IDEA 1`.
- **"AI analyses fresh reviews … then coaches Noor":** true. The AI labels each review's themes and prices; code verifies prices against the review text, counts themes and writes up to three actions from fixed templates; the Wolof text is machine-written and unverified. Latest run: 70 public reviews from 15 operators (2019 to 2026). Nothing raw is stored.
- "Fresh": the weekly sync re-reads a small public sample of reviews; it is fresh, not real time. Do not say real time.
- "Approves each answer with one digit": true; the REVIEW flow shows the Wolof transcript and the numbers, and nothing reaches a visitor before approval.
- "A person connects them": true; referrals are suggestions, the partner list is simulated, and no payment or number sharing is claimed in the video.
- "It all runs on SMS, offline. WhatsApp is only a weekly sync": true for Noor and the community champion. Visitors use WhatsApp for real (the tourist segment shows it), so say "for Noor".
- The footer states that Wolof audio is synthetic and Noor is fictional; Wolof wording is unverified by a native speaker (README, "Honest limits").

---

# Long-form script (earlier plan, target 3 to 4 minutes; limit 5)

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

"Because of Teranga, a Gambian tourism operator will turn one phone call in Wolof into answers tourists can read in English, German or Dutch, without internet. Her Google listing is drafted from those answers, and tourists can leave a review by voice. Each week she learns what tourists ask, and her community looks out for one another with shared notices and referrals. Without it, she misses or answers late the enquiries she can't read. We know because the World Bank figures above show how much tourism earns and how many Gambians are still offline. This is the gap we target, not a measured result."

## Script (full cut about 4 minutes 50 seconds; limit 5:00)

**0:00 The problem (20 s).** "Meet Noor, a fictional tourism operator in The Gambia. She knows her tours. Visitors write in English, German or Dutch. She speaks Wolof and has a basic phone. Tourism earned The Gambia US$157 million in 2019, and about half of Gambians are still not online. [Show the numbers on the live page; every one links to the World Bank.]"

**0:20 Why AI, not just SMS (20 s).** "Teranga is Wolof for hospitality. Plain SMS cannot hear Wolof, cannot translate and check the meaning, and cannot speak an answer in a visitor's language. Teranga does all three, and Noor never needs the internet: she records by phone call and keeps what she needs as text messages." [On screen: the 'Works offline' and 'AI beyond SMS' tabs.]

**0:40 Scene 1, the call (30 s).** Runbook scene 1. "A simple phone call. Speech recognition turns her Wolof into text." Say that the clips are synthetic and the summary arrives on WhatsApp because SMS registration is in review.

**Say this once, early (scene 2), word for word:** "Everything for Noor, her household champion and the community champion is built for SMS, so it works with no internet. US carrier registration for SMS is still in review, so in this demo we run the same commands on WhatsApp, which mirrors them. Tourists use WhatsApp for real, because they have data and it carries voice."

**1:10 Scene 2, Noor approves her answers (40 s).** Runbook scene 2. State the roles first: "Noor records by phone call and approves her own answers by text, visitors use WhatsApp." "She sees Wolof, not English: the transcript and the numbers the AI heard, here about 1500 dalasi, so she can confirm a price without reading English. One digit approves it. Nothing reaches a visitor without her approval."

**1:50 Scene 3, the visitor (35 s).** Runbook scene 3. "A tourist sends a voice note in English or German; speech recognition hears the language and the question, and she gets the approved answer as text and an AI voice, labeled machine-translated. If it is not sure, it says Noor will answer. Matching is plain rules, on purpose, and we tested it on real questions from Gambian operators' FAQ pages. [Quote the measured numbers from the What's real tab.]"

**2:25 Scene 4, the Google listing (20 s).** Runbook scene 4. "From her approved answers Teranga builds a Google listing draft: description, services, meeting point, how to book. It shows what is missing and which question to record next. It never invents a phone number or hours, and it sends nothing to Google: a person publishes it."

**2:45 Scene 5, one-tap Google review (20 s).** Runbook scene 5. "After the tour the visitor speaks their review. The AI writes it down without changing a fact or the feeling. They tap the same link everyone gets, paste, and choose their own stars. We never post for them, and there is no review gating."

**3:05 Scene 6, the community champion (40 s).** Runbook scene 6. "Every operator has a household champion. A community has one too. When a road floods, the community champion sends one notice: members get an SMS in Wolof, visitors see it under every answer in their language, fixed wording, never machine-translated in an emergency, always labeled a community notice, not an official warning. And when a household champion is unsure about a translation, a bilingual person in the community checks it." [One sourced line: almost a fifth of the country's land is less than 5 metres above sea level, World Bank, 2015.]

**3:45 Scene 7, no internet needed (20 s).** Runbook scene 7. "Noor texts COACH from her phone and gets her coaching as a plain message she can keep all week. Today the text arrives on WhatsApp because US carrier registration is still in review. Say so."

**4:05 Scene 8, coaching (20 s).** Runbook scene 8. "From real public Google Maps reviews, a small sample, Noor gets plain advice in Wolof. If there is not enough data, it says so."

**4:25 Limits and what is next (25 s).** Read the limits from the runbook section 10 plainly: synthetic audio, unverified Wolof, SMS pending registration, simulated parts labeled, features not yet tried by real users. "Next: a native Wolof speaker to test recognition and wording, real partner operators, and community champions in real circles."

**Short cut (about 3 minutes 30 seconds):** problem, why AI, scene 1, scene 2, scene 3, scene 6, limits.

## Model and data notes for the submission text

- Speech to text and text to speech: ElevenLabs (Scribe for Wolof; voice for English, German, Dutch). Translation and coaching summaries: Lovable AI. Matching: keyword rules (no AI).
- Messaging: Twilio (WhatsApp sandbox, voice calls; SMS pending A2P registration). Backend: Lovable Cloud.
- Reviews: Google Maps Places data, a few reviews per place, no raw review text stored.
- The 20-question matching test is agent-written test data, tuned on its misses; not real-visitor accuracy.
