# In-place shuffle
# # **************** # 

# Write a function for doing an in-place ↴ shuffle of a list.

# The shuffle must be "uniform," meaning each item in the original 
# list must have the same probability of ending up in each spot in the final list.

# Assume that you have a function get_random(floor, ceiling) for getting a random 
# integer that is >= floor and <= ceiling.

import random

def inplaceShuffle(intList):

    length = len(intList)
    lastIndex = length - 1

    for index in range(0, length-1 ):

        index2 = random.randint(index, lastIndex)

        if index != index2:
            intList[index], intList[index2] = intList[index2], intList[index]
    
    return intList


# Complexity :
# Time O(n) , Space O(1)

# Tests
# ****** #

def main():

    array1 = [1,2,3,4,5]
    print (array1, end = " => ")
    print(inplaceShuffle(array1))

    array2 = [23,2,1]
    print( array2, end = " => ")
    print( inplaceShuffle(array2) )

if __name__ == "__main__":
    main()


