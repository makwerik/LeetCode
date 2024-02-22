class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        """Возвращаем пустую строку, если пуста строка =)"""
        if len(strs) == 0:
            return ''

        """Берём первое слово из списка и создаем цикл равный длинне этого слова"""
        first_word = strs[0]
        for index_ in range(len(first_word)):
            """Дальше создаем цикл в котором будем проходиться по каждому слову, пропуская нулевое"""
            for word in strs[1:]:
                """
                Если индекс равен длинне слова или буквы которые мы получаем по индексу index_ не равны, 
                вовзращаем срез first_word[:index_]    
                """
                if index_ == len(word) or first_word[index_] != word[index_]:
                    return first_word[:index_]
        return first_word

