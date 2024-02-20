class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        result = {}
        for index, values in enumerate(nums):
            operation = target - values
            if operation in result:
                return result[operation], index
            result[values] = index

