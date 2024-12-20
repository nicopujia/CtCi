from typing import Any, Iterator, Self


class LinkedListNode:
    def __init__(self, data: Any, next: Self | None = None) -> None:
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return str(self.data) + (f" → {self.next}" if self.next else "")

    def __iter__(self) -> Iterator[Self]:
        node = self
        yield node
        while node.next:
            node = node.next
            yield node

    def __next__(self) -> Self:
        return self.next

    def __gt__(self, other: Self) -> bool:
        return self.data > other.data

    def __lt__(self, other: Self) -> bool:
        return self.data < other.data


# O(n^2), O(1)
def remove_dups(head: LinkedListNode) -> LinkedListNode:
    # TODO: doesn't remove last element
    for node in head:
        if not node.next:
            break
        for following_node in node:
            if not following_node.next:
                break
            is_duplicate = node.data == following_node.next.data
            if is_duplicate:
                following_node.next = following_node.next.next
    return head


# O(n), O(1)
def get_kth_to_last(head: LinkedListNode, k: int) -> LinkedListNode:
    length = 0
    for _ in head:
        length += 1

    for i, node in enumerate(head):
        if length - i == k:
            return node

    raise IndexError()


# O(n), O(n)
def delete_middle_node(node: LinkedListNode) -> None:
    if node.next:
        node.data = node.next.data
        if node.next.next:
            node.next.delete()
        else:
            node.next = None
    else:
        node = None


# O(n), O(n)*
def partition(head: LinkedListNode, x: int) -> LinkedListNode:
    left, right = [], []
    for node in head:
        if node < x:
            left.append(node)
        else:
            right.append(node)
    full = left + right
    for i in range(len(full)):
        full[i].next = full[i + 1] if i < len(full) - 1 else None
    return full[0]


# O(n + m + d), O(d)
def sum_lists(
    head_1: LinkedListNode, head_2: LinkedListNode
) -> LinkedListNode:
    def ll_to_int(head: LinkedListNode) -> int:
        num = 0
        for i, node in enumerate(head):
            num += node.data * 10**i
        return num

    num = ll_to_int(head_1) + ll_to_int(head_2)
    head = tail = LinkedListNode(num % 10)

    while num // 10 > 0:
        num //= 10
        tail.next = LinkedListNode(num % 10)
        tail = tail.next

    return head


# O(n + m + d), O(d)
def sum_lists_follow_up(
    head_1: LinkedListNode, head_2: LinkedListNode
) -> LinkedListNode:
    def ll_to_int(head):
        length = 0
        for _ in head:
            length += 1

        num = 0
        for i, node in enumerate(head, 1):
            num += node.data * 10 ** (length - i)

        return num

    num = str(ll_to_int(head_1) + ll_to_int(head_2))

    head = tail = LinkedListNode(int(num[0]))
    for digit in num[1:]:
        tail.next = LinkedListNode(int(digit))
        tail = tail.next

    return head


# O(n), O(1)
def check_palindrome(head: LinkedListNode) -> bool:
    length = 0
    for _ in head:
        length += 1

    node = head.next
    head.next = None
    i = 1
    while i < length // 2:
        i += 1
        old_next = node.next
        node.next = head
        head = node
        node = old_next

    for n, m in zip(head, node if length % 2 == 0 else node.next):
        if n.data != m.data:
            return False
    return True


# O(n), O(1)
def check_intersection(head_1: LinkedListNode, head_2: LinkedListNode) -> bool:
    # TODO: it only works with lists of the same length. Fix that.
    for n, m in zip(head_1, head_2):
        if n is m:
            return True
    return False


# O(n^2), O(1)
def detect_loop(head: LinkedListNode) -> LinkedListNode:
    for node in head:
        for checking_node in head:
            if checking_node is node.next:
                return checking_node

            if checking_node is node:
                break


# * means that the complexity is not optimal.
# See the book for more optimal solutions on those problems.
