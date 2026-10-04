import json, os, subprocess, sys
CL="../clips/"
def run(cmd):
    r=subprocess.run(cmd,capture_output=True,text=True)
    if r.returncode: print(" ".join(cmd)[:300]); print(r.stderr[-2200:]); sys.exit(1)
def dur(p): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p]).decode())
ENC=["-r","30","-c:v","libx264","-crf","21","-preset","fast","-pix_fmt","yuv420p","-c:a","aac","-ar","44100","-ac","2","-b:a","160k"]
def piece(i,clip,ss,to,speed,audio):
    out=f"tmp5/s{i}.mp4"; L=(to-ss)/speed
    if clip=="J": vf=("drawbox=x=0:y=135:w=480:h=525:color=0xF8BEC7:t=fill,"f"setpts=PTS/{speed},scale=424:920:flags=lanczos,fps=30,format=yuv420p")
    else: vf=f"setpts=PTS/{speed},scale=424:920:flags=lanczos,fps=30,format=yuv420p"
    cmd=["ffmpeg","-v","error","-y","-ss",str(ss),"-to",str(to),"-i",CL+clip+".mp4"]
    if audio: cmd+=["-vf",vf,"-af","aresample=44100,aformat=channel_layouts=stereo","-c:a","aac","-b:a","128k"]
    else: cmd+=["-f","lavfi","-t",str(L+0.5),"-i","anullsrc=r=44100:cl=stereo","-map","0:v","-map","1:a","-vf",vf,"-c:a","aac","-b:a","128k","-shortest"]
    cmd+=["-c:v","libx264","-crf","20","-preset","fast",out]; run(cmd); return out
def phone(name,pieces):
    for i,p in enumerate(pieces): os.replace(piece(f"{name}_{i}",*p),f"tmp5/s{name}_{i}.mp4")
    open(f"tmp5/s{name}.txt","w").write("".join(f"file 's{name}_{i}.mp4'\n" for i in range(len(pieces))))
    run(["ffmpeg","-v","error","-y","-f","concat","-safe","0","-i",f"tmp5/s{name}.txt","-c","copy",f"tmp5/s{name}.mp4"]); return f"tmp5/s{name}.mp4"
