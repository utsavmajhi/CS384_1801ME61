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
    with open('studentinfo_cs384.csv', 'r') as file:
        reader=csv.reader(file)
        for row in reader:
            if(row[0]=='id'):
                headerrow=row
            else:
                dirpath='analytics/'+'country'
                if(not os.path.exists(dirpath)):
                    os.makedirs(dirpath)
                #fetching country from csv file
                stdcountry=row[2].lower()
                #now writing the data accrding to country he/she is residing 
                if(not os.path.exists(dirpath+'/'+stdcountry+'.csv')):
                    with open(dirpath+'/'+stdcountry+'.csv', 'w',newline='') as fily:
                            writer=csv.writer(fily)
                            writer.writerow(headerrow)
                            writer.writerow(row)
                            fily.close()
                else:
                    with open(dirpath+'/'+stdcountry+'.csv', 'a',newline='') as fily:
                            writer=csv.writer(fily)
                            writer.writerow(row)
                            fily.close()
        file.close()
    pass


def email_domain_extract():
    # Read csv and process
    with open('studentinfo_cs384.csv', 'r') as file:
        reader=csv.reader(file)
        for row in reader:
            if(row[0]=='id'):
                headerrow=row
            else:
                dirpath='analytics/'+'email_domain'
                if(not os.path.exists(dirpath)):
                    os.makedirs(dirpath)
                #fetching email id first
                full_email_id=row[3]
                #trimming it using regex to get domain
                email_domain=re.search(r'@.+',full_email_id).group()
                fursplit=re.split(r'[.]',email_domain)
                fur2split=re.split(r'@',fursplit[0])
                
                if(not os.path.exists(dirpath+'/'+fur2split[1]+'.csv')):
                    with open(dirpath+'/'+fur2split[1]+'.csv', 'w',newline='') as fily:
                            writer=csv.writer(fily)
                            writer.writerow(headerrow)
                            writer.writerow(row)
                            fily.close()
                else:
                    with open(dirpath+'/'+fur2split[1]+'.csv', 'a',newline='') as fily:
                            writer=csv.writer(fily)
                            writer.writerow(row)
                            fily.close()
        file.close()


    pass


def gender():
    # Read csv and process
    with open('studentinfo_cs384.csv', 'r') as file:
        reader=csv.reader(file)
        for row in reader:
            if(row[0]=='id'):
                headerrow=row
            else:
                dirpath='analytics/'+'gender'
                if(not os.path.exists(dirpath)):
                    os.makedirs(dirpath)
                #fetching Gender of the person
                std_gender=row[4].lower()
                if(not os.path.exists(dirpath+'/'+std_gender+'.csv')):
                    with open(dirpath+'/'+std_gender+'.csv', 'w',newline='') as fily:
                            writer=csv.writer(fily)
                            writer.writerow(headerrow)
                            writer.writerow(row)
                            fily.close()
                else:
                    with open(dirpath+'/'+std_gender+'.csv', 'a',newline='') as fily:
                            writer=csv.writer(fily)
                            writer.writerow(row)
                            fily.close()
    file.close()
    pass


def dob():
    # Read csv and process
    with open('studentinfo_cs384.csv', 'r') as file:
        reader=csv.reader(file)
        for row in reader:
            if(row[0]=='id'):
                headerrow=row
            else:
                dirpath='analytics/'+'dob'
                if(not os.path.exists(dirpath)):
                    os.makedirs(dirpath)
                #fetching dob of people
                date_of_birth=row[5]
                listsplit=re.split('-',date_of_birth)
                year=int(listsplit[2])
                month=int(listsplit[1])
                day=(listsplit[0])
                #making files for range dates
                intialyearrange=1995
                for i in range(0,5):
                    finalyearrange=intialyearrange+4
                    if(i==4):
                        finalyearrange=finalyearrange+1
                    if(year<=finalyearrange and year>=intialyearrange):
                        if(not os.path.exists(dirpath+'/'+'bday_'+str(intialyearrange)+'_'+str(finalyearrange)+'.csv')):
                            with open(dirpath+'/'+'bday_'+str(intialyearrange)+'_'+str(finalyearrange)+'.csv', 'w',newline='') as fily:
                                writer=csv.writer(fily)
                                writer.writerow(headerrow)
                                writer.writerow(row)
                                fily.close()
                        else:
                            with open(dirpath+'/'+'bday_'+str(intialyearrange)+'_'+str(finalyearrange)+'.csv', 'a',newline='') as fily:
                                writer=csv.writer(fily)
                                writer.writerow(row)
                                fily.close()
                    intialyearrange=intialyearrange+5
        file.close()
                
    pass


def state():
    # Read csv and process
    with open('studentinfo_cs384.csv', 'r') as file:
        reader=csv.reader(file)
        for row in reader:
            if(row[0]=='id'):
                headerrow=row
            else:
                dirpath='analytics/'+'state'
                if(not os.path.exists(dirpath)):
                    os.makedirs(dirpath)
                #fetching state of people
                person_state=row[7].lower()
                if(not os.path.exists(dirpath+'/'+person_state+'.csv')):
                    with open(dirpath+'/'+person_state+'.csv', 'w',newline='') as fily:
                            writer=csv.writer(fily)
                            writer.writerow(headerrow)
                            writer.writerow(row)
                            fily.close()
                else:
                    with open(dirpath+'/'+person_state+'.csv', 'a',newline='') as fily:
                            writer=csv.writer(fily)
                            writer.writerow(row)
                            fily.close()
    file.close()
    pass


def blood_group():
    # Read csv and process
    with open('studentinfo_cs384.csv', 'r') as file:
        reader=csv.reader(file)
        for row in reader:
            if(row[0]=='id'):
                headerrow=row
            else:
                dirpath='analytics/'+'blood_group'
                if(not os.path.exists(dirpath)):
                    os.makedirs(dirpath)
                #fetching blood group of people
                blood_grp=row[6].lower()
                if(not os.path.exists(dirpath+'/'+blood_grp+'.csv')):
                    with open(dirpath+'/'+blood_grp+'.csv', 'w',newline='') as fily:
                            writer=csv.writer(fily)
                            writer.writerow(headerrow)
                            writer.writerow(row)
                            fily.close()
                else:
                    with open(dirpath+'/'+blood_grp+'.csv', 'a',newline='') as fily:
                            writer=csv.writer(fily)
                            writer.writerow(row)
                            fily.close()
    file.close()
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    with open('studentinfo_cs384.csv', 'r') as file:
        reader=csv.reader(file)
        for row in reader:
            if(row[0]=='id'):
                headerrow=row
                final_headrow=['id','first_name','last_name']
                final_headrow=final_headrow+row[2:]
            else:
                #for first name and last name fetching
                full_name=row[1]
                names_split=re.split(' ',full_name)
                first_name=names_split[0]
                last_name=names_split[1]
                list_fname_lastname=[row[0],first_name,last_name]
                final_rowlist=list_fname_lastname+row[2:]
                dirpath='analytics/'
                if(not os.path.exists(dirpath)):
                    os.makedirs(dirpath)
                if(not os.path.exists(dirpath+'studentinfo_cs384_names_split.csv')):
                    with open(dirpath+'studentinfo_cs384_names_split.csv', 'w',newline='') as fily:
                            writer=csv.writer(fily)
                            writer.writerow(final_headrow)
                            writer.writerow(final_rowlist)
                            fily.close()
                else:
                    with open(dirpath+'studentinfo_cs384_names_split.csv', 'a',newline='') as fily:
                            writer=csv.writer(fily)
                            writer.writerow(final_rowlist)
                            fily.close()
    file.close()

    pass


new_file_sort()