import sys


class Solution:

    def countWaystoDivide(self, N, K):
        dp = [[[0 for _ in range(K+1)] for _ in range(N+1)]
              for _ in range(N+1)]
        for i in range(1, N+1):
            dp[i][0][0] = 1
        for max_value in range(1, N+1):
            for remaining_sum in range(1, N+1):
                for remaining_groups in range(1, K+1):
                    dp[max_value][remaining_sum][remaining_groups] = dp[max_value -
                                                                        1][remaining_sum][remaining_groups]
                    if remaining_sum >= max_value:
                        dp[max_value][remaining_sum][remaining_groups] += dp[max_value][remaining_sum -
                                                                                        max_value][remaining_groups-1]
        ans = 0
        for i in range(1, N+1):
            ans += dp[i][N-i][K-1]
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(1000000)

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N =int(input())
        K=int(input())
        ob = Solution()
        print(ob.countWaystoDivide(N,K))
        
        T -= 1
# } Driver Code Ends