# overlays: list of (png, start, end, fade_in, fade_out, mode) ; mode "drop" = drops in from above
def act(name,pieces,overlays,narr,pad=0.4):
    pv=phone(name,pieces); P=dur(pv); D=round(P+pad,2)
    L=["-loop","1","-framerate","30","-t",str(D),"-i"]
    inputs=[*L,f"cl5/bg_{name}.png",*L,f"cl5/fig_{name}.png",*L,f"cl5/fg_{name}.png","-i",pv,*L,"v4/mask.png",*L,"v4/shadow.png",*L,"v4/border.png"]
    for o in overlays: inputs+=[*L,o[0]]
    for k,s in narr: inputs+=["-i",f"v5/vo/{k}.mp3"]
    fc=[]
    # backdrop: slow push, then stepped 12 fps with grain
    fc.append(f"[0:v]scale=2112:1188,zoompan=z='1.0+0.0004*on':x='(iw-iw/zoom)*0.5':y='(ih-ih/zoom)*0.5':d=1:s=1920x1080:fps=30,format=rgba[bg]")
    figx={"n":150,"t":90,"c":150}[name]; figy={"n":140,"t":150,"c":130}[name]
    fc.append(f"[1:v]format=rgba[fg1]")
    fc.append(f"[bg][fg1]overlay=x='{figx}-30*pow(max(0,1-t/0.6),3)':y='{figy}+6*sin(t*5.2)+700*pow(max(0,1-t/0.6),3)':eof_action=repeat[w1]")
    fc.append(f"[2:v]format=rgba[fg2]")
    fc.append(f"[w1][fg2]overlay=x='40*pow(max(0,1-t/0.9),3)+(-4*t)':y='30*pow(max(0,1-t/0.9),3)':eof_action=repeat[w2]")
    fc.append(f"[w2]fps=12,noise=alls=6:allf=t,fps=30,format=rgba[stp]")
    # phone card tears up from below
    fc.append("[3:v]scale=424:920,format=rgba[ph]; [ph][4:v]alphamerge[pm]")
    fc.append("[stp][5:v]overlay=628:'-90+1100*pow(max(0,1-(t-0.2)/0.7),3)':eof_action=repeat[s0]")
    fc.append("[s0][pm]overlay=748:'40+1100*pow(max(0,1-(t-0.2)/0.7),3)':eof_action=repeat[s1]")
    fc.append("[s1][6:v]overlay=748:'40+1100*pow(max(0,1-(t-0.2)/0.7),3)':eof_action=repeat[s2]")
    last="[s2]"
    for j,(png,a,b,fi,fo,mode) in enumerate(overlays):
        idx=7+j
        fc.append(f"[{idx}:v]format=rgba,fade=t=in:st={a}:d={fi}:alpha=1,fade=t=out:st={b-fo}:d={fo}:alpha=1[ov{j}]")
        if mode=="drop":
            fc.append(f"{last}[ov{j}]overlay=x=0:y='-420*pow(max(0,1-(t-{a})/0.35),3)+8*sin((t-{a})*18)*max(0,1-(t-{a})/0.5)*gte(t,{a})':eof_action=repeat[o{j}]")
        else: fc.append(f"{last}[ov{j}]overlay=0:0:eof_action=repeat[o{j}]")
        last=f"[o{j}]"
    fc.append(f"{last}fade=t=in:d=0.25,fade=t=out:st={D-0.3}:d=0.3,format=yuv420p[v]")
    base=7+len(overlays); labs=[]
    for i,(k,s) in enumerate(narr):
        fc.append(f"[{base+i}:a]aresample=44100,aformat=channel_layouts=stereo,adelay={int(s*1000)}|{int(s*1000)}[n{i}]"); labs.append(f"[n{i}]")
    fc.append(f"[3:a]apad,atrim=0:{D}[ca]")
    fc.append("[ca]"+"".join(labs)+f"amix=inputs={1+len(labs)}:duration=longest:normalize=0,atrim=0:{D},afade=t=in:d=0.2,afade=t=out:st={D-0.3}:d=0.3[a]")
    run(["ffmpeg","-v","error","-y",*inputs,"-filter_complex",";".join(fc),"-map","[v]","-map","[a]","-t",str(D),*ENC,f"v5/seg_{name}.mp4"]); print(name,"P",round(P,2),"D",D)
which=sys.argv[1:] or ["n","t","c"]
if "n" in which: act("n",[("J",1.5,14.5,1.4,False),("H",0,4.4,1.0,False),("G",0,9,4.0,False),("C",0,14,2.2,False)],
  [("cl5/title_n.png",0.0,1.3,0.05,0.25,"drop"),("cl5/corner_n.png",1.4,22.6,0.2,0.2,"x"),
   ("cl5/qlist.png",1.2,3.7,0.2,0.2,"drop"),("cl5/cap_j1.png",3.8,5.4,0.2,0.2,"drop"),("cl5/cap_j2.png",5.6,9.2,0.2,0.2,"drop"),
   ("cl5/chip_a.png",5.5,7.4,0.2,0.2,"drop"),("cl5/chip_b.png",7.5,9.4,0.2,0.2,"drop"),("cl5/chip_c.png",9.5,15.9,0.2,0.2,"x"),
   ("cl5/cap_h1.png",9.6,11.8,0.2,0.2,"drop"),("cl5/cap_h2.png",11.9,13.7,0.2,0.2,"drop"),("cl5/cap_g1.png",14.1,15.9,0.2,0.2,"drop"),
   ("cl5/coach_h.png",16.5,22.5,0.05,0.25,"drop"),("cl5/coach_1.png",17.3,22.5,0.05,0.25,"drop"),("cl5/coach_2.png",18.5,22.5,0.05,0.25,"drop"),("cl5/coach_3.png",19.8,22.5,0.05,0.25,"drop")],
  [("m1a",0.9),("m1b",5.5),("m1c",9.45),("m2",14.05),("m3",16.4)],pad=0.1)
