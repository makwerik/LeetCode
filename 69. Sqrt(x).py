class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        while left <= right:
            """
                Пока левая позиция меньше правой, складываем две позиции и делим на 2
            """
            mid = (left + right) // 2
            if mid * mid < x:
                """
                    Если полученое значение умножить на себя и оно останется меньше таргета, меняем левую позицию на полученый результат +1
                """
                left = mid + 1
            elif mid * mid > x:
                """
                    Если наоборот, то отнимаем -1
                """
                right = mid - 1
            else:
                """В противном случаем возвращаем значение"""
                return mid

        return right

if __name__ == '__main__':
    s = Solution()
    assert s.mySqrt(4) == 2