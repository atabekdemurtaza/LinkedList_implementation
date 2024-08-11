from typing import Optional


class ListNode:
    def __init__(self, val: int, next: Optional['ListNode'] = None):
        self.val = val
        self.next = None

    def __repr__(self) -> str:
        return str(self.val)
