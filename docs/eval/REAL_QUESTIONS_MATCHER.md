# Does the answer matcher guess? A test on 82 real questions

Date: 2026-10-04. Code: `teranga-gambia/src/lib/match.ts`. Questions: `docs/data/gambia_tour_questions.json`
(copy used by the tests: `teranga-gambia/src/test/fixtures/gambia_tour_questions.json`).

## The short version

- Teranga makes one promise: when a visitor asks something Noor has not answered, the system says
  **"Not sure, Noor will answer"** and passes the question to her. It never guesses.
- Until now that promise was checked on only 20 questions written by an agent. This time we used **82 real
  questions** copied from the public FAQ pages of 10 Gambian tour websites.
- **First pass (before any change):** for questions Noor has no answer for, the system gave an answer anyway
  **17 times out of 37 (46%)**. The promise was broken almost every second time.
- **After the fix:** 0 out of 37. For questions Noor does have an answer for, right answers went from 32 to 40 out of 45
  and wrong-topic answers from 2 to 0.
- **Read the "after" numbers with care.** The same 82 questions were used to find the problems, so they are better than
  what to expect on new questions.
- **The real test is a fresh set nobody tuned on.** It was run once afterwards on 103 other real questions: 4 of 58
  out-of-scope questions (7%) still got an answer, 0 of 45 in-scope questions got a wrong-topic answer, and 12 of 45 got
  "Not sure" (see "Untuned check on a fresh set").

## What was tested and why

The matcher is a list of words. Each of Noor's ten answers (price, meeting point, duration, what to bring, children, food,
safety, what's included, how to book, cancellation) has a list of English, German and Dutch words. A visitor's question is
compared with the lists. If one topic clearly wins, the visitor gets Noor's approved answer for it. If not, the visitor
gets "Not sure, Noor will answer."

There is no AI in this step, so the result can be checked exactly. What can go wrong is a coincidence: a common word like
"need" or "time" appears in a question that has nothing to do with the topic that owns the word.

## The data

| Site | Questions |
|---|---|
| Gambia Jobe Tours & Travel (4 tour pages) | 15 |
| The Gambia Experience | 14 |
| Gambia Tourism Authority (visitthegambia.com) | 12 |
| SenGambia Experience Tours | 9 |
| Footsteps Eco-Lodge | 8 |
| Alkamba Tours & Travel | 7 |
| Gambia Tours, Senegal Trips (gambiantour.com) | 6 |
| Bushwhacker Tours | 6 |
| Gambia Birding Tours | 4 |
| Wikivoyage (Talk:Gambia) | 1 |
| **Total** | **82** |

- 81 of the 82 are **search-tool text extracts**, not text read on the page itself: the sandbox used for collecting could not
  open the operator sites. Only the Wikivoyage question was read directly. See `docs/data/README.md` for the details.
- 6 questions (all Bushwhacker Tours) were written as questions by the collector from answer blocks on the page.
- All 82 are English. They are FAQ headings written by businesses, not messages typed by visitors.
- The topic label on each question (and so the split below) is **the collector's own judgment**.
- 45 questions belong to one of Noor's ten topics ("in scope"): how to book 11, safety 9, meeting point 5, food 4,
  what to bring 4, what's included 4, children 3, cancellation 2, duration 2, price 1. The other 37 are marked "other":
  visa, vaccines, money, weather, flights and similar, which Noor's ten answers do not cover.
  Price and duration have only 1 and 2 questions, so these results say little about those two topics.

## How a question is scored

- **In scope:** *right* (the correct topic's answer), *wrong* (another topic's answer), or *Not sure* (safe, but a miss).
- **Out of scope:** *Not sure* is the right behaviour. Any answer is a broken promise.

## First pass: the matcher before any change

| | Questions | Right answer | Wrong answer | Not sure |
|---|---|---|---|---|
| In scope (Noor has an answer) | 45 | 32 (71%) | 2 (4%) | 11 (24%) |
| Out of scope (no answer exists) | 37 | | **17 answered (46%)** | 20 Not sure (54%) |

