# 10번 테스트 케이스 반복 
for test_case in range(10) :
    N = int(input()) # 암호문의 길이 저장
    code = list(map(int, input().split())) # code를 list로 저장
    C = int(input()) # 명령어의 개수 저장
    command = list(input().split()) # 명령어를 list로 저장
    com = []  #명령문을 나눌 변수 초기화
    
    #명령문을 변경시킬 반복문_길이는 명령어의 수 만큼 
    for i in range(len(command)) :
        # I를 만나면
        if command[i] == "I" :
            #오버플로우 방지 
            if i != 0 :
                com.append(tmp)
            #빈배열로 초기화
            tmp = []  
        # 마지막 숫자를 만나면 
        elif i == len(command)-1 :
            #tmp에 마지막 숫자를 저장
            tmp.append(int(command[i]))
            #tmp를 com에 복사
            com.append(tmp)
        # tmp변수에 값을 하나씩 추가
        else :
            tmp.append(int(command[i]))
        	
    for i in range(C) : 
        # x,y,s의 수를 찾기
        x = com[i][0] 
        y = com[i][1]
        s = com[i][2:]
        # y의 수만큼 반복
        for j in range(y) : 
            #x + j 위치에 s의 값으로 수정
            code.insert(x+j, s[j])
        
    # 변경된 암호문을 출력한다.
    print("#{} {} {} {} {} {} {} {} {} {} {}".format(test_case+1, *code))