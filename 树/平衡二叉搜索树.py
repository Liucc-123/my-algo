"""
File: 平衡二叉搜索树.py
Created Time: 2025-09-16
Author: falcon (liuc47810@gmail.com)
"""
from modules import TreeNode, print_tree


# 二叉搜索树经过多次插入或删除操作，可能会退化为链表，复杂度变为O(n).
# AVL树既是二叉搜索树，也是平衡二叉树，同时满足这两类树的特性，因此是一颗平衡二叉搜索树（balanced binary search tree）

class AVLTree:
    """平衡二叉搜索树"""

    def __init__(self):
        """构造方法"""
        self._root = None

    def get_root(self):
        """获取二叉树的根节点"""
        return self._root

    def height(self, node: TreeNode) -> int:
        """获取指定树节点的高度"""
        # 空节点的高度为 -1，叶节点的高度为 0
        if node is None:
            return -1
        return node.height

    def update_height(self, node: TreeNode):
        """更新指定节点的高度"""
        # 左子树和右子树的最大高度 + 1
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def balance_factor(self, node: TreeNode) -> int:
        """获取指定节点的平衡因子"""
        # 空节点的平衡因子为 0
        if node is None:
            return 0
        # 节点的平衡因子 = 左子树高度 - 右子树高度
        # 因此如果节点的平衡因子在[-1, 1]之间，则该节点平衡
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, node: TreeNode) -> TreeNode:
        """
        右旋操作
        :param node:失衡节点
        :return:平衡后子树的新根节点
        """
        child = node.left
        grand_child = child.right
        node.left = grand_child
        # 以 child 为原点向右旋转 node
        child.right = node
        # 更新 child 和 node 节点的高度
        self.update_height(node)
        self.update_height(child)
        return child

    def left_rotate(self, node: TreeNode) -> TreeNode:
        """
        左旋操作
        :param node:失衡节点
        :return:平衡后子树的新根节点
        """
        child = node.right
        grand_child = child.left
        node.right = grand_child
        # 以 child 为原点向左旋转 node
        child.left = node
        # 更新 child 和 node 节点的高度
        self.update_height(node)
        self.update_height(child)
        return child

    def rotate(self, node: TreeNode) -> TreeNode:
        """
        自动旋转失衡节点，使其转为平衡节点
        :param node: 失衡子树的节点
        :return: 平衡后新的根节点
        """
        # 左偏树
        if self.balance_factor(node) > 1:
            if self.balance_factor(node.left) >= 0:
                # 右旋
                return self.right_rotate(node)
            else:
                # 先左旋再右旋
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        # 右偏树
        elif self.balance_factor(node) < -1:
            if self.balance_factor(node.right) <= 0:
                # 左旋
                return self.left_rotate(node)
            else:
                # 先右旋再左旋
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
        else:
            # 已经是平衡节点，直接返回
            return node

    def insert(self, val: int):
        """
        插入节点
        :param val:新节点的值
        :return:
        """
        self._root = self.insert_helper(self._root, val)

    def insert_helper(self, node: TreeNode, val: int) -> TreeNode:
        """
        平衡二叉搜索树帮助器，在插入新节点时会从底部向根节点扫描每个节点，使其转为平衡节点
        :param node: 开始扫描的节点
        :param val: 插入新值
        :return:平衡操作后新的根节点
        """
        if node is None:
            return TreeNode(val)
        # 遍历查找适合插入的位置
        if node.val < val:
            node.right = self.insert_helper(node.right, val)
        elif node.val > val:
            node.left = self.insert_helper(node.left, val)
        else:
            # 节点重复，直接返回
            return node
        # 更新节点的高度
        self.update_height(node)
        # 执行旋转操作，使当前子树恢复平衡
        return self.rotate(node)

    def remove(self, val: int):
        """
        删除指定节点
        :param val: 删除节点的值
        :return:
        """
        self._root = self.remove_helper(self._root, val)

    def remove_helper(self, node: TreeNode, val: int) -> TreeNode | None:
        """
        二叉树删除操作帮助器，在删除指定节点后，从底部向根部扫描，使其恢复平衡状态
        :param node: 开始扫描的节点
        :param val: 删除的值
        :return: 删除后二叉树的根节点
        """
        # 未找到，直接返回
        if node is None:
            return None
        # 遍历找到要删除的节点
        if node.val < val:
            node.right = self.remove_helper(node.right, val)
        elif node.val > val:
            node.left = self.remove_helper(node.left, val)
        else:
            # 找到删除节点
            if node.left is None or node.right is None:
                child = node.left or node.right
                if child is None:
                    # 度为 0,直接返回None
                    return None
                else:
                    # 度为 1，替换 node，返回
                    node = child
            # 度为 2
            else:
                # 中序遍历，找到右子树中最小节点
                tmp = node.right
                while tmp.left:
                    tmp = tmp.left
                # 递归删除这个叶子节点
                self.remove(tmp.val)
                # 替换删除节点
                node.val = tmp.val
        # 更新节点的高度
        self.update_height(node)
        # 执行旋转操作，恢复节点的平衡状态
        return self.rotate(node)

    def search(self, target: int) -> TreeNode | None:
        """
        查找指定的节点
        :param target: 搜索节点的值
        :return: 搜索节点
        """
        # 从根节点找起
        cur = self._root
        while cur is not None:
            # 找到目标值
            if cur.val == target:
                return cur
            # 在左子树
            if target < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        return None


if __name__ == '__main__':
    # 初始化平衡二叉搜索树
    bst = AVLTree()
    nums = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    # 请注意，不同的插入顺序会生成不同的二叉树，该序列可以生成一个完美二叉树
    for num in nums:
        bst.insert(num)
    print("\n初始化的二叉树为\n")
    print_tree(bst.get_root())

    # 查找节点
    node = bst.search(7)
    print("\n查找到的节点对象为: {}，节点值 = {}".format(node, node.val))

    # 插入节点
    bst.insert(16)
    print("\n插入节点 16 后，二叉树为\n")
    print_tree(bst.get_root())

    bst.insert(17)
    print("\n插入节点 17 后，二叉树为\n")
    print_tree(bst.get_root())

    # 删除节点
    bst.remove(1)
    print("\n删除节点 1 后，二叉树为\n")
    print_tree(bst.get_root())

    bst.remove(2)
    print("\n删除节点 2 后，二叉树为\n")
    print_tree(bst.get_root())

    bst.remove(4)
    print("\n删除节点 4 后，二叉树为\n")
    print_tree(bst.get_root())

    print("删除节点 13，检查是否会自动恢复平衡二叉树？")
    bst.remove(13)
    print("\n删除节点 13 后，二叉树为\n")
    print_tree(bst.get_root())
