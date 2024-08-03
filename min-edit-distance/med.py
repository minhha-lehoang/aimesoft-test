def min_edit_distance(source, target):
    """Calculate minimum edit distance from the source string
       to the target string using Levenshtein distance algorithm.
       Cost of insertion, deletion, and substitution are 1, 1, and 2 respectively.

    Args:
       source: (str) the source string
       target: (str) the target string

    Returns:
       The minimum edit distance from source to target
    """

    # initialize
    m = len(source)
    n = len(target)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # base conditions
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if source[i - 1] == target[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,    # Deletion
                               dp[i][j - 1] + 1,    # Insertion
                               dp[i - 1][j - 1] + 2) # Substitution with cost 2
                
    return dp[m][n]


if __name__ == "__main__":
    # read input from stdin
    source = input().strip()
    target = input().strip()

    # calculate minimum edit distance
    result = min_edit_distance(source, target)
    print(result)