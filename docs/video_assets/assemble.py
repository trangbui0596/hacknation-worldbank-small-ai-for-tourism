#!/usr/bin/env python3
"""Assemble the Teranga demo video from screen clips + narration.

Put one clip per scene in ./clips/ named like the narration files (00_problem.mp4, 01_idea.mp4 ... 09_limits.mp4).
Scenes without a clip are skipped. Each clip is scaled to 1080p, trimmed or frozen on its last frame to match the
narration, and the narration is laid over it. Title, limits and end cards are added. Output: ./teranga_demo.mp4
Needs ffmpeg. Run: python3 assemble.py
"""
import glob, json, os, subprocess, sys

W, H, FPS = 1920, 1080, 30
here = os.path.dirname(os.path.abspath(__file__))
os.chdir(here)
scenes = json.load(open("narration.json"))
os.makedirs("build", exist_ok=True)

def run(*a):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *a], check=True)

def still(png, secs, out, audio=None):
    args = ["-loop", "1", "-t", str(secs), "-i", png]
    args += ["-i", audio] if audio else ["-f", "lavfi", "-t", str(secs), "-i", "anullsrc=r=44100:cl=stereo"]
    run(*args, "-vf", f"scale={W}:{H},fps={FPS},format=yuv420p", "-c:v", "libx264", "-c:a", "aac", "-shortest", out)

parts = []
still("cards/01_title.png", 3, "build/title.mp4"); parts.append("build/title.mp4")
for s in scenes:
    name, dur = s["scene"], s["seconds"] + 0.8
    clips = glob.glob(f"clips/{name}.*")
    if not clips:
        print("no clip for", name, "(skipped)"); continue
    out = f"build/{name}.mp4"
    labels = sorted(glob.glob(f"clips/{name}.label_*.png"))  # optional overlay, e.g. clips/02_call.label_synthetic.png
    vf = f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=0xfdf3e1,fps={FPS},tpad=stop_mode=clone:stop_duration={dur},format=yuv420p"
    cmd = ["-i", clips[0], "-i", f"vo/{name}.mp3"]
    if labels:
        cmd += ["-i", labels[0], "-filter_complex", f"[0:v]{vf}[b];[2:v]scale={W}:{H}[l];[b][l]overlay=0:0[v]", "-map", "[v]", "-map", "1:a"]
    else:
        cmd += ["-vf", vf, "-map", "0:v", "-map", "1:a"]
    run(*cmd, "-t", str(dur), "-c:v", "libx264", "-c:a", "aac", "-ar", "44100", out)
    parts.append(out)
    if name == "08_coaching":
        still("cards/02_limits.png", 4, "build/limits.mp4"); parts.append("build/limits.mp4")
still("cards/03_end.png", 4, "build/end.mp4"); parts.append("build/end.mp4")
open("build/list.txt", "w").write("".join(f"file '{os.path.basename(p)}'\n" for p in parts))
run("-f", "concat", "-safe", "0", "-i", "build/list.txt", "-c", "copy", "teranga_demo.mp4")
print("done: teranga_demo.mp4")
