def findNumberOfStrings(n):
    DP = [[0 for i in range(6)]
             for i in range(n + 1)]
    DP[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, 6):
            if (i == 1):
                DP[i][j] = DP[i][j - 1] + 1
            else:
                DP[i][j] = DP[i][j - 1]+ DP[i - 1][j]
    return DP[n][5]
if __name__ == '__main__':
    N = 2
    print(findNumberOfStrings(N))
 

 
