from sys import stdin
def maxfreq(arr):
    
    
    d={}
    
    for i in arr:
        d[i] = d.get(i,0)+1
        ans = arr[0]
    for i in arr:
        if d[i] > d[ans]:
            ans = i
        #ans = num
    return ans
    
    #Write your code here 
    pass

    
    
    
    
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(maxfreq(arr))