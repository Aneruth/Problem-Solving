# Two sum method
#  Consider a list and a sum. Compute a pair which holds the values of the sum.
def two_sum(aList,target):
    #  Looping through the list in a specific range. 
    for i in range(len(aList)): 
        # Loops through i'th  value
        for j in range(i+1,len(aList)):
            # To set find sum of two pairs in aList
            sum_value = aList[i] + aList[j]
            # To check if sum of two pairs is same as target value
            if target == sum_value:
                out = [aList[i],aList[j]] # to print index pair we can just mention like out = [i,j]
            else:
                out = False
    return out 
print(two_sum([1,2,4,4],8))