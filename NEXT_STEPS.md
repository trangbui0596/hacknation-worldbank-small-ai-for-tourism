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

## Blocked on
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
