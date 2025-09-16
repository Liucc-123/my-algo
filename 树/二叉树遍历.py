"""
File: 二叉树遍历.py
Created Time: 2025-09-17
Author: falcon (liuc47810@gmail.com)
"""
from collections import deque

from modules import TreeNode, list_to_tree, print_tree


def level_order(root: TreeNode | None) -> list[int]:
    """层序遍历"""
    # 初始化队列，加入根节点
    queue: deque[TreeNode] = deque()
    queue.append(root)
    # 初始化一个列表，用于保存遍历序列
    res = []
    while queue:
        node: TreeNode = queue.popleft()  # 队列出队
        res.append(node.val)  # 保存节点值
        if node.left is not None:
            queue.append(node.left)  # 左子节点入队
        if node.right is not None:
            queue.append(node.right)  # 右子节点入队
    return res

def pre_order(root: TreeNode | None):
    """前序遍历"""
    if root is None:
        return
    # 访问优先级：根节点 -> 左子树 -> 右子树
    res.append(root.val)
    pre_order(root=root.left)
    pre_order(root=root.right)


def in_order(root: TreeNode | None):
    """中序遍历"""
    if root is None:
        return
    # 访问优先级：左子树 -> 根节点 -> 右子树
    in_order(root=root.left)
    res.append(root.val)
    in_order(root=root.right)


def post_order(root: TreeNode | None):
    """后序遍历"""
    if root is None:
        return
    # 访问优先级：左子树 -> 右子树 -> 根节点
    post_order(root=root.left)
    post_order(root=root.right)
    res.append(root.val)


"""Driver Code"""
if __name__ == "__main__":
    # 初始化二叉树
    # 这里借助了一个从数组直接生成二叉树的函数
    root: TreeNode = list_to_tree(arr=[1, 2, 3, 4, 5, 6, 7])
    print("\n初始化二叉树\n")
    print_tree(root)

    # 层序遍历
    res: list[int] = level_order(root)
    print("\n层序遍历的节点打印序列 = ", res)

    # 前序遍历
    res = []
    pre_order(root)
    print("\n前序遍历的节点打印序列 = ", res)

    # 中序遍历
    res.clear()
    in_order(root)
    print("\n中序遍历的节点打印序列 = ", res)

    # 后序遍历
    res.clear()
    post_order(root)
    print("\n后序遍历的节点打印序列 = ", res)