import sys

T = int(sys.stdin.readline())

for _ in range(T) :
    a, b = map(int, sys.stdin.readline().split())
    print("Case #{}: {}".format(_+1,a+b))