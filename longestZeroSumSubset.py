from collections import OrderedDict

def subsetSum(li):
    
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    n=len(l)
    sum=[0]*n
    sum[0]=l[0]
    m={l[0]:0}
    start,end=-1,-2
    if sum[0]==0:
        start,end=0,0
    for i in range(1,n):
        sum[i]=sum[i-1]+l[i]
        if sum[i]==0:
            start,end=0,i
        elif sum[i] in m:
            if i-m[sum[i]]>end-start+1:
                start,end=m[sum[i]]+1,i
        else:
            m[sum[i]]=i
    return end-start+1

    


# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(subsetSum(l))