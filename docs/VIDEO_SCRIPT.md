# Teranga video script (target 3 to 4 minutes; limit 5)

Track: World Bank x Hack-Nation "Small AI for Development", Tourism.
Companion: `docs/DEMO_RUNBOOK.md` (exact steps and what to click). Persona Noor is fictional. All Wolof test audio is synthetic.

## Evidence (verified 2026-10-04 from the World Bank WDI API, country GMB)

| Fact | Value | Year | WDI indicator |
|---|---|---|---|
| Individuals using the Internet | 49.5% of population | 2024 | IT.NET.USER.ZS |
| Mobile cellular subscriptions | 126 per 100 people | 2024 | IT.CEL.SETS.P2 |
| International tourism receipts | US$53 million, 30.2% of exports | 2020 (latest value in the series; a COVID year) | ST.INT.RCPT.CD, ST.INT.RCPT.XP.ZS |
| International tourism arrivals | 246,000 | 2020 (latest value in the series; a COVID year) | ST.INT.ARVL |

What this shows: tourism matters to the economy, and about half the population is not online while mobile phones are everywhere. It does NOT show that operators lose enquiries or that Teranga fixes it. Say "the gap we target", not "proof".
Not yet sourced (do not state as fact): language barriers, share of operators with a smartphone, lost enquiries, translation quality for Wolof.

## Required one-liner (use this wording on screen and aloud)

"Because of this tool, a Gambian tour operator will be able to answer visitors in English, German and Dutch with her own pre-approved words instead of missing enquiries she cannot read or reply to. The need: about half of Gambians were not online in 2024 (49.5%, World Bank), while tourism brought in 30% of exports in 2020. This is the gap we target, not a measured result."

## Script

**0:00 The problem (20 s).** "Meet Noor, a fictional tour operator in The Gambia. She knows her tours. Visitors write in English, German or Dutch. She speaks Wolof and has a basic phone. About half of Gambians are not online. [Show the evidence table.]"

**0:20 The idea (15 s).** "Teranga is Wolof for hospitality. Noor records her answers once, by phone call, in her own language. Visitors then get her own pre-approved answers in their language, on WhatsApp. It never makes up an answer."

**0:35 Scene 1, the call (40 s).** Follow runbook scene 1. Say: "No internet needed. A simple phone call." Say that the clips are synthetic and the summary arrives on WhatsApp because SMS registration is in review.

**1:15 Scene 2, the family helper (60 s).** Runbook scene 2. "A family member reviews on WhatsApp. She sees Wolof, not English: the transcript, the numbers it heard, and flags. She approves or asks for a re-record. Nothing reaches a visitor without her approval."

**2:15 Scene 3, the visitor (50 s).** Runbook scene 3. "A visitor asks in English or German and gets the approved answer as text and an AI voice, labeled machine-translated. If it is not sure, it says Noor will answer. It never guesses."

**3:05 Scene 4, coaching (25 s).** Runbook scene 4. "From real public Google Maps reviews, a small sample, Noor gets plain advice in Wolof. If there is not enough data, it says so."

**3:30 Limits and what is next (25 s).** Read the limits from the runbook section 6 plainly: synthetic audio, unverified Wolof, SMS pending registration, simulated parts labeled. "Next: a native Wolof speaker to test recognition and wording, and other languages."

## Model and data notes for the submission text

- Speech to text and text to speech: ElevenLabs (Scribe for Wolof; voice for English, German, Dutch). Translation and coaching summaries: Lovable AI. Matching: keyword rules (no AI).
- Messaging: Twilio (WhatsApp sandbox, voice calls; SMS pending A2P registration). Backend: Lovable Cloud.
- Reviews: Google Maps Places data, a few reviews per place, no raw review text stored.
- The 20-question matching test is agent-written test data, tuned on its misses; not real-visitor accuracy.
