class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        
        subs_matrix = [[False for j in range(n + 1)] for i in range(m + 1)]
        
        for j in range(n + 1):
            subs_matrix[0][j] = True
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    subs_matrix[i][j] = subs_matrix[i-1][j-1]
                else:
                    subs_matrix[i][j] = subs_matrix[i][j - 1]
                    
        return subs_matrix[m][n]
    
print(Solution().isSubsequence("abc", "ahbgdc"))