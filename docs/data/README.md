# Real Gambia tour data (questions, prices, exchange rate)

Collected on **2026-10-04** to replace invented test data with real, sourced public data.
Everything here comes from a public page and carries its link. Nothing is invented. The only text I wrote
myself is the six rewritten questions and the topic labels, and both are flagged below.

## Read this first: how much was checked on the page itself

Almost all Gambian operator websites were **blocked by the network policy of the sandbox** I worked in
(the fetch tool answered "EGRESS_BLOCKED" for 22 hosts, see the end of this file).
So I could not open those pages and read them myself. What I did instead:

- **Direct reads (verified on the page):** the Wikivoyage entries (4 prices, 1 question) and the World Bank exchange rate.
- **Search-tool extracts (not read on the page):** everything else. The search tool returns a short text
  written from the page content. It is not a copy of the page. I limited each search to one operator's
  site where I could, and asked for headings or prices.

Every record has a `capture` field: `direct_fetch` or `search_extract`. Treat `search_extract`
records as "very likely right, please spot-check the link before you show them in a demo".

Why I am careful: in repeat searches the same operator's price for the same tour sometimes came back
different (for example Jobe Tours prices 5 EUR apart; I cannot tell whether that was the search tool or two
different pages on the site). So I kept a price only when at least two separate searches returned the same
figure, currency and basis; where they differed I used the figure that the page-specific searches agreed on
(Jobe Tours: Kunta Kinteh, Makasutu, home cooking, Fathala) or dropped the entry. This lowers the risk of errors but does not remove it.

## Files

| File | What it is | Entries |
|---|---|---|
| `gambia_tour_questions.json` | Short visitor-style questions about booking and joining tours (and some off-topic ones) | 82, from 10 sites |
| `gambia_tour_prices.json` | Publicly listed prices for tours and excursions | 61, from 16 operators or listings on 12 sites |
| `exchange_rate.json` | World Bank official GMD per USD rate | 1 (2025 value, 2024 and 2023 for context) |
| `README.md` | This note | |

### Question fields
`question`, `language` (all `en`), `source_url`, `source_name`, `retrieved` (2026-10-04),
`topic_label`, `rewritten` (true/false), `capture`.

- Wording is kept as published, including quirks: "Is it safe in The Gambia" (no question mark),
  "can I book and pay for my holiday online?" (lower case), "Do i need a visa?".
- `rewritten: true` (6 questions, all from the Bushwhacker Tours FAQ) means the page gives answer-form
  blocks (pick-up details, refreshments, what to bring, currency, mosquitoes, what is included), so I wrote a short question for each.
- `topic_label` is **my own judgment**, not the source's. Counts: other 37, how to book 11, safety 9,
  meeting point 5, food 4, what to bring 4, whats included 4, children 3, cancellation 2, duration 2, price 1.
  "Other" holds visas, vaccines, money, weather, flights and similar, which are good for testing that the system says "not sure".
- Only 1 `price` and 2 `duration` questions are in the file. The sources simply ask few of them.
- No German, Dutch or French questions: none of the reachable FAQ pages had them (the Dutch operator sites only gave prices).

### Price fields
`operator`, `tour`, `price`, `currency` (GMD, EUR or GBP), `per`, `duration_hours`, `includes`,
`source_url`, `retrieved`, `page_date`, `capture`.

- Prices are exactly as listed, in the listed currency. **No conversion was done.**
- `per`: `person` (51), `group` (4: three Paradise Fishing trips "for 1-3 or 1-4 persons" and Omi Tours Basse and Fatoto "for two people"),
  `unclear` (6: two FairPlay boat trips listed as "(1-10 people)" and the four Wikivoyage entry fees, which give no unit).
  Do not quote `unclear` entries to a visitor as a per-person price.
- Conditions are written in `includes` (minimum group size, solo-traveller price, what is or is not covered).
  Jobe Tours has a separate solo-traveller rate for each tour; it is in the text, the main price is the per-person group rate.
