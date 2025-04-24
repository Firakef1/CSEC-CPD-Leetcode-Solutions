class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        output = [nums[0]]

        
        for i in nums[1:]:

            output.append(output[-1]+i)

        return output
        