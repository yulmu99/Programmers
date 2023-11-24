from collections import deque

def solution(queue1, queue2):
    # 기본값
    n = len(queue1)
    sum_que1 = sum(queue1)
    sum_que2 = sum(queue2)
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    # 계산 불가 (홀수) -> -1
    if (sum_que1 + sum_que2) / 2 ==1 :
        return -1
    
    # 각 큐의 합이 동일할 때 까지 반복
    for i in range(4 * n):
        if sum_que1 == sum_que2:
            return i
        
        elif sum_que1 > sum_que2 :
            q1_val = q1.popleft()
            sum_que1 -= q1_val
            
            q2.append(q1_val)
            sum_que2 += q1_val
            
        else :
            q2_val = q2.popleft()
            sum_que2 -= q2_val
            
            q1.append(q2_val)
            sum_que1 += q2_val
            
    return -1