N = int(input())
M = list(map(int, input().split()))
M_max = max(M)
M_avg = [] 
for new_avg in M :
    M_avg.append(new_avg/M_max *100) 
result = sum(M_avg)/N
print(result)
      