- `duration_hours` is filled only when the page states one hour figure (Gambia Experience Fathala drive 3 h,
  FairPlay River Gambia National Park 6 h, Footsteps Roots tour 12 h) or two times (Omi Tours cruise: pick-up 9:00,
  back about 17:00 = 8 h). Ranges like "6-8 hours" are left `null` and written in `includes`.
- `page_date` is `null` unless the page shows a date. Only Wikivoyage did ("as of Dec 2025", "04/2026").
  **No operator page showed a date**, so prices may be one to three years old (the search tool suggested the Omi Tours
  Fishing Trip page was over 3 years old).
- Mix: GMD 20, EUR 27, GBP 14.

### Exchange rate
World Bank API, indicator `PA.NUS.FCRF`, country `GMB`, newest year **2025**: **71.2893818242692 GMD per USD**
(annual average of the official rate; 2024 was 67.66, 2023 was 61.10). Source last updated by the World Bank on 2026-07-13.
This is the only rate I recorded. I did not fetch or invent EUR or GBP rates; prices stay in their own currency.

## How it was collected

1. **Exchange rate:** direct request to `https://api.worldbank.org/v2/country/GMB/indicator/PA.NUS.FCRF?format=json&mrv=3` (2 requests).
2. **Direct page reads:** Wikivoyage (robots.txt checked first, only normal `/wiki/` article pages requested): Gambia (read twice),
   Banjul (twice), Kunta Kinteh Island, Serekunda (twice), Yundum, Juffureh, Talk:Gambia (twice), Bakau (404). About 13 requests in all.
   Second reads asked for word-for-word quotes of the listings I kept.
3. **Search:** about 155 web-search queries on 2026-10-04: first broad ones (operator FAQ pages, price lists, German, Dutch and French
   variants), then queries limited to one operator site each. For FAQ pages I asked for the question headings;
   for prices I asked for price, currency, per person or per group, duration and what is included.
4. **Checks:** a question was kept when its wording came back in one search and the page's topics were confirmed by a second one
   (several lists came back twice with the same wording). A price was kept only when two searches agreed (see above).
   Questions longer than 24 words, contact details and personal names were not recorded.
5. **Build:** `gambia_tour_questions.json` and `gambia_tour_prices.json` were generated from a hand-checked list and validated
   (labels, currencies, word counts, duplicates).

Total real requests were about 15, well under the 60 allowed.

## Sources used

| Site | Used for | Capture |
|---|---|---|
| gambia.co.uk (The Gambia Experience) | 14 questions (FAQ page and "How much do things cost?" guide page), 2 prices | search extract |
| alkamba.com | 7 questions (its FAQ repeats some Gambia Experience wording; repeated ones left out) | search extract |
| sengambiaexperiencetours.com | 9 questions (contact page FAQ) | search extract |
| gambiantour.com | 6 questions | search extract |
| footstepsinthegambia.com (Footsteps Eco-Lodge) | 8 questions, 6 prices | search extract |
| gambiajobetoursandtravel.com (Gambia Jobe Tours & Travel) | 15 questions (4 tour pages), 9 prices | search extract |
| bushwhackertours.com | 6 rewritten questions | search extract |
| visitthegambia.com (Gambia Tourism Authority) | 12 of its 28 FAQ questions (institutional questions and topics already covered left out). Its search results also show unrelated casino spam pages, so the site may be compromised; check this FAQ before relying on it | search extract |
| gambia-birdingtours.com | 4 questions | search extract |
| en.wikivoyage.org | 1 question (Talk:Gambia), 4 prices (Arch 22, National Museum, Bijilo Forest Park, Kachikally) | **direct fetch** |
| omitours.com (Omi Tours Gambia) | 12 prices (GMD) | search extract |
| excursies-gambia.nl, gambiasantosudrivesexperiences.com | 6 + 4 prices (EUR, Dutch sites) | search extract |
| janeyatours.com, my-gambia.com (incl. Paradise Fishing Gambia), gambianexcursions.com, fairplaygambia.com, tripsingambia.com | 4 + 7 + 4 + 2 + 1 prices | search extract |

