import itertools
import logging
import random
import re
from collections import deque
from dataclasses import dataclass
from typing import Optional


logger = logging.getLogger("tree_walk")


@dataclass
class BinaryTreeNode:
    val: int
    left: Optional["BinaryTreeNode"] = None
    right: Optional["BinaryTreeNode"] = None

    def __repr__(self):
        return f"<BinaryTreeNode[{self.val}]>"


def walk(root: BinaryTreeNode):
    queue = deque([root])

    while queue:
        node = queue.popleft()

        logger.info(f"Visiting {node!r}")

        if node.left:
            logger.debug(
                f"{node!r} left is not empty. Adding {node.left!r} to the queue"
            )
            queue.append(node.left)

        if node.right:
            logger.debug(
                f"{node!r} right is not empty. Adding {node.right!r} to the queue"
            )
            queue.append(node.right)


counter = itertools.count(random.randint(1, 10 ** 6))


def get_tree(max_depth: int, level: int = 1) -> Optional[BinaryTreeNode]:
    if max_depth == 0:
        return None

    node_left = get_tree(max_depth - 1, level=level + 1)
    node_right = get_tree(max_depth - 1, level=level + 1)
    node = BinaryTreeNode(val=next(counter), left=node_left, right=node_right)

    return node


def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    pattern = '[-+]?\d+'
    with open(path_to_log_file, 'r') as log_file:
        binary_tree = dict()
        for i_step in log_file:
            if i_step.startswith('INFO:Visiting'):
                node = int(re.findall(pattern, i_step)[0])
                binary_tree[node] = {}

            elif i_step.startswith('DEBUG') and 'left is not empty' in i_step:
                up_node = int(re.findall(pattern, i_step)[0])
                left_node = int(re.findall(pattern, i_step)[1])
                binary_tree[left_node] = dict()
                binary_tree[up_node]['left_node'] = left_node

            else:
                up_node = int(re.findall(pattern, i_step)[0])
                right_node = int(re.findall(pattern, i_step)[1])
                binary_tree[up_node]['right_node'] = right_node

    return print(binary_tree)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s:%(message)s",
        filename="walk_log_4.txt",
    )

    root = get_tree(7)
    walk(root)
    restore_tree('walk_log_4.txt')
