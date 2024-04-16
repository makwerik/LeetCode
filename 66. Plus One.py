class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ''.join(list(map(str, digits)))
        result = list(map(int, list(str(int(num) + 1))))  #""" Не обессудьте, что так запутанно ^_^ """#

        return result


if __name__ == '__main__':
    s = Solution()
    assert s.plusOne([1, 2, 3]) == [1, 2, 4]
