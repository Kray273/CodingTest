# 10번의 태스트 케이스 
for test_case in range(10) :
    t = int(input()) #테스트케이스의 번호 
    queue = list(map(int, input().split())) # 암호화할 번호 
    i = 1 #반복을 체크할 변수 초기화
    check = 0 #변경될 값을 저장할 변수
    
    while True :
        # i가 5면 i를 다시 1로 변경
        if i > 5:
            i = 1 
        # 첫번째 값을 꺼내서 i 만큼 뺴주기 
        check = queue.pop(0) - i
        # ch값이 0이거나 0보다 작아진다면 0을 추가하고 반복문 종료
        if check <= 0:
            queue.append(0)
            break
        # 변경된 ch값을 queue의 맨뒤로 추가한다.
        queue.append(check)
        # i를 하나씩 증가시킨다. 
        i += 1
    
    # *queue를 사용하여 list의 값을 순차대로 출력
    print("#{} {} {} {} {} {} {} {} {}".format(t, *queue))