import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    x = int(sys.stdin.readline())
    
    if x == 0:                                # x가 0이면 최댓값 출력하고 배열에서 삭제
        if heap:                              # 예외처리 : try -> 실행할 코드
            print((-1)*heapq.heappop(heap))   # 최소 힙을 뽑아 다시 -1 곱하여 최댓값으로 만들기
        else:                                 # except -> 예외 발생했을 때 처리하는 코드
            print(0)
    else:         
        heapq.heappush(heap,(-1)*x)           # 자연수라면 배열에 -x 값 추가 
                                              # heapq는 min heap만 지원하므로 -를 통해 뒤집어준다.