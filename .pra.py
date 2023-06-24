def solution(w, h):
    answer = 0
    a = max(w,h)
    b = min(w,h)
    for i in range(1, min(w,h)):
        
        n = int(a*i) // b
        answer += n

    return 2*answer
