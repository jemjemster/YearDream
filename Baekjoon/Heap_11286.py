import sys
import heapq

n = int(input())
heapq = []

for i in range():
    x = int(sys.stdin.readline().rstrip())

    if x != 0:
        heapq.heappush(heapq, (abs(x), x))  # abs(x) 변환하면 최솟값 정렬이 절대값 정렬로 바뀐다. 

    else:            
        if not heapq:                       # 배열이 비어있는데 절댓값 가장 작은 값 출력하라는 경우 
           print(0)                         
   
        else:                               # 원소 추가 : (-x, x) 튜플로 넣으면 첫번째 원소 기준으로 힙 구성
           print(heapq.heappop(x)[1])       # 실제값은 튜플 두번째 자리에 저장되어있으니 [1] 인덱싱으로 접근
                                             
            