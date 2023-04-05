total = int(input())
N = int(input())
result = 0
for test_case in range(N) :
    p,c = map(int, input().split())
    result += p * c
print("Yes") if result == total else print("No")