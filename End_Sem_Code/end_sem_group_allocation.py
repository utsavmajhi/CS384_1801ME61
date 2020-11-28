import csv
import os
import re

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
        print(branchcount_dict)
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
        print(listbranchname)
        print(listbranchcount)
        dirpath='groups'
        
        for ind_branch in listbranchname:
            ind_grplist=[]
            with open(dirpath+'/'+ind_branch+'.csv', 'w',newline='') as fily:
                writer=csv.writer(fily)
                writer.writerow(headerrow)
                with open(filename, 'r') as file:
                    reader3=csv.reader(file)
                    for row3 in reader3:
                        print(row3)
                        if(row3[0]!="Roll"):
                            t2=re.split(r'[\d+]',row3[0])
                            if(t2[4]==ind_branch):
                                ind_grplist.append(row3)
                for i in ind_grplist:
                    writer.writerow(i)
                
                            



        
            


filename = "Btech_2020_master_data.csv"
number_of_groups = 12 
group_allocation(filename, number_of_groups)