import sys
from collections import deque         # 큐로 맨 앞 사람 번호 확인, 순서가 아닐 땐 스택으로 확인  
input = sys.stdin.readline            

n = int(input())
st = deque(map(int,input().split()))

num = 1
stack = []

while num <= n:                       # 번호가 n이 된 것은 간식을 모두 받았다는 것으로 while문 종료
    if st and num == st[0]:           # 줄 서있는 학생이 존재하고 맨 앞의 학생이 받을 차례면 간식을 준다.
        num += 1
        st.popleft()
    elif stack and num == stack[-1]:  # 스택에 순서 없을 땐 큐에서 맨 앞에 있는 사람을 스택에 넣기
        num += 1
        stack.pop()

    else:
        if not st:
            break                      # 위 두 개의 조건이 아닐시 줄 서있는 학생이 없으므로 간식 줄 수 없다.  
        else:
            cur = st.popleft()         # 아직 줄 서있는 학생이 있다면 앤 앞에 있는 학생을 옆 통로로 옮긴다.
            stack.append(cur)

if num > n:
    print('Nice')
else:
    print('Sad')           





