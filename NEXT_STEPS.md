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
- First pass sent: schema + screens 1-5 + seeded SAMPLE data, NO external API calls. Project knowledge (safeguards, simulated labeling) is set.
- Demo: airplane-mode phone = feature phone; user's WhatsApp = visitor via the Twilio WhatsApp sandbox; SMS digest via Twilio. Phone numbers go ONLY in Lovable secrets (DEMO_SMS_NUMBER, DEMO_WHATSAPP_NUMBER), never in chat or the repo.
- User reports ElevenLabs and Twilio are connected in Lovable (not verified by Claude). The Twilio 401 on a direct key test was still unresolved at last report.
- User still to do: link the project to this GitHub repo (Lovable project settings), verify the Twilio number for SMS, join the Twilio WhatsApp sandbox from their WhatsApp.
- Next build steps: wire `transcribe` (ElevenLabs scribe_v2, wol), `translate`/`roundtrip` (Lovable AI), `match`, `speak`; then Twilio SMS/WhatsApp; then evaluation and video.

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
