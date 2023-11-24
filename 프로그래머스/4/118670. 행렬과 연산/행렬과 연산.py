from collections import deque

def solution(rc, operations):
    ## 2차원 배열 -> deque
    # 각 행과 전체 
    rc = deque([deque(r) for r in rc])
    
    # 양 끝 
    firsts = deque()
    lasts = deque()
    
    for r in rc:
        firsts.append(r.popleft())
        lasts.append(r.pop())
        
    ## ShiftRow와 Rotate
    for op in operations:
        # ShiftRow
        if op == 'ShiftRow':
            rc.appendleft(rc.pop())
            firsts.appendleft(firsts.pop())
            lasts.appendleft(lasts.pop())
            
         # Rotate
        elif op == 'Rotate':
            rc[0].appendleft(firsts.popleft())
            lasts.appendleft(rc[0].pop())
            rc[-1].append(lasts.pop())
            firsts.append(rc[-1].popleft())
            
    ## rc,firsts,lasts 합치기
    for r in rc:
        r.appendleft(firsts.popleft())
        r.append(lasts.popleft())
    
    # 1차원 배열을 2차원 배열로 
    answer = [list(r) for r in rc]

    return answer