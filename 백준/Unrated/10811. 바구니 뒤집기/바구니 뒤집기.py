N , M = map(int, input().split())
basket = [i for i in range(N + 1 )]

for reverse_order in range(M) :
    i, j = map(int, input().split())
    basket[i:j+1] = reversed(basket[i:j+1])
basket.remove(basket[0])
print(*basket)