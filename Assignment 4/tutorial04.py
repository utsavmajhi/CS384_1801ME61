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


dforign = pd.read_csv('acad_res_stud_grades.csv')
#not required columns dropppin off
dforign = dforign.drop(['sl','year','timestamp'],axis=1)


#declaring column for individual roll number
columns = ['Sem','Subject','Credits','Grade','Type']

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





        
        




