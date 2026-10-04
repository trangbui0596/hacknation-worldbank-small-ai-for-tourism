# How the 60-second demo video was made

**Current video: 59.4 s, 1080p, 30 fps, paper-collage storybook style.** Script and timings: `docs/VIDEO_SCRIPT.md` (section "Current 60-second cut").
The longer 9-clip kit from the first plan (`assemble.py`, `cards/`, `vo/`) is kept in `docs/video_assets/` for a longer cut but is not what we submit.

## What is real and what is generated
- **Real:** the WhatsApp screen recordings of the live prototype (clips A to J in the working folder). Messages are filmed on WhatsApp and mirror the SMS commands
  because US SMS delivery is awaiting carrier registration. The voice notes you hear inside the phone are the app's own AI voice.
- **Generated:** the narration (ElevenLabs voice, `docs/video_assets/narration_60s.json`) and all paper-collage art (Higgsfield images, see `docs/video_assets/AI_ILLUSTRATIONS.md`).
  The art must be credited as "AI-generated illustration". No real person is depicted.
- **Music:** "Third Pulse" from Artlist. The file we had is the watermarked preview (a voice says "Music licensing reimagined" at 30.6 s and "Artlist.io" at 60.6 s).
  `docs/video_assets/pipeline/clean_music.sh` patches the first one. **For the submission, download the licensed clean track from Artlist and confirm the licence covers the use.**

## Structure (five segments, 0.5 s cross-fades, music ducked under the voice, loudness about -15 LUFS)
| Segment | Length | What it shows |
| --- | --- | --- |
| Opening | 8.4 s | Three cut-paper pages tear in (tourist writing "Guten Tag!", Noor with an unread message, close-up of the unread phone), then the stamp-bridge page and the Teranga logo card |
| 1 Noor | 22.5 s | AI-suggested questions about her business, voice answers, SMS-first and weekly-sync tags, approval with one digit, Google listing, AI coaching card |
| 2 The tourist | 12.5 s | Question in her own language, the approved answer as a voice note, a voice review, she posts it herself |
| 3 The community | 12.9 s | Flood notice, shown under every answer, a neighbour suggested and a person connects them |
| Closing | 5.1 s | Logo, "Teranga gives Noor her voice, and her community its champion.", links, stamp bridge between tourist and Noor |

## Rebuild it
All scripts are in `docs/video_assets/pipeline/` and expect the working-folder layout used here (`../clips/*.mp4` screen recordings, `v3/vo` and `v5/vo` narration mp3s, `cl/` and `cl5/` generated art). They need Python with Pillow, numpy and scipy, and ffmpeg.
1. Generate the art (see `AI_ILLUSTRATIONS.md`), put the images in `pc/L/`, run `cut.py` to cut figures out of the white backgrounds.
2. `mk_labels.py` (opening label tags), `mk_act_assets.py` (act backdrops, figures, captions, coaching card), `mk_end_assets.py` (closing page).
3. Narration: ElevenLabs text-to-speech with the settings in `narration_60s.json`; one mp3 per line id.
4. `python3 build_open2.py v4/seg_o.mp4` (opening), `python3 build5.py n t c e` (acts and closing), then `python3 join_v5.py` to join, mix the music and normalise.
5. Check: total under 60 s, and transcribe the final audio to confirm there is no stray voice (the music preview watermark is the usual culprit).

## Hard-won rules
- Never show the demo champion PIN on screen; the phone clips are cropped or cut around it.
- The "champion" closing word uses the natural delivery (a forced falling pitch sounded unnatural).
- Say the SMS-first line for Noor ("It all runs on SMS, offline"). Visitors do use WhatsApp for real, and the tourist segment shows it; WhatsApp is the household champion's weekly sync and the tourists' channel.
- Keep every statistic linked to its source on the live page; the 60-second cut states none on screen except the evidence strip on the logo card (US$157M tourism receipts 2019, about half of Gambians offline, World Bank WDI).
