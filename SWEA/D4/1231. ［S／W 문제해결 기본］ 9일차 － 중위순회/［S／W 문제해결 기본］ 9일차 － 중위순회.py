# In_order함수 지정
def in_order(idx):
    # idx가 정점의 수 보다 커지면 종료
    if idx > N : 
        return
    # idx에 *2 보다 N이 크면 왼쪽노드가 있다는 의미
    if (2 * idx) <= N :
        #idx *2 를 지정
        in_order(2*idx)        
    # node에 인덱스 값을 추가 
    idx_node.append(node[idx])
    # idx*2 +1 보다 N이 크면 오른쪽 노드가 있다는 의미
    if (2 * idx +1) <= N : 
    	# idx * 2 +1을 추가
        in_order(idx * 2 + 1)
    
# test_case를 10번 반복
for test_case in range(10):
	# N에 정점의 수를 받는다.
    N = int(input())
    # node 초기화 : 0으로 점점의 수만큼 초기화  
    node = [0] * (N+1)
    
    #N번만큼 반복
    for n in range(N):
        #노드에 넣을 값 받아오기 
        vals= list(input().split())
        #노드에 문자 추가
        node[int(vals[0])] = vals[1]
    #idx를 추가할 node값 초기화
    idx_node = []
    # 중위 순회 함수 호출
    in_order(1)
    #출력
    print("#{} {}".format(test_case +1, ''.join(idx_node)))