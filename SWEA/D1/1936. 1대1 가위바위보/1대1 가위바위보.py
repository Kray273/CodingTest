# 입력된 값을 변수 A,B에 담는다
A, B = map(int, input().split())

#A가 이기는 경우의 수인 1과 -2를 찾아 A를 출력 나머지는 B
if (A - B) == 1 or -2 :  
    print('A')
else : 
    print('B')