import sys
sys.stdin = open('sample_input.txt')
T=int(input())
for tc in range(1,T+1):
    N =int(input())
    grid = [list(input().strip()) for _ in range(N)]
        # 상 하 좌 우 상좌 상우 하좌 하우
    dr = [-1,1,0,0,-1,-1, 1, 1]
    dc = [0,0,-1,1,-1, 1, -1, 1]

    result = 'NO' # 도움 받음

    for r in range(N):
        
        for c in range(N):

            for d in range(8):
                    
                    count = 0 # 도움 받음

                    for distance in range(5):

                        nr = r + dr[d] * distance
                        nc = c + dc[d] * distance

                        if 0 <= nr < N and 0 <= nc < N:
                            if grid[nr][nc] == 'o':
                                  count += 1
                            else:
                                 break
                        else:
                             break

                    if count == 5:
                        result = 'YES'
                    # else: # 도움 받음
                    #     result = 'NO'

    print(f'#{tc} {result}')