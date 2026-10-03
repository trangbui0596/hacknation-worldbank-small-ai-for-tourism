# TourCoach Gambia: Lovable build plan (DRAFT for review, nothing built yet)

Companion to `docs/PRD_v2.md`. Status: waiting for the user's sign-off before any Lovable
project is created (creating one spends Pro-plan credits).

## 0. Decisions so far

- Lovable-only architecture. No Python server for the demo. Speech and language steps run in
  Lovable Cloud edge functions. (This changes PRD v2 section 6; see "What changes vs the PRD".)
- Workspace: "Trang's Lovable" (id `ISuNR3d5wXthfaFr5bZG`, Pro plan, 0 projects, owner).
- Connectors to add in the Lovable dashboard (by the user, not Claude): ElevenLabs,
  WhatsApp Business, Twilio. Lovable Cloud and Lovable AI are already available.
- Project knowledge (not workspace knowledge) holds the TourCoach rules, so unrelated
  projects in the workspace are not affected.
- GitHub sync: the user links the new project to this repo in Lovable's GitHub settings.

## 1. Users and screens

| # | Screen | Who | What it does |
|---|---|---|---|
| 1 | Question card + import | Champion | Shows the 10 standard questions in order. Upload the audio files copied from Fatou's feature phone (file import stands in for Bluetooth transfer). Order = question. |
| 2 | Weekly sync | Champion | One button: transcribe, translate to English, then German and Dutch, round-trip check, voice. Shows progress per answer. |
| 3 | Review | Champion | Per answer: original audio, transcript, English, German, Dutch. Flags: round-trip mismatch, low confidence, "machine-translated". Numbers, prices and place names highlighted. Actions: approve, re-record, "needs bilingual reviewer". No step needs the champion to read English. |
| 4 | Answer library | Champion | Approved answers only. |
| 5 | Visitor page (QR target) | Visitor | Pick a language, ask a question (text, voice optional). Gets the nearest approved answer as text and audio, labeled "machine-translated". Low confidence shows "not sure, Fatou will answer". "Was this clear?" prompt. Neutral review link for everyone. |
| 6 | Digest (P1) | Fatou | Counts of questions by topic, unanswered questions, feedback. Sent by SMS or call (Twilio) or shown on screen, labeled simulated if not live. |

## 2. Data model (Lovable Cloud / Postgres)

- `questions` (id, position, text_en, topic): the fixed 10-question card.
- `recordings` (id, question_id, audio_path, week, status)
- `answers` (id, recording_id, transcript_src, english, german, dutch, roundtrip_score,
  flags[], review_status {pending, approved, rerecord, needs_bilingual}, approved_by, approved_at)
- `answer_audio` (answer_id, lang, audio_path)
- `visitor_questions` (id, text, lang, matched_answer_id, confidence, was_clear, created_at)
- `unanswered` (id, visitor_question_id, added_to_round_week)

Row-level security: the champion role writes; visitors only read `answers` where
`review_status = approved`. Visitor feedback is shared with the operator only after opt-in.
Recordings are deletable on request.

## 3. Edge functions

1. `transcribe`: ElevenLabs Speech to Text, `scribe_v2`, `language_code=wol` (verified accepted
   by the API; accuracy on real Wolof audio is NOT yet tested).
2. `translate`: Lovable AI. Wolof to English, then English to German and Dutch.
3. `roundtrip`: translate English back to Wolof, compare with the transcript, store a score,
   flag low scores. Unverified until a bilingual reviewer checks (an LLM's Wolof is weak).
4. `speak`: ElevenLabs Text to Speech (`eleven_v3` / `eleven_multilingual_v2`), neutral stock
   voice by default. Voice cloning stays optional and consent-gated (P2).
5. `match`: visitor question to nearest approved answer (embedding or LLM ranking with a
   confidence threshold). Below threshold returns the honest fallback, never a guess.
6. `digest` (P1) and `whatsapp-webhook` (P1, Twilio/WhatsApp), labeled simulated until live.

## 4. Build order (P0 first)

1. Schema + screens 1, 3, 4 with seeded sample data (clearly labeled sample).
2. `transcribe` + `translate` + `roundtrip` wired into screen 2.
3. `match` + visitor page (screen 5) with honest fallbacks.
4. `speak` for voice output.
5. Evaluation page: intent accuracy on a small hand-labeled set; translation quality note.
6. P1: WhatsApp/SMS, digest, polish, video.

## 5. What changes vs the PRD

- Translation model is Lovable AI, not NLLB-200. Consequence: we cannot report the FLORES-200
  NLLB score. We can still run a small FLORES Wolof-English check against the LLM if the
  Hugging Face block is lifted (the `.tsv` text files are small and already reachable).
- No local MMS fallback for speech recognition. If Scribe is poor on Wolof, the demo says so.
- PRD v2 should be updated once this plan is approved (sections 3, 6, 9).

## 6. Draft project knowledge (to paste into the Lovable project)

```
TourCoach Gambia: pre-approved answers for tour operators. Rules that always apply:
- The tool only says what the operator recorded and the champion approved. Never invent answers.
- The champion may not speak English. No review step may require judging English.
- Every visitor-facing answer is labeled "machine-translated". Wolof translations are
  "unverified" until a bilingual reviewer checks them.
- Low match confidence: say "not sure, Fatou will answer". Never guess.
- Review link is shown neutrally to every visitor. No review gating.
- Anything simulated (WhatsApp, SMS, sample data) is labeled "Simulated" in the UI.
- Never expose API keys in client code; use edge functions and secrets.
- Plain, large, mobile-first UI. Voice-first where possible.
```

## 7. Draft first message to Lovable (sent only after sign-off)

> Build screens 1 to 5 from docs/PRD_v2.md and docs/LOVABLE_PLAN.md using Lovable Cloud. Start
> with the schema and seeded sample data, labeled sample. No external API calls yet.

## 8. Open questions for the user

- Approve the screens and build order above?
- Is it acceptable that the NLLB score is dropped (see section 5)?
- Who is the "champion" role in the demo: one login, or a shared demo account?
- Do you have a Meta business account for WhatsApp, or should WhatsApp be simulated?
