import math
import os
import random
import re
import sys

#
# Complete the 'cardPackets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY cardTypes as parameter.
#
#4,7,5,11,15   we want evens
def cardPackets(cardTypes):
    count2 = 0
    count3 = 0
    for i in range(len(cardTypes)):
        if cardTypes[i]%2!=0:
            cardTypes[i]=cardTypes[i]+1
            count2 = count2 + 1
    
    for i in range(len(cardTypes)):
        if cardTypes[i]%3!=0:
            cardTypes[i]=cardTypes[i]+1
            count3 = count3 + 1
    if count2 <= count3:
        return count2
    else:
        return count3
    

if __name__ == '__main__':
    

    cardTypes_count = int(input().strip())
    cardTypes = []

    for _ in range(cardTypes_count):
        cardTypes_item = int(input().strip())
        cardTypes.append(cardTypes_item)

    result = cardPackets(cardTypes)
    print(result)
    #fptr.write(str(result) + '\n')

    
