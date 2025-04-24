class NumArray(object):

    output  = []
    

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums 
        NumArray.output = [nums[0]]

        for i in nums[1:]:

            NumArray.output.append(NumArray.output[-1]+i)

        
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        end = 0
        output = NumArray.output
        if left == 0:

            end = output[right]

        else:

            end = output[right]-output[left-1]

        return end

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)