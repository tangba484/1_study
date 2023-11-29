from collections import deque
def solution(q1, q2):
    q1,q2 = deque(q1),deque(q2)
    q1_diff, q2_diff = sum(q1), sum(q2)
    if (q1_diff + q2_diff) % 2 == 1:
        return -1
    cnt = 0
    while q1 and q2:
        if q1_diff > q2_diff:
            x = q1.popleft()
            q2_diff += x
            q1_diff -= x
            q2.append(x)
        elif q1_diff < q2_diff:
            x = q2.popleft()
            q2_diff -= x
            q1_diff += x
            q1.append(x)
        else:
            return cnt
        cnt += 1
        if cnt >600000:
            return -1
    return -1

            