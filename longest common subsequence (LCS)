def lcsub(s1, s2, ind1, ind2, dp):
    if ind1 == -1 or ind2 == -1:
        return 0
    if dp[ind1][ind2] != -1:
        return dp[ind1][ind2]
    
    if s1[ind1] == s2[ind2]:
        dp[ind1][ind2] = 1 + lcsub(s1, s2, ind1 - 1, ind2 - 1, dp)
    else:
        dp[ind1][ind2] = max(
            lcsub(s1, s2, ind1 - 1, ind2, dp),
            lcsub(s1, s2, ind1, ind2 - 1, dp),
            lcsub(s1, s2, ind1 - 1, ind2 - 1, dp)
        )
    
    return dp[ind1][ind2]

def main():
    s1 = "adebcc"
    s2 = "dcadbzzc"
    
    # Create a dp table initialized to -1
    dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
    
    # Find the length of the longest common subsequence
    result = lcsub(s1, s2, len(s1) - 1, len(s2) - 1, dp)
    print("Length of longest common subsequence:", result)
    
    # Uncomment below lines to print the dp table
    # for row in dp:
    #     print(row)

if __name__ == "__main__":
    main()
