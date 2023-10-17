import itertools as it
def solution(orders, course):

    for i in range (len(orders)):
        orders[i]=sorted(orders[i])

    answer={}
    for order in orders:
        k = len(order)
        for i in range(2,k+1):
            a = it.combinations(order,i)
            for s in a:
                if s not in answer:
                    answer[s] = 1
                else:
                    answer[s] +=1
    result={}
    for x in answer:
        if answer[x] !=1:
            result[x] = answer[x]
    X=sorted(result.keys(),key = lambda x:len(x))
    
    answer=[[]for _ in range(max(course)+1)]    
    
    for i in X[::-1]:
        if len(i) in course:
            answer[len(i)].append((i,result[i]))
    M=[]
    for i in range(max(course)+1):
        m=0
        for k in answer[i]:
            m = max(m,k[1])
        M.append(m)
    result=[]
    
    for i in range(max(course)+1):
        for k in answer[i]:
            if M[i] == k[1]:
                result.append("".join(k[0]))
    return (sorted(result))