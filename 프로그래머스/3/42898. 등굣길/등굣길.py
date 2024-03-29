def solution(m, n, puddles):
    matrix = [[0]*(m+1) for _ in range(n+1)]
    matrix[1][1] = 1
    
    for a, b in puddles:
        matrix[b][a] = -1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
                continue
            matrix[i][j] += (matrix[i-1][j] + matrix[i][j-1]) % 1000000007
    
    return (matrix[n][m])