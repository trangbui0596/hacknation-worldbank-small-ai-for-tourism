# How to film the Teranga demo video (plain-language guide)

Target: 4 to 4.5 minutes (the limit is 5). You need: your phone (WhatsApp, the call), a laptop (plays the clips, shows the live page), and a free video editor. Use `docs/VIDEO_SCRIPT.md` for the words and `docs/DEMO_RUNBOOK.md` for the exact messages to send. This guide is only about filming.

Honesty rule for the whole video: say out loud that the Wolof audio is synthetic, the Wolof wording is unchecked by a native speaker, and the partner recommendation and Google listing parts are simulated. The script already includes these lines.

## 1. Before you film (15 minutes, once)

1. Phone: charge it, turn on Do Not Disturb, and close WhatsApp chats from other people (their names and messages would show on screen). Turn notifications off.
2. Change the champion PIN for the video. Typing `REVIEW <PIN>` shows the PIN on screen. In Lovable, open the project's secrets and set `DEMO_CHAMPION_PIN` to a throwaway value like `4821` just for filming; change it back or to something else afterward.
3. Check the Twilio sandbox message counter ("Try out WhatsApp" page). You need about 35 messages for one clean run of all eight scenes. Top up before you start if you are below 40.
4. Make the coaching data fresh (the cache lasts 24 hours): run the one-line command in runbook section 0.
5. Put `SYNTHETIC_q01_price.mp3` and `SYNTHETIC_q05_children.mp3` on the laptop (from the repo folder `docs/test_audio/`). Turn the laptop volume up.
6. Open on the laptop, in separate tabs: the live page (https://teranga-gambia.lovable.app), and `docs/VIDEO_SCRIPT.md` (the evidence table).
7. Send `EXIT` once in WhatsApp so the chat starts in visitor mode.
8. Do one silent practice run of scene 2 only if you have spare messages. Otherwise skip practice; the runbook is exact.

## 2. How to record each part

Record each scene as its own short clip, with no talking. Add your voice afterward (section 3). This makes every clip easy to redo and keeps message use low.

| # | Scene | What to record | How |
|---|---|---|---|
| 0 | Problem and idea | The numbers on the live page, then the "Works offline" and "AI beyond SMS" tabs | Laptop screen recording: Mac `Cmd+Shift+5`, Windows `Win+Alt+R` (Game Bar) or the free OBS app. Scroll slowly. |
| 1 | The call | You calling the Twilio number from the demo phone (Wi-Fi and mobile data OFF, signal ON), the clip playing from the laptop speaker | Phone screen recorders usually do not capture call audio. Film the phone with a second device (another phone or the laptop webcam) leaning on a book stack. Show the call screen and the laptop playing the clip. Then turn data back ON; the "Got 2 of 2 answers" WhatsApp message arrives; screen-record that. |
| 2 | Household helper | WhatsApp: `REVIEW <PIN>`, `REVIEW`, `1`, `1` | Phone screen recording (iPhone: Control Center, record button; Android: Quick Settings, Screen record). |
| 3 | Visitor | `EXIT`, then the questions in the runbook, including the one it should NOT know | Phone screen recording. Play the voice note on screen once so viewers see the "AI-generated voice" label. |
| 4 | Google listing | `REVIEW <PIN>`, `LISTING`; long-press the description to show it can be copied | Phone screen recording. |
| 5 | One-tap review | `FEEDBACK`, your own English voice note, `POST`, then tap the link and paste (do not post) | Phone screen recording. |
| 6 | Community | `COMMUNITY <PIN>`, `ALERT 2 Tendaba road`, `EXIT`, a question (notice appears), `COMMUNITY <PIN>`, `BILINGUAL`, `1`, `ALERT 6` | Phone screen recording. This is the scene that sets Teranga apart: take your time on the notice under the visitor's answer and on the translation check. |
| 7 | No internet needed | In the Messages app text `COACH` to the Twilio number; show the reply | Phone screen recording of Messages, then WhatsApp if the copy arrives there. Say which one it is. |
| 8 | Coaching | `REVIEW <PIN>`, `COACH` | Phone screen recording. Pause on the counts and the footer. |

Tips: wait for each reply before sending the next message (the voice note can take about 10 seconds). Do not retry a failed message in a loop; each one uses sandbox budget. If something fails, write down the error code from Twilio's Message Logs and tell Claude. Keep the failed clip out of the video and use the fallback in runbook section 11.

Do not point the camera at anything with your own phone number or address. If your number appears on screen, blur it in the editor (section 4).

## 3. The voice-over

1. Print or open `docs/VIDEO_SCRIPT.md`. Read it once out loud to hear the pace; each scene has a time.
2. In a quiet room, record the narration with the voice recorder on your phone (or the editor's built-in recorder), one scene at a time. Speak slowly. It is fine to read the script word for word.
3. Include the required one-liner exactly as written in the script.
4. Say the limits plainly at the end. Judges value honesty more than polish.

## 4. Editing (free tools: CapCut, iMovie, or DaVinci Resolve)

1. Put the clips in order: 0 to 8, then the limits slide.
2. Lay the voice-over over each clip. Cut dead time (waiting for replies) with a quick cut or a 2x speed-up and a small "sped up" caption.
3. Add short text overlays: "SYNTHETIC audio" on scene 1, "Machine-translated" on scene 3, "Draft: a person publishes it" on scene 4, "Simulated members" on scene 6, "US SMS registration pending" on scene 7, "Unverified Wolof" on scenes 2, 6 and 8.
4. Blur any personal phone numbers.
5. Add one last slide: the live link, the GitHub link, and "Prototype. Noor is fictional."
6. Check the total length is under 5:00. Export 1080p MP4.

## 5. Upload and submit

1. Upload the video (YouTube "Unlisted" is fine, or whatever the hackathon page asks for) and open the link in a private window to check it plays.
2. Collect the links: the video, the live page (https://teranga-gambia.lovable.app), the code (https://github.com/trangbui0596/teranga-gambia), and the docs repo.
3. Paste the required one-liner and the model and data notes from `docs/VIDEO_SCRIPT.md` into the submission form. Check the form itself for any other required fields.
4. After filming, change `DEMO_CHAMPION_PIN` again, and keep the Twilio sandbox for judges only if you want to.

## 6. If you are short on time

Minimum viable video (about 2:30): scene 0, scene 1, scene 2, scene 3, then the limits. Add scenes 4 to 8 only if the takes went smoothly. If you have time for only one extra scene, make it scene 6 (community).
