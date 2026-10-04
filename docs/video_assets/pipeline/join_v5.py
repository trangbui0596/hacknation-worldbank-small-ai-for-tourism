import subprocess,sys
DIR={"o":"v4","n":"v5","t":"v5","c":"v5","e":"v5"}
order=[("o","fade"),("n","fade"),("t","slideleft"),("c","slideleft"),("e","fade")]
def dur(p): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p]).decode())
names=[o[0] for o in order]; D=[dur(f"{DIR[n]}/seg_{n}.mp4") for n in names]
T=0.5
inputs=[]; 
for n in names: inputs+=["-i",f"{DIR[n]}/seg_{n}.mp4"]
inputs+=["-i","music_clean.wav"]
fc=[]; offs=0.0; prev="[0:v]"; aprev="[0:a]"
for i in range(1,len(names)):
    offs+=D[i-1]-T
    tr=order[i][1]
    fc.append(f"{prev}[{i}:v]xfade=transition={tr}:duration={T}:offset={offs:.3f}[x{i}]"); prev=f"[x{i}]"
    fc.append(f"{aprev}[{i}:a]acrossfade=d={T}[ax{i}]"); aprev=f"[ax{i}]"
total=sum(D)-T*(len(names)-1)
fc.append(f"{aprev}apad=pad_dur=3,atrim=0:{total:.3f},asplit=2[vv][vk]")
fc.append(f"[{len(names)}:a]atrim=0:{total:.3f},asetpts=PTS-STARTPTS,aresample=44100,aformat=channel_layouts=stereo,volume=0.55,afade=t=in:d=1.2,afade=t=out:st={total-2:.3f}:d=2[m0]")
fc.append("[m0][vk]sidechaincompress=threshold=0.02:ratio=10:attack=15:release=450:makeup=1[md]")
fc.append(f"[vv][md]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-15:TP=-1.5:LRA=9,atrim=0:{total:.3f}[a]")
cmd=["ffmpeg","-v","error","-y",*inputs,"-filter_complex",";".join(fc),"-map",prev,"-map","[a]","-t",f"{total:.3f}","-r","30","-c:v","libx264","-crf","25","-maxrate","2200k","-bufsize","4400k","-preset","medium","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","demo_v5.mp4"]
r=subprocess.run(cmd,capture_output=True,text=True)
if r.returncode: print(r.stderr[-1500:]); sys.exit(1)
print("ok",total)
