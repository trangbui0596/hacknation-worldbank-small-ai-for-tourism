# Next steps (handoff for a new session)

Read `docs/PRD_v2.md` first. It is the agreed spec ("record once, translate weekly").
Deadline: 9:00 AM ET, Oct 4, 2026 (prototype + 2–5 min video).

## Where we are
- PRD v2 written and pushed. No application code yet; repo is otherwise empty.
- Decisions made: Wolof as the likely demo language (pending ElevenLabs check); English is
  the pivot language, plus German and Dutch; no review gating (neutral review link for
  everyone); pricing = labeled range with an "ask a person" flag; voice cloning optional
  with recorded consent; quiet-recording assumption stated as a limit; the champion may
  NOT speak English, so no step may rely on that.
- Public model check done: NLLB-200 has Wolof (`wol_Latn`), Bambara, Fula, English, German,
  Dutch, but NOT Mandinka. MMS speech recognition has adapters for Wolof, Mandinka, Bambara
  and Fula.
- Network: HuggingFace, World Bank and Wikivoyage reachable. Kaggle and Overpass were
  blocked/flaky (add `kaggle.com` to the environment's allowed domains if needed).

## Update (new session): steps 1-2 DONE
- `ELEVENLABS_API_KEY` is visible and works (Creator tier, 130,965 characters of credit, none used).
- Speech to Text (`scribe_v1`, `scribe_v2`) ACCEPTS Wolof (`wol`). It REJECTS Mandinka (`mnk`) and Bambara (`bam`).
  Caveat: the API accepting the code does not prove good accuracy. We still need a real Wolof audio sample.
- Text to Speech covers English, German and Dutch on `eleven_v3`, `eleven_v4` and `eleven_multilingual_v2`. It has NO Wolof/Mandinka voice.
- Decision: Wolof is the demo language. Fallback ASR: Meta MMS.

## Update 2 (new session): decisions and blockers
- User decisions: Python backend + Lovable UI; test with public Wolof audio (FLEURS `wo_sn`, CC-BY-4.0); search for real Gambian review data first.
- Real Gambian review data: searched Hugging Face (queries: gambia tourism, gambia reviews, tour reviews, west africa tourism). NOTHING usable. The only hits are generic scraped TripAdvisor hotel sets, which the PRD excludes. Synthetic reviews need explicit user approval (only the P1 digest depends on them).
- BLOCKER: the environment network policy denies `us.aws.cdn.hf.co` (Hugging Face large-file CDN) with 403. Small files on huggingface.co work (e.g. `dev.tsv`), but anything large does not: FLEURS audio (dev.tar.gz is 126 MB) AND model weights (NLLB-200, MMS, sentence-embedding models). `datasets-server.huggingface.co` and `kaggle.com` are also denied.
  Fix (user): environment settings -> Network access -> Custom, add `cdn.hf.co` (and `*.hf.co` / `cas-bridge.xethub.hf.co` if the error names them), keep the default package-manager list. Then start a NEW session.
- Python deps installed OK via pip (pypi is reachable): fastapi, python-multipart, sentence-transformers, soundfile. torch and transformers are already present.

## Update 3: Lovable project created
- Architecture is now Lovable-only (see `docs/LOVABLE_PLAN.md`). The Python/NLLB plan is superseded; the HF network block matters much less.
- Lovable workspace "Trang's Lovable" (`ISuNR3d5wXthfaFr5bZG`). Project `8698e7a7-7be2-4ef9-87d0-56f82e8d381d`.
  Editor: https://lovable.dev/projects/8698e7a7-7be2-4ef9-87d0-56f82e8d381d
  Preview: https://id-preview--8698e7a7-7be2-4ef9-87d0-56f82e8d381d.lovable.app
- UPDATE: user chose option A (WhatsApp + SMS only, no web UI). Lovable was told the final scope: backend only, phase 1 = WhatsApp text round trip with a PIN-switched champion mode. User confirmed their Twilio key works. Webhook URL must be set in the Twilio WhatsApp sandbox settings by the user.
- First pass sent (now superseded): schema + screens 1-5 + seeded SAMPLE data, NO external API calls. Project knowledge (safeguards, simulated labeling) is set.
- Demo: airplane-mode phone = feature phone; user's WhatsApp = visitor via the Twilio WhatsApp sandbox; SMS digest via Twilio. Phone numbers go ONLY in Lovable secrets (DEMO_SMS_NUMBER, DEMO_WHATSAPP_NUMBER), never in chat or the repo.
- User reports ElevenLabs and Twilio are connected in Lovable (not verified by Claude). The Twilio 401 on a direct key test was still unresolved at last report.
- User still to do: link the project to this GitHub repo (Lovable project settings), verify the Twilio number for SMS, join the Twilio WhatsApp sandbox from their WhatsApp.
- Next build steps: wire `transcribe` (ElevenLabs scribe_v2, wol), `translate`/`roundtrip` (Lovable AI), `match`, `speak`; then Twilio SMS/WhatsApp; then evaluation and video.

## Update 4: Lovable phase 1 built (option A, backend only)
- Lovable commit `d6f29e2` (message umsg_01m41ssq7jexksjc6qh7zw2h5d, ~5.9 credits). NOT yet tested with real messages. Only checked: unsigned webhook calls and digest calls without the secret header get rejected.
- This Lovable stack has no edge functions; the backend is two TanStack server routes: `POST /api/public/whatsapp-webhook` and `POST /api/public/weekly-digest` (header `x-digest-secret`). Logic: `src/lib/tourcoach.server.ts` in the Lovable project. Placeholders for transcribe/translate/roundtrip/speak return null (phase 2).
- Twilio sandbox webhook (after PUBLISHING the project): `https://project--8698e7a7-7be2-4ef9-87d0-56f82e8d381d.lovable.app/api/public/whatsapp-webhook`, HTTP POST. If signature checks fail, add secret `TWILIO_WEBHOOK_URL` = that exact URL.
- Secrets the user must enter in Lovable (Project Settings -> Secrets), never in chat: `DEMO_CHAMPION_PIN`, `DEMO_SMS_NUMBER` (user's phone, receives digest), `DEMO_WHATSAPP_NUMBER` (the Twilio SANDBOX sender number, NOT the user's own), `TWILIO_AUTH_TOKEN`, `TWILIO_SMS_FROM` (Twilio SMS sender), `DIGEST_TRIGGER_SECRET`, optional `GOOGLE_REVIEW_URL`. `PHONE_HASH_SALT` is auto-generated.
- Twilio WhatsApp sandbox ("Try out WhatsApp") showed "98 free messages left" on 2026-10-03. Budget test messages; every bot reply likely counts.
- Lovable advice: enable Twilio SMS Pumping Protection and limit SMS Geo Permissions before real texts.
- Preview screenshot from `get_project` showed a generic "This page didn't load" error page; the minimal index page has not been verified.
- Phase 2 (next): wire ElevenLabs scribe_v2 (wol) transcription, Lovable AI translation + round trip, ElevenLabs TTS voice notes, then the evaluation and the video.

## Update 5: full scope decided (see docs/LOVABLE_PLAN.md section 10)
- User declined to publish yet: wants the full scope built first. Build order 2A core loop, 2B call input, 2C voice review paste, 2D coaching digest, 2E cross-community (scripted), 2F Google listing preview (simulated).
- Noor's input is a PHONE CALL to a Twilio number. Google Maps = demo only. Review data = REAL ONLY (no synthetic).

## Update 6: Lovable progress (2026-10-03 evening)
- DONE in Lovable (code, not yet tested end to end): phase 1 (commit d6f29e2), phase 2A (commit 93a6326, ~8.5 credits: ElevenLabs wol STT, Lovable AI translation + round trip, ElevenLabs TTS audio after approval, daily outbound cap `MAX_OUTBOUND_PER_DAY` default 60, `POST /api/public/eval-match`), rename of the old persona name to Noor (commit 1504d36).
- Lovable's own tests: translation kept "1500 dalasi", "9:00", "Tanji Bridge" exact; round trip 1.0; German TTS generated; keyword match 17/20 on 20 agent-written test questions (test data, not real); cap logic fixed and tested. NOT tested: real Wolof speech-to-text, Twilio media download, the full WhatsApp flow, background work after the quick reply on the published app.
- Phase 2B (phone-call input via Twilio Voice) message sent, result not yet read.
- Preview screenshot still shows "This page didn't load"; unverified. Project display name still the old auto-generated one (Lovable cannot rename it; user must rename it to Teranga in project settings).
- User still to do: enter secrets, publish, set Twilio sandbox webhook, later Twilio Voice webhook, add Google Maps Platform connector for phase 2D.

## Update 7: PUBLISHED (2026-10-03 ~22:50 UTC)
- Lovable project published at **https://teranga-gambia.lovable.app** (deployment d1711594-e248-4ef2-ab19-5488727bc274, republished after a crash fix). Earlier publish had a start-up crash: a module-scope `Response` in the WhatsApp webhook broke every route on the live host (fixed in Lovable commit c27126f; AGENTS.md now forbids it).
- NOTE: this differs from the `project--8698e7a7-....lovable.app` address that Lovable's README suggested. Use the published address above for ALL Twilio webhooks and for `TWILIO_WEBHOOK_URL`.
- Webhooks to set in Twilio (all HTTP POST): WhatsApp sandbox "When a message comes in" -> `/api/public/whatsapp-webhook`; phone number "A call comes in" -> `/api/public/voice-incoming`; "Call status changes" -> `/api/public/voice-status`. Also add secret `TWILIO_WEBHOOK_URL` = the full whatsapp-webhook URL (voice routes use its origin).
- All queued phases landed before publishing: 2G agent (b37fb87), 2C voice feedback (a6eb4ef), 2E/2F demos (96a213a), Teranga rename (6c26580), SMS templates + WhatsApp fallback (2f7f831). Claude has NOT yet read their test reports and could not test the live app (sandbox network blocks lovable.app).
- User reports the secrets are entered, Twilio number obtained, A2P campaign form in progress (policy pages on Google Docs, not yet made public by the user).
- Next: user does the Twilio webhooks, then first test: send "hello" on WhatsApp (expect "Not sure, Noor will answer." + clarity question + review line).

## Update 8: FIRST LIVE WHATSAPP REPLY WORKS (2026-10-03 ~23:30 UTC)
- Live app https://teranga-gambia.lovable.app answers WhatsApp "hello" via the Twilio sandbox (sender +14155238886; the earlier +1 737 number was an old sandbox). Fix history: module-scope Response crash (fixed), wrong DEMO_WHATSAPP_NUMBER secret (sandbox sender had changed), sandbox webhook pointed at an old address.
- Lovable states all env reads happen at request time (secrets apply without republish); not independently verified.
- Still to test live: visitor price question, champion mode (REVIEW <PIN>, START, synthetic voice clip), phone call (voice-incoming), agent chat, FEEDBACK voice review, MORE/LISTING demos, digest trigger + SMS/WhatsApp fallback.
- Sandbox free message budget: watch the "messages left" counter.

## Update 9: pipeline reliability fixes landed (2026-10-03 ~23:50 UTC)
- LIVE-VERIFIED by the user: WhatsApp visitor reply; champion START + synthetic Wolof clip -> Wolof transcript visible in REVIEW (also an English clip -> English transcript). Speech-to-text on the real clip: 200 in ~0.5 s (Lovable local run).
- Root problem fixed: background work after the response is cut off on the Workers host. Now resumable stages (received -> transcribed -> translated -> checked), request-time work (~11 s budget), `finishAnswers`, `POST /api/public/process-pending` (header x-digest-secret). Lovable commit b7f9a63. Approved-answer voice files (EN/DE/NL) now made inside the approval or visitor request (commit 04fb395, 31 tests pass, real German TTS 3.3 s locally).
- Republished at https://teranga-gambia.lovable.app after each fix.
- NOT yet verified live: approving an answer (voice files within ~10 s), a visitor getting a voice note, phone call, agent chat, FEEDBACK, MORE/LISTING demos, digest + SMS/WhatsApp fallback.
- Sandbox free messages left: 70 at 23:45 UTC. Suggested secret MAX_OUTBOUND_PER_DAY=30 for tonight.

## Update 10: matcher fix verified live; 2D coaching built (2026-10-04 ~00:45 UTC)
- LIVE-VERIFIED by the user: champion approves a real answer (reply 1) and a visitor asking "How much does it cost?" gets the real approved answer (matcher fix be10ec3: topic scoring, real preferred over sample, approval refused while untranslated).
- 2D review scanning/coaching built (commit 7329e39, ~7.2 credits): Google Places (New) via the user's Google Maps connector. One local run: 15 places, 70 reviews (2019-04 to 2026-08), top themes guide quality 56/70, wildlife 30, booking/communication 15; no price mentions found; 5 coaching actions each based on only 2 complaints out of 70 (weak evidence, labeled). No raw review text or author names stored. WhatsApp COACH only reads results cached for 24 h; fresh run = POST /api/public/coach-run with header x-digest-secret (~26 s). Nothing refreshes it on a schedule: run it before the demo. COACH / COACH MORE not yet tested on real WhatsApp; AI theme labels not hand-checked.
- Remaining live tests: phone call, digest SMS + WhatsApp fallback, voice note for visitors, agent chat, FEEDBACK, MORE/LISTING demos, COACH.

## Update 11: SMS blocked by A2P (2026-10-04 ~01:30 UTC)
- Live phone call test WORKED (voice enabled on the Twilio number). The post-call summary arrived on WhatsApp via the built-in SMS->WhatsApp fallback, because the number shows "Messaging disabled: complete A2P registration". A2P brand registration is complete; the CAMPAIGN is "In Review" (can take days to weeks). No real SMS sandbox exists for US numbers; WhatsApp sandbox is the working path. If the campaign is approved, SMS should start working with no code change.
- Demo plan: say clearly that SMS awaits carrier registration and the fallback delivered the message on WhatsApp; showing the A2P status screen is honest evidence.
- Queued in Lovable at this point: Wolof-first COACH (templates, COACH EN), call scoped to 2 questions (price pos 1, children pos 5) with slower pacing and "Got [N] of [M] answers", read-only log diagnosis of the SMS failure.

## Update 12: LOVABLE OUT OF CREDITS; known COACH bug (2026-10-04 ~01:50 UTC)
- Lovable `send_message` now fails: "workspace is out of credits" (https://lovable.dev/settings/billing). `deploy_project` still works. No more code changes are possible until credits are added (the Lovable repo is NOT linked to GitHub, so nothing can be edited here either).
- SMS root cause found: secret `TWILIO_SMS_FROM` was missing (the user had created `TWILIO_SMS_NUMBER`), so the app never called Twilio and used the WhatsApp fallback. The user then added `TWILIO_SMS_FROM` (must be UPPERCASE). Even with it, US SMS is blocked until the A2P campaign is approved (number shows "Messaging disabled").
- Published latest commit 74d9489 (deployment 1538016d): call flow now asks 2 questions (card positions 1 price and 5 children), slower pacing, summary "Got N of 2 answers"; plus Wolof-first COACH templates (commit 450399b, 71+ tests; 77 tests total).
- CORRECTION (Claude read the code, src/lib/coach.ts + coach.templates.ts): there is NO confirmed COACH actions bug. The Wolof `kañ nañu ko` = "praise it" and `ñaxtu nañu` = "complain". `actionLines` orders complaint themes first, praise second, like the first English version. Lovable's sample output showed only praise lines, probably because of the test data it used. To settle it, run COACH live once (the cached run from ~00:14 UTC is fresh for 24 h) and check that complaint items (boat/equipment, children, duration at 2 of 70) come first.
- Wolof strings are machine-translated and unverified; back-translation drift was found and corrected for 6 strings.

## Blocked on (old; resolved above)
- `ELEVENLABS_API_KEY` was saved as an environment variable but was not visible in the
  earlier session (container predates the change). A NEW session should have it. Never
  print or commit the key; read it from the environment only.

## To do, in order
1. Check `ELEVENLABS_API_KEY` is set. Then run the ElevenLabs test: list `/v1/models`
   (languages per model), check whether Speech to Text lists Wolof or Mandinka, confirm
   text-to-speech covers English/German/Dutch, and check remaining credits
   (`/v1/user/subscription`). The key is scoped to Speech to Text, Text to Speech,
   Models (access), Voices (read) and User (access) only.
2. Confirm the demo language (Wolof unless the test changes the picture). Fallback for
   speech recognition: Meta MMS.
3. Search for real Gambian tourism review data. If none is usable, ask the user before
   using synthetic reviews; if approved, label them synthetic everywhere.
4. Scaffold the P0 build: recording library, Bluetooth-style file import, weekly sync
   (speech-to-text, translate to English, then German/Dutch, round-trip check), champion
   review screen, answer library, visitor Q&A with intent matching and honest fallbacks.
5. Small evaluation: FLORES-200 Wolof translation score on a sample and intent accuracy on
   a hand-labeled set.
6. Then P1 (voice output, real SMS/WhatsApp, weekly digest, Lovable UI) and the video.

## Working preferences
- The user is not an experienced coder and works with Claude Code and Cursor. Ask for their
  input before big decisions and explain in plain language.
- Label anything simulated as simulated. Never present synthetic data as real.
