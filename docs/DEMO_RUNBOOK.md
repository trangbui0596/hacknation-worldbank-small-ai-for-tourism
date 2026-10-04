# Teranga demo runbook (for the 2 to 5 minute video)

> **Current submission cut: 60 seconds.** The scenes below are how the clips were filmed; the finished video uses only parts of them. See `docs/VIDEO_SCRIPT.md` (60-second cut and claim check) and `docs/VIDEO_PRODUCTION.md`.

Live app: https://teranga-gambia.lovable.app. Code: https://github.com/trangbui0596/teranga-gambia (branch main).
Persona: Noor, a FICTIONAL tourism operator in The Gambia. Test audio is SYNTHETIC (ElevenLabs reading Wolof text), not a real speaker.

## 0. Before recording (do once, about 10 minutes)

- [ ] Twilio WhatsApp sandbox: your WhatsApp has joined it (send the join code; a message "You are all set" comes back). Webhook "When a message comes in" = `https://teranga-gambia.lovable.app/api/public/whatsapp-webhook`, HTTP POST.
- [ ] Twilio number voice settings: "A call comes in" = `.../api/public/voice-incoming`, "Call status changes" = `.../api/public/voice-status`, both HTTP POST.
- [ ] Lovable secrets present (names exact, UPPERCASE): `DEMO_CHAMPION_PIN`, `DEMO_SMS_NUMBER`, `DEMO_WHATSAPP_NUMBER` (the sandbox sender), `TWILIO_AUTH_TOKEN`, `TWILIO_SMS_FROM`, `DIGEST_TRIGGER_SECRET`, `TWILIO_WEBHOOK_URL`. Phone numbers in `+1...` format, no spaces.
- [ ] Sandbox free messages left: check the counter on the "Try out WhatsApp" page. One full run uses about 25 to 30 messages. Raise `MAX_OUTBOUND_PER_DAY` only if needed.
- [ ] Fresh coaching data (the cache lasts 24 hours). In a terminal, with your digest secret:
  - Mac/Linux: `read -s -p "Digest secret: " S; echo; curl -s -m 60 -X POST https://teranga-gambia.lovable.app/api/public/coach-run -H "x-digest-secret: $S"; unset S`
  - Windows PowerShell: `$s = Read-Host "Digest secret"; Invoke-RestMethod -TimeoutSec 60 -Method Post -Uri https://teranga-gambia.lovable.app/api/public/coach-run -Headers @{"x-digest-secret"=$s}`
- [ ] Optional secret `GOOGLE_REVIEW_URL`: the link everyone gets for the review. Without it the message says "[review link not set yet, Simulated]", which is honest but looks unfinished. Use the real Google review link of a place you own or run; never a real business you do not own, and never post a fake review.
- [ ] Optional, only for the "Noor texts COACH" scene: Twilio Console, Phone Numbers, your number, Messaging, "A message comes in" = `https://teranga-gambia.lovable.app/api/public/sms-webhook`, HTTP POST. Without it the scene still works from the WhatsApp side.
- [ ] Optional secrets: `SMS_RECEIPTS=off` stops approval receipts to Noor's phone; `SMS_VISITOR_MODE=on` lets visitors use text-only SMS (leave it off for the video).
- [ ] For the translation check (scene 6): one answer must be waiting for a bilingual reviewer. One already is in the database from earlier tests. To make another, in household-champion mode review an answer and reply `3`.
- [ ] Put the two clips on the laptop: `SYNTHETIC_q01_price.mp3` and `SYNTHETIC_q05_children.mp3` (folder `docs/test_audio/` in the repo).
- [ ] Phone: Wi-Fi and mobile data OFF for the call scene (a feature phone has no data). Voice signal ON.
- [ ] Do NOT type the word STOP in the WhatsApp sandbox: Twilio treats it as "leave the sandbox". Use DONE.
- [ ] Reset the demo state if needed: send `EXIT` to leave any open round.

## Loading or redoing answers (read this before sending voice notes)

