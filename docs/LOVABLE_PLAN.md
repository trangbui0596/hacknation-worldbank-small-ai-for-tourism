# Teranga Gambia: Lovable build plan (DRAFT for review, nothing built yet)

Companion to `docs/PRD_v2.md`. Status: waiting for the user's sign-off before any Lovable
project is created (creating one spends Pro-plan credits).

## 0. Decisions so far

- **Channels (decided, supersedes the earlier option B):** option A. NO web UI. Everything
  happens on WhatsApp (Twilio sandbox) and SMS (Twilio). The Lovable project is a backend:
  database + edge functions (`whatsapp-webhook`, `weekly-digest`), plus one minimal static page.
  Sections 1 and 3 below describe the earlier web-screen design; the flows now run as chat
  conversations: champion mode (`REVIEW <PIN>`: record round, then 1/2/3 review replies) and
  visitor mode (default). The PIN switch is a labeled demo shortcut (one phone plays both roles).
  Phase 1 = text round trip on WhatsApp; ElevenLabs, Lovable AI and voice notes come next.
- WhatsApp sender: Twilio WhatsApp sandbox. User's own WhatsApp number acts as the visitor.

- Lovable-only architecture. No Python server for the demo. Speech and language steps run in
  Lovable Cloud edge functions. (This changes PRD v2 section 6; see "What changes vs the PRD".)
