"""
各数据结构打印方法集合
"""
from modules.list_node import ListNode


def list_node_to_list(head):
    """将链表转化为数组"""
    arr: list[int] = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr


def print_linked_list(head: ListNode | None):
    # 将链表转换为列表
    arr:list[int] = list_node_to_list(head)
    # 打印
    print(" -> ".join(str(item) for item in arr))
