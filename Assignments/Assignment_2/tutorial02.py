# All decimal 3 places
import math#FOR SQRT FUNCTION
# Function to compute mean
def mean(first_list):
    # mean Logic
    size= len(first_list)
    sum=0
    #check condition
    for i in first_list:
        if (not(isinstance(i,(int,float)))):
            return 0  
    mean_value=summation(first_list)/size
    return mean_value


# Function to compute median. You cant use Python functions
def median(first_list):
    # median Logic
    median_value=0
    for i in first_list:
        if (not(isinstance(i,(int,float)))):
            return 0
    first_listmod= sorted(first_list)
    if (len(first_listmod)%2==1):
        index=int((len(first_listmod)+1)/2)
        median_value=first_listmod[index-1]
    else:
        index=int(len(first_listmod)/2)
        median_value=(first_listmod[index-1]+first_listmod[index])/2
    return median_value


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
    for i in first_list:
        if (not(isinstance(i,(int,float)))):
            return 0
    #SINCE STANDARD DEVIATION IS JUST SQUARE ROOT OF DEVIATION
    standard_deviation_value=math.sqrt(variance(first_list))
    return round(standard_deviation_value,3)


# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic
    variance_value=0
    for i in first_list:
        if (not(isinstance(i,(int,float)))):
            return 0
    x_bar=mean(first_list)
    templist=[]
    for i in first_list:
        templist.append((i-x_bar)*(i-x_bar))
    variance_value=summation(templist)/len(first_list)
    return variance_value


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    if(not(len(first_list)== len(second_list))):
        return 0

    for i in first_list:
        if (not(isinstance(i,(int,float)))):
            return 0
    for i in second_list:
        if (not(isinstance(i,(int,float)))):
            return 0
    rmse_value=0
    sum=0
    tempsqr=[]
    for i in range(0,len(first_list)):
        tempsqr.append((first_list[i]-second_list[i])*(first_list[i]-second_list[i]))
    
    rmse_value=math.sqrt(summation(tempsqr)/len(first_list))
    return rmse_value


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    if(not(len(first_list)== len(second_list))):
        return 0
    for i in first_list:
        if (not(isinstance(i,(int,float)))):
            return 0
    for i in second_list:
        if (not(isinstance(i,(int,float)))):
            return 0
    tempsqr=[]
    for i in range(0,len(first_list)):
        tempsqr.append((first_list[i]-second_list[i])*(first_list[i]-second_list[i]))
    mse_value=summation(tempsqr)/len(first_list)
    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    if(not(len(first_list)== len(second_list))):
        return 0
    mae_value=1
    for i in first_list:
        if (not(isinstance(i,(int,float)))):
            return 0
    for i in second_list:
        if (not(isinstance(i,(int,float)))):
            return 0
    tempitemlist=[]
    for i in range(0, len(first_list)):
        tempitemlist.append(abs(first_list[i]-second_list[i]))
    mae_value=summation(tempitemlist)/len(first_list)
    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    if(not(len(first_list)== len(second_list))):
        return 0
    for i in first_list:
        if (not(isinstance(i,(int,float)))):
            return 0
    for i in second_list:
        if (not(isinstance(i,(int,float)))):
            return 0
    t1list=[]
    t2list = []
    x_bar=mean(first_list)
    y_bar = mean(second_list)
    for i in range(0, len(first_list)):
        t1list.append((first_list[i]-second_list[i])**2)
        t2list.append((first_list[i]-x_bar)**2)
    nse_value=1-(summation(t1list)/summation(t2list))
    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # nse Logic
    if(not(len(first_list)== len(second_list))):
        return 0
    x_bar=mean(first_list)
    y_bar = mean(second_list)
    list1=[]
    list2=[]
    list3=[]
    for i in range(0,len(first_list)):
        list1.append((first_list[i]-x_bar)*(second_list[i]-y_bar))
        list2.append(first_list[i]-x_bar**2)
        list3.append(second_list[i]-y_bar**2)
    pcc_value=summation(list1)/((standard_deviation(first_list)*math.sqrt(len(first_list)))*(standard_deviation(second_list)*math.sqrt(len(first_list))))
    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    # Skewness Logic
    for i in first_list:
        if (not(isinstance(i,(int,float)))):
            return 0

    standevia_val=standard_deviation(first_list)
    mean_val=mean(first_list)
    templist=[]
    for i in first_list:
        templist.append(((i-mean_val)/standevia_val)*((i-mean_val)/standevia_val)*((i-mean_val)/standevia_val))

    skewness_value=summation(templist)/len(first_list)
    return skewness_value
    
def sorting(first_list):
    # Sorting Logic
    for i in first_list:
        if (not(isinstance(i,(int,float)))):
            return 0

    sorted_list=first_list[:]
    for i in range(0,len(sorted_list)):
        for j in range(1,len(sorted_list)):
            if(sorted_list[i]>sorted_list[j]):
                temp=sorted_list[i]
                sorted_list[i]=sorted_list[j]
                sorted_list[j]=temp
    return sorted_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    # Kurtosis Logic
    for i in first_list:
        if (not(isinstance(i,(int,float)))):
            return 0

    standevia_val=standard_deviation(first_list)
    mean_val=mean(first_list)
    templist=[]
    for i in first_list:
        templist.append(math.pow(((i-mean_val)/standevia_val),4))

    kurtosis_value=summation(templist)/len(first_list)
    
    return kurtosis_value


# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic
    summation_value=0
    for i in first_list:
        if (not(isinstance(i,(int,float)))):
            return 0
    for i in first_list:
        summation_value=summation_value+i
    return summation_value
