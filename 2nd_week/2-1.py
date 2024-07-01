from collections import deque

#후위 표기법 계산은 왼쪽부터 읽어서 피연산자 2개와 연산자 1개를 발견할때마다 계산
#2 3 * 5 + 11 / 2 - => (2*3) + 5 / 11 - 2 = -1
a= input("후위 표시법 수식: ")

op_check = ['+','-','*','/']
deq = deque(a.split())

stack = [] #연산 스택
op1 = 0 #피연산자
op2 = 0 #피연산자2

while len(deq):
    if deq[0].isdigit():
        stack.append(int(deq.popleft()))
    elif deq[0] == '+':
        deq.popleft()
        op2 = stack.pop(-1)
        op1 = stack.pop(-1)
        stack.append(op1 + op2)
    elif deq[0] == '-':
        deq.popleft()
        op2 = stack.pop(-1)
        op1 = stack.pop(-1)
        stack.append(op1 - op2)
    elif deq[0] == '*':
        deq.popleft()
        op2 = stack.pop(-1)
        op1 = stack.pop(-1)
        stack.append(op1 * op2)
    elif deq[0] == '/':
        deq.popleft()
        op2 = stack.pop(-1)
        op1 = stack.pop(-1)
        stack.append(op1 // op2)

print(stack)