import heapq
def solution(L):
    L.sort()
    for i in L:
        i[0]=(60*int(i[0][:2])+int(i[0][-2:]))
        i[1]=(60*int(i[1][:2])+int(i[1][-2:]))
    ans=[-10]
    
    for i in range(len(L)):
        if ans[0] +10 <= L[i][0]:
            heapq.heappop(ans)
        heapq.heappush(ans,L[i][1])
    return(len(ans))