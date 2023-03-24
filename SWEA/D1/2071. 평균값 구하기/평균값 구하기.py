T = int(input())
for test_case in range( 1, T+1) : 
    num = list(map(int, input().split()))
    avg_num = round(sum(num) / len(num))
    print("#{} {}".format(test_case, avg_num))