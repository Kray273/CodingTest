# 출력할 값을 담을 list 초기화 
output = []

# 후위표기법을 만들 반복문_ test_case는 10번으로 고정
for test_case in range(10):
    N=int(input()) #문자열의 길이
    S=input() #변경시킬 문자열
    stack=[] # 후위표기법을 담을 list
    postfix='' #후위 표기식 문자열
    cal=[]  #계산할 문자
    
    # S에 담긴 문자열을 후위 표기식으로 변경
    for i in S:
        # 스택이 비어있고 i가 '+' 일 경우 Stack에 추가 
        if not stack and i =='+':
            stack.append(i)
        # 스택이 비어있지 않고 i가 '+' 일 경우  stack에 값을 꺼내어 후위 표기법을 담을 변수에 더하고 i 값을 스택에 추가
        elif stack and i=='+':
            postfix+=stack.pop()
            stack.append(i)
        # 숫자인 경우 모두 후위표기법을 담을 변수에 i를 더함
        else:
            postfix+=i
    # 스택에 남아 있을 '+"를 빼기위해 for ~ else를 사용 _ for문이 break없이 끝까지 수행된 경우 else 문 실시 
    else:
        postfix+=stack.pop()
	
    #print(postfix)
    
    # 결과값 계산을 위한 반복문 
    for i in postfix :
        # +가 아닌 경우 cal변수에 int로 추가
        if i !='+':
            cal.append(int(i))
        # +일 경우 cal변수에서 마지막 값 2개를 뽑아 더한 후 다시 cal변수에 추가
        elif i=='+':
            cal.append(cal.pop()+cal.pop())
            
    #계산된 값을 순서대로 output변수에 넣기 
    output.append(cal.pop())
    
# output에 있는 값을 출력
for i in range(len(output)):
    print("#{} {}".format( i +1 , output[i]))