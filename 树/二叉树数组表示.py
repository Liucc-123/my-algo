"""
File: 二叉树数组表示.py
Created Time: 2025-09-17
Author: falcon (liuc47810@gmail.com)
"""

from modules.tree_node import list_to_tree
from modules.print_util import print_tree

"""
二叉树的常见操作如下：
给定某节点值，获取它的值、左右子节点、父节点
层序遍历、前序、中序、后序遍历
"""


class ArrayBinaryTree:
    """数组表示下的二叉树类"""

    def __init__(self, arr: list[int | None]):
        self._tree = arr

    def size(self):
        """列表容量"""
        return len(self._tree)

    def val(self, i: int):
        """获取指定节点的值"""
        # 索引越界
        if i < 0 or i >= self.size():
            return None
        return self._tree[i]

    def left(self, i: int):
        """获取索引为 i 的节点的左子节点对应的索引"""
        return 2 * i + 1

    def right(self, i: int):
        """获取索引为 i 的节点的右子节点对应的索引"""
        return 2 * i + 2

    def parent(self, i: int):
        """获取父节点"""
        return (i - 1) // 2

    def level_order(self) -> list[int]:
        """层序遍历"""
        self.res = []
        for item in self._tree:
            if item is not None:
                self.res.append(item)
        return self.res

    def dfs(self, i: int, order: str) -> list[int]:
        """深度优先遍历"""
        if self.val(i) is None:
            return
        # 前序遍历
        if order == 'pre':
            self.res.append(self._tree[i])
        self.dfs(self.left(i), order)
        # 中序遍历
        if order == 'in':
            self.res.append(self._tree[i])
        self.dfs(self.right(i), order)
        # 后序遍历
        if order == 'post':
            self.res.append(self._tree[i])
        return self.res


    def pre_order(self, i: int) -> list[int]:
        """前序遍历：根左右"""
        self.res = []
        return self.dfs(i, 'pre')

    def in_order(self, i):
        """中序遍历：左根右"""
        self.res = []
        return self.dfs(i, 'in')

    def post_order(self, i):
        """后序遍历：左右根"""
        self.res = []
        return self.dfs(i, 'post')


"""测试代码"""
if __name__ == "__main__":
    # 初始化二叉树
    # 这里借助了一个从数组直接生成二叉树的函数
    arr = [1, 2, 3, 4, None, 6, 7, 8, 9, None, None, 12, None, None, 15]
    root = list_to_tree(arr)
    print("\n初始化二叉树\n")
    print("二叉树的数组表示：")
    print(arr)
    print("二叉树的链表表示：")
    print_tree(root)

    # 数组表示下的二叉树类
    abt = ArrayBinaryTree(arr)

    # 访问节点
    i = 1
    l, r, p = abt.left(i), abt.right(i), abt.parent(i)
    print(f"\n当前节点的索引为 {i} ，值为 {abt.val(i)}")
    print(f"其左子节点的索引为 {l} ，值为 {abt.val(l)}")
    print(f"其右子节点的索引为 {r} ，值为 {abt.val(r)}")
    print(f"其父节点的索引为 {p} ，值为 {abt.val(p)}")

    # 遍历树
    res = abt.level_order()
    print("\n层序遍历为：", res)
    res = abt.pre_order(0)
    print("前序遍历为：", res)
    res = abt.in_order(0)
    print("中序遍历为：", res)
    res = abt.post_order(0)
    print("后序遍历为：", res)