What went wrong, in plain words:

1. **One everyday word was enough.** 14 of the 17 wrong answers came from a single common word: "need" (6 times, for
   example "Do I need a visa?" got the *what to bring* answer), "time" (3, "When is the best time to visit?" got the
   *duration* answer), "pay" (3, "Which currency can I pay in?" got the *price* answer), "money" (1) and "kind" (1).
2. **A word that means something else in German and Dutch.** "kind" means "child" there, so "What kind of vaccines do I
   need?" got the *children* answer.
3. **Subjects Noor never covers had no handling.** Visa, passport, vaccines, cards and cash machines, currency, time
   difference, airport. In 3 of the 17 a clear word like "book" or "insurance" sat in a question about something else
   ("How can I book assistance at the airport?").
4. **Misses.** 11 real in-scope questions got "Not sure". For 9 of them the lists simply lacked plain words such as shark,
   crime, swim, dress code, special diets, private tours.

## What I changed, rule by rule

1. **One weak word is not enough.** Everyday words that appear in questions about everything ("need", "time", "where",
   "pay", "bring") no longer decide a topic. A topic needs at least one specific word ("refund", "vegetarian", "life jacket").
   A short list of exceptions lets a few weak words stand alone for one topic only: "start" (meeting point), "age"
   (children), "include" (what's included), "booking" (how to book) and "drinks" (food). A bare "bring" does not count
   ("Can I bring my laptop?"), but phrases like "what should I bring" do.
2. **One word, one vote.** "child" and "children" are one word in two spellings and used to count twice. Now they count once.
   Questions that mix two topics ("Is lunch included?", "Is it safe for children?") end in "Not sure" instead of a coin flip.
3. **The longest phrase wins.** "how much time" is a duration question, not price; "change my booking" is cancellation, not
   booking; "included in the price" is what's included, not price.
4. **Words that mean something else in another language only count inside a phrase.** "kind", "alter" and "hat" now need a
   phrase such as "mein Kind", "mijn kind" or "welchem Alter". I also dropped the English word "boots" because it matches the
   start of the German "Bootstour" (boat tour).
5. **Subjects Noor has no answer for always go to Noor,** even if the question also has a clear word like "book" or "cost".
   Covered: visa, passport, vaccines, malaria, travel insurance, doctors and hospitals; cash, cards, cash machines,
   currency, exchange, tipping; flights, airport, luggage, taxis, time difference; tap water; languages spoken by guides;
   pets and swimming pools; opening hours; restaurants, "nearby" and "nearest"; nature reserves; "how long have you been in
   business". The list has about 150 entries in English, German and Dutch. I first tried the softer rule (decline only when no
   clear word is present). It still answered 2 of the 37 real out-of-scope questions, because "book" counts as a clear word,
   and it gained no extra right answers, so I made the rule strict.
6. **Hotel words only count in pick-up questions.** "Can you pick us up from our hotel?" works. "Is breakfast included at the
   hotel?" or "Can I book a hotel through you?" go to Noor.
7. **Money and weather words cancel weak guesses.** With "euros", "pay", "rain", "season" or "weather" in the question only a
   specific word may answer: "When does the rainy season start?" gets "Not sure", "Can I cancel because of bad weather?"
   still gets the cancellation answer.
8. **More plain topic words in English, German and Dutch,** for example shark, crime, "swim in", licensed (safety); dress code,
   clothes, sunscreen (what to bring); special diets, vegan, dishes (food); private tours, custom tours, group bookings (how
   to book); discount, rates (price). The word lists grew from about 150 to about 420 entries. None of them is a whole question
   copied from the 82.
9. **Ties never guess (kept from before).** If two topics have equal evidence the answer is "Not sure". A topic with more
   specific words beats one with weaker words.

A visitor still sees the same sentence as before when the matcher is unsure: "Not sure, Noor will answer."

## After: the same 82 questions, current matcher