- A voice note only counts as an answer during a recording round. Send `START` first; the app asks question 1 (price), you send the voice note, it asks question 2, and so on. Send `DONE` to end the round.
- A voice note sent outside a round goes to the AI assistant instead and gets a "Man naa:" menu reply. That is not an error, just the wrong mode.
- Reply `2` ("record again") to a review card only marks it; then send `START` and record again from question 1.
- Use the synthetic clips from `docs/test_audio/` (send them as voice messages). Speaking Wolof yourself, or playing a clip through a speaker, can make the recognizer return Cyrillic or Arabic letters. The app now retries once without a language hint and otherwise flags the answer so you can record it again.

## Filming decision: all scenes on WhatsApp

Live SMS is blocked (carrier registration in review; your carrier also blocked the test text). Film scenes 2, 6 and 7 on WhatsApp using the same commands and say the line in the video script ("WhatsApp mirrors the SMS commands"). For scene 7 show the Try SMS tab on the live page as a labeled simulation. Skip the Twilio SMS webhook setup.

## 0b. Message budget (when only about 20 sandbox messages are left)

Counts are the messages the app SENDS (my estimate from the code; I do not know if Twilio also counts your inbound messages, so watch the counter on the "Try out WhatsApp" page after the first take). A visitor answer costs 2 when the voice note is ready (text, then voice).

| Take | You send | App replies | About |
|---|---|---|---|
| 1. Call | (phone call) | WhatsApp summary of the call | 1 |
| 2. Noor approves (this is also the smoke test of the new layout) | `REVIEW <PIN>`, `REVIEW`, `1`, `1` | menu, review message, approval x2 | 5 |
| 3. Visitor | `EXIT`, price question, kids question, unrelated question, `YES` | 1 + 2 + 2 + 1 + 1 | 7 |
| 4. Google listing | `REVIEW <PIN>`, `LISTING` | menu, listing pack, description to copy | 3 |
| 5. One-tap review | `FEEDBACK`, your own voice note, `POST` | prompt, clean text + options, then 2 (text, link) | 4 |
| 6. Community | `COMMUNITY <PIN>`, `ALERT 2 Tendaba road`, `EXIT`, a question, `COMMUNITY <PIN>`, `BILINGUAL`, `1`, `ALERT 6` | menu, notice posted, mode, answer + notice (2 with voice), menu, translation check, confirmation, cleared | 9 |
| 7. Offline SMS | text `COACH` from the Messages app | 1 SMS (or 1 WhatsApp copy) | 1 |
| 8. Coaching | `REVIEW <PIN>`, `COACH` | menu, Wolof coaching message (+ SMS copy note) | 2 |
| Spare | `COACH EN`, German question, `MORE` | | 1 to 5 |

Core total about 32 to 36. Skip the optional scenes (digest, referrals). Record each take separately and cut them together. Do not retry a take in a loop. If a take fails, note the error code and use the fallback recording (section 11).

## 1. Scene: Noor records by phone call (about 40 seconds)

1. Call the Twilio number from the demo phone (data and Wi-Fi off).
2. Say on camera: "A basic phone with no internet." (Twilio plays a short trial notice first: mention it or cut it.)
3. The line says "Hello Noor..." then "Question one. Price." After the beep, play `SYNTHETIC_q01_price.mp3` from the laptop speaker into the phone. Press # (or wait 8 seconds of silence).
4. "Question two. Children." Play `SYNTHETIC_q05_children.mp3`. Press #.
5. "Thank you. Your answers were saved. Goodbye."
6. A summary arrives: "Teranga: Got 2 of 2 answers from your call..." It arrives on WhatsApp because US SMS needs carrier registration, which is submitted and in review. Say so.

## 2. Scene: Noor approves her answers (about 40 seconds)

Roles to say out loud: Noor records by phone call and approves her own answers by SMS. Visitors use WhatsApp. SMS needs no internet. US SMS registration is still in review, so in the demo Noor's SMS replies arrive on WhatsApp with the line "SMS copy (shown here because US SMS registration is pending)".

