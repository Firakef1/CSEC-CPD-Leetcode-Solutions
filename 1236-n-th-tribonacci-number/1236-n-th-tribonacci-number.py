class Solution(object):
    def tribonacci(self, n, memo={}):
        """
        :type n: int
        :rtype: int
        """

        if n in memo:

            return memo[n]
        if n == 0:
            memo[0] = 0
            return 0

        if n == 2 or n == 1:
            memo[n] = 1
            return 1
        
        memo[n] = self.tribonacci(n-3, memo)+self.tribonacci(n-2, memo)+self.tribonacci(n-1, memo)
        return memo[n]
    