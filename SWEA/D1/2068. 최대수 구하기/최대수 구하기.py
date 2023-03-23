#T 변수에 값을 받는다.
T = int(input())

for test_case in range(1, T +1) : 
	#num 변수에 테스트 값을 받는다.
	num = map(int, input().split())
    #max()를 이용하여 최대값을 찾는다. 
	max_ = max(num)
	print('#{} {}'.format(test_case, max_))