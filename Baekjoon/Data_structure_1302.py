import sys
input = sys.stdin.readline

n = int(input())
sell = {}                         # sell을 딕셔너리형 {}으로 초기화

for i in range(n):                 
    book = input()                
    if book not in sell:          # book을 key 값으로 팔린 개수 value 추출
        sell[book] = 1            # 기존 딕셔너리 sell에 없으면 빈도 1
    else:
        sell[book] += 1           # 있으면 빈도 1 추가

max_value = max(sell.values())    # value 중에 가장 큰 값 찾기 

best = []
for key, value in sell.items():
    if value == max_value:
        best.append(key)          # max_value 가지는 key들을 best 리스트로 저장 

best = sorted(best)               # 오름차순으로 정렬  
print(best[0])                    # 가장 첫번째 책 이름 출력 