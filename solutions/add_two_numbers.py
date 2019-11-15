# Definition for singly-linked list.
from typing import Generator, Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def list_to_int(self, l: ListNode) -> int:
        def unpack_number(node: ListNode):
            if node.next is None:
                return f"{node.val}"
            else:
                return unpack_number(node.next) + f"{node.val}"
        return int(unpack_number(l))

    def int_to_list(self, x: int) -> ListNode:
        s = str(x)
        last_node = ListNode(int(s[0]))

        for i in range(1, len(s)):
            tmp_node = ListNode(int(s[i]))
            tmp_node.next = last_node
            last_node = tmp_node

        return last_node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        int_sum = self.list_to_int(l1) + self.list_to_int(l2)
        return self.int_to_list(int_sum)

