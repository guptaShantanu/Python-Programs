#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    dict={}
    lis=[]
    res=[]
    for i in range(len(scores)):
        try:
            d=dict[scores[i]] 
        except:
            lis.append(scores[i])
            dict[scores[i]]=1
    n=len(lis)
    
    for i in range(len(alice)):
        start=0
        end=n-1
        if alice[i]<lis[n-1]:
            res.append(n+1)
            continue
        while(start<end):
            mid=int((start+end)/2)
            if alice[i]>lis[mid]:
                end=mid-1
            elif alice[i]<lis[mid]:
                start=mid+1
            else:
                res.append(mid+1)
                print(mid+1)
                break
        else:
            if start==end:
                res.append(start+1)
            else:
                res.append(end+3)

    return res
   




        
        
        

if __name__ == '__main__':


    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)
    print(result)
