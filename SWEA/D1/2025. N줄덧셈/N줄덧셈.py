# N변수에 숫자를 입력 받는다. 
N = int(input())
# total 이란 변수를 초기화 한다. 
total = 0 
# N숫자 만큼 반복하여 total변수에 더한다. 
for i in range(1,N+1) :
    total += i
#total을 출력한다
print(total)