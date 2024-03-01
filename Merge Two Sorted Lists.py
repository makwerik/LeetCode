# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# without ops after while loop
class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


"""
Рекурсивный подход:
Рекурсивный подход основан на идее, что мы сравниваем значения первых узлов двух списков, и тот из них, который имеет
меньшее значение, мы добавляем этот узел в наш объединенный связанный список и рекурсивно вызываем ту же функцию со
следующим узлом этого списка и текущим узлом другого списка. Мы повторяем этот процесс до тех пор, пока один из
списков не закончится, и мы возвращаем объединенный список.
"""