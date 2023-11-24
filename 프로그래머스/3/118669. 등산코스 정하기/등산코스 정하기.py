from collections import defaultdict
from heapq import heappush, heappop

def solution(n, paths, gates, summits):
    
    # 산봉우리는 순서 상관 없이 선택 -> set
    set_summits = set(summits)
    
    ## graph
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((w,j))
        graph[j].append((w,i))
    
    ## 초기 설정 (heap / inf)
    heap = []
    intensities = [10000001] * (n+1) # [inf] * (vertex +1)
    
    ## gate는 시작점으로 intensity = 0으로 업데이트 -> heappush
    for gate in gates:
        intensities[gate] = 0
        heappush(heap,(0,gate))
    
    ## 이웃 노드 계산 (pop -> 이웃 노드의 intensity가 기존 값 보다 작으면 업데이트 -> push)
    while heap:
        i, node = heappop(heap)
        if i > intensities[node] or node in set_summits:
            continue
            
        for next_i, next_node in graph[node]:
            new_intensity = max(next_i, i)
            if new_intensity < intensities[next_node]:
                intensities[next_node] = new_intensity
                heappush(heap,(new_intensity,next_node))
        
    ## answer -> [summit,min_intensity] / summits가 더 작은 경우 선택 
    answer = [-1,10000001] #초기화 -> 산봉우리 번호는 -1, intensity는 10000001
    for summit in sorted(set_summits):
        if intensities[summit] < answer[1]:
            answer = [summit,intensities[summit] ]
        
    return answer