

from sys import stdin

def longestConsecutiveSubsequence(arr,n): 
    d = {}
    max = 0
    for i in arr:
        d[i] = 0
        
    for i in arr:
        s = i
        c = 0
        while s in d:
            d[s] = d[s]+1
            s += 1
            c += 1
        if c>max:
            si = i
            max = c
            
    return si,max+si-1        
            
        


def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

    
# Main 
arr,n=takeInput()
ans = longestConsecutiveSubsequence(arr,n) 
# This ans array contains two numbers, ie, start and end of longest sequence respectively
print(*ans)