1. From the demo phone's Messages app (SMS) send `REVIEW` (Noor's number needs no PIN). Expected: "REVIEW = check answers (then 1 approve, 2 record again, 3 bilingual)...". (If SMS is still blocked this arrives on WhatsApp with the "SMS copy" line. Either is fine; say which.)
2. Send `REVIEW`. Expected: one compact text: "1/N Njekk", the Wolof transcript in quotes, "Limu: ... (about 1500) + dalasi", and "1 Nangu, 2 Waxaat ko, 3 Nit ku xam ñaar yi làkk".
3. Say: "Noor does not need English: she sees the Wolof transcript and the numbers, and confirms with one digit."
4. Reply `1` to approve the price answer. The confirmation comes as one text and the next answer as another. Voice files for English, German and Dutch are created in the background (about 10 seconds). Reply `1` again for the next answer.
5. If an approval says "Still processing", send REVIEW again in a minute.
6. The same commands work on WhatsApp (richer formatting) if you prefer to film there.

## 3. Scene: a visitor asks, in their language (about 50 seconds)

1. On WhatsApp send `EXIT` to switch to visitor mode (or use a second phone as the visitor).
2. Ask by VOICE NOTE: record "How much does the tour cost?" in English. Expected: "🎙️ “How much does the tour cost?”" (what it heard), the approved answer labeled "Machine-translated", and an AI voice note. Say: "Speech recognition hears the tourist and detects the language; the answer comes back in that language as text and voice."
3. Record a German voice note: "Wie viel kostet die Tour?" Expected: German heard text and German answer (and voice note if ready).
4. Ask by text `Can we bring our kids?` Expected: the children answer.
5. Ask something unrelated, for example `Do you offer night tours?` Expected: "Not sure, Noor will answer." Say: "When it is not sure, it says so. We tested this on real questions from Gambian operators; see the What's real tab for the measured numbers."
6. Reply `YES` to "Was this clear?". Say: "The review link is the same for everyone. No review gating."

## 4. Scene: the Google listing (about 25 seconds)

1. In household-champion mode (by SMS or WhatsApp: `REVIEW <PIN>`), send `LISTING`.
2. Expected: a Wolof-first message: answers approved (x of 10), listing fields ready (y of 10), a ✅ / 📝 / ❌ list of the fields, which question cards to record next, what only Noor or her household champion can add (name, hours, phone, photos), five short steps to claim the profile, then the description alone as a second message (press and hold to copy).
3. Say: "Built only from answers Noor approved. It never invents a phone number or opening hours: those say 'needs input'. It sends nothing to Google. A person claims the profile at business.google.com and pastes it."

## 5. Scene: one-tap Google review, in the visitor's own words (about 25 seconds)

What is real: the voice note, the speech-to-text, the clean-up and the link message are all live. What stays with the visitor: pasting and pressing "Post" on Google. Teranga never posts a review for anyone, and Google does not let a page pre-fill review text, so the visitor pastes it.

One-time setup (3 minutes): in Google Maps, open the place whose review box you want to show, tap "Write a review" (or "Reviews", then "Write a review"), copy the page address, and save it as the Lovable secret `GOOGLE_REVIEW_URL`. In real use this is Noor's own Google review link. For the video you may use any public place; say out loud that it stands in for Noor's link.

1. In visitor mode (`EXIT`), send `FEEDBACK`. Expected: a prompt saying nothing is posted for you and the review is yours.
2. Record a WhatsApp voice note in English about a pretend tour (10 to 15 seconds). Speak as yourself. Do not name real people.
3. Expected: your words as clean text (no facts or feelings changed) plus the options POST / EDIT / NO. The text is cleaned only: it never adds anything you did not say.
4. Send `POST`. Expected: two messages. The text alone (press and hold, Copy), then "To post it: tap the link, paste..." and the same review link everyone gets.
5. Tap the link. Google opens the review box. Paste your text. Say: "No stars were asked. Everyone gets the same link. We never post for the visitor."
6. Do NOT press Post unless this is a genuine review of a place you really visited. Close the page instead. Posting a made-up review is against Google's rules and against what this tool is for.

## 6. Scene: the community champion (about 50 seconds)

Say first: "Every operator has a household champion. A community has one too."

