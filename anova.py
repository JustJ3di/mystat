import numpy as np
from numpy import RankWarning, array, float64, random
import numpy

def _ssw_(number_of_group:int,sizes:int,list_of_sample:list,list_of_mu:list):
    '''
    Return the ssw    
    '''
   
   
    ssw = 0
    for j in range(number_of_group):
        for i in range(sizes):
            ssw = ssw + ((list_of_sample[j][i] - list_of_mu[j])**2)

    return ssw

def _ssb_(size_of_sample:int,mu_total:float,mu_array:list):
    '''
    Return the ssb
    '''
    ssb = sum(size_of_sample*((mu_array - mu_total)**2))    
    return ssb

def _f_test(ssb,ssw,total_element,number_of_group):
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



def Anova_one_way(sample_list:list):

    '''
    return the statistic test of the ANOVA one way test
    sample_list : The list of the sample on we want do the test
    '''

    sizes = len(sample_list[0])
    
    ng = len(sample_list)
    
    mu_list = _list_of_mu(number_of_group=ng,sample_list = sample_list)

    mu_total = np.mean(mu_list)

    ssb = _ssb_(size_of_sample = sizes,mu_total= mu_total, mu_array= mu_list)
    ssw = _ssw_(number_of_group=ng,sizes = sizes,list_of_sample=sample_list,list_of_mu=mu_list)

    total_element = len(sample_list)*len(sample_list[0])
    
    f = _f_test(ssb = ssb,ssw = ssw,total_element = total_element,number_of_group = ng)

    result = f"F oneway result {f}"
    return result
        


