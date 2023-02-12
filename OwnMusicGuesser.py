import os,csv
pvc=','
if not os.path.exists('OwnMusicGuesser.csv'):
    with open('OwnMusicGuesser.csv', 'w') as bigounce:
        csv.DictWriter(bigounce,delimiter=pvc,escapechar='*',fieldnames=['session','files','difficulty','corr','guess','isright','time','score','record']).writeheader()
else:
    try:
        with open('OwnMusicGuesser.csv', 'r') as bigounce:maxscore=list(csv.DictReader(bigounce,delimiter=pvc,escapechar='*'))[-1]['record']
        #print(maxscore)
    except (IndexError,KeyError): 
        with open('OwnMusicGuesser.csv', 'w') as bigounce:
            csv.DictWriter(bigounce,delimiter=pvc,escapechar='*',fieldnames=['session','files','difficulty','corr','guess','isright','rwratio','time','avgtime','streak','maxstreak','score','record']).writeheader()
import tkinter.font as fnt
win,lplusratio,winstreakmax =0,0,0
idkman2021,start,avgtime,fcount,finalscore,averagestuff,winstreak,keepmalding,L,mold,moldy,ablibibabium,bigounce,peopleobserver,dababy,zigzag,wlacom,ikdmium,yoda,jesust=0,0,[],0,0,0,0,0,False,[],0,0,0,0,0,0,0,0,0,0
session,corr,guess,isright,timongus,scoremongus,record,borat,xqcl=[],[],[],[],[],[],[],[],[]
import random, vlc, ffmpeg, time, math
def big_chungus(what):
    global sound, idkman2021, win, lplusratio, start,avgtime, fcount,finalscore, L,maxscore,averagestuff, winstreak,winstreakmax,keepmalding,mold,moldy,ablibibabium,bigounce,peopleobserver,zigzag,idkmium,dababy,wlacom,fifafofufe,yoda,session,corr,guess,isright,timongus,score,record,borat,xqcl,jesust
    if what==0 or what==1:
        if what==0:
            jesust+=1
            if fcount<=int(amount.get()): keepmalding=fcount
            else: keepmalding=int(amount.get())
            ablibibabium=math.ceil(float(keepmalding)/10)
            window.columnconfigure([0,1,2,3,4,5,6,7,8], minsize=int(100/ablibibabium))
            amount.grid_forget()
            title.grid_forget()
            titled.grid_forget()
            titledd.grid_forget()
            folderbutton.grid_forget()
            dur.grid_forget()
            #zigzag=int((5+keepmalding/5)**0.9)
            zigzag = math.ceil(5.3*math.log(keepmalding))-2
            #if keepmalding>24 and keepmalding<65:zigzag=int(zigzag*0.8)
            dababy=int(math.ceil(keepmalding/zigzag))
            #print(dababy)
            wlacom=int(80/(max(dababy**0.5,1)))
            if dababy==3 and keepmalding<50: wlacom=int(wlacom*0.8)
            if dababy==4 and keepmalding<50: wlacom=int(wlacom*0.7)
            #print(wlacom)
            #print(zigzag)
            if keepmalding>13:
                for mrkrabs in reversed(range(int(zigzag-(zigzag//(2.4 / min((30/keepmalding)**0.8, 1)))),int((zigzag+(zigzag//(3 / min((50/keepmalding)**0.8, 1))))))):
                    #print(zigzag, mrkrabs, keepmalding%mrkrabs)
                    if keepmalding%mrkrabs==0 and keepmalding!=mrkrabs:
                        zigzag=mrkrabs
                        break
            for i in range(int(keepmalding)):
                peopleobserver=max(peopleobserver, (int((zigzag-1)/ablibibabium)*math.floor(i/zigzag))+(int((zigzag-1)/ablibibabium)))
            window.minsize(1000, 100)
            bigounce=max(int((8-int(((keepmalding//5)**0.7)-1))*(ablibibabium**0.4)), 6)
            if dababy==2: bigounce=min(bigounce,9)
            idkmium=2 if zigzag>7 and keepmalding>7 else 1
            bababooey=tk.Label(text='Right:\nWrong:', justify='left', font=("Segoe UI", bigounce))
            bababooey.grid(row=1*idkmium-idkmium+1,rowspan=idkmium, column=peopleobserver, sticky='w')
            bababooey=tk.Label(text='Current score\nSession max score:', justify='left', font=("Segoe UI", bigounce))
            bababooey.grid(row=4*idkmium-idkmium+1,rowspan=idkmium, column=peopleobserver, sticky='w')
            bababooey=tk.Label(text='Last guess:\nAvg guess:', justify='left', font=("Segoe UI", bigounce))
            bababooey.grid(row=2*idkmium-idkmium+1,rowspan=idkmium, column=peopleobserver, sticky='w')
            bababooey=tk.Label(text='Current streak:    \nMax streak:   ', justify='left', font=("Segoe UI", bigounce))
            bababooey.grid(row=3*idkmium-idkmium+1,rowspan=idkmium, column=peopleobserver, sticky='w')
            finalscocurrectnscorered=tk.Label(text='0       \n0     ', justify='left', font=("Segoe UI", bigounce))
            finalscocurrectnscorered.grid(row=4*idkmium-idkmium+1,rowspan=idkmium, column=peopleobserver+1, sticky='w')
            score = tk.Label(text='0        \n0       ', justify='left', font=("Segoe UI", bigounce))
            score.grid(row=1*idkmium-idkmium+1,rowspan=idkmium, column=peopleobserver+1, sticky='w')
            stunlock = tk.Label(text='0     \n0     ', justify='left', font=("Segoe UI", bigounce))
            stunlock.grid(row=3*idkmium-idkmium+1,rowspan=idkmium, column=peopleobserver+1, sticky='w')
#
            if folder=='':
                import sys as sus
                sus.exit()
            yoda=int(max(bigounce,(12-math.floor(float(keepmalding)/7))))
            if keepmalding>24 and keepmalding<65 or dababy==2: yoda=int(yoda-1)
            if idkman2021==1:
                sound.stop()
                win,lplusratio,avgtime,finalscore=0,0,[],0
                lastguess=tk.Label(text='               \n              ', justify='left', font=("Segoe UI", bigounce))
                lastguess.grid(row=2, column=peopleobserver+1, sticky='w')
            for i in range(min(int(keepmalding),10)):window.rowconfigure(i, minsize=10, pad=0)
        # creates a list of SONGS
        global songs
        songs=['']*int(keepmalding)
        a=0
        b=0
        for i in range(int(keepmalding)):
            while not (songs[i].lower().endswith(('.mp3','.wav', '.flac', '.aac', '.ogg', '.wma', '.pcm', '.aiff', '.alac', '.dsd')) or a>100):
                songs[i]=random.choice(os.listdir(folder))
                a+=1
                while ((songs[i] in songs[:i]+songs[i+1:]) and b<100): 
                    songs[i]=random.choice(os.listdir(folder))
                    b+=1
        global chosen
        chosen=random.choice(songs)
        big_chungus(2)
    else:
        idkman2021=1
        choice=[tk.Button]*int(keepmalding)
        for i in range(int(keepmalding)):
            if len(songs[i])>wlacom:choice[i] = tk.Button(text=songs[i][:wlacom],command=lambda x=songs[i]: big_chungus(x), bg='grey90', font =fnt.Font(size= yoda))
            else: choice[i] = tk.Button(text=songs[i].center(wlacom),command=lambda x=songs[i]: big_chungus(x), bg='grey90', font =fnt.Font(size= yoda))
            choice[i].grid(row=(i%(zigzag))+1, column=int((zigzag-1)/ablibibabium)*math.floor(i/zigzag), columnspan=int((zigzag-1)/ablibibabium), sticky="we", padx=10, pady=int(2-(keepmalding//90)))
            #print(int((zigzag-1)/ablibibabium)*math.floor(i/zigzag), int((zigzag-1)/ablibibabium), peopleobserver)
        if what==2:
            sound = vlc.MediaPlayer()
            amongus=vlc.Media(folder+'/'+chosen)
            amongus.add_option('start-time='+str(random.randrange(int(float((ffmpeg.probe(folder+'/'+chosen)['format']['duration'])))-20)))
            if float(dur.get())!=0:
                amongus.add_option('run-time='+str(0.4+float(dur.get())))
                #print('aight')
            sound.set_media(amongus)
            sound.play()
            start = time.time()
        elif what==chosen:
            win+=1
            isright.append(1)
            corr.append(what)
            guess.append(chosen)
            borat.append(keepmalding)
            xqcl.append(fcount)
            if L==False: 
                avgtime.append(time.time()-start)
                mold.append(time.time()-start)
            else: mold=[]
            L=False
            averagestuff=sum(avgtime)/max(len(avgtime),1)
            moldy=sum(mold)/max(len(mold),1)
            #scoreavg = tk.Label(text='Average guess time:\n' + str(round(averagestuff,2)) +' s')
            #scoreavg.grid(row=3, column=9, sticky='we')
            winstreak+=1
            winstreakmax=max(winstreak, winstreakmax)
            currectnscore=max((fcount**0.5)*(win/((lplusratio+1)))*(1/max(moldy**2, 1))*((int(keepmalding)/2)**1.4)*((dur.get()!=0)*(1/(max(float(dur.get()), 0.1)*10))), (fcount**0.5)*winstreak*(1/max(moldy**2, 1))*((int(keepmalding)/4)**2))*((dur.get()!=0)*(1/(max(float(dur.get()), 0.1)*10)))
            scoremongus.append(currectnscore)
            #finalscocurrectnscorered=tk.Label(text='Current score:\n' + str(round(currectnscore)))
            #finalscocurrectnscorered.grid(row=4, column=9, sticky='we')
            finalscore=max(finalscore,currectnscore)
            #finalscored=tk.Label(text='Current maximum score:\n' + str(round(finalscore)), font=("Arial 10 bold"))
            #finalscored.grid(row=5, column=9, sticky='we')
            maxscore=max(float(finalscore),float(maxscore))
            record.append(maxscore)
            session.append(jesust)
            finalsmaxscorecored=tk.Label(text='Top score:       \n' + str(round(float(finalscore)))+'     ', justify='left', font=("Segoe UI", bigounce))
            finalsmaxscorecored.grid(row=50,column=peopleobserver, sticky='w')
            fifafofufe=tk.Label(text='Record score:\n' + str(int(max(float(maxscore), float(finalscore)))),font=("Segoe UI", bigounce))
            fifafofufe.grid(row=50,column=peopleobserver+1, sticky='we')
            #qwqq   
            lgmongi=round((time.time()-start),3)
            lgmongus=str(lgmongi) +' s      \n'+str(round(averagestuff,2)) +' s     '
            lastguess=tk.Label(text=lgmongus, justify='left', font=("Segoe UI", bigounce))
            lastguess.grid(row=2*idkmium-idkmium+1,rowspan=idkmium,  column=peopleobserver+1, sticky='w')
            timongus.append(lgmongi)
            finalscocurrectnscorered=tk.Label(text=str(round(currectnscore))+'      \n'+str(round(finalscore))+'        ', justify='left', font=("Segoe UI", bigounce))
            finalscocurrectnscorered.grid(row=4*idkmium-idkmium+1,rowspan=idkmium, column=peopleobserver+1, sticky='w')
            
            score = tk.Label(text=str(win)+'        \n'+str(lplusratio)+'       ', justify='left', font=("Segoe UI", bigounce))
            score.grid(row=1*idkmium-idkmium+1,rowspan=idkmium, column=peopleobserver+1, sticky='w')
            stunlock = tk.Label(text=str(winstreak)+'       \n'+str(winstreakmax)+'     ', justify='left', font=("Segoe UI", bigounce))
            stunlock.grid(row=3*idkmium-idkmium+1,rowspan=idkmium, column=peopleobserver+1, sticky='w')
            #score.grid_remove()
            sound.stop()
            #print('thats right!!!') 
            for i in range(int(keepmalding)):
                choice[i].grid_forget()
            
            big_chungus(1)
        else:
            #score.grid_remove()
            #print('L + ratio') 
            lplusratio+=1
            winstreak=0
            score = tk.Label(text=str(win)+'\n'+str(lplusratio), justify='left', font=("Segoe UI", bigounce))
            score.grid(row=1*idkmium-idkmium+1,rowspan=idkmium, column=peopleobserver+1, sticky='w')
            currectnscore=max((fcount**0.5)*(win/((lplusratio+1)))*(1/max(moldy**2, 1))*((int(keepmalding)/4)**2)*((dur.get()!=0)*(1/(max(float(dur.get()), 0.1)*10))), (fcount**0.5)*winstreak*(1/max(moldy**2, 1))*((int(keepmalding)/4)**2))*((dur.get()!=0)*(1/(max(float(dur.get()), 0.1)*10)))
            scoremongus.append(currectnscore)
            finalscocurrectnscorered=tk.Label(text=str(round(currectnscore))+'\n'+str(round(finalscore)), justify='left', font=("Segoe UI", bigounce))
            finalscocurrectnscorered.grid(row=4*idkmium-idkmium+1,rowspan=idkmium, column=peopleobserver+1, sticky='w')
            stunlock = tk.Label(text=str(winstreak)+'\n'+str(winstreakmax), justify='left', font=("Segoe UI", bigounce))
            stunlock.grid(row=3*idkmium-idkmium+1,rowspan=idkmium, column=peopleobserver+1, sticky='w')
            session.append(jesust)
            timongus.append('L')
            record.append(maxscore)
            corr.append(what)
            isright.append(0)
            borat.append(keepmalding)
            xqcl.append(fcount)
            guess.append(chosen)
            L=True



sussyamongus=69
#ask for  afolder 
def folderget():
    global sussyamongus
    global folder, fcount,jesust
    a=0
    if sussyamongus==69:
        sussyamongus=68
        if not os.path.exists('OwnMusicGuesserData.txt'):
            return
        else:
            with open('OwnMusicGuesserData.txt', 'r') as bigounce:
                akak=bigounce.read()
                jesust=int(akak.split('<|>')[1])
                folder= akak.split('<|>')[0]
    else: 
        folder=  tk.filedialog.askdirectory ()
        if not os.path.exists('OwnMusicGuesserData.txt'):
            with open('OwnMusicGuesserData.txt', 'w') as bigounce:bigounce.write(f'{folder}<|>1')
            jesust=int(1)
        else:
            with open('OwnMusicGuesserData.txt', 'r+') as bigounce:
                akak=bigounce.read()
                jesust=int(akak.split('<|>')[1])
                folder= akak.split('<|>')[0]

    foldertext = tk.Label(text=folder +' - ')
    foldertext.grid(row=50, column=1, sticky="ew") #ew linus towald ew linus towald ew linus towald
    a=1
    start = tk.Button(text="Begin",command=lambda: big_chungus(0))
    start.grid(row=50, column=0, sticky="w", pady=5, padx=10)
    fcount=len([entry for entry in os.listdir(folder) if (os.path.isfile(os.path.join(folder, entry)) and entry.lower().endswith(('.mp3','.wav', '.flac', '.aac', '.ogg', '.wma', '.pcm', '.aiff', '.alac', '.dsd')))])
    count = tk.Label(text=str(fcount)+' songs')
    count.grid(row=50, column=2, sticky='we')

import tkinter.filedialog
from tkinter import ttk
import tkinter as tk

window=tk.Tk()
#window.maxsize(1200, 1200)
window.title('Own Music Guesser')
window.tk.call('tk', 'scaling', 2.0)


#ask for flder 
title = tk.Label(text="Music Guesser", font=("Arial", 15))
title.grid(row=0, column=0, columnspan=10, sticky="we", pady=10)

folderbutton = tk.Button(
    text="Select folder",
    command=folderget
)
folderbutton.grid(row=1, column=0, columnspan=9, sticky="we", pady=5, padx=10)
folderbutton.invoke()
#amount of sonsgs
amount = tk.Entry()
amount.insert(0, "5")
amount.grid(row=2, column=0, sticky="we", pady=5, padx=10, columnspan=9)
titled = tk.Label(text="Difficulty")
titled.grid(row=2, column=9, sticky="w")
dur = tk.Entry()
dur.insert(0, "0")
dur.grid(row=3, column=0, sticky="we", pady=5, padx=10, columnspan=9)
titledd = tk.Label(text="Duration (0 to disable)")
titledd.grid(row=3, column=9, sticky="w")
try: 
    tmp=float(maxscore)
    tmp=float(finalscore)
except: 
    maxscore=0
    finalscore=0



window.mainloop()
with open('OwnMusicGuesserData.txt', 'r+') as bigounce:
    jesust=int(bigounce.read().split('<|>')[1])
    folder= bigounce.read().split('<|>')[0]
    bigounce.write(f'{folder}<|>{jesust+1}')
with open('OwnMusicGuesser.csv', 'a', encoding='utf8') as rip:
    sasuke=csv.writer(rip,delimiter=pvc,escapechar='*')
    for idiots in range(len(session)):
        sasuke.writerow([session[idiots],xqcl[idiots],borat[idiots],corr[idiots],guess[idiots],isright[idiots],timongus[idiots],scoremongus[idiots],record[idiots]])
    rip.close()
# savegaming = open('OwnMusicGuesser.txt', 'w+')
# savegaming.write(str(max(float(maxscore), float(finalscore))))
# savegaming.close()
