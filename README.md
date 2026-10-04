# Teranga: documentation and demo kit

**One phone call in Wolof becomes answers every tourist can read.**

Documentation for **Teranga**, a prototype for the World Bank x Hack-Nation "Small AI for Development" Tourism track.
A fictional Gambian tourism operator, Noor, records her answers once by phone call and approves them by text.
Tourists ask on WhatsApp in English, German or Dutch and get her approved words back, as text and voice. The system
also drafts her Google listing, turns voice reviews into clean text, sends community flood notices and referrals
between neighbours, and texts Noor weekly coaching in Wolof. Noor never needs the internet.

- **Live prototype:** https://teranga-gambia.lovable.app
- **Code:** https://github.com/trangbui0596/teranga-gambia

## What is in this repository

| Path | What it is |
| --- | --- |
| `docs/VIDEO_SCRIPT.md` | The required one-sentence problem statement, the sourced evidence table and the demo script |
| `docs/DEMO_RUNBOOK.md` | Exact messages to send for every scene, message budget and fallbacks |
| `docs/FILMING_GUIDE.md`, `docs/VIDEO_PRODUCTION.md` | How the demo video is filmed and assembled |
| `docs/COMMUNITY_CHAMPION_GUIDE.md` | The household and community champion roles, notices, referrals |
| `docs/data/` | Real visitor questions from public FAQ pages, prices and exchange-rate notes |
| `docs/DATA_INSIGHTS.md` | What the World Bank figures told us, which design decisions they support, and what they did not show |
| `docs/eval/WOLOF_TRANSLATION_CHECK.md` | Wolof to English check on 54 open FLEURS/FLORES sentences (chrF++ 47.6) |
| `docs/eval/REAL_QUESTIONS_MATCHER.md` | How the question matcher was tested (82 for tuning, 103 untuned held-out) |
| `docs/test_audio/` | Ten synthetic Wolof test clips (text-to-speech, not a native speaker) |
| `docs/video_assets/` | Narration, cards and the assembly script for the demo video |
| `NEXT_STEPS.md` | Running log of decisions, status and what is left |

## Honest limits

- The Wolof test audio is synthetic. All Wolof wording is machine-written and unverified by a native speaker.
- Speech recognition on real Wolof speech is untested and unreliable. The app retries and flags bad transcripts.
- Translations are machine translations and say so.
- US SMS delivery is awaiting carrier registration, so the live demo mirrors the SMS commands on WhatsApp.
- The partner list and other community members are simulated; the Google listing is a draft a person publishes.
- No real operator or tourist has used it yet. The World Bank figures give context; they do not measure lost enquiries.

## Tech stack

Lovable (app, database, AI), Twilio (voice, WhatsApp, SMS), ElevenLabs (speech-to-text and text-to-speech),
Google Maps Platform Places (public reviews), World Bank WDI API (every statistic, linked).
