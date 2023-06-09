import sys
input = sys.stdin.readline

n,m = map(int,input().split())
square = []
dp = [[0]*(m) for _ in range(n)]
answer = 0

for _ in range(n) :
    square.append(list(map(int,list(input().rstrip()))))

for i in range(n) :
    for j in range(m) :
        if i==0 and j == 0 :
            dp[i][j] = square[i][j]
        elif square[i][j] == 1 :
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        
        answer = max(dp[i][j], answer)
    
    # 행마다 max값 다시 확인하면 -> 시간초과
    # answer = max(max[i][j]), answer) 
print(answer**2)