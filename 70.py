class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        """Первое значение"""
        one = 1
        """Второе значение"""
        two = 1
        """Тотал результата"""
        total = 0

        """Запускаем цикл по диапазону числа n - 1"""
        for r in range(n - 1):
            """Тотал результата равен one + two"""
            total = one + two
            """Втрое значение равно первому"""
            two = one
            """Первое значение равно тоталу"""
            one = total

        return total