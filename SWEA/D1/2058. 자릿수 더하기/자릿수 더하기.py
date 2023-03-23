# N변수에 값은 문자열로 받아온다.
N = input()
#빈 list 배열을 선언 
lst = []
#반복문을 이용 lst에 N변수의 문자열을 하나씩 꺼내 더한다. 
for i in N :
    lst.append(int(i))
#sum함수를 이용 lst를 출력한다.
print(sum(lst))