For The Gambia Experience Lazy Day Cruise price, several pages of that site matched the search, so `source_url` is the best-matching page
(the excursions page), and the price may be on a sibling page of the same site.

## Skipped sources and why

- **TripAdvisor:** your policy forbids scraping it. Not fetched. Nothing was taken from it, although it came up in search results.
- **Viator, GetYourGuide, TourRadar, Responsible Travel, G Adventures and similar agencies:** resellers whose terms normally restrict automated copying,
  and their prices are not the operators' own. Not used.
- **Reddit, Quora, Lonely Planet Thorn Tree, HolidayCheck forums:** terms or robots rules do not allow scraping, or content needs a login. Not used.
- **Stack Exchange (Travel) and its API:** the fetch tool refused these hosts. Not used.
- **Operator sites in general:** I did not crawl them. I could not read their robots.txt or terms (blocked), and I did not try to get around
  the block (no mirrors, caches, archives or other proxies).
- **Seen but left out because they could not be confirmed or were off-scope:** the gambiabirdtours.com FAQ (8 headings seen once, not
  repeatable); the Enjoy Gambia price list (3 prices seen once, page says "will be updated to October 2023"); Jobe Tours prices that changed
  between searches or were seen once (Jola Village, MyFarm, Village Life); Footsteps kayaking and village-walk prices that conflicted; Omi Tours Guinea-Bissau
  trips and the excursies-gambia.nl South Senegal trip (outside The Gambia); Gambia Tours (gambiatours.gm) shows "price on request";
  SenGambia, Bushwhacker and Gambia Birding Experience showed no prices; Glow Adventure Xtours is in Punta Cana, not The Gambia.

## Limits

- Small and not random: whoever has a clear FAQ page or price page is over-represented. Ten sites, sixteen operators or listings.
- Prices are operators' own marketing prices, change often, and carry no visible date. Tourists, locals and groups may pay different amounts.
- Mostly search-tool extracts, not page reads (see the top). Numbers and wording can still be wrong; spot-check before demo use.
- `topic_label` and `rewritten` are my judgment. Just under half the questions (37 of 82) are "other".
- These are FAQ headings written by businesses, not raw messages typed by visitors.
- Question wording may differ slightly from the page if the search tool normalised it (for example all-caps headings).

## Licence note

The files hold short factual strings (question headings, prices, tour names) and numbers, each with a link to its source.
The owners keep all rights to their pages. Do not copy whole pages or long descriptions. If an owner asks, remove their entries.
Wikivoyage text is CC BY-SA (credit "Wikivoyage contributors" and keep the link; exact version is on the page footer).
World Bank data is published under CC BY 4.0 by default (credit the World Bank). Contact details seen in the extracts
(phone numbers, emails, personal names) were deliberately not recorded; business names only.

## To get direct-read verification (needs one setting change)

Allow these hosts under the environment's Network access (Custom, add to Allowed domains), start a new session, and re-run the
collection so each record can be read on its page:
`www.omitours.com`, `janeyatours.com`, `www.gambiajobetoursandtravel.com`, `www.my-gambia.com`, `www.gambia.co.uk`,
`www.gambianexcursions.com`, `www.fairplaygambia.com`, `www.tripsingambia.com`, `www.excursies-gambia.nl`,
`gambiasantosudrivesexperiences.com`, `footstepsinthegambia.com`, `alkamba.com`, `www.sengambiaexperiencetours.com`,
`www.gambiantour.com`, `bushwhackertours.com`, `visitthegambia.com`, `gambia-birdingtours.com`.
Also blocked in my tests but not used: `www.enjoygambia.com`, `www.gambiatours.gm`, `www.africatouroperators.org`,
`www.travellersquest.com`, `www.gambiabirdtours.com`.

## Hold-out questions (second batch): `gambia_tour_questions_holdout.json`

