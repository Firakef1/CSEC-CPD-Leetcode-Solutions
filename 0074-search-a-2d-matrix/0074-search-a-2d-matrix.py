class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        for row in range(len(matrix)):

            for col in range(len(matrix[0])):

                if matrix[row][-1] < target:

                    break
                elif matrix[row][0] > target:
                    return False

                if matrix[row][col] == target:

                    return True

        return False
        