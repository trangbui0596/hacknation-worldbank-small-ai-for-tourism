# Community champions: how Teranga works for a whole circle of operators

Teranga is built around people. Every operator has a **household champion**, and a circle of operators has a **community champion**.

## The two roles

| | Household champion | Community champion |
|---|---|---|
| Who | A family member of one operator | One trusted person for a circle: an association, a village, a guides' group |
| Needs | A smartphone, online about once a week | A smartphone with WhatsApp |
| Does | Reviews that operator's answers: sees the Wolof transcript and the numbers the AI heard, then approves, asks for a re-record, or sends the answer to a bilingual reviewer | Posts community notices, checks translations that household champions could not, passes on referral requests |
| In the demo | `REVIEW <PIN>` | `COMMUNITY <PIN>` (same demo PIN; a real deployment would use real sign-in) |

## Why a community role

Operators share the same roads, rivers and rainy season, so some jobs are too big for one household. About 18.9% of The Gambia's land is less than 5 metres above sea level (World Bank, 2015): when water rises, every operator on that road or river is affected at once. One trusted person who can reach all members quickly, and who can be a bilingual second pair of eyes for translations, lifts the whole circle instead of one business.

## What the community champion can do today (built, unit-tested, not yet tried by real users)

**1. Post a community notice** (`ALERT`).
`ALERT 2 Tendaba road` posts "Road closed or flooded: Tendaba road". Six fixed kinds: flooding, road closed or flooded, storm or heavy rain, boat trips paused, tours closed today, all clear (`ALERT 6` ends all running notices).
- Members get an SMS in Wolof. No internet needed to read it.
- Visitors see it under every answer, in English, German or Dutch, for 24 hours or until cleared. `STATUS` shows it on request.
- The wording is fixed in four languages, so nothing is machine-translated at the moment it matters. Only the place name is free text, and it is cleaned (no links, phone numbers or markup, 40 characters).
- Every notice says it is a community notice, not an official warning, and that Noor will confirm the tour. Teranga does not replace official warnings.

**2. Check translations** (`BILINGUAL`).
When a household champion is not sure a translation is right (option 3 in her review), the answer waits in the community queue. The community champion sees the Wolof transcript, the English, and the numbers the AI heard, and replies 1 (English is right), 2 (record again) or 3 (leave it). When approved, visitors see "English checked by a bilingual reviewer". German and Dutch stay machine translations of that English, and the label says so.

**3. Pass on referrals** (`LEDGER`).
Visitors can ask for a suggestion for another tour. Suggestions rotate fairly between partner operators, no money changes hands, the visitor's number is never shared, and contact requests wait for the community champion. The partners in the demo are fictional.

**4. See the picture** (`PULSE`).
Members (real and simulated, counted separately), active notices, translations waiting, contact requests waiting, answers approved.

## Safeguards

- Notices and labels never claim more than they know: community notice, not an official warning; English checked, German and Dutch still machine-translated.
- A bilingual check never changes an answer silently: it only approves, or sends it back to be re-recorded.
- Members receive an opt-out line on every SMS. A real roster would store phone numbers only with each member's consent.
- Only Noor is a real member in the demo. The other members are simulated and are never messaged.

## What would come next with real communities

- A consented member roster per circle, and sign-in for each champion instead of a demo PIN.
- Training for community champions, run through existing associations.
- A shared view of what visitors ask across a circle (counts only), so the circle records the answers nobody has yet.
- Linking notices to official sources where an agency publishes a feed.
- A native Wolof speaker to review all Wolof wording, starting with the notices.

All Wolof in the app is machine-written and unverified by a native speaker.
