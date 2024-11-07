def lcsub_tabulation(s1, s2):
    m, n = len(s1), len(s2)
    
    # Create a dp table with (m+1) x (n+1) size, initialized to 0
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # The result is in dp[m][n]
    return dp[m][n]

def main():
    s1 = "adebcc"
    s2 = "dcadbzzc"
    
    # Find the length of the longest common subsequence using tabulation
    result = lcsub_tabulation(s1, s2)
    print("Length of longest common subsequence:", result)

if __name__ == "__main__":
    main()
