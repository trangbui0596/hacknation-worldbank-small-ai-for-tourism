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

## Script (target 4 minutes 15 seconds; limit 5:00)

**0:00 The problem (20 s).** "Meet Noor, a fictional tour operator in The Gambia. She knows her tours. Visitors write in English, German or Dutch. She speaks Wolof and has a basic phone. About half of Gambians are not online. [Show the evidence table.]"

**0:20 Why AI, not just SMS (25 s).** "Teranga is Wolof for hospitality. Plain SMS cannot do three things Noor needs. It cannot hear Wolof. It cannot translate her words and check the meaning survived. It cannot speak an answer in a visitor's language. Teranga does all three, and it never makes up an answer." [On screen: the three icons or the 'What the AI does that plain SMS cannot' section of the live page.]

**0:45 Scene 1, the call (35 s).** Runbook scene 1. "No internet needed. A simple phone call. Speech recognition turns her Wolof into text." Say that the clips are synthetic and the summary arrives on WhatsApp because SMS registration is in review.

**1:20 Scene 2, the family helper (50 s).** Runbook scene 2. "A family member reviews on WhatsApp. She sees Wolof, not English: the transcript, and the numbers the AI heard, here about 1500 dalasi, so she can confirm a price without reading English. She approves. Nothing reaches a visitor without her approval."

**2:10 Scene 3, the visitor (45 s).** Runbook scene 3. "A visitor asks in English or German and gets the approved answer as text and an AI voice, labeled machine-translated. If it is not sure, it says Noor will answer. It never guesses. Matching here is plain rules, on purpose."

**2:55 Scene 4, one-tap Google review (25 s).** Runbook scene 4. "After the tour the visitor speaks their review. The AI writes it down as clean text without changing a fact or the feeling. They tap the same link everyone gets, paste, and choose their own stars. We never post for them, and there is no review gating."

**3:20 Scene 5, cross-community recommendation (20 s).** Runbook scene 5. "A visitor can opt in to a suggestion for another tour. It rotates fairly between partner operators, no money, no number shared, and a person passes on the contact. The partners here are fictional and this part is simulated."

**3:40 Scene 6, coaching (20 s).** Runbook scene 6. "From real public Google Maps reviews, a small sample, Noor gets plain advice in Wolof. If there is not enough data, it says so."

**4:00 Limits and what is next (20 s).** Read the limits from the runbook section 8 plainly: synthetic audio, unverified Wolof, SMS pending registration, simulated parts labeled. "Next: a native Wolof speaker to test recognition and wording, and real partner operators."

## Model and data notes for the submission text

- Speech to text and text to speech: ElevenLabs (Scribe for Wolof; voice for English, German, Dutch). Translation and coaching summaries: Lovable AI. Matching: keyword rules (no AI).
- Messaging: Twilio (WhatsApp sandbox, voice calls; SMS pending A2P registration). Backend: Lovable Cloud.
- Reviews: Google Maps Places data, a few reviews per place, no raw review text stored.
- The 20-question matching test is agent-written test data, tuned on its misses; not real-visitor accuracy.
