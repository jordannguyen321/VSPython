import math
import os
import random
import re
import sys


def optimizeTikTokWatchTime(m, initialWatch, repeatWatch):
    timeTaken = 0
    count=0
    for i in range(len(repeatWatch)):
        minVal = repeatWatch[i]
        minInd = i
        for j in range(i+i,len(repeatWatch)):
            if repeatWatch[j]<minVal:
                minVal = repeatWatch[j]
                minInd = j
    for i in range(len(initialWatch)):
        if i == 0:
            timeTaken+= initialWatch[0]+repeatWatch[0]
            count+=1
        if i < minInd:   
            timeTaken+= initialWatch[i]+repeatWatch[i]
            count+=1
        elif i == minInd:
            timeTaken += repeatWatch[minInd] * (m-count)
        
    return timeTaken


if __name__ == '__main__':


    m = int(input().strip())

    initialWatch_count = int(input().strip())

    initialWatch = []

    for _ in range(initialWatch_count):
        initialWatch_item = int(input().strip())
        initialWatch.append(initialWatch_item)

    repeatWatch_count = int(input().strip())

    repeatWatch = []

    for _ in range(repeatWatch_count):
        repeatWatch_item = int(input().strip())
        repeatWatch.append(repeatWatch_item)

    result = optimizeTikTokWatchTime(m, initialWatch, repeatWatch)
print(result)