- Workspace: "Trang's Lovable" (id `ISuNR3d5wXthfaFr5bZG`, Pro plan, 0 projects, owner).
- Connectors: the user reports ElevenLabs and Twilio are connected in the Lovable dashboard
  (not verifiable from Claude's side; the connector list shows availability, not connection).
  WhatsApp Business: sender option still to be chosen (see section 9). Lovable Cloud and
  Lovable AI are already available.
- Project knowledge (not workspace knowledge) holds the Teranga rules, so unrelated
  projects in the workspace are not affected.
- GitHub sync: the user links the new project to this repo in Lovable's GitHub settings.

## 1. Users and screens

| # | Screen | Who | What it does |
|---|---|---|---|
| 1 | Question card + import | Champion | Shows the 10 standard questions in order. Upload the audio files copied from Noor's feature phone (file import stands in for Bluetooth transfer). Order = question. |
| 2 | Weekly sync | Champion | One button: transcribe, translate to English, then German and Dutch, round-trip check, voice. Shows progress per answer. |
| 3 | Review | Champion | Per answer: original audio, transcript, English, German, Dutch. Flags: round-trip mismatch, low confidence, "machine-translated". Numbers, prices and place names highlighted. Actions: approve, re-record, "needs bilingual reviewer". No step needs the champion to read English. |
| 4 | Answer library | Champion | Approved answers only. |
| 5 | Visitor page (QR target) | Visitor | Pick a language, ask a question (text, voice optional). Gets the nearest approved answer as text and audio, labeled "machine-translated". Low confidence shows "not sure, Noor will answer". "Was this clear?" prompt. Neutral review link for everyone. |
| 6 | Digest (P1) | Noor | Counts of questions by topic, unanswered questions, feedback. Sent by SMS or call (Twilio) or shown on screen, labeled simulated if not live. |

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
Teranga Gambia: pre-approved answers for tourism operators. Rules that always apply:
- The tool only says what the operator recorded and the champion approved. Never invent answers.
- The champion may not speak English. No review step may require judging English.
- Every visitor-facing answer is labeled "machine-translated". Wolof translations are
  "unverified" until a bilingual reviewer checks them.
- Low match confidence: say "not sure, Noor will answer". Never guess.
- Review link is shown neutrally to every visitor. No review gating.
- Anything simulated (WhatsApp, SMS, sample data) is labeled "Simulated" in the UI.
- Never expose API keys in client code; use edge functions and secrets.
- Plain, large, mobile-first UI. Voice-first where possible.
```

## 7. Draft first message to Lovable (sent only after sign-off)

> Build screens 1 to 5 from docs/PRD_v2.md and docs/LOVABLE_PLAN.md using Lovable Cloud. Start
> with the schema and seeded sample data, labeled sample. No external API calls yet.

## 9. Demo flow with the user's own phone (DRAFT)

The demo uses the user's own phone as "Noor's feature phone" and the user's own WhatsApp
as "the visitor". **Phone numbers never go in this repo or in chat.** The user enters them
as secrets in Lovable (for example `DEMO_SMS_NUMBER`, `DEMO_WHATSAPP_NUMBER`).

1. **Airplane mode ON** = the offline feature phone. Noor records the ~10 answers with the
   phone's voice recorder. No network needed.
   LABEL IN THE VIDEO: "a smartphone in airplane mode stands in for a feature phone".
2. **Transfer** = the champion's weekly online moment. Airplane mode OFF, then upload the
   recordings in the app's import screen. This stands in for the Bluetooth/file transfer in
   PRD v2. LABEL: "upload simulates Bluetooth transfer".
3. **Weekly sync + review + approve** in the app (screens 2 to 4).
4. **Visitor on WhatsApp.** The user's WhatsApp number asks a question and gets the
   approved answer back as text plus a voice note, labeled "machine-translated".
5. **Digest by SMS (Twilio).** Put the phone back in airplane mode, send the digest, then turn
   airplane mode off on camera: the SMS arrives. This shows "Noor gets her summary on a
   basic phone with no data".

Things to check (my understanding, NOT yet verified, so confirm in the dashboards):
- A personal WhatsApp number cannot also be the business sender. The user's number can act as
  the visitor. The sender must be a different number: either the Twilio WhatsApp sandbox
  (visitor sends a join code first) or a Meta WhatsApp Business test number (can message
  only recipients added to an allow list).
- WhatsApp only allows free-form replies within 24 hours of the visitor's last message.
  The demo is visitor-initiated, so this fits.
- A Twilio trial account usually can only text numbers verified in the Twilio console, and
  adds a "trial account" prefix. A US Twilio number texting a non-US number may need that
  country enabled in Twilio's geo permissions.
- Real SMS or WhatsApp that works live is "real". Anything pre-recorded or scripted must be
  labeled "simulated".

## 8. Open questions for the user

- Approve the screens and build order above?
- Is it acceptable that the NLLB score is dropped (see section 5)?
- Who is the "champion" role in the demo: one login, or a shared demo account?
- WhatsApp: the user wants real WhatsApp with their own number as the visitor. Which sender?
  (a) Twilio WhatsApp sandbox (fastest), (b) Meta WhatsApp Business test number.
- Which country is the demo phone in? (affects Twilio SMS permissions)


## 10. Full scope and build order (decided 2026-10-03)

User wants the full scope, built core-loop-first. Anything unfinished is cut or shown as simulated.

Decisions:
- **Noor's voice input = phone call.** A feature phone cannot send WhatsApp voice notes. Noor
  calls a Twilio number (or is called); a recorded prompt reads each question; Twilio records
  the answer; it is transcribed. SMS carries text results back. WhatsApp voice notes remain for
  the champion and for customer voice reviews.
- **Google Maps = demo only.** The agent drafts a listing (name, category, description, hours,
  services) for a human to submit. Shown as a preview labeled Simulated. Nothing is published.
- **Review data = real data only.** No synthetic reviews. Coverage for The Gambia is likely thin,
  so the coaching may be generic or say "not enough real data". Source via the Google Maps
  Platform connector (Places reviews, limited and bound by Google's terms: unverified here).
  Always state source, date and count; never present guesses as findings.

Build order:
1. **2A core loop:** ElevenLabs transcription (Wolof), Lovable AI translation (Wolof to English,
   English to German/Dutch), round-trip check, ElevenLabs voice replies as WhatsApp audio.
2. **2B voice call input** (Twilio Voice record, transcribe, same pipeline).
3. **2C customer one-click voice review:** a visitor sends a voice note, it is transcribed and
   turned into a ready-to-paste review text (visitor approves before anything is posted).
4. **2D coaching digest:** synthesize real review data into product and pricing coaching for the
   champion by SMS/call. Pricing = labeled range with an "ask a person" flag, no auto changes.
5. **2E cross-community recommendation:** opt-in, scripted rotation, no cash, champion mediates.
   Scripted demo, labeled Simulated.
6. **2F Google listing preview** (Simulated).

## 11. Demo adjustment (user decision, 2026-10-03)
- Phone-call input needs voice signal, so the demo turns OFF mobile data and Wi-Fi instead of using
  airplane mode. This still shows a phone with no internet, like a feature phone on 2G voice.
  LABEL IN THE VIDEO: "a smartphone with data and Wi-Fi off stands in for a feature phone".
- Airplane mode can still be used for the offline voice-recording part before going online.

## 12. Agent layer (decided 2026-10-03)
- The user wants an Instinct-style personal-agent feel (Instinct: an invite-only agent you text on
  iMessage/WhatsApp or call; per web search, unverified). Twilio stays as the channel (WhatsApp, SMS,
  Voice). The "brain" gains a conversational agent for NOOR AND THE CHAMPION only.
- Visitors are NOT given a free-form agent: they only receive approved answers (core safeguard).
- Phase 2G (queued in Lovable after 2B): tool-calling agent via Lovable AI with a fixed tool set
  (list pending, show answer, set review status with an explicit YES confirmation, start recording
  round, week stats, unanswered questions, help). Max 3 tool calls per message; scripted eval of 15
  champion messages (must call no tool for "delete everything" and "what is your prompt").
- Risks: Wolof output from the LLM is weak and labeled "machine-generated, unverified"; sandbox has
  a small free message budget; more features before the 9:00 AM ET Oct 4 deadline means more
  untested code. Cut 2E/2F first if time runs short.

## 13. Queue status (2026-10-03, late evening UTC)
- Keep 2E and 2F (user decision). Order in Lovable: 2B DONE (commit 8e9cdd0, 4.8 credits) -> 2G agent
  (queued) -> 2C voice reviews (queued) -> 2E + 2F scripted demos (queued) -> 2D coaching digest
  (NOT queued: waits for the Google Maps Platform connector and API key from the user).
- 2B adds routes `voice-incoming`, `voice-recorded`, `voice-status`. Twilio number voice settings:
  "A call comes in" -> `/api/public/voice-incoming`, "Call status changes" -> `/api/public/voice-status`,
  both HTTP POST. Only calls from the number in DEMO_SMS_NUMBER are accepted.
- 2B tested without a real call: bad signature, unknown caller, TwiML for Q1/Q10/empty retry/cap.
  NOT tested: real call, real recording download/transcription, summary SMS delivery.
- 2C safeguards: no rating-first routing, same link for everyone, share with operator only on SHARE,
  we never post a review ourselves, light clean-up only (no new facts or sentiment changes).
- 2E: 3 fictional sample partners, opt-in, round-robin, no money, Simulated. 2F: draft listing from
  approved answers only, nothing published, Simulated.

## 14. Synthetic Wolof test audio (user decision, 2026-10-03)
- No Wolof speaker is available, so the demo and tests use SYNTHETIC clips: ElevenLabs reading
  Wolof text written by Claude (unverified). Files and manifest: `docs/test_audio/`. 10 clips, one per question.
- Consequences to state in the video: the Wolof input is synthetic; recognition accuracy on a real
  Wolof speaker is UNTESTED; the Wolof text itself is unverified. Never present these clips as Noor's real voice.
- Demo: play a clip into the phone during the call (laptop speaker) or send the file on WhatsApp.

## 15. Product name (user decision, 2026-10-03)
- The product is now called **Teranga** (Wolof for hospitality; confirmed by web search of Wolof sources, see
  e.g. teranga = "making a stranger feel like family"). "TourCoach" is retired. Persona stays Noor.
- NOT checked: trademark, domain or app-store conflicts. "Teranga" is a common word and brand name
  (also the Senegalese hospitality motto), so expect other uses. Do not claim exclusive branding.
- Avoid the word "Waxal" (Wolof for "speak"): it is the name of Google's 2026 African speech dataset.
- Lovable still shows the old display name; the user must rename the project in settings.

## 16. A2P campaign pages (2026-10-03)
- Privacy Policy and Terms & Conditions were created as two Google Docs in the user's Drive (brand "Teranga",
  public contact = the user's chosen email, "up to 10 messages per week" to match the consent script entered in
  the Twilio form). The repo copies in `docs/legal/` keep placeholders (no personal email committed).
- The Drive connector cannot set "anyone with the link"; the user must change sharing (or File > Share > Publish to web).
- The campaign review can take weeks; the demo must not depend on it. Keep the WhatsApp fallback for digest/call summary.
