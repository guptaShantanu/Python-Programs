#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    res=[]
    if len(arr)==1:
        return "YES"
    for i in range(len(arr)):
        leftsum=0
        rightsum=0
        if i==0:
            k=1
            while k<len(arr):
                rightsum+=arr[k]
                k+=1
            if rightsum==0:
                return "YES"
        elif i==len(arr)-1:
            leftsum=0
            rightsum=0
            k=0
            while k<len(arr)-1:
                leftsum+=arr[k]
                k+=1
            if leftsum==0:
                return "YES"
            else:
                return "NO"
        else:
            start=0
            end=len(arr)-1
            leftsum=0
            rightsum=0
            leftsum+=arr[start]
            rightsum+=arr[end]
            while start<=end:
                
                if leftsum<rightsum:
                    start+=1
                    leftsum+=arr[start]
                    
                elif leftsum>rightsum:
                    end+=1
                    rightsum+=arr[end]
                else:
                    if start+2==end:
                        return "YES"
                    start+=1
                
            
            
            
            
            
            
            
            # j=0
            # k=i+1
            # rightsum=0
            # leftsum=0
            # while j<i:
            #     leftsum+=arr[j]
            #     j+=1
            # while k<len(arr):
            #     rightsum+=arr[k]
            #     k+=1
            # if leftsum==rightsum:
            #     return "YES"
            #     break


if __name__ == '__main__':


    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)
        print(result)

