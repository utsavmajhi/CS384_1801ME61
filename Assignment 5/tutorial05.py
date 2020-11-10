import os
import re
os.system("cls")
def rename_FIR(folder_name):
    # rename Logic
    if(os.path.exists('Subtitles/'+folder_name)):
        print("Season Number Padding:")
        seasonpad=int(input())
        print("Episode Number Padding")
        episodepad=int(input())

        listoldname=[]
        listnewnames=[]
        listfiletype=[]

        for f in os.scandir('Subtitles/'+folder_name):
            if(f.is_file()):
                originalname=f.name
                split=re.findall(r'\d+',originalname)
                #epiosde number fetched
                episodeno=split[0]
                pattern=re.compile(r'.mp4')
                if(re.search(pattern,originalname)):
                    filetype='.mp4'
                else:
                    filetype='.srt'
                if(episodepad-len(split[0])>=0):
                    for i in range(0,episodepad-len(split[0])):
                        episodeno='0'+str(episodeno)
                finaltitle=folder_name+' - '+"Episode "+str(episodeno)
                listoldname.append(originalname)
                listnewnames.append(finaltitle)
                listfiletype.append(filetype)
        for i in range(0,len(listoldname)):
            if(os.path.exists('Subtitles/'+folder_name+'/'+listnewnames[i]+listfiletype[i])):
                os.rename('Subtitles/'+folder_name+'/'+listoldname[i], 'Subtitles/'+folder_name+'/'+listnewnames[i]+'2'+listfiletype[i])
            else:
                os.rename('Subtitles/'+folder_name+'/'+listoldname[i], 'Subtitles/'+folder_name+'/'+listnewnames[i]+listfiletype[i])
                


    pass 
    

def rename_Game_of_Thrones(folder_name):
    # rename Logic
    if(os.path.exists('Subtitles/'+folder_name)):
        print("Season Number Padding:")
        seasonpad=int(input())
        print("Episode Number Padding")
        episodepad=int(input())

        listoldname=[]
        listnewnames=[]
        for f in os.scandir('Subtitles/'+folder_name):
            if(f.is_file()):
                originalname=f.name
                #to get all the relevanr info about the string by regex
                split=re.split(r'[ - ]',originalname)
                fursplit=re.split(r'[x]',split[4])
                #got season no and episode no
                episodeno=fursplit[1]
                seasonno=fursplit[0]
                namesplit=re.split(r'[-]',originalname)
                #print(namesplit[2])
                pattern=re.compile(r'.mp4')
                if(re.search(pattern,namesplit[2])):
                    prsplit=re.split(r'[.]',namesplit[2])
                    #fetched prime name of episode
                    episodename=prsplit[0]
                    filetype='.mp4'
                else:
                    prsplit=re.split(r'[.]',namesplit[2])
                    #fetched prime name of episode
                    episodename=prsplit[0]
                    filetype='.srt'
                #Forming filename accrding to instructions
                
                if(seasonpad-len(fursplit[0])>=0):
                    for i in range(0,seasonpad-len(fursplit[0])):
                        seasonno='0'+str(seasonno)
                if(episodepad-len(fursplit[1])>=0):
                    for i in range(0,episodepad-len(fursplit[1])):
                        episodeno='0'+str(episodeno)
                if(seasonpad==1):
                    seasonno=int(seasonno)
                if(episodepad==1):
                    episodeno=int(episodeno)
                finaltitle=folder_name+' - '+"Season "+str(seasonno)+" Episode "+str(episodeno)+' -'+episodename+filetype
                #print(finaltitle)
                listoldname.append(originalname)
                listnewnames.append(finaltitle)
                #APPLYING RENAMING FUNCTION TO ACTUAL FILE
        for i in range(0,len(listoldname)):
            os.rename('Subtitles/'+folder_name+'/'+listoldname[i], 'Subtitles/'+folder_name+'/'+listnewnames[i])
    pass 
    

