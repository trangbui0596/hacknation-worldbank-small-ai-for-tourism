# Make the demo video with the least effort from you

**What is already done (by Claude):** the narration for every scene, spoken by an AI voice (`docs/video_assets/vo/*.mp3`, text in `narration.json`, 3 minutes in total), title, limits and end cards, on-screen labels, and a script that assembles everything (`assemble.py`). You do NOT record your voice and you do NOT need lighting for screen recordings.
**What only you can do:** record 9 short screen clips on your phone and put them in a folder.

## 1. Look and sound (what makes it feel professional)
- Screen recordings: phone brightness at 100%, Do Not Disturb on, close other chats, hide notifications, battery above 50%, clean home screen. No lighting needed.
- The call scene (the only one that needs a camera): film the demo phone with a second phone on a stack of books, near a window (daylight from the side), steady, no flash. Keep the clip silent; the narration covers it.
- Sound: the narration is a studio-quality AI voice. Add a quiet royalty-free track (YouTube Audio Library or Pixabay, "calm, warm, acoustic") at about 10% volume.
- Pace: each clip should last about as long as its narration (listed below). Extra length is trimmed; short clips freeze on the last frame.
- AI video tools (for example Higgsfield): optional and not recommended for the proof. Judges want real footage of the real product. If you use one, use it only for a 3 to 5 second intro of generic Gambian scenery, and label it "AI-generated illustration". Never generate footage of Noor as a real person.

## 2. The 9 clips (silent screen recordings, in this order, saved as `00_problem.mp4` ... `09_limits.mp4`)
| File | Narration length | Record this |
|---|---|---|
| `00_problem` | 21 s | Laptop: the live page top (https://teranga-gambia.lovable.app), slow scroll over the six number tiles |
| `01_idea` | 15 s | Laptop: the How it works tab, slow pan over the five-step flow |
| `02_call` | 10 s | Second phone filming the demo phone (data and Wi-Fi OFF) dialing the Twilio number; laptop speaker plays `SYNTHETIC_q01_price.mp3` |
| `03_review` | 21 s | Phone screen recording: `REVIEW`, the review card, `1` (WhatsApp mirrors the SMS commands) |
| `04_tourist` | 17 s | Phone screen recording as the tourist: send a voice note in English, then a German one; show the answer and the voice note |
| `05_listing` | 19 s | See section 3 |
| `06_review` | 13 s | Phone: `FEEDBACK`, your own voice note, `POST`, tap the link, paste (do not post) |
| `07_community` | 21 s | Phone: `COMMUNITY <PIN>`, `ALERT 2 Tendaba road`, `EXIT`, a question (notice appears under the answer), `ALERT 6` |
| `08_coaching` | 9 s | Phone: `COACH` |
(`09_limits` can be left out: the script adds the limits card.)

## 3. Filming the Google listing demo, step by step
Before filming (about 5 minutes, once):
1. In WhatsApp send `REVIEW` (Noor's number needs no PIN) and `START`. Send 4 clips from `docs/test_audio/`: `SYNTHETIC_q02_meeting_point.mp3`, `q03_duration`, `q08_included`, `q09_how_to_book`. Wait for each "Got question" reply.
2. Send `DONE`, then `REVIEW`, and reply `1` to approve each one (about 15 messages).
Filming (about 20 seconds, start the screen recording now):
3. Send `LISTING`.
4. First message: pause 3 seconds on it. Slowly scroll it: the ✅ / 📝 / ❌ list, the "record card" line, the "Only you can fill" line, the claim steps.
5. Second message: long-press the description, tap Copy (this shows the copy step).
6. Stop recording. Then on your laptop (separate 8-second clip, optional): open https://business.google.com, click Add business, paste the description into the form, stop and close the tab. Do NOT submit or create a real listing.
The narration for this clip is `05_listing.mp3`.

## 4. Put it together (pick one)
- **Easiest, fully by me:** put your clips in a Google Drive folder and tell me. For me to read them, add `drive.google.com` and `*.googleusercontent.com` to the environment's allowed domains (Network access, Custom), then I run `assemble.py` and upload the finished video. I could not open the reference video for the same reason.
- **Yourself in CapCut (free):** import the clips and the `vo/` files, place each narration under its clip, add `cards/` images at the start, before the end, and at the end, drop the `label_*.png` overlays on the right clips, add captions (Auto captions) and the music. Export 1080p.

## 5. The reference video
I cannot open large videos from Drive (the connector only reads documents and images). Either allow the Drive domains above and share the link again, or send me 8 to 10 screenshots from it plus a sentence on what you like (pace, graphics, voice). I will match the structure and tell you exactly what to change.
