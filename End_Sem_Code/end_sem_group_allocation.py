import csv
import os
import re
import math
import operator

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
    if(~os.path.exists('groups')):
        os.makedirs('groups')

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
        #############################################################################
        print(listbranchname)
        print(listbranchcount)
        dirpath='groups'
        with open(dirpath+'/'+'branch_strength'+'.csv', 'w',newline='') as fily:
            writer=csv.writer(fily)
            newheader=['BRANCH_CODE','STRENGTH']
            writer.writerow(newheader)
            for i in range(len(listbranchname)):
                writer.writerow([listbranchname[i],listbranchcount[i]])
            fily.close()
        ################################################################################
        
        #second part of the question
        ##################################################################################
        for ind_branch in listbranchname:
            ind_grplist=[]
            with open(dirpath+'/'+ind_branch+'.csv', 'w',newline='') as fily:
                writer=csv.writer(fily)
                writer.writerow(headerrow)
                with open(filename, 'r') as file:
                    readert2=csv.reader(file)
                    reader3=sorted(readert2,key=operator.itemgetter(0))
                    for row3 in reader3:
                        
                        if(row3[0]!="Roll"):
                            t2=re.split(r'[\d+]',row3[0])
                            if(t2[4]==ind_branch):
                                ind_grplist.append(row3)
                    file.close()
                for i in ind_grplist:
                    writer.writerow(i)
                fily.close()
        ####################################################################################

        #third part of the question
        ##########################################################################
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
        #############################################################################

        #consuming leftover mat into the final matrix
        ##########################################################################
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
        ##########################################################################
        #Packing of Groups
        Distri_Dict_Branches={}
        
        for uniq_bname in edit_branchname:
            templist=[]
            with open(filename, 'r') as file2:
                readert=csv.reader(file2)
                reader4=sorted(readert,key=operator.itemgetter(0))
                for row4 in reader4:
                    if(row4[0]!="Roll"):
                        t2_bname=re.split(r'[\d+]',row4[0])
                        final_bname=t2_bname[4]
                        if(uniq_bname==final_bname):
                            templist.append(row4)
                file2.close()
            Distri_Dict_Branches[uniq_bname]=templist

        #Creating Separate Group Files
        for grp_no in range(number_of_groups):
            if(grp_no<9):
                padded_grpno='0'+str(grp_no+1)
            else:
                padded_grpno=str(grp_no+1)
            with open('groups'+'/Group_G'+padded_grpno+'.csv', 'w',newline='') as file3:
                writer3=csv.writer(file3)
                writer3.writerow(headerrow)
                for i in range(len(edit_branchname)):
                    curr_bname=edit_branchname[i]
                    curr_batch_count=Distri_Mat[i][grp_no]
                    temp2=Distri_Dict_Branches[curr_bname]
                    for j in range(curr_batch_count):
                        writer3.writerow(temp2[0])
                        temp2.pop(0)
        #Part 4 of the question
        #Creating statistics file
        with open('groups'+'/stats_grouping'+'.csv', 'w',newline='') as file4:
            writer4=csv.writer(file4)
            stat_header=['group','total']
            for i in edit_branchname:
                stat_header.append(i)
            print(stat_header)
            writer4.writerow(stat_header)
            for grpno in range(number_of_groups):
                details_list=[]
                if(grpno<9):
                    padded_grpno='0'+str(grpno+1)
                else:
                    padded_grpno=str(grpno+1)
                grp_name="Group_G"+padded_grpno
                details_list.append(grp_name+'.csv')
                init_tot=0
                branch_specs=[]
                for j in range(len(edit_branchname)):
                    init_tot=init_tot+Distri_Mat[j][grpno]
                    branch_specs.append(Distri_Mat[j][grpno])
                details_list.append(init_tot)
                for m in branch_specs:
                    details_list.append(m)
                writer4.writerow(details_list)
                


            


                        



        
            
filename = "Btech_2020_master_data.csv"
number_of_groups = 12 
group_allocation(filename, number_of_groups)