if "t" in which: act("t",[("A",0.5,12,3.2,False),("A",15.5,19.5,1.3,True),("F",22,55,7.0,False)],
  [("cl5/title_t.png",0.0,1.3,0.05,0.25,"drop"),("cl5/corner_t.png",1.4,20,0.2,0.2,"x"),("cl5/chip_c.png",1.4,20,0.2,0.2,"x"),
   ("cl5/cap_a1.png",1.0,3.5,0.2,0.2,"drop"),("cl5/cap_a2.png",3.8,7.4,0.2,0.2,"drop"),("cl5/cap_f1.png",7.7,9.9,0.2,0.2,"drop"),("cl5/cap_f2.png",10.1,12.4,0.2,0.2,"drop")],
  [("b1n",0.8),("b3",7.8)],pad=0.2)
if "c" in which: act("c",[("D",11.5,23,3.0,False),("D",46.5,52.7,1.6,False),("B",8,32.5,4.9,False)],
  [("cl5/title_c.png",0.0,1.3,0.05,0.25,"drop"),("cl5/corner_c.png",1.4,20,0.2,0.2,"x"),("cl5/chip_c.png",1.4,20,0.2,0.2,"x"),
   ("cl5/cap_d1.png",1.2,3.8,0.2,0.2,"drop"),("cl5/cap_d2.png",4.0,7.6,0.2,0.2,"drop"),("cl5/cap_r1.png",7.9,9.4,0.2,0.2,"drop"),("cl5/cap_r2.png",9.5,11.0,0.2,0.2,"drop"),("cl5/cap_r3.png",11.1,12.9,0.2,0.2,"drop")],
  [("c1n",1.2),("c2b",4.5),("c3t",7.9)],pad=0.2)

def end_scene():
    D=5.1
    L=["-loop","1","-framerate","30","-t",str(D),"-i"]
    ins=[*L,"cl5/end_pageB.png",*L,"cl5/end_bridge.png",*L,"cl5/end_tourist.png",*L,"cl5/end_noor.png",*L,"cl5/end_plane.png","-i","v5/vo/e3.mp3"]
    drop=lambda a:f"-420*pow(max(0,1-(t-{a})/0.35),3)+8*sin((t-{a})*18)*max(0,1-(t-{a})/0.5)*gte(t,{a})"
    fc=["[0:v]crop=1920:1080:0:0,format=rgba[p0]"]; last="[p0]"
    pcs=[(1,0.3,1020,740),(2,0.6,1000,585),(3,0.85,1730,585)]
    for i,(idx,a,x,yy) in enumerate(pcs):
        fc.append(f"[{idx}:v]format=rgba[q{i}]")
        fc.append(f"{last}[q{i}]overlay=x={x}:y='{yy}+{drop(a)}':enable='gte(t,{a})':eof_action=repeat[pq{i}]"); last=f"[pq{i}]"
    fc.append("[4:v]format=rgba[pl]")
    fc.append(f"{last}[pl]overlay=x='900+1100*max(0,(t-0.5))/4.4':y='250-150*max(0,(t-0.5))/4.4':enable='gte(t,0.5)':eof_action=repeat[wP]")
    fc.append(f"[wP]fps=12,fps=30,fade=t=in:d=0.3,fade=t=out:st={D-0.35}:d=0.35,format=yuv420p[v]")
    fc.append(f"[5:a]aresample=44100,aformat=channel_layouts=stereo,adelay=400|400,apad,atrim=0:{D},afade=t=out:st={D-0.3}:d=0.3[a]")
    run(["ffmpeg","-v","error","-y",*ins,"-filter_complex",";".join(fc),"-map","[v]","-map","[a]","-t",str(D),*ENC,"v5/seg_e.mp4"]); print("e",D)
if "e" in which: end_scene()
