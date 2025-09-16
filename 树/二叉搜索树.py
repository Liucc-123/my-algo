"""
File: 二叉搜索树.py
Created Time: 2025-09-16
Author: falcon (liuc47810@gmail.com)
"""

"""
二叉搜索树的常用操作：
1、查找节点
2、插入节点
3、删除节点
"""
from modules import TreeNode, print_tree


class BinarySearchTree:
    def __init__(self):
        """构造方法"""
        # 初始化空树
        self._root: TreeNode | None = None

    def get_root(self):
        """获取根节点"""
        return self._root

    def search(self, target: int):
        """查找目标节点"""
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

    def insert(self, num: int):
        """
        插入指定节点
        实现思路：
        先遍历二叉树，找到插入位置 cur
        需要定义新指针 pre 来存储上一轮遍历节点的位置。根据 num 和 pre 节点值的比较，来决定新节点是存放在 pre 的左子节点还是右子节点
        """
        # 如果是一棵空树，初始化之
        if self._root is None:
            self._root = TreeNode(num)
            return
        cur, pre = self._root, None
        insert_node = TreeNode(num)
        # 查找插入位置
        while cur is not None:
            pre = cur
            # 往左子树
            if num < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        # 插入新节点
        if num < pre.val:
            pre.left = insert_node
        else:
            pre.right = insert_node

    def remove(self, target: int):
        """
        删除指定节点
        实现思路：
        二叉搜索树删除指定节点，分三类情况：
        1、删除节点度为 0，可直接删除
        2、删除节点度为 1，将其子节点替换删除节点
        3、删除节点度为 2，这种情况相对麻烦。因为删除节点后仍然需要保持二叉搜索树的特性，需要找到其右子树的最小节点或者左子树的最大节点来替换删除节点，再将这个最大（或最小）节点给删除掉。
        以右子树最小节点为例，我们可以通过中序遍历，找到下一个节点就是要替换的节点。
        """
        # 根节点为空，直接返回
        if self._root is None:
            print("二叉树为空，无法删除")
            return
        cur, pre = self._root, self._root
        # 遍历查找待删除节点
        while cur is not None:
            if cur.val == target:
                # 找到目标节点
                break
            pre = cur
            if cur.val < target:
                cur = cur.right
            else:
                cur = cur.left

        # 未找到删除节点，返回
        if cur is None:
            return
        # 根据以下三种情况，删除指定节点
        # 情况一：度为 0
        # 实现思路：直接删除此节点即可
        # 情况二：度为 1
        # 实现思路：将删除节点的子节点来替换删除节点

        # 度为 0 或 1
        if cur.left is None or cur.right is None:
            if cur.val < pre.val:
                pre.left = cur.left if cur.left is not None else cur.right
            else:
                pre.right = cur.left if cur.left is not None else cur.right
        # 度为 2
        # step1：找到待删除节点 cur
        # step2：通过中序遍历，找到下一个节点 nex，也就是用来替换删除节点
        # step3：替换节点的值，cur.val = nex.val
        # step4： 直接删除节点 nex
        else:
            # 根据中序遍历找到下一个节点，也就是右子树中的最小节点
            tmp = cur.right
            while tmp.left is not None:
                tmp = tmp.left
            # 递归删除最小节点
            self.remove(tmp.val)
            cur.val = tmp.val


if __name__ == '__main__':
    # 初始化二叉搜索树
    bst = BinarySearchTree()
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