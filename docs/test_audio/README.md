# SYNTHETIC test audio (plumbing tests and a labeled demo only)

Generated with ElevenLabs text-to-speech (`eleven_v3`, one stock American-accent voice) reading Wolof
text. ElevenLabs has NO Wolof voice, so these are NOT real Wolof speech and NOT Noor's voice.
The Wolof text was written by Claude and has NOT been checked by a native speaker.

Files: `SYNTHETIC_q01_price.mp3` ... `SYNTHETIC_q10_cancellation.mp3` (one per standard question, in
order) plus two earlier attempts (`SYNTHETIC_price_wolof_attempt.mp3`, `SYNTHETIC_duration_wolof_attempt.mp3`).
`manifest.csv` lists, per clip: the Wolof text, the intended English meaning, and what ElevenLabs Scribe
(`scribe_v2`, `language_code=wol`) heard.

What Scribe heard is close for most clips and wrong in places (for example q01 "Njëg bi" became
"Niech by mój"). This says nothing about accuracy on a real Wolof speaker.

Rules:
- Use them to test that upload/download, transcription, translation, the round-trip check and the review steps run.
- In any demo or video, say clearly: "synthetic test audio, not a real Wolof speaker".
- Never present them as real data, and never use them to claim Wolof recognition accuracy.
- Real accuracy needs a recording by a native Wolof speaker (none available as of 2026-10-03).
