import numpy as np
from numpy import RankWarning, array, float64, random
from math import pow



def _ssw_(number_of_group:int,sizes:list,list_of_sample:list,list_of_mu:list):
    '''
    Return the ssw    
    '''
    ssw = 0
    for j in range(number_of_group):
        for i in range(sizes[j]):
            ssw = float(ssw + (pow((list_of_sample[j][i] - list_of_mu[j]),2)))
    
    return ssw



def _ssb_(sizes:list,mu_total:float,mu_array:list):
    '''
    Return the ssb
    '''   
    ssb = float(sum(sizes*((mu_array - mu_total)**2)))   

    return ssb

def _f_test(ssb,ssw,total_element,number_of_group):
    '''
    compute the F test
    '''
    dfn = (total_element- number_of_group)
    dfd = number_of_group - 1
   
    msb = ssb/dfd
    msw = ssw/dfn
  
    f = msb/msw

    return f

def _list_of_mu(number_of_group:int,sample_list:list):

    '''
    return the list of mu of all group
    '''
    mu_list = []
    for i in range(number_of_group):
        mu_list.append(np.mean(sample_list[i]))
    return mu_list

def sample_count_size(sample_list:list,n_group:int):
    '''
    Ritorn a list that contains the size of each sample
    '''
    list_of_sample_size = []

    for i in range(n_group):
        list_of_sample_size.append(len(sample_list[i]))
    
    return list_of_sample_size

def Anova_one_way(sample_list:list):

    '''
    return the statistic test of the ANOVA one way test
    sample_list : The list of the sample on we want do the test
    '''
    
    ng = len(sample_list) #Number of groups
    
    sizes_samples = sample_count_size(sample_list= sample_list, n_group = ng) #array contains the sample's size
    
    mu_list = _list_of_mu(number_of_group=ng,sample_list = sample_list)#array contains the sample's means of the samples

    mu_total = np.mean(mu_list) #mean of all 

    ssb = _ssb_(sizes = sizes_samples, mu_total = mu_total, mu_array = mu_list)#Compute the ssb 
    ssw = _ssw_(number_of_group = ng, sizes = sizes_samples, list_of_sample = sample_list, list_of_mu = mu_list)#Compute the ssw

    total_element = sum(sizes_samples)#count total elements

    f = _f_test(ssb = ssb,ssw = ssw,total_element = total_element,number_of_group = ng) #compute the f test

    result = f"F oneway result {f}" 
    
    return result
        


