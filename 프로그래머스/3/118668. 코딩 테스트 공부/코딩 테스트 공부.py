def solution(alp, cop, problems):
    """
    주어진 문제를 모두 풀 수 있는 alp, cop 값을 가지는 
    최단 시간구하기
    times[알고력][코딩력]
    """ 
    ## 알고력과 코딩력의 max값 구하기
    max_alp = max_cop = 0
    
    for alp_req, cop_req, _, _, _ in problems:
        max_alp = max(max_alp, alp_req) #알고력 최대값 갱신
        max_cop = max(max_cop, cop_req) #코딩력 최대값 갱신
    
    ## 최단시간 기본 설정
    # 무한대(inf)로 가정
    times = [[float('inf') for _ in range(max_cop + 1)] \
                            for _ in range(max_alp + 1)] 
             
    # alp > max_alp인 경우 대비
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
             
    # 기본 능력 -> times = 0
    times[alp][cop] = 0
             
    ## 코딩력 알고력 향상 
    for a in range(alp, max_alp +1 ):
        for c in range(cop, max_cop +1):
            # 시간 +1
            if a + 1 <= max_alp:
                times[a+1][c] = min(times[a+1][c] , times[a][c] + 1) # 최소 시간
            if c + 1 <= max_cop:
                times[a][c+1] = min(times[a][c+1] , times[a][c] + 1)
            
            # 문제 풀이
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a >= alp_req and c >= cop_req:
                    na, nc = min(a + alp_rwd, max_alp) , min(c + cop_rwd, max_cop)
                    times[na][nc] = min(times[na][nc] , times[a][c] + cost)
    
    ## answer 
    answer = times[-1][-1]
             
    return answer