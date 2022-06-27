while True:
    a = input()
    stack = []

    if a == "." :                                       # 각 줄 마침표로 끝남
        break

    for i in a :                               
        if i == '[' or i == '(' :
            stack.append(i)
        
        elif i == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop()                              # 맞으면 pop으로 리스트 비우기

            else:
                stack.append(']')                        # 짝이 없으면 stack 리스트 그대로 두기  
                break 

        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :    
                stack.pop()

            else :
                stack.append(')')
                break                                            

        if len(stack) == 0 :                             # stack 비어있으면 yes 출력 
            print('yes')

        else :                                           
            print('no')                                 