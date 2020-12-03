import os
import csv
import shutil
import numpy as np
import pandas as pd

#for removing the directory
os.getcwd()
path = 'grades'
path = os.path.join(os.getcwd(),path)
if os.path.exists(path):
    shutil.rmtree(path)
os.mkdir(path)

#Dictionary for grades parsing for further use
grade = {'AA':10,
         'AB':9,
         'BB':8,
         'BC':7,
         'CC':6,
         'CD':5,
         'DD':4,
         'F' :0,
         'I' :0
          }

def individual_roll():
    #declaring column for individual roll number
    dforign = pd.read_csv('acad_res_stud_grades.csv')
    #not required columns dropppin off
    dforign = dforign.drop(['sl','year','timestamp'],axis=1)
    columns = ['Sem','Subject','Credits','Grade','Type']




    for i,roll in enumerate(dforign.roll):

        filepath = os.path.join(path,f'{roll}_individual.csv')
        if (not os.path.exists(filepath)):
            #for header row
            f = open(filepath,'w',newline='')
            writer = csv.writer(f)

            writer.writerow([f"Roll: {roll}"])
            writer.writerow([f'Semester Wise Details'])
            writer.writerow(columns)
            f.close()

        filerow = list(dforign.values[i])
        filerow.pop(0)
    

        #for misc files with nan values or empty
        if filerow[-2] not in list(grade.keys()):

            filepath = os.path.join(path,'misc.csv')
            if (not os.path.exists(filepath)):
               f = open(filepath,'w',newline='')
               writer = csv.writer(f)
               writer.writerow(["Misc values"])
               writer.writerow(columns)
               f.close() 

            with open(filepath,'a',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(filerow)
            continue

        try:
            with open(filepath,'a',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(filerow)

        except:

            filepath = os.path.join(path,'misc.csv')
            if not os.path.exists(filepath):
               f = open(filepath,'w',newline='')
               writer = csv.writer(f)
               writer.writerow(["Misc values"])
               writer.writerow(columns)
               f.close() 

            with open(filepath,'a',newline='') as f:
                writer = csv.writer(f)
                writer.writerow(filerow)
    
    


def overall_spi_cpi():
    #For overall details of a roll no
    #parsing the individual files which were created above to get the rowd of credits and then calculating all the things
    for file in os.listdir(path):
        if file=='misc.csv':
            continue
        rowd = []
        totcred = 0
        totcredclear = 0
        spilist =[]
        parsemcredits = []
        colsk=3
        with open(os.path.join(path,file),newline='') as csvfile:
            writer2 = csv.reader(csvfile)
        
            for row in writer2:
                if colsk==0:
                    rowd.append(row)
                else:
                    colsk = colsk -1
                    if colsk==0:
                        head = row

        dforign = pd.DataFrame(rowd,columns=head)
        smeunicol = (dforign.Sem).unique()
    
        newfile = file.split('_')[0] + '_overall.csv'
    
        with open(os.path.join(path,newfile),'w',newline='') as csvfile:

            writer2 = csv.writer(csvfile)
            rno = file.split('_')[0]
            writer2.writerow([f'Roll: {rno}'])   
            writer2.writerow(['Semester','Semester Credits','Semester Credits Cleared','SPI','Total Credits','Total Credits Cleared','CPI'])
       
            for sem in smeunicol:
                s = dforign[dforign.Sem ==sem]
                sem_credit = 0
                t=0
                for i in s.Credits:
                    t=int(i)+t
                    sem_credit=t
                totcred = totcred + int(sem_credit)
                cleared_credits = 0

                for grades,credits in zip(s.Grade,s.Credits):
                    if grades in list(grade.keys()) :
                        if grade[grades]>0:
                            cleared_credits = cleared_credits + int(credits)
                    
                totcredclear = totcredclear + cleared_credits
                sum_spi = 0
                for g,c in zip(s.Grade,s.Credits):
                    sum_spi = sum_spi  + int(c) * int(grade[g])
            
                #calc spi 
                spi = sum_spi/sem_credit
                spilist.append(spi)
                parsemcredits.append(sem_credit)
                cpi_sum = 0
                #calc cpi overall
                for c,g in zip(parsemcredits,spilist):
                    cpi_sum = cpi_sum + c*g
            
                cpi = cpi_sum/sum(parsemcredits)
                writer2.writerow([sem,sem_credit,cleared_credits,round(spi,2),totcred,totcredclear,round(cpi,2)])

    
individual_roll()
overall_spi_cpi()
