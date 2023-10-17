def solution(number, k):
    A=[];idx=[]
    ans=''
    for i in list(number):
        A.append(int(i))
    for i in A:
        if i not in idx:
            idx.append(i)
    idx=sorted(idx,reverse=True)
    while len(ans)!=len(number)-k:
        len_number=len(number)
        len_ans=len(ans)
        for i in idx:
            try:
                AI=A.index(i)
            except:
                continue
            if AI!=-1 and len(A[AI:])>=len_number-k-len_ans:
                ans+=str(i)
                A=A[AI+1:]
                break
    return (ans)