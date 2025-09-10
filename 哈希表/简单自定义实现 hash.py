"""下面简单实现一个自定义的 hash 表，其中将 key 和 val 封装成一个 Pair 类来表示键值对"""

class Pair:
    def __init__(self, key: int, val: str):
        self.key = key
        self.val = val

class ArrayHashMap:

    def __init__(self):
        """构造方法"""
        # 初始化 100个桶
        self.buckets: list[Pair | None] = [None] * 100

    def hash_func(self, key: int):
        """计算 key 的 hash 值"""
        index = key % len(self.buckets)
        return index

    def get(self, key: int):
        """根据 key 获取 val"""
        index = self.hash_func(key)
        pair: Pair = self.buckets[index]
        return pair.val if pair else None

    def put(self, key: int, val: str):
        """更新键值对"""
        pair: Pair = Pair(key, val)
        index = self.hash_func(key)
        self.buckets[index] = pair

    def remove(self, key: int):
        """删除操作"""
        index = self.hash_func(key)
        self.buckets[index] = None

    def entry_set(self):
        """获取所有键值对"""
        pairs: list[Pair] = []
        for pair in self.buckets:
            if pair is not None:
                pairs.append(pair)
        return pairs

    def keys(self):
        """获取所有的键值"""
        keys: list[int] = []
        for pair in self.buckets:
            if pair:
                keys.append(pair.key)
        return keys

    def values(self):
        """"获取所有的 val 值"""
        values: list[str] = []
        for pair in self.buckets:
            if pair:
                values.append(pair.val)
        return values

    def print(self):
        """打印所有键值对信息"""
        for pair in self.buckets:
            if pair:
                print(f"{pair.key} -> {pair.val}")


"""测试代码"""
if __name__ == "__main__":
    # 初始化哈希表
    hmap = ArrayHashMap()

    # 添加操作
    # 在哈希表中添加键值对 (key, value)
    hmap.put(12836, "小哈")
    hmap.put(15937, "小啰")
    hmap.put(16750, "小算")
    hmap.put(13276, "小法")
    hmap.put(10583, "小鸭")
    print("\n添加完成后，哈希表为\nKey -> Value")
    hmap.print()

    # 查询操作
    # 向哈希表中输入键 key ，得到值 value
    name = hmap.get(15937)
    print("\n输入学号 15937 ，查询到姓名 " + name)

    # 删除操作
    # 在哈希表中删除键值对 (key, value)
    hmap.remove(10583)
    print("\n删除 10583 后，哈希表为\nKey -> Value")
    hmap.print()

    # 遍历哈希表
    print("\n遍历键值对 Key->Value")
    for pair in hmap.entry_set():
        print(pair.key, "->", pair.val)

    print("\n单独遍历键 Key")
    for key in hmap.keys():
        print(key)

    print("\n单独遍历值 Value")
    for val in hmap.values():
        print(val)
