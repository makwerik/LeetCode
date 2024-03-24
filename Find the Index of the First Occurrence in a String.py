class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)


if __name__ == '__main__':
    s = Solution()
    assert s.strStr('sadbutsad', 'sad') == 0
    assert s.strStr('leetcode', 'leeto') == -1
