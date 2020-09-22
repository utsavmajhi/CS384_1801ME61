# All decimal 3 places

# Function to compute mean
def mean(first_list):
    # mean Logic
    size= len(first_list)
    sum=0
    #check condition
    for i in first_list:
        if (not(isinstance(i,(int,float)))):
            return 0  
    for i in first_list:
        sum=sum + i
    mean_value=sum/size
    return round(mean_value,3)


# Function to compute median. You cant use Python functions
def median(first_list):
    # median Logic
    median_value=0
    for i in first_list:
        if (not(isinstance(i,(int,float)))):
            return 0
    if (len(first_list)%2==1):
        index=int((len(first_list)+1)/2)
        median_value=first_list[index+1]
    return round(median_value,3)


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
    standard_deviation_value=1
    return standard_deviation_value


# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic
    variance_value=1
    return variance_value


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    rmse_value=1
    return rmse_value


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    mse_value=1
    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    mae_value=1
    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    nse_value=1
    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # nse Logic
    pcc_value=1
    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    # Skewness Logic
    skewness_value=1
    return skewness_value
    
def sorting(first_list):
    # Sorting Logic
    sorted_list=1
    return sorted_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    # Kurtosis Logic
    kurtosis_value=1
    return kurtosis_value


# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic
    summation_value=1
    return summation_value
