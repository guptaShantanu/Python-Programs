#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    dict1={}
    dict2={}
    n=len(s)
    st=s[0]
    wt=ord(s[0])-96

    for i in range(1,n):
        if s[i]==s[i-1]:
            st=st+s[i]
            wt=wt+ord(s[i])-96
        else:
            dict1[wt]=wt
            st=s[i]
            wt=ord(s[i])-96
        if i==n-1:
            dict1[wt]=wt
            

    print(dict1)
    result=[]
    for i in range(len(queries)):
        try:
            res=dict1[queries[i]]
            result.append("Yes")
        except:
            result.append("No")
    return result

if __name__ == '__main__':
  

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)


