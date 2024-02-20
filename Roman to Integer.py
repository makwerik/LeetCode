class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = []
        split_text = s
        if 'IV' in s:
            split_text = split_text.replace('IV', '')
            result.append(4)
        if 'IX' in s:
            split_text = split_text.replace('IX', '')
            result.append(9)
        if 'XL' in s:
            split_text = split_text.replace('XL', '')
            result.append(40)
        if 'XC' in s:
            split_text = split_text.replace('XC', '')
            result.append(90)
        if 'CD' in s:
            split_text = split_text.replace('CD', '')
            result.append(400)
        if 'CM' in s:
            split_text = split_text.replace('CM', '')
            result.append(900)


        if len(split_text) == 0:
            return sum(result)
        else:
            for i in split_text:
                result.append(d[i])
            return sum(result)