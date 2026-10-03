# SYNTHETIC test audio (plumbing tests only)

These two clips were generated with ElevenLabs text-to-speech (`eleven_v3`, a stock American-accent
voice) reading Wolof text. ElevenLabs has NO Wolof voice, so this is NOT real Wolof speech.

- `SYNTHETIC_price_wolof_attempt.mp3`: text "Njëg bi mooy junni ak juróom téeméer dalasi." (intended: "The price is 1500 dalasi.")
- `SYNTHETIC_duration_wolof_attempt.mp3`: text "Tuur bi dafay yagg ñett waxtu." (intended: "The tour lasts three hours.")

The Wolof text was written by Claude and has NOT been checked by a native speaker.

ElevenLabs Scribe (`scribe_v2`, `language_code=wol`) returned, for the same clips (v3):
- price: "Niech by mój juni, a k jurą te mer dalasy." (partly right: numbers/currency roughly recovered, rest garbled)
- duration: "Tourbi dafay yagn net wahtu" (close)

Use ONLY to test that upload, download, transcription, translation and review steps run.
Do NOT use them to claim Wolof recognition accuracy, and never present them as Noor's voice or as real data.
Real accuracy needs a recording by a native Wolof speaker.
