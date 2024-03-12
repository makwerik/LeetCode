class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Создаём переменную, которая будет в себе хранить кол-во уникальных элементов
        """
        result = 1
        """
        Проходимся в цикле по длинне списка
        """
        for n in range(1, len(nums)):
            """
            Если нынешняя n не сходится по индексу с пердыдущим индексом
            """
            if nums[n] != nums[n - 1]:
                """
                То меняем в нашем списке значение по индексу result, на значение полученное по индексу n
                """
                nums[result] = nums[n]
                """
                И увеличиваем переменную result на +1 после каждой замены
                """
                result += 1
        """После выводим сколько раз мы производили замены"""

        return result


if __name__ == '__main__':
    s = Solution()
    assert s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
    assert s.removeDuplicates([1, 1, 2]) == 2
