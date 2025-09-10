# 哈希表的常见操作包括：初始化、查询操作、添加键值对和删除键值对等

# 初始化哈希表
# {学号: 姓名}
hmap:dict[int, str] = {}
# hmap = dict()

# 添加键值对
hmap[1001] = "小哈"
hmap[1002] = "小啰"
hmap[1003] = "小算"
hmap[1004] = "小法"
hmap[1005] = "小鸭"

# 查询操作
# 获取学号是 1004的学生信息
print(f"学生是 1004的学生姓名是：{hmap.get(1004)}")
print(f"学生是 1004的学生姓名是：{hmap[1004]}")

# 删除键值对
hmap.pop(1002)
del hmap[1001]
print(hmap)

# 遍历哈希表
# 方式一：同时获取键值对
print("方式一：同时获取键值对")
for key, val in hmap.items():
    print(f"{key} -> {val}", end="\n")
# 方式二：通过 key获取 val
print("# 方式二：通过 key获取 val")
for key in hmap.keys():
    print(f"{key} -> {hmap[key]}")

# 清空哈希表
hmap.clear()

# 删除哈希表
del hmap
# print(hmap)
