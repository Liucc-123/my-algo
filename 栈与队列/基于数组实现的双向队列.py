"""
与环形数组实现队列相似，这里可以继续使用环形数组实现双向队列
front表示队首元素的位置
rear表示队尾元素的下一位置，也即下一个元素可以插入的索引位置
"""


class ArrayDeque:
    def __init__(self, size: int):
        """构造器，初始化指定容量的环形数组"""
        self._front: int = 0
        self._rear: int = 0
        self._size: int = 0
        self._arr = [0] * size

    def size(self):
        """队列长度"""
        return self._size

    def capacity(self):
        """队列容量"""
        return len(self._arr)

    def is_empty(self):
        """队列是否为空"""
        return self.size() == 0

    def index(self, i: int) -> int:
        """
        计算i应该在环形数组中的索引位置，当到达队列头部/尾部时，下一次索引位置会跳转到队列尾部/头部
        """
        return (i + self.capacity()) % self.capacity()

    def append_last(self, val: int):
        """从队列尾部添加元素"""
        # 队列是否已满
        if self.size() == self.capacity():
            print("队列已满")
            return
        self._arr[self._rear] = val
        self._size += 1
        self._rear = self.index(self._rear + 1)

    def append_first(self, val: int):
        """从队列头部添加元素"""
        # 队列是否已满
        if self.size() == self.capacity():
            print("队列已满")
            return
        self._front = self.index(self._front - 1)
        self._arr[self._front] = val
        self._size += 1

    def pop_last(self):
        """从队列尾部删除元素"""
        if self.is_empty():
            print("队列为空，无法删除")
            return None
        self._rear = self.index(self._rear + 1)
        val = self._arr[self._rear]
        self._size -= 1
        return val

    def pop_first(self):
        """从队列头部删除元素"""
        if self.is_empty():
            print("队列为空，无法删除")
            return None
        val = self._arr[self._front]
        self._front = self.index(self._front - 1)
        self._size -= 1
        return val
    def peek_last(self):
        """访问队列尾部元素"""
        if self.is_empty():
            raise IndexError("队列为空")
        return self._arr[self.index(self._rear-1)]

    def peek_first(self):
        """访问队列头部元素"""
        if self.is_empty():
            raise IndexError("队列为空")
        return self._arr[self._front]

    def to_array(self):
        """将队列转为数组，便于打印"""
        arr: list[int] = []
        idx = self._front
        for _ in range(self.size()):
            arr.append(self._arr[idx])
            idx = self.index(idx +1)
        return arr

if __name__ == '__main__':
    deq = ArrayDeque(5)
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