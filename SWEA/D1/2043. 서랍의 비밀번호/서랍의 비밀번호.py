# P, K 변수에 값을 넣는다.
P , K = map(int, input().split())

# 조건문을 통해 P >= K인 경우 P에서 K를 뺀 후 1을 더한다. 
if P >= K :
    print(P - K +1)
elif P < K:  
    # 만약 P가 더 작은 경우 K에서 P를 뺀 후 1을 더한다. 이후 한 방향으로 돌기 떄문에 + 999를 해준다 
    print(K - P +1 + 999) 