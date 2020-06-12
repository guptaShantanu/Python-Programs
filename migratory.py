#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    arr=sorted(arr)
    max_count=0
    count=1
    number=arr[0]
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            count+=1
        else:
            if count>max_count:
                max_count=count
                number=arr[i-1]
            count=1
    return number

if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    print(result)

