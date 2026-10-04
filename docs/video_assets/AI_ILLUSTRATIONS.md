# AI-generated illustrations used in the 60-second video

All paper-collage art in the video is AI-generated and must be credited as "AI-generated illustration".
Model: Higgsfield `gpt_image_2_5` (about 0.25 credit each, about 5 credits in total). Nothing here depicts a real person; the figures
(a tourist, "Noor", a community champion, three neighbours) are invented. The real WhatsApp screen recordings are the only live footage.
The Higgsfield `/paper-collage` command itself needs Adobe After Effects on a desktop, so we generated the cut-paper layers and
animated them with Pillow and ffmpeg (`docs/video_assets/pipeline/`).

Shared style words: "layered torn cut-paper collage, visible paper fibre, matte, soft shadows, cream / teal / bronze / mustard".

| Layer | What was asked for |
| --- | --- |
| Opening pages (3) | Tourist in a sun hat typing a message on a paper beach with a bubble "Guten Tag!"; Noor with a basic button phone and an unread-envelope icon; close-up of a paper hand holding the phone with an unread envelope |
| Backdrop layers | Teal paper sky with a mustard sun; strip of Banjul skyline (Arch 22, mosque, baobab, colonial buildings); torn-paper river with a pirogue; two rocky banks |
| Closing scene | A bridge of six postage stamps (palm, arch, heron, sun, sailboat, baobab) and a paper plane with a dashed trail |
| Cut-out figures | Full-length tourist (hat, backpack, phone); Gambian woman in a patterned dress and headwrap with a basic phone; older community champion in an indigo boubou; three neighbours (woman with a baby, young man in a yellow shirt, elderly woman) |
| Foreground | Hibiscus, marigold, delphinium and palm fronds |
| Not used in the final cut | "NEXT" cards (SMS phone, speech bubbles with an ear, paper globe) |

Figures were cut out from a plain white background with a flood fill (`pipeline/cut.py`) and given a thin white "cut paper" border.
