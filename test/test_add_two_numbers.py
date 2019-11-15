from unittest import TestCase
from solutions.add_two_numbers import Solution, ListNode, Solution2


class TestAddTwoNumbers(TestCase):
    def test_example_1(self):
        # setting up data
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        # checking answer
        output = Solution().addTwoNumbers(l1, l2)

        self.assertEqual(output.val, 7)
        self.assertEqual(output.next.val, 0)
        self.assertEqual(output.next.next.val, 8)

    def test_list_to_int(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        self.assertEqual(
            342,
            Solution().list_to_int(l1)
        )

    def test_int_to_list(self):
        input = 342
        output = Solution().int_to_list(input)

        self.assertEqual(output.val, 2)
        self.assertEqual(output.next.val, 4)
        self.assertEqual(output.next.next.val, 3)


class TestAddTwoNumbers(TestCase):
    def test_example_1(self):
        # setting up data
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        # checking answer
        output = Solution2().addTwoNumbers(l1, l2)

        self.assertEqual(output.val, 7)
        self.assertEqual(output.next.val, 0)
        self.assertEqual(output.next.next.val, 8)

    def test_appendElement(self):
        node = ListNode(2)
        node.next = ListNode(3)
        node.next.next = ListNode(4)

        Solution2().appendElement(node, 42)

        self.assertEqual(42, node.next.next.next)




