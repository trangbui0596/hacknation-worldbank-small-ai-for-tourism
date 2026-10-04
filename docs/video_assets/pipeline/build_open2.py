import json, subprocess, sys
def run(cmd):
    r=subprocess.run(cmd,capture_output=True,text=True)
    if r.returncode: print(" ".join(cmd)[:300]); print(r.stderr[-2500:]); sys.exit(1)
ENC=["-r","30","-c:v","libx264","-crf","20","-preset","fast","-pix_fmt","yuv420p","-c:a","aac","-ar","44100","-ac","2","-b:a","160k"]
D=8.4
T=[0.0,2.5,4.7,6.0]            # page start times
PAGES=["s0","s1","s2","s3"]
LAB=[("1",0.25,2.5),("2",2.95,4.7),("3",5.15,5.95)]
# pan/zoom per page (zoompan expressions, in/out)
ZP=["z='1.0+0.00045*on':x='(iw-iw/zoom)*0.9':y='(ih-ih/zoom)*0.5'",
    "z='1.10-0.00040*on':x='(iw-iw/zoom)*0.15':y='(ih-ih/zoom)*0.6'",
    "z='1.0+0.00060*on':x='(iw-iw/zoom)*0.45':y='(ih-ih/zoom)*0.4'",
    "z='1.0+0.00035*on':x='(iw-iw/zoom)*0.5':y='(ih-ih/zoom)*0.55'"]
inputs=[]
for i,p in enumerate(PAGES):
    dur=D-T[i]+0.2
    inputs+=["-loop","1","-framerate","30","-t",f"{dur}","-i",f"pc/{p}.png"]
base=4
for l,_,_ in LAB: inputs+=["-loop","1","-framerate","30","-t",str(D),"-i",f"cl/lab_{l}.png"]
base2=base+3
inputs+=["-loop","1","-framerate","30","-t",str(D),"-i","cl/reveal_mask.png","-loop","1","-framerate","30","-t",str(D),"-i","cl/reveal_shadow.png","-loop","1","-framerate","30","-t",str(D),"-i","cl/title_ov.png"]
rm,rs,ti=base2,base2+1,base2+2
narr=[("o1g",0.3),("o2",2.6),("o3",4.8)]
ab=ti+1
for k,s in narr: inputs+=["-i",f"v3/vo/{k}.mp3"]
fc=[]
for i,p in enumerate(PAGES):
    if i==0: fc.append(f"[{i}:v]scale=2880:1620:flags=lanczos,zoompan={ZP[i]}:d=1:s=1920x1080:fps=30,setsar=1,format=rgba[pg{i}]")
    else: fc.append(f"[{i}:v]scale=3150:1770:flags=lanczos,zoompan={ZP[i]}:d=1:s=2100x1180:fps=30,crop=1920:1180,setsar=1,format=rgba[pg{i}]")
fc.append(f"[pg0]setpts=PTS-STARTPTS[b0]"); last="[b0]"
for i in (1,2,3):
    t=T[i]
    fc.append(f"[pg{i}]null[pp{i}]")
    fc.append(f"[pp{i}][{rm}:v]alphamerge,setpts=PTS-STARTPTS+{t}/TB[pa{i}]")
    fc.append(f"[{rs}:v]format=rgba,setpts=PTS-STARTPTS+{t}/TB[sh{i}]")
    y=f"-50+1180*pow(max(0,1-(t-{t})/0.7),3)"
    fc.append(f"{last}[sh{i}]overlay=x=0:y='{y}+8':enable='gte(t,{t})':eof_action=repeat[ws{i}]")
    fc.append(f"[ws{i}][pa{i}]overlay=x=0:y='{y}':enable='gte(t,{t})':eof_action=repeat[w{i}]"); last=f"[w{i}]"
# labels (drop in with a small overshoot, fade out before the next page tears over)
for j,(l,a,b) in enumerate(LAB):
    li=base+j
    fc.append(f"[{li}:v]format=rgba,fade=t=in:st={a}:d=0.01:alpha=1,fade=t=out:st={b-0.15}:d=0.15:alpha=1[lb{j}]")
    fc.append(f"{last}[lb{j}]overlay=x=0:y='-420*pow(max(0,1-(t-{a})/0.35),3)+8*sin((t-{a})*18)*max(0,1-(t-{a})/0.5)*gte(t,{a})':enable='between(t,{a},{b})':eof_action=repeat[lx{j}]"); last=f"[lx{j}]"
fc.append(f"{last}fps=12,noise=alls=7:allf=t,fps=30,format=rgba[stp]")
fc.append(f"color=c=black:s=1920x1080:r=30:d={D},format=rgba,fade=t=in:st=6.7:d=0.4:alpha=1,colorchannelmixer=aa=0.62[dim]")
fc.append(f"[stp][dim]overlay=0:0:eof_action=repeat[dd]")
fc.append(f"[{ti}:v]format=rgba,fade=t=in:st=6.95:d=0.35:alpha=1[tt]")
fc.append(f"[dd][tt]overlay=0:0,fade=t=in:d=0.3,fade=t=out:st={D-0.35}:d=0.35,format=yuv420p[v]")
labs=[]
for i,(k,s) in enumerate(narr):
    fc.append(f"[{ab+i}:a]aresample=44100,aformat=channel_layouts=stereo,adelay={int(s*1000)}|{int(s*1000)}[n{i}]"); labs.append(f"[n{i}]")
fc.append("".join(labs)+f"amix=inputs={len(labs)}:duration=longest:normalize=0,apad,atrim=0:{D},afade=t=out:st={D-0.3}:d=0.3[a]")
out=sys.argv[1] if len(sys.argv)>1 else "v4/seg_o2.mp4"
run(["ffmpeg","-v","error","-y",*inputs,"-filter_complex",";".join(fc),"-map","[v]","-map","[a]","-t",str(D),*ENC,out]); print("ok",out)