A fresh set for an untuned test of the keyword matcher. **103 questions from 14 sites that are not in the first file**
(checked by site and by exact wording; no question is repeated from the first file). I did not open the matcher or its
keyword lists, and I did not adjust any wording: it is copied as published (collected 2026-10-04).

- **Fields:** same as the first file plus `region`. `region` is `gambia` for 98 (Gambian business, official page, or a page about
  The Gambia) and `other` for 5 (a Ghana operator FAQ, 2; a South Senegal trip page of a Gambian operator, 3).
  `capture` is `search_extract` for all 103, `rewritten` is `false` for all. Nothing could be read on the page: all 14 source hosts
  are blocked in the sandbox (see the last bullet). The only reachable site, Wikivoyage, has no further visitor questions on its Gambia talk pages.
- **Sources (count):** Explorer Gambia page FAQs 21; SeneGambia Travel guide FAQs 15 (a guide site that also lists hotels and tours,
  so drop these 15 if you treat it as a reseller); Senegambia Birding FAQ 14; Evergreen Eco Retreat FAQ 12; Lemon Creek Hotel FAQ and two
  blog titles 10; Gambia Birding Tour FAQ 9 (`gambiabirdingtour.com`, a different site from `gambia-birdingtours.com` in the first file;
  search results also show spam pages on it); Visit Gambia to Support Gambia 8 (4 FAQ, 4 page titles); Janeya Tours guide FAQ 4;
  Embassy of The Gambia in Brussels FAQ 4; Time4Africa Tours (Ghana) FAQ 2; four price-type page titles from BudgetYourTrip,
  The World Travel Index, Lovely Camel and SizzleRoom. The question part of each title is kept, the rest of the title is dropped.
- **Label mix (my judgment):** other 58, safety 11, how to book 8, what to bring 8, children 5, price 4, whats included 3,
  food 3, duration 3, meeting point 0, cancellation 0. The sources had no meeting-point or cancellation questions.
  Airport-transfer questions ("Do you supply an Airport Service?") are labelled `other`, not `meeting point`. The off-topic share is
  high on purpose (visas, vaccines, money, electricity, internet, photography, flights, language, tipping, alcohol, pets).
- **How questions were kept:** the exact wording had to come back in at least two separate searches (page titles: in at least two result
  lists). Two exceptions: "How long does the Barra ferry take?" (one search plus one repeat) and the Kunta Kinteh Island guide, where one
  run gave shorter headings ("How long is the boat trip?"), so I used the wording that came back twice. All-caps headings (Lemon Creek) are in
  sentence case; a missing question mark was added where another run showed one. Left out: questions seen once, headings that are not
  questions ("Special diet (including vegetarian)"), Nepal-trekking template leftovers on some Explorer Gambia pages, consular questions
  (birth certificates, passports), the BudgetYourTrip "How Much Do Tours to the Gambia Cost?" page (it lists tours for sale), forums
  (terms), and My Gambia and kimkim (booking platforms).
- **Caveats:** wording comes from search-tool text, not from the pages, so small differences from the published text are possible.
  Page-title questions (10 of 103) are SEO titles, not typed messages. Several questions come from one template per operator, so
  Explorer Gambia items are alike. Same skip list as above (TripAdvisor, resellers, Reddit, Quora, forums).
- **Blocked for fetching (EGRESS_BLOCKED), so not read directly:** all 14 source hosts (`www.explorergambia.com`, `senegambiatravel.com`,
  `www.senegambiabirding.com`, `evergreengambia.com`, `gambiabirdingtour.com`, `www.lemoncreek.net`, `visitgambiatosupportgambia.com`,
  `janeyatours.com`, `gambiaembassy.eu`, `time4africatours.com`, `www.budgetyourtrip.com`, `theworldtravelindex.com`, `lovelycamel.com`,
  `sizzleroom.com`) and also `feelfreegambia.com`, `gambia.gov.gm`, `www.gov.uk`, `wwwnc.cdc.gov` and the German, French and Dutch
  Wikivoyage. About 160 searches and 3 Wikivoyage requests (Talk:Banjul read, 2 pages not found) were used.