| | Questions | Right answer | Wrong answer | Not sure |
|---|---|---|---|---|
| In scope (Noor has an answer) | 45 | **40 (89%)** | **0** | 5 (11%) |
| Out of scope (no answer exists) | 37 | | **0 answered** | **37 Not sure (100%)** |

Compared with the first pass: out-of-scope answers 17 to 0; wrong in-scope answers 2 to 0; right in-scope answers 32 to 40;
in-scope "Not sure" 11 to 5. Of the 82 results, 29 changed (listed in the appendix). The 20 agent-written questions
from the earlier check still get 20 of 20 right.

The numbers are stored in `teranga-gambia/src/lib/match-eval-results.ts` (`REAL_QUESTION_RESULTS`). The test
`src/test/real-questions-matcher.test.ts` fails if the matcher stops producing exactly these numbers, so any page text that
quotes them must import them from there.

## Untuned check on a fresh set

After the matcher was finished, it was evaluated once on **103 other real questions from 14 other sites**, collected afterwards
(`teranga-gambia/src/test/fixtures/gambia_tour_questions_holdout.json`; the numbers are stored as `HOLDOUT_RESULTS` in
`src/lib/match-eval-results.ts`). No rule has been changed since these numbers were recorded (code formatting only). I have
not read those questions or the individual results; the labels are the collector's judgment, as before.

| | Questions | Right answer | Wrong answer | Not sure |
|---|---|---|---|---|
| In scope (Noor has an answer) | 45 | 33 (73%) | 0 | 12 (27%) |
| Out of scope (no answer exists) | 58 | | **4 answered (7%)** | 54 Not sure (93%) |

What this says:

- The gap between the 82 questions we tuned on and the fresh set is the optimism described below: out-of-scope answers went
  from 0 of 37 to 4 of 58, and in-scope "Not sure" from 11% to 27%. Why the 4 and the 12 happened has not been analysed yet;
  the likely causes are words and phrasings the lists do not know.
- The part of the promise that matters most mostly holds on questions nobody tuned on: 54 of 58 out-of-scope questions get
  "Not sure", and no in-scope question got another topic's answer. The old matcher answered 46% of out-of-scope questions on the
  82, but this report has no old-matcher number for the fresh set, so the two are not a like-for-like comparison.
- 4 broken promises out of 58 is not zero. Those 4 (and the 12 misses) are what to study next. Fix them with general rules, then
  test on yet another fresh set, because this one has now been used.
- The test `untuned holdout` in `src/test/real-questions-matcher.test.ts` fails whenever the matcher stops scoring exactly these
  numbers. After any rule change the numbers must be updated, and from then on this set is no longer untuned.

## Remaining failures on these 82 questions

No out-of-scope question is answered and no in-scope question gets a wrong-topic answer. Five in-scope questions get
"Not sure":

| Question (label) | Why |
|---|---|
| Can I go on safari? (how to book) | Nothing in it says "book"; the label itself is a stretch. |
| Can you build a custom Gambia itinerary? (how to book) | "custom" and "itinerary" are not next to each other, and "custom" alone would also match "customs". |
| How can I pay for my holiday? (how to book) | "pay" is a weak word. It was a *wrong* answer (price) before; "Not sure" is the safer result. |
| Is lunch included? (food) | Two topics tie (food, what's included). It was a wrong answer (what's included) before. |
| Is it safe to travel with children? (children) | Two topics tie (safety, children). It was right before, by an accident of double counting. |

## Caveats

1. **The "after" numbers on the 82 are optimistic.** The rules and word lists were developed while looking at these 82
   questions, including the choice of which plain words to add. The fresh set confirms it: 4 of 58 out-of-scope questions were
   answered and 27% of in-scope questions got "Not sure". Use the fresh-set numbers as the honest estimate, and expect them
   to move a little with every new set.
2. **The labels are one person's judgment.** Several are debatable (for example "Can I go on safari?" as *how to book*, "Is
   lunch included?" as *food*, "How much do things cost?" as *price*).
