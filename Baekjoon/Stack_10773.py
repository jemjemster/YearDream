count = int(input())        # 입력받을 스택 리스트 안의 총 숫자의 수
stack = [] 

for i in range(count): 
    money = int(input())
    if(money == 0):         # money가 0이면 pop
        stack.pop()
    else:
        stack.append(money) # 그게 아니라면 money = append
print(sum(stack))
