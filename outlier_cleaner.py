#!/usr/bin/python
import numpy as np

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    cleaned_data = []
    #print("ages = ", ages)
    #print("Start cleaned_data = ", cleaned_data)

    ### your code goes here
    indic_to_remove = []
    #print ("indic_to_remove", indic_to_remove)
    d = np.subtract(predictions, net_worths)
    #print ("d", d)
    b = [abs(number) for number in d]  # b has absolute value of error
    #print ("b", b)
    count_to_remove = int (len(b) * .1)  # 10%
    print("count_to_remove = ", count_to_remove)
    for j in range(0, count_to_remove ):
        #b.remove(max(b))
        i = np.argmax(b)
        indic_to_remove.append(i)
        #cleaned_data.remove(ages[i])
        #del cleaned_data[i]
        b[i] = 0
             
    #maxval = max(b)
    for i in range(0, len(ages)):
        if i not in indic_to_remove:
            cleaned_data.append([ages[i][0], net_worths[i][0], b[i][0]])


    #print("cleaned_data = ", cleaned_data)   
    return cleaned_data