def rename_Sherlock(folder_name):
    # rename Logic
    if(os.path.exists('Subtitles/'+folder_name)):
        print("Season Number Padding:")
        seasonpad=int(input())
        print("Episode Number Padding")
        episodepad=int(input())
        listoldname=[]
        listnewnames=[]
        for f in os.scandir('Subtitles/'+folder_name):
            if(f.is_file()):
                originalname=f.name
                
                split=re.split(r'[.E]',originalname)
                #for season number
                fursplit=re.split(r'[S]',split[1])
                seasonno=fursplit[1]
                #for episode no
                article = re.sub(r'[E]', '(', originalname)
                splitepi=re.split(r'[(]',article)
                fursplit2=re.split(r'[.]',splitepi[1])
                #fetched episode number
                episodeno=fursplit2[0]

                if(seasonpad-len(fursplit[0])>=0):
                    for i in range(0,seasonpad-len(fursplit[1])):
                        seasonno='0'+str(seasonno)
                if(episodepad-len(fursplit[1])>=0):
                    for i in range(0,episodepad-len(fursplit2[0])):
                        episodeno='0'+str(episodeno)

                if(seasonpad==1):
                    seasonno=int(seasonno)
                if(episodepad==1):
                    episodeno=int(episodeno)

                #fetching filetype
                filetype=fursplit2[len(fursplit2)-1]
                finaltitle=folder_name+' - '+"Season "+str(seasonno)+" Episode "+str(episodeno)+'.'+filetype
                listoldname.append(originalname)
                listnewnames.append(finaltitle)
        for i in range(0,len(listoldname)):
            os.rename('Subtitles/'+folder_name+'/'+listoldname[i], 'Subtitles/'+folder_name+'/'+listnewnames[i])

    pass 
    

def rename_Suits(folder_name):
    # rename Logic
    if(os.path.exists('Subtitles/'+folder_name)):
        print("Season Number Padding:")
        seasonpad=int(input())
        print("Episode Number Padding")
        episodepad=int(input())
        listoldname=[]
        listnewnames=[]
        listfiletype=[]
        for f in os.scandir('Subtitles/'+folder_name):
            if(f.is_file()):
                originalname=f.name
                
                split=re.split(r'[-]',originalname)
                #get season no & episode no
                seasplit=re.split(r'[x]',split[1])
                seno1=re.split(r'[ ]',seasplit[1])
                episodeno=seno1[0]
                seno2=re.split(r'[ ]',seasplit[0])
                seasonno=seno2[1]
                newlist=[]
                for i in range(2,len(split)):
                    if(i==2):
                        newlist.append(split[i])
                    else:
                        newlist[0]=str(newlist[0])+str(split[i])
                
                advsplit=re.split(r'\.HDTV|\.720p|\.en|TBA',newlist[0])
                #fetched episode name
                episodename=advsplit[0]
                pattern=re.compile(r'.mp4')
                if(re.search(pattern,originalname)):
                    filetype='.mp4'
                else:
                    filetype='.srt'

                #print(seasplit[0])
                if(seasonpad-len(seno2[1])>=0):
                    for i in range(0,seasonpad-len(seno2[1])):
                        seasonno='0'+str(seasonno)
                if(episodepad-len(seno1[0])>=0):
                    for i in range(0,episodepad-len(seno1[0])):
                        episodeno='0'+str(episodeno)

                if(seasonpad==1):
                    seasonno=int(seasonno)
                if(episodepad==1):
                    episodeno=int(episodeno)
                
                if(episodename!=' '):
                    finaltitle=folder_name+' - '+"Season "+str(seasonno)+" Episode "+str(episodeno)+' -'+episodename
                else:
                    finaltitle=folder_name+' - '+"Season "+str(seasonno)+" Episode "+str(episodeno)
                
                listoldname.append(originalname)
                listnewnames.append(finaltitle)
                listfiletype.append(filetype)
        for i in range(0,len(listoldname)):
            if(os.path.exists('Subtitles/'+folder_name+'/'+listnewnames[i]+listfiletype[i])):
                os.rename('Subtitles/'+folder_name+'/'+listoldname[i], 'Subtitles/'+folder_name+'/'+listnewnames[i]+'2'+listfiletype[i])
            else:
                os.rename('Subtitles/'+folder_name+'/'+listoldname[i], 'Subtitles/'+folder_name+'/'+listnewnames[i]+listfiletype[i])
    pass 
    

def rename_How_I_Met_Your_Mother(folder_name):
    # rename Logic

    pass 
    
#rename_Game_of_Thrones("Game of Thrones")
#rename_Sherlock("Sherlock")
#rename_Suits('Suits')
rename_FIR('FIR')