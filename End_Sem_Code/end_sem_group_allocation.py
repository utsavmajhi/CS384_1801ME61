import csv
import os
import re
import math
if(os.path.exists('groups')):
    for root, dirs, files in os.walk('groups', topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))

def group_allocation(filename, number_of_groups):
    # Entire Logic 
	# You can add more functions, but in the test case, we will only call the group_allocation() method,
    rollnoorig=[]
    rawbranches=[]
    branchcount_dict = {}

    with open(filename, 'r') as file:
        reader=csv.reader(file)
        for row in reader:
            if(row[0]!="Roll"):
                rollnoorig.append(row[0])
                branchname=re.split(r'[\d+]',row[0])
                bname=branchname[4]
                rawbranches.append(branchname[4])
            else:
                headerrow=row
        branchunique=list(set(rawbranches))
        #counting particular branches
    
    for i in branchunique:
        branchcount_dict[i]=0
    with open(filename, 'r') as file:
        reader2=csv.reader(file)
        for row2 in reader2:
            if(row2[0]!="Roll"):
                t1=re.split(r'[\d+]',row2[0])
                branchcount_dict[t1[4]]+=1
        listbranchname=[]
        listbranchcount=[]
        for i in branchcount_dict:
            listbranchname.append(i)
            listbranchcount.append(branchcount_dict[i])

        for j in range(len(listbranchname)):
            for k in range(j+1,len(listbranchname)):
                if(listbranchcount[j]<listbranchcount[k]):
                    tname=listbranchname[j]
                    listbranchname[j]=listbranchname[k]
                    listbranchname[k]=tname

                    tvalue=listbranchcount[j]
                    listbranchcount[j]=listbranchcount[k]
                    listbranchcount[k]=tvalue
                else:
                    if(listbranchcount[j]==listbranchcount[k]):
                        if(listbranchname[j]>listbranchname[k]):
                            tname=listbranchname[j]
                            listbranchname[j]=listbranchname[k]
                            listbranchname[k]=tname

                            tvalue=listbranchcount[j]
                            listbranchcount[j]=listbranchcount[k]
                            listbranchcount[k]=tvalue
        #sorting done
        #first part of question
        print(listbranchname)
        print(listbranchcount)
        dirpath='groups'
        with open(dirpath+'/'+'branch_strength'+'.csv', 'w',newline='') as fily:
            writer=csv.writer(fily)
            newheader=['Branch_code','Strength']
            writer.writerow(newheader)
            for i in range(len(listbranchname)):
                writer.writerow([listbranchname[i],listbranchcount[i]])
            fily.close()


        #second part of the question
        for ind_branch in listbranchname:
            ind_grplist=[]
            with open(dirpath+'/'+ind_branch+'.csv', 'w',newline='') as fily:
                writer=csv.writer(fily)
                writer.writerow(headerrow)
                with open(filename, 'r') as file:
                    reader3=csv.reader(file)
                    for row3 in reader3:
                        
                        if(row3[0]!="Roll"):
                            t2=re.split(r'[\d+]',row3[0])
                            if(t2[4]==ind_branch):
                                ind_grplist.append(row3)
                    file.close()
                for i in ind_grplist:
                    writer.writerow(i)
                fily.close()
        #third part of the question
        edit_branchname=listbranchname
        edit_branchcount=listbranchcount
        #initialisation of matrix
        Distri_Mat=[]
        left_over_Mat=[]
        for i in range(len(edit_branchname)):
            t1=[]
            for j in range(number_of_groups):
                floor_count=math.floor(edit_branchcount[i]/number_of_groups)
                left=edit_branchcount[i]-(floor_count*number_of_groups)
                t1.append(floor_count)
            Distri_Mat.append(t1)
            left_over_Mat.append(left)
        print(Distri_Mat)
        print(left_over_Mat)
        #consuming leftover mat into the final matrix
        curr_pointer=0
        c=0
        while(curr_pointer<len(left_over_Mat)):

            if(left_over_Mat[curr_pointer]!=0):
                Distri_Mat[curr_pointer][c]+=1
                left_over_Mat[curr_pointer]-=1
                c=c+1
                if(c==number_of_groups):
                    c=0
            else:
                curr_pointer+=1
                if(curr_pointer==len(left_over_Mat)):
                    break
        print(Distri_Mat)
            
filename = "Btech_2020_master_data.csv"
number_of_groups = 12 
group_allocation(filename, number_of_groups)