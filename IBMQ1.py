import math
import os
import random
import re
import sys

#
# Complete the 'getQueryAnswers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_STRING_ARRAY cache_entries
#  2. 2D_STRING_ARRAY queries
#

def getQueryAnswers(cache_entries, queries):
    result = []
    for i in range(len(cache_entries)):
        for j in range(len(queries)):
            if queries[j][0]==cache_entries[i][1]:
                result.append(cache_entries[i][2])
                break
    return result

if __name__ == '__main__':
    

    cache_entries_rows = int(input().strip())
    cache_entries_columns = int(input().strip())

    cache_entries = [] #3x3

    for i in range(cache_entries_rows):
        cache_entries.append(input().rstrip().split())

    queries_rows = int(input().strip())
    queries_columns = int(input().strip())

    queries = [] #1x2

    for i in range(queries_rows):
        queries.append(input().rstrip().split())

    
    result = getQueryAnswers(cache_entries, queries)
    print(result)
    
