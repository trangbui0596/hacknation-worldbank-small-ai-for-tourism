#!/usr/bin/env bash
# Removes the spoken "Music licensing reimagined" watermark of the Artlist PREVIEW file of "Third Pulse"
# (found at 30.6-32.8 s) by replacing 30.39-33.41 s with a beat-aligned bar from earlier in the same track
# (99.4 bpm, bar = 2.414 s; copy offset = 2 bars). The preview also says "Artlist.io" at 60.6 s (after the video ends).
# For the final submission use the licensed clean download from Artlist instead and skip this script.
# usage: clean_music.sh Third_Pulse.mp3 music_clean.wav
set -euo pipefail
ffmpeg -v error -y -i "$1" -filter_complex "
[0:a]atrim=0:30.43,asetpts=PTS-STARTPTS,afade=t=out:st=30.39:d=0.04[p1];
[0:a]atrim=25.56:28.62,asetpts=PTS-STARTPTS,afade=t=in:d=0.04,afade=t=out:st=3.02:d=0.04,adelay=30390|30390[p2];
[0:a]atrim=33.37:75,asetpts=PTS-STARTPTS,afade=t=in:d=0.04,adelay=33370|33370[p3];
[p1][p2][p3]amix=inputs=3:duration=longest:normalize=0[m]" -map "[m]" -ar 44100 "$2"
