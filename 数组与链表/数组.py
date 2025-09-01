import random


def insert(nums: list[int], index: int, num: int):
    """
    向列表指定位置插入元素
    :param nums: 源数组
    :param index: 索引位置
    :param num: 待插入元素
    :return:
    """
    # 插入元素位置及之后的元素全部向后移动一个位置(倒序遍历)
    for i in range(len(nums) - 1, index, -1):
        nums[i] = nums[i - 1]
    # 插入元素
    nums[index] = num


def random_access(nums: list[int]):
    """
    随机访问给定数组中的一个元素
    :param nums:
    :return:
    """
    index = random.randint(0, len(nums) - 1)
    return nums[index]


def remove(nums: list[int], index: int):
    """
    删除指定索引index位置的元素，将index之后的元素逐个前移
    :param nums:数组
    :param index:删除元素下标索引
    :return:返回被删除的元素
    """
    for i in range(index, len(nums) - 1):
        data = nums[index]
        # 将index位置后面的元素逐个前移一个
        nums[i] = nums[i + 1]
        return data
    return None


def traverse(nums: list[int]):
    """遍历数组"""
    # python提供三种遍历序列对象的方式
    # 1、直接遍历数组元素
    print("直接遍历方式：".center(20))
    for num in nums:
        print(num, end="\t")
    print()
    # 2、通过下标索引
    print("通过下标索引遍历方式：".center(20))
    print("索引:", end=' ')
    for i in range(len(nums)):
        print(i, end="\t")
    print()
    print("元素:", end=' ')
    for i in range(len(nums)):
        print(nums[i], end="\t")
    print()
    # 3、同时遍历数据索引和元素
    print("同时遍历数据索引和元素：".center(20))
    for i, v in enumerate(nums):
        print(i, v)


def find(nums: list[int], target: int):
    """
    在数组中查找指定元素，并返回索引位置。不存在返回-1
    :param nums:
    :param target:
    :return:
    """
    index = -1
    for i in range(len(nums)):
        if target == nums[i]:
            index = i
            break
    return index


def grow(nums: list[int], enlarge: int):
    """
    将原数组扩容n倍
    :param nums:
    :param enlarge:
    :return: 扩容后的新数组
    """
    # 初始化一个扩容倍数后的新数组
    grown_list = [0] * len(nums) * enlarge
    # 复制原数组元素到新数组中
    for i, v in enumerate(nums):
        grown_list[i] = v
    return grown_list

""" 测试代码 """
if __name__ == '__main__':
    # 初始化数组
    arr = [0] * 5
    print(f"数组 arr = {arr}")
    # 给定初始值
    nums = [1, 3, 2, 5, 4]
    print(f"数组 nums = {nums}")

    # 随机访问
    random_data = random_access(nums)
    print(f"获取数组nums随机的一个元素：{random_data}")

    #  插入元素
    insert(nums, 1, 6)
    print(f"向nums数组的索引为1的位置插入元素6，更新后的数组：{nums}")

    # 删除元素
    data = remove(nums, 2)
    print(f"删除下标索引为2的元素：{data}")

    # 遍历数组
    traverse(nums)

    # 查找元素
    target = 5
    index = find(nums, target)
    print(f"找到指定元素{target}，索引位置是：{index}" if index != -1 else f"未找到指定元素{target}")

    # 扩容数组
    nums = grow(nums, 2)
    print(f"扩容后新数组：{nums}")