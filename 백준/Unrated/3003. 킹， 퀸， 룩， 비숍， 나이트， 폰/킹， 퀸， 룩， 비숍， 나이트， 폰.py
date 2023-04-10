piece = [1,1,2,2,2,8]

lst = list(map(int, input().split()))
for i in range(6):
    print(piece[i]-lst[i], end=' ')