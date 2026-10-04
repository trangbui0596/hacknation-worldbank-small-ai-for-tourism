# Wolof to English translation check (small, indicative)

**Result:** on 54 Wolof sentences, the translator inside Teranga scored **chrF++ 47.6** and **BLEU 22.1** against the English references
(50 sentences: chrF++ 48.5, BLEU 22.8, after removing four where the English reference clearly does not match the Wolof source).
Median sentence chrF++ was 47.4 (range 16.0 to 84.7); 19 of 54 sentences scored below 40.

## How it was run
- **Data:** the open FLEURS development set. FLEURS sentences are the FLORES-200 sentences, with the same id in every language, so the Wolof
  (`wo_sn`) and English (`en_us`) files pair by id. Source: https://huggingface.co/datasets/google/fleurs (text only, no audio used).
  FLORES-200 is licensed CC BY-SA 4.0; attribution: Meta AI / NLLB Team and Google.
- **System:** the app's own translator (Lovable AI, the same prompt used for Noor's answers), Wolof to English.
- **Sample:** the first 54 sentences by id (not hand-picked). The protected route `/api/public/eval-translate` fetched them, translated them and stored
  the pairs; scoring was done offline with sacrebleu (chrF++ with word order 2, default BLEU).
- **Pairs:** `wolof_translation_check.csv` (id, English reference, Teranga translation).

## What it does and does not tell us
- It is a measured number for general Wolof quality, from professional references. Nothing here was tuned on it.
- Sentences are long news and encyclopaedia text. Noor's answers are short and practical (prices, meeting points). The score does not measure those.
- English references are themselves translations, so valid paraphrases lose points. A few references do not match the Wolof source (for example id 1572).
- Models may have seen FLORES text in training, which can flatter the score. 54 sentences is an indicative sample, not a benchmark.
- What went wrong in the weaker sentences: dropped or changed content words (id 1545 "curry" became "skin"; id 1560 "swimming" became "paying"), and
  names left half-translated ("Niseriya", "Corée du Nord"). Numbers, dates and quantities in the sample were kept (21 to 20, 15 wins, 108, 56, ten and five years).
- Because the translator can still change a word, every answer is shown to Noor in Wolof with the numbers it heard, and a price that is missing
  from the English is flagged.

## Next steps this points to
1. Score speech recognition on real Wolof speech (FLEURS `wo_sn` audio, Common Voice) with word error rate. Today we only tested synthetic audio.
2. Compare against NLLB-200 and a Meta MMS fallback on the same sentences.
3. Add a small word list of the terms operators use (prices, places, "dalasi") to both recognition and translation prompts.
4. Have a native Wolof speaker review the weakest 19 sentences and all Wolof wording in the app.