3. **English only.** There are no real German or Dutch questions. German and Dutch behaviour is covered only by the older
   agent-written tests and by the new rule tests I wrote, so its quality on real questions is unknown.
4. **Weak source.** 81 of 82 are search-tool extracts of business FAQ headings, not visitor messages and not read on the page.
5. **Small and not random.** 82 questions from 10 sites, with 1 price and 2 duration questions.
6. **More caution means more "Not sure".** That is the price of the promise: Noor answers more questions herself. One question that
   used to be answered correctly is now "Not sure" (the children and safety tie above).
7. **Known weak spots** found in my own extra checks (below): the system cannot tell what a price is *for*, so "How much is the
   national park entrance?" still gets the tour price; "Is it safe to eat street food?" gets the food answer; a question that
   uses words the lists do not know is not recognised in either direction.
8. **Bigger word lists, more room for surprises,** especially German and Dutch words that happen to match another word.

## Extra checks (not evidence)

To see whether the rules hold beyond the 82, I wrote 606 more questions myself: English, German and Dutch, tricky ones with
in-scope words in other senses, and short WhatsApp-style messages. Old matcher against current matcher:

| | Old matcher | Current matcher |
|---|---|---|
| Out-of-scope questions answered (of 282) | 93 (33%) | 3 (1%) |
| In-scope: right / wrong / Not sure (of 324) | 213 / 20 / 91 | 285 / 1 / 38 |

These questions were written by the same person who wrote the rules, partly after seeing the first results, so they are **not
independent** and are not stored in the repository. They show that the rules are not limited to the 82; they do not predict the
fresh-set result.

## Where things are

- Matcher and its rules: `teranga-gambia/src/lib/match.ts`
- Scoring harness: `src/lib/match-eval.ts`; published numbers (82 questions and the fresh set): `src/lib/match-eval-results.ts`
- Tests: `src/test/real-questions-matcher.test.ts` (the 82 questions) and `src/test/match-topics.test.ts` (the rules)
- Run: `npx vitest run src/test/real-questions-matcher.test.ts src/test/match-topics.test.ts`

## Appendix: the 29 questions whose result changed

Out of scope (all 17 were answered before, all are "Not sure" now):

| Question | First pass answered with |
|---|---|
| Do I need a visa to visit The Gambia? | what to bring |
| Do you need vaccinations to visit The Gambia? | what to bring |
| Do I need travel insurance and when should I take this out? | safety |
| What is the currency in The Gambia and how can I pay? | price |
| Is there any time difference between here and The Gambia? | duration |
| Do I need a visa to visit Senegal? | what to bring |
| How can I book assistance at the airport? | how to book |
| Do I need a passport for any of the tours? | what to bring |
| Can I book a Polish-speaking guide in Gambia? | how to book |
| When is the best time to visit The Gambia? | duration |
| Do I need cooking experience? | what to bring |
| Which currency can I pay in? | price |
| Do i need a visa? | what to bring |
| What kind of vaccines do I need? | children |
| Where can I exchange the money - is there ATMs? | price |
| Can I use credit or debit cards to pay for goods and services? | price |
| When is the best time to go? | duration |

In scope (12):

| Question (label) | First pass | Now |
|---|---|---|
| Are you a licensed and registered tourism operator? (safety) | Not sure | right |
| Can you organise private tours for our group? (how to book) | Not sure | right |
| Do you offer private tours in Gambia? (how to book) | Not sure | right |
| Can I swim in the Gambia River? (safety) | Not sure | right |
| What traditional Gambian dishes will we prepare? (food) | Not sure | right |
| Are there sharks? (safety) | Not sure | right |
| Is there a lot of crime? (safety) | Not sure | right |
| What is the common dress code? (what to bring) | Not sure | right |
| Do you cater for special diets? (food) | Not sure | right |
| How can I pay for my holiday? (how to book) | wrong (price) | Not sure |
| Is lunch included? (food) | wrong (what's included) | Not sure |
| Is it safe to travel with children? (children) | right | Not sure |
