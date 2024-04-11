class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split()[-1])


if __name__ == '__main__':
    s = Solution()
    assert s.lengthOfLastWord("Hello World") == 5
    assert s.lengthOfLastWord("   fly me   to   the moon  ") == 4
    assert s.lengthOfLastWord("luffy is still joyboy") == 6
