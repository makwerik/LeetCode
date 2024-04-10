class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            return nums.index(target)
        except:
            result = []

            for i in nums:
                if target > i:
                    result.append(i)

            if len(result) > 0:
                return nums.index(result[-1]) + 1
            else:
                return 0


if __name__ == '__main__':
    s = Solution()
    assert s.searchInsert([1, 3, 5, 6], 5) == 2
    assert s.searchInsert([1, 3, 5, 6], 2) == 1
    assert s.searchInsert([1, 3, 5, 6], 7) == 4


