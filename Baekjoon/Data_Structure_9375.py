from collections import Counter     # Counter 모듈로 자동으로 개수 세주는 기능 이용 
t = int(input())

for i in range(t):
    n = int(input())
    wear = []                       # 핵심 원리는 딕셔너리, 입력받은 의류에서 종류 key, 품명 value 저장

    for w in range(n):
        a, b = input().split()
        wear.append(b)

    wear_Counter = Counter(wear)
    cnt = 1 

    for key in wear_Counter:
        cnt *= wear_Counter[key] +1  # 한 종류의 의상 착용해도 되고 안해도 되기 때문  
                                     # 그 종류의 의상을 입지 않는 경우 포함이라 +1 
    print(cnt-1)                     # 모든 의상을 착용하지 않은 경우 제외 

# 적어도 1개만 걸치면 밖에 나갈 수 있다. 모든 경우의 수에서 전부 다 안 입는 경우 제외해서 계산하면 됨
# 딕셔너리에 kwy를 옷의 종류로 종하고 이미 있는 종류면 key에 해당하는 값에 +1
# 아니라면 새롭게 key를 추가해주면 된다. 