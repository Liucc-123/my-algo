"""
自定义实现列表，着重关注以下三个重点：
1、初始容量：选取一个合适的数组初始容量，在这个案例中，我们选取10作为初始容量
2、容量记录：定义一个变量size，用于记录当前列表中元素的个数。当发生元素变更（添加或删除）时，size进行实时变更
3、扩容机制：如果当前列表的容量已满，则需要扩容；先根据扩容倍数创建一个更大的数组，再将之前数据里的元素复制到新数组中。
在这个案例中，我们定义扩容倍数为2
"""

nums = [1, 2, 3]
nums.clear()

class MyList:
    def __init__(self):
        self._capacity: int = 10  # 列表初始容量是10
        self._arr: list[int] = [0] * self._capacity  # 数组（真正存储元素的容器）
        self._size: int = 0  # 列表长度（当前数组内元素个数）
        self._extend_ratio = 2  # 扩容倍数

    def capacity(self) -> int:
        """获取列表容量"""
        return self._capacity

    def size(self):
        """当前列表的长度"""
        return self._size

    def append(self, num: int):
        """链表末尾添加新元素"""
        # 是否需要扩容
        if self.size() == self.capacity():
            self.extend_capacity()
        self._arr[self.size()] = num
        # 更新数组长度
        self._size += 1

    def insert(self, index: int, num: int):
        """在列表指定位置添加元素"""
        # 检查索引越界
        if index < 0 or index >= self.size():
            raise IndexError("数组越界异常")
        if self.size() == self.capacity():
            self.extend_capacity()
        # 将插入位置及其之后的元素全部后移一位 1, 3, 2, 5, 4, 9, 7 0
        for j in range(self.size(), index, -1):
            self._arr[j] = self._arr[j - 1]
        # 插入元素
        self._arr[index] = num
        # 更新数组长度
        self._size = len(self._arr)

    def remove(self, index: int) -> int:
        """删除指定位置的元素"""
        # 检查索引越界
        if index < 0 or index >= self.size():
            raise IndexError("数组越界异常")
        tmp = self._arr[index]
        # 指定索引及之后的元素前移一位 1 [3] 2 5 4
        for j in range(index, self.size() - 1):
            self._arr[j] = self._arr[j + 1]
        # 返回被删除的元素
        return tmp

    def set(self, index: int, num: int):
        """更新指定位置的元素"""
        # 检查索引越界
        if index < 0 or index >= self.size():
            raise IndexError("数组越界异常")
        self._arr[index] = num
        pass

    def get(self, index: int):
        """获取指定位置的元素"""
        # 检查索引越界
        if index < 0 or index >= self.size():
            raise IndexError("数组越界异常")
        return self._arr[index]

    def to_array(self) -> list[int]:
        """返回有效长度的列表"""
        return self._arr[:self.size()]

    def extend_capacity(self):
        """列表扩容"""
        # 新建一个数组，容量是当前容量的两倍，将原数组的元素复制到新数组中
        self._arr = self._arr + [0] * (self._extend_ratio - 1) * self.capacity()
        # 更新列表容量
        self._capacity = len(self._arr)


if __name__ == '__main__':
    my_list = MyList()
    my_list.append(1)
    my_list.append(3)
    my_list.append(2)
    my_list.append(5)
    my_list.append(4)
    print(f"初始列表：{my_list.to_array()}")
    my_list.append(9)
    my_list.append(7)
    print(f"追加元素后的列表：{my_list.to_array()}")
    print(f"获取列表最后一个元素：{my_list.get(my_list.size() - 1)}")
    num = 10
    my_list.insert(2, num)
    print(f"向索引为2的位置插入元素{num}后的列表：{my_list.to_array()}")
    rem_num = my_list.remove(4)
    print(f"删除索引为4位置的元素，被删除的元素是：{rem_num}，删除后的列表：{my_list.to_array()}")
    my_list.set(3, 100)
    print(f"更新后的列表：{my_list.to_array()}")
