from operator import index

from modules.list_node import ListNode
from modules.print_util import print_linked_list


def insert(n0: ListNode, p: ListNode):
    """向指定位置插入新节点p"""
    p.next = n0.next
    n0.next = p


def remove(n0: ListNode):
    """删除链表的节点n0之后的首个节点"""
    if not n0:
        return
    # 删除n0之后的首个节点
    # n0 -> P -> n1
    P = n0.next
    n1 = P.next
    n0.next = n1


def access(head: ListNode, index: int):
    """访问链表中索引为index的节点"""
    for _ in range(index):
        if not head:
            return None
        head = head.next
    return head


def find(head: ListNode, target: int) -> int:
    """遍历链表，查找值为target的节点对应的索引"""
    index = 0
    while head:
        if head.val == target:
            return index
        index += 1
        head = head.next
    return -1


# 测试代码
if __name__ == '__main__':
    # 初始化链表 1->3->2->5->4
    # 1、初始化各个链表节点
    n0 = ListNode(1)
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(5)
    n4 = ListNode(4)
    # 2、构建各个节点之间的引用关系
    n0.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = None
    print("初始化的链表为")
    print_linked_list(n0)

    # 插入节点：在节点2后面插入新节点node(8)
    p = ListNode(8)
    insert(n2, p)
    print("插入新节点8后的链表结构：")
    print_linked_list(n0)

    # 删除节点：删除节点2
    remove(n1)
    print("删除节点2后的链表结构：")
    print_linked_list(n0)

    # 访问节点
    node = access(n0, 2)
    print(f"索引为2处的节点的值 = {node.val}")

    # 查找节点
    target = 8
    print(f"值为8的节点对应的索引是 = {find(n0, target)}")