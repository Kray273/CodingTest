N , M = map(int, input().split())
basket = [0] * N
for cycle in range(M) :
    i, j, k = map(int, input().split())
    for shot in range(i, j + 1):
        basket[shot-1] = k
print(*basket, sep="\n")
    