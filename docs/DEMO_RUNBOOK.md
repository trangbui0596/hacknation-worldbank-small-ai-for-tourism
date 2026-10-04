# Teranga demo runbook (for the 2 to 5 minute video)

Live app: https://teranga-gambia.lovable.app. Code: https://github.com/trangbui0596/teranga-gambia (branch main).
Persona: Noor, a FICTIONAL tour operator in The Gambia. Test audio is SYNTHETIC (ElevenLabs reading Wolof text), not a real speaker.

## 0. Before recording (do once, about 10 minutes)

- [ ] Twilio WhatsApp sandbox: your WhatsApp has joined it (send the join code; a message "You are all set" comes back). Webhook "When a message comes in" = `https://teranga-gambia.lovable.app/api/public/whatsapp-webhook`, HTTP POST.
- [ ] Twilio number voice settings: "A call comes in" = `.../api/public/voice-incoming`, "Call status changes" = `.../api/public/voice-status`, both HTTP POST.
- [ ] Lovable secrets present (names exact, UPPERCASE): `DEMO_CHAMPION_PIN`, `DEMO_SMS_NUMBER`, `DEMO_WHATSAPP_NUMBER` (the sandbox sender), `TWILIO_AUTH_TOKEN`, `TWILIO_SMS_FROM`, `DIGEST_TRIGGER_SECRET`, `TWILIO_WEBHOOK_URL`. Phone numbers in `+1...` format, no spaces.
- [ ] Sandbox free messages left: check the counter on the "Try out WhatsApp" page. One full run uses about 25 to 30 messages. Raise `MAX_OUTBOUND_PER_DAY` only if needed.
- [ ] Fresh coaching data (the cache lasts 24 hours). In a terminal, with your digest secret:
  - Mac/Linux: `read -s -p "Digest secret: " S; echo; curl -s -m 60 -X POST https://teranga-gambia.lovable.app/api/public/coach-run -H "x-digest-secret: $S"; unset S`
  - Windows PowerShell: `$s = Read-Host "Digest secret"; Invoke-RestMethod -TimeoutSec 60 -Method Post -Uri https://teranga-gambia.lovable.app/api/public/coach-run -Headers @{"x-digest-secret"=$s}`
- [ ] Optional secret `GOOGLE_REVIEW_URL`: the link everyone gets for the review. Without it the message says "[review link not set yet, Simulated]", which is honest but looks unfinished. Use the real Google review link of a place you own or run; never a real business you do not own, and never post a fake review.
- [ ] Put the two clips on the laptop: `SYNTHETIC_q01_price.mp3` and `SYNTHETIC_q05_children.mp3` (folder `docs/test_audio/` in the repo).
- [ ] Phone: Wi-Fi and mobile data OFF for the call scene (a feature phone has no data). Voice signal ON.
- [ ] Do NOT type the word STOP in the WhatsApp sandbox: Twilio treats it as "leave the sandbox". Use DONE.
- [ ] Reset the demo state if needed: send `EXIT` to leave any open round.

## 0b. Message budget (when only about 20 sandbox messages are left)

Counts are the messages the app SENDS (my estimate from the code; I do not know if Twilio also counts your inbound messages, so watch the counter on the "Try out WhatsApp" page after the first take). A visitor answer costs 2 when the voice note is ready (text, then voice).

| Take | You send | App replies | About |
|---|---|---|---|
| 1. Call | (phone call) | WhatsApp summary of the call | 1 |
| 2. Family helper (this is also the smoke test of the new layout) | `REVIEW <PIN>`, `REVIEW`, `1`, `1` | menu, review message, approval x2 | 5 |
| 3. Visitor | `EXIT`, price question, kids question, unrelated question, `YES` | 1 + 2 + 2 + 1 + 1 | 7 |
| 4. One-tap review | `FEEDBACK`, your own voice note, `POST` | prompt, clean text + options, then 2 (text, link) | 4 |
| 5. Cross-community | `MORE`, `1 YES`, `CONNECT` | question, suggestion, confirmation | 3 |
| 6. Coaching | `REVIEW <PIN>`, `COACH` | menu, Wolof coaching message | 2 |
| Spare | `COACH EN`, German question | | 1 to 4 |

Core total about 22 to 24. Skip the optional scenes (LISTING, digest). Record each take separately and cut them together. Do not retry a take in a loop. If a take fails, note the error code and use the fallback recording (section 9).

## 1. Scene: Noor records by phone call (about 40 seconds)