1. Send `COMMUNITY <PIN>`. Expected: the "Mbootaay" menu: ALERT, ALERTS, BILINGUAL, PULSE, LEDGER.
2. Send `ALERT 2 Tendaba road`. Expected: "Notice posted: Road closed or flooded · Tendaba road", the SMS line (sent, or "not delivered: US carrier registration pending"), "Visitors see it under every answer (24 h)", and that N simulated members were not messaged. Say: "The wording is fixed in four languages, so nothing is machine-translated in an emergency, and it always says it is not an official warning."
3. Send `EXIT`, then ask `Where do we meet?`. Expected: the answer and under it "⚠️ Community notice (just now): Road closed or flooded: Tendaba road" with the disclaimer. Send `DE`, ask again: the notice is in German. (`STATUS` also shows the notice.)
4. Send `COMMUNITY <PIN>`, then `BILINGUAL`. Expected: a Translation check card with the Wolof transcript, the English, the numbers heard, and 1 / 2 / 3. Reply `1`. Expected: "approved, and marked as checked by a bilingual reviewer". Say: "When the household champion is not sure, a bilingual person in the community checks. Visitors then see 'English checked by a bilingual reviewer'. German and Dutch stay machine translations of that English."
5. Send `ALERT 6` to clear the notice.
6. Optional: `MORE`, `1 YES`, `CONNECT` (fair referrals between fictional partner operators, SIMULATED), then in the community menu `LEDGER` shows the contact request waiting. Say: "No money, no number shared, and a person passes on the contact."

## 7. Scene: Noor keeps it on her phone, no internet (about 25 seconds)

1. On the demo phone open the Messages app (not WhatsApp) and text `COACH` to the Twilio number.
2. Expected: if US SMS registration has cleared, the coaching arrives as an SMS in Wolof (three parts at most). Until then the same text arrives on WhatsApp, starting "SMS copy (shown here because US SMS registration is pending)". Say that out loud; it is true.
3. If SMS is still blocked, ALSO show the "Try SMS" tab on the live page: pick "I am Noor", tap COACH, LISTING, WEEK; then "I am a visitor" and ask a question. Say plainly: "This is a simulation of the SMS. It uses the same code and demo data. US carrier registration is still in review; once approved, nothing changes in the code." (Never present the simulator as a live delivery.)
4. Say: "Noor needs no internet. She records by phone call and keeps her coaching, listing progress and community notices as plain text messages, and can text COACH, LISTING or WEEK to get them again."
5. Optional: text `LISTING` or `WEEK` the same way. `WEEK` is the weekly learning: what visitors asked, how the public reviews moved since last week, and up to three actions.

## 8. Scene: coaching from real public reviews (about 20 seconds)

1. `REVIEW <PIN>`, then `COACH`. Expected: Wolof message with counts (places, reviews analyzed, date range), top themes, up to 3 actions, limits, the unverified-Wolof label, and a line saying whether the SMS copy reached Noor's phone.
2. Say: "Real Google Maps data: a small sample, a few reviews per place. If there is not enough data, it says so." Send `COACH EN` only if you have messages to spare.

## 9. Optional scenes (only if time allows and they were tested)

- Weekly sync: in household-champion mode send `SYNC` (report on WhatsApp plus an SMS copy to Noor). The full scheduled version is `POST /api/public/weekly-sync` with the digest secret: it re-scans public reviews first (takes about 30 seconds).
- Weekly digest: trigger with the digest secret; Noor gets it by SMS in Wolof (counts only), the household champion's WhatsApp fallback has the full text.

## 10. What to say about limits (honest, required)

- The Wolof audio is synthetic text-to-speech, not a native speaker. Recognition accuracy on real Wolof speech is UNTESTED.
- The Wolof text in the app (labels, coaching) is machine-written and UNVERIFIED by a native speaker.
- Translation is machine translation and says so on every answer.
- The 20-question matching test is agent-written test data (not real visitors). Do not quote it as accuracy.
- SMS needs US carrier registration (in review), so messages are delivered on WhatsApp via Twilio's sandbox.
- Parts that are simulated: the partner list and recommendation, and the other community members (only Noor is a real member). The Google listing is a draft a person must publish. The review flow is real up to the link: the visitor posts it themselves. SMS, community notices, translation checks and the listing pack are built and unit-tested but have not been tried by real users.
- SMS: US delivery needs carrier registration (in review), so in the demo SMS copies arrive on WhatsApp.
- Reviews data: real, public, small sample, coverage thin.

## 11. If something fails during recording

- Do not retry in a loop (each message uses sandbox budget). Check the Twilio Message Logs and tell Claude the error code.
- Fall back to a pre-recorded successful run, and label it as a recording of an earlier run.
