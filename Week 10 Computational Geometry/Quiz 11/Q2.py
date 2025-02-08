# We need this to create our tree nodes.
from collections import namedtuple
Node = namedtuple("Node", ["value", "left", "right"])

def binary_search_tree(nums, start=None, end=None):
    """
    This function turns a list of numbers (nums) into a balanced binary search tree.
    Instead of slicing the list, it uses 'start' and 'end' to know which part of the list to work with.
    """
    
    # If 'start' or 'end' is not provided, we sort the list and set 'start' and 'end' to cover the whole list.
    if start is None or end is None:
        nums = sorted(nums)
        start, end = 0, len(nums)

    # Calculate the number of elements in the current part of the list.
    n = end - start

    # If there's only one element, make a leaf node.
    if n == 1:
        tree = Node(nums[start], None, None)  # A leaf
    else:
        # Find the middle index of the current part of the list.
        mid = start + n // 2  # Halfway (approx)
        
        # Make a binary search tree from the left half and the right half of the current part of the list.
        left = binary_search_tree(nums, start, mid)
        right = binary_search_tree(nums, mid, end)

        # Create a new node with the middle value and the left and right trees we just made.
        tree = Node(nums[mid - 1], left, right)
        
    return tree  # Return the tree we've made.

def print_tree(tree, level=0):
    """
    This function prints a tree in a nicely indented way.
    """
    
    # If the node is a leaf (has no children), print "Leaf" and its value.
    if tree.left is None and tree.right is None: 
        print(2 * level * ' ' + f"Leaf({tree.value})")
    else:
        # Otherwise, print "Node" and its value, and print its left and right children (subtrees).
        print(2 * level * ' ' + f"Node({tree.value})")
        print_tree(tree.left, level + 1)
        print_tree(tree.right, level + 1)



nums = [22, 41, 19, 27, 12, 35, 14, 20,  39, 10, 25, 44, 32, 21, 18]
tree = binary_search_tree(nums)
print_tree(tree)

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