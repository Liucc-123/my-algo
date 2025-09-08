"""
双向队列支持从队首、队尾分别添加和删除元素，因此对于链表来说，需要在添加一个指针prev，代表指向前驱节点
"""


class ListNode:
    def __init__(self, val: int):
        """构造方法"""
        self.val: int = val
        self.next: ListNode | None = None  # 指向后继节点
        self.prev: ListNode | None = None  # 指向前驱节点


class LinkedListDeque:
    """基于链表实现的双向队列"""

    def __init__(self):
        """构造方法"""
        self._front: ListNode | None = None  # 头指针
        self._rear: ListNode | None = None  # 尾指针
        self._size: int = 0  # 队列长度

    def size(self):
        """队列长度"""
        return self._size

    def is_empty(self) -> bool:
        """队列是否为空"""
        return self.size() == 0

    def _append(self, val: int, is_front: bool):
        """
        向队列添加元素
        :is_front: 是否从队首添加元素，否则从队尾添加
        """
        node = ListNode(val)
        # 首次添加
        if self.is_empty():
            self._front = node
            self._rear = node
        elif is_front:  # 队首添加
            tmp = self._front
            node.next = tmp
            tmp.prev = node
            self._front = node
        else:  # 队尾添加
            tmp = self._rear
            tmp.next = node
            node.prev = tmp
            # 更新尾指针
            self._rear = node
        self._size += 1

    def append_last(self, val: int):
        """从队尾添加元素"""
        self._append(val, False)

    def append_first(self, val: int):
        """从队首添加元素"""
        self._append(val, True)

    def _pop(self, is_front: bool):
        """
        元素出队
        :is_front:表示是否从队首出队
        """
        if self.is_empty():
            raise IndexError("队列为空")
        if is_front:
            val = self._front.val
            next: ListNode | None = self._front.next
            if next:
                next.prev = None
            # 更新头指针
            self._front = next
        else:
            val = self._rear.val
            prev = self._rear.prev
            if prev:
                prev.next = None
            # 更新尾指针
            self._rear = prev
        self._size -= 1
        return val

    def pop_last(self):
        """从队尾删除元素"""
        return self._pop(False)

    def pop_first(self):
        """从队首删除元素"""
        return self._pop(True)

    def peek_last(self):
        """从队尾查看元素"""
        if self.is_empty():
            raise IndexError("队列为空")
        return self._rear.val

    def peek_first(self):
        """从队首查看元素"""
        if self.is_empty():
            raise IndexError("队列为空")
        return self._front.val

    def to_array(self):
        """将队列转为数组，方便打印"""
        arr: list[int] = []
        # 遍历链表
        tmp = self._front
        while tmp:
            arr.append(tmp.val)
            tmp = tmp.next
        return arr


if __name__ == '__main__':
    deq = LinkedListDeque()
    deq.append_last(1)
    deq.append_last(3)
    deq.append_last(2)
    deq.append_first(5)
    deq.append_first(4)
    print(f"队列元素是： {deq.to_array()}")
    print(f"队首元素是：{deq.peek_first()}")
    print(f"队尾元素是：{deq.peek_last()}")
    print(f"队首弹出元素：{deq.pop_first()}")
    print(f"队尾弹出元素：{deq.pop_last()}")
    print(f"此时队列长度为：{deq.size()}")
