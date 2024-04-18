# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
def reverse(head):

    li = list()
    while(head != None):
        li.append(head.val)
        head = head.next
    print(li)
    fair, res = None, None
    if len(li) != 0:
        fair = ListNode(li.pop(), None)
        res = fair
    # print(li)
    while(len(li) != 0):
        fair.next = ListNode(li.pop(), None)
        fair = fair.next
    return res
'''


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        return reverse(head)
        '''

        prev = None
        current = head
        
        while current:
            next_node = current.next  # 保存下一個節點 (current還需要/保留)
            current.next = prev  # 將當前節點的下一個指針指向前一個節點 (轉向)
            prev = current  # 更新前一個節點 (prev推進)
            current = next_node  # 移動到下一個節點 (current推進)
        
        # 最終 prev 會指向新的頭節點
        return prev
