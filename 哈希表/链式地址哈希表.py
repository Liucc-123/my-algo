"""链式地址法解决哈希冲突，这里每一个桶元素使用列表替代链表来存放hash 冲突的元素，简化开发"""

class Pair:
    def __init__(self, key: int, val: str):
        self.key = key
        self.val = val


class HashMapChaining:
    def __init__(self):
        """构造方法"""
        self.size = 0  # 键值对的数量
        self.capacity = 4  # 数组容量
        self.extend_ratio = 2  # 扩容倍数
        self.thres = 2.0 / 3.0  # 触发扩容临界值
        self.buckets = [[] for _ in range(self.capacity)]  # 桶数组

    def hash_func(self, key: int):
        """哈希函数"""
        return key % self.capacity

    def load_factor(self):
        """负载因子，负载因子超过 thres，会触发扩容"""
        return self.size / self.capacity

    def get(self, key: int) -> str | None:
        """通过 key 获取键值对的值"""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # 遍历
        for pair in bucket:
            if key == pair.key:
                return pair.val
        return None

    def put(self, key: int, val: str):
        """添加或更新键值对"""
        # 检查是否需要扩容
        if self.load_factor() > self.thres:
            self.extend()
        pair = Pair(key, val)
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # bucket 内元素为空，说明未发生冲突，可直接添加
        if len(bucket) == 0:
            bucket.append(pair)
            self.size += 1
            return
        # 遍历 hash冲突的桶列表
        for item in bucket:
            # 找到 key 相同的元素，覆盖
            if item.key == key:
                item.val = val
                return
        # key 均不相同，追加到桶列表的末尾
        bucket.append(pair)
        self.size += 1

    def remove(self, key: int) -> str | None:
        """删除键值对，返回被删除元素的值"""
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair.key == key:
                # tmp = pair.val
                bucket.remove(pair)
                self.size -= 1
                return pair.val

    def print(self):
        """打印哈希表"""
        for bucket in self.buckets:
            res = []
            for pair in bucket:
                res.append(f"{pair.key} -> {pair.val}")
            print(res)

    def extend(self):
        """数组的扩容"""
        # 保留旧数组
        old_buckets = self.buckets
        self.capacity *= self.extend_ratio
        new_buckets = [[] for _ in range(self.capacity)]
        self.buckets = new_buckets
        self.size = 0
        # 迁移旧数组中的元素到新数组中
        for bucket in old_buckets:
            for pair in bucket:
                self.put(pair.key, pair.val)


"""测试代码"""
if __name__ == "__main__":
    # 初始化哈希表
    hashmap = HashMapChaining()

    # 添加操作
    # 在哈希表中添加键值对 (key, value)
    hashmap.put(12836, "小哈")
    hashmap.put(15937, "小啰")
    hashmap.put(16750, "小算")
    hashmap.put(13276, "小法")
    hashmap.put(10583, "小鸭")
    print("\n添加完成后，哈希表为\n[Key1 -> Value1, Key2 -> Value2, ...]")
    hashmap.print()

    # 查询操作
    # 向哈希表中输入键 key ，得到值 value
    name = hashmap.get(13276)
    print("\n输入学号 13276 ，查询到姓名 " + name)

    # 删除操作
    # 在哈希表中删除键值对 (key, value)
    print(f"删除元素：{hashmap.remove(12836)}")
    print("\n删除 12836 后，哈希表为\n[Key1 -> Value1, Key2 -> Value2, ...]")
    hashmap.print()