class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

 
        length = len(nums)
        counter = 0
        print(nums)
        for i in range(length):

            for j in range(i+1, length):

                if (i*j)%k == 0 and nums[i] == nums[j]:

                    counter += 1

                    print(i, j)

        return counter 
        