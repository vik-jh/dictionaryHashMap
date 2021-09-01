
def printPairDiffK(l, k):
    if k<0:
        k*=-1
    paircount=0
    m={}
    for num in l:
        if num+k in m:
            paircount+=m[num+k]
        if k!=0 and num-k in m:
            paircount+=m[num-k]
        if num in m:
            m[num]+=1
        else:
            m[num]=1
    return paircount


n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
print(printPairDiffK(l, k))