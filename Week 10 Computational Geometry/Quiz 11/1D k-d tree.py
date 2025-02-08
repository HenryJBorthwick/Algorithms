# Do not alter the next two lines
from collections import namedtuple
Node = namedtuple("Node", ["value", "left", "right"])

# Rewrite the following function to avoid slicing
def binary_search_tree(nums, is_sorted=False):
    """Return a balanced binary search tree with the given nums
       at the leaves. is_sorted is True if nums is already sorted.
       Inefficient because of slicing but more readable.
    """
    if not is_sorted:
        nums = sorted(nums)
    n = len(nums)
    if n == 1:
        tree = Node(nums[0], None, None)  # A leaf
    else:
        mid = n // 2  # Halfway (approx)
        left = binary_search_tree(nums[:mid], True)
        right = binary_search_tree(nums[mid:], True)
        tree = Node(nums[mid - 1], left, right)
    return tree
    
# Leave the following function unchanged
def print_tree(tree, level=0):
    """Print the tree with indentation"""
    if tree.left is None and tree.right is None: # Leaf?
        print(2 * level * ' ' + f"Leaf({tree.value})")
    else:
        print(2 * level * ' ' + f"Node({tree.value})")
        print_tree(tree.left, level + 1)
        print_tree(tree.right, level + 1)


# nums = [22, 41, 19, 27, 12, 35, 14, 20,  39, 10, 25, 44, 32, 21, 18]
# tree = binary_search_tree(nums)
# print_tree(tree)

# Node(21)
#   Node(14)
#     Node(10)
#       Leaf(10)
#       Node(12)
#         Leaf(12)
#         Leaf(14)
#     Node(19)
#       Node(18)
#         Leaf(18)
#         Leaf(19)
#       Node(20)
#         Leaf(20)
#         Leaf(21)
#   Node(32)
#     Node(25)
#       Node(22)
#         Leaf(22)
#         Leaf(25)
#       Node(27)
#         Leaf(27)
#         Leaf(32)
#     Node(39)
#       Node(35)
#         Leaf(35)
#         Leaf(39)
#       Node(41)
#         Leaf(41)
#         Leaf(44)

# nums = [228]
# tree = binary_search_tree(nums)
# print_tree(tree)

# Leaf(228)

# nums = [228, 227, 3]
# tree = binary_search_tree(nums)
# print_tree(tree)

# Node(3)
#   Leaf(3)
#   Node(227)
#     Leaf(227)
#     Leaf(228)