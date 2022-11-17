class Solution:
    dp = collections.defaultdict(int)
    def fib(self, N: int) -> int:
        self.dp[0] = 0
        self.dp[1] = 1
        
        for i in range(2, N+1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]
        return self.dp[N]
        
        # if N <=1:
        #     return N
        # if self.dp[N]:
        #     return self.dp[N]
        # self.dp[N] = self.fib(N-1) + self.fib(N-2)
        # return self.dp[N]