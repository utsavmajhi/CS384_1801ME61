import csv
import os
import re
os.system('cls')
if(os.path.exists('analytics')):
    for root, dirs, files in os.walk('analytics', topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

def course():
    # Read csv and process
    with open('studentinfo_cs384.csv', 'r') as file:
        reader=csv.reader(file)
        for row in reader:
            if(row[0]=='id'):
                headerrow=row
            else:
                list2=[]
                list3=[]
                if(re.fullmatch(r'\d\d\d\d\D\D\d\d',row[0])):
                    #if the pattern matches of given sequence
                    list2=re.findall(r'[a-zA-z]+',row[0])
                    #for branch name
                    branch=list2[0].lower()
                    #for Year
                    list3=re.findall(r'..',row[0])
                    year=list3[0]
                    #for coursecode
                    if(list3[1]=='01'):
                        coursecode='btech'
                    if(list3[1]=='11'):
                        coursecode='mtech'
                    if(list3[1]=='12'):
                        coursecode='msc'
                    if(list3[1]=='21'):
                        coursecode='phd'
                    dirpath='analytics/'+'course/'+branch
                    if(not os.path.exists(dirpath)):
                        os.makedirs(dirpath)
                    fname=year+'_'+branch+'_'+coursecode
                    if(os.path.exists(dirpath+'/'+fname+'.csv')):
                        with open(dirpath+'/'+fname+'.csv', 'a',newline='') as fily:
                            writer=csv.writer(fily)
                            writer.writerow(row)
                            fily.close()
                    else:
                        with open(dirpath+'/'+fname+'.csv', 'w',newline='') as fily:
                            writer=csv.writer(fily)
                            writer.writerow(headerrow)
                            writer.writerow(row)
                            fily.close()
    file.close()

                

    pass


def country():
    # Read csv and process
    pass


def email_domain_extract():
    # Read csv and process
    pass


def gender():
    # Read csv and process
    pass


def dob():
    # Read csv and process
    pass


def state():
    # Read csv and process
    pass


def blood_group():
    # Read csv and process
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass

course()