1. Call the Twilio number from the demo phone (data and Wi-Fi off).
2. Say on camera: "A basic phone with no internet." (Twilio plays a short trial notice first: mention it or cut it.)
3. The line says "Hello Noor..." then "Question one. Price." After the beep, play `SYNTHETIC_q01_price.mp3` from the laptop speaker into the phone. Press # (or wait 8 seconds of silence).
4. "Question two. Children." Play `SYNTHETIC_q05_children.mp3`. Press #.
5. "Thank you. Your answers were saved. Goodbye."
6. A summary arrives: "Teranga: Got 2 of 2 answers from your call..." It arrives on WhatsApp because US SMS needs carrier registration, which is submitted and in review. Say so.

## 2. Scene: the family helper reviews on WhatsApp (about 60 seconds)

1. Send `REVIEW <PIN>`. Expected: champion menu, Wolof first, English below.
2. Send `REVIEW`. Expected for each answer: Wolof transcript (unverified), "Numbers heard" (for price: about 1500 + dalasi), flags, reply options 1/2/3.
3. Say: "The helper does not need English: she sees the Wolof transcript and the numbers, and confirms."
4. Reply `1` to approve the price answer. Voice files for English, German and Dutch are created (about 10 seconds). Reply `1` again for the children answer.
5. If an approval says "Still processing", send REVIEW again in a minute.

## 3. Scene: a visitor asks, in their language (about 50 seconds)

1. Send `EXIT` to switch to visitor mode.
2. Ask `How much does it cost?` Expected: the approved answer, labeled "Machine-translated", and a voice note labeled "AI-generated voice".
3. Send `DE`, then `Wie viel kostet die Tour?` Expected: German answer (and voice note if ready).
4. Ask `Can we bring our kids?` Expected: the children answer.
5. Ask something unrelated, for example `Do you offer night tours?` Expected: "Not sure, Noor will answer." Say: "It never guesses."
6. Reply `YES` to "Was this clear?". Say: "The review link is the same for everyone. No review gating."

## 4. Scene: one-tap Google review, in the visitor's own words (about 25 seconds)

1. Still in visitor mode, send `FEEDBACK`. Expected: a prompt saying nothing is posted for you and the review is yours.
2. Record a WhatsApp voice note in English about a pretend tour (10 to 15 seconds). It is your own voice playing a visitor. Do not invent a real business or a real person.
3. Expected: your words as clean text (no facts or feelings changed) plus the options POST / EDIT / NO.
4. Send `POST`. Expected: two messages. The text alone (press and hold to copy), then "To post it: tap the link, paste..." and the same review link everyone gets.
5. Say: "No stars were asked. Everyone gets the same link. We never post for the visitor." Do not tap through to Google and do not post a review.

## 5. Scene: cross-community recommendation (about 20 seconds, SIMULATED)

1. Send `MORE`. Expected: "Do you prefer nature, culture or food?... (opt-in)... (Simulated)".
2. Send `1 YES`. Expected: a suggestion for a fictional partner, "(Simulated partner)", no payment, number not shared.
3. Send `CONNECT`. Expected: "Noted (Simulated)... a person passes on the contact".
4. Say: "These partners are fictional samples. Suggestions rotate fairly. In real use only operators who opted in would appear."
5. Optional, only if time allows: in champion mode send `LEDGER` to show the contact request waiting (costs 2 messages).

## 6. Scene: coaching from real public reviews (about 20 seconds)

1. `REVIEW <PIN>`, then `COACH`. Expected: Wolof message with counts (places, reviews analyzed, date range), top themes, up to 3 actions, limits, and the unverified-Wolof label.
2. Say: "Real Google Maps data: a small sample, a few reviews per place. If there is not enough data, it says so." Send `COACH EN` only if you have messages to spare.

## 7. Optional scenes (only if time allows and they were tested)

- `LISTING`: draft Google Business profile from approved answers only (SIMULATED, nothing published).
- Weekly digest: trigger with the digest secret; lands on WhatsApp in Wolof first (SMS pending registration).

## 8. What to say about limits (honest, required)

- The Wolof audio is synthetic text-to-speech, not a native speaker. Recognition accuracy on real Wolof speech is UNTESTED.
- The Wolof text in the app (labels, coaching) is machine-written and UNVERIFIED by a native speaker.
- Translation is machine translation and says so on every answer.
- The 20-question matching test is agent-written test data (not real visitors). Do not quote it as accuracy.
- SMS needs US carrier registration (in review), so messages are delivered on WhatsApp via Twilio's sandbox.
- Parts that are simulated: the partner list and recommendation, the Google listing preview, anything labeled Simulated. The review flow is real up to the link: the visitor posts it themselves.
- Reviews data: real, public, small sample, coverage thin.

## 9. If something fails during recording

- Do not retry in a loop (each message uses sandbox budget). Check the Twilio Message Logs and tell Claude the error code.
- Fall back to a pre-recorded successful run, and label it as a recording of an earlier run.
