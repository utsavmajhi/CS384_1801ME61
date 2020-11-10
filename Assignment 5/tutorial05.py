import os
import re
os.system("cls")
def rename_FIR(folder_name):
    # rename Logic
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
    pass 
    

def rename_How_I_Met_Your_Mother(folder_name):
    # rename Logic
    pass 
    
#rename_Game_of_Thrones("Game of Thrones")
rename_Sherlock("Sherlock")