import sys
import heapq
input = sys.stdin.readline

min_heap = []

for _ in range(int(input())):
    x = int(input())

    if x == 0:
        if len(min_heap):                     # x가 0이면 가장 작은 값 출력하고 배열에서 삭제
            print(heapq.heappop(min_heap))    # heappop() : 힙에서 원소 삭제   

        else:
            print(0)

    else:                                     # 자연수라면 배열에 x 값 추가 
        heapq.heappush(min_heap, x)           # heappush() : 원소 추가       