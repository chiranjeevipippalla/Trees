class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

    def search(root, key):
        if root is None or root.data == key:
            return root

        if root.data<key:
                return search(root.right, key)

        else:
            return search(root.left, key)

    def insert(root, node):
        if root is None:
            root = node
        else:
            if root.data<node.data:
                if root.right is None:
                    root.right = node
                else:
                    insert(root.right, node)

            else:
                if root.left is None:
                    root.left = node
                else:
                    insert(root.left, node)

    def findMin(self, root):
        if root is None:
            return -1

        while root.left is not None:
            root = root.left

        return root.data

    def findMax(self, root):
        if root is None:
            return -1

        while root.right is not None:
            root = root.right

        return root

    def findHeight(self, root):
        if root is None:
            return -1

        left_tree_height = findHeight(self, root.left)
        right_tree_height = findHeight(self, root.right)

        return max(left_tree_height, right_tree_height)+1

    def preorder(self, root):
        if root is None:
            return
        else:
            print(root.data)
            preorder(root.left)
            preorder(root.right)

    def inorder(self, root):
        if root is None:
            return
        else:
            inorder(root.left)
            print(root.data)
            inorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        else:
            postorder(root.left)
            postorder(root.right)
            print(root.data)

    def delete(self, root, data):
        
        if root is None:
            return root

        elif data<root.data:
            root.left = delete(root.left, data)

        elif data>root.data:
            root.right = delete(root.right, data)

        else:
            
            if root.left is None and root.right is None:
                del root
                root = None

            elif root.left is None:
                temp = root
                root = root.right
                del temp

            elif root.right is None:
                temp = root
                root = root.left
                del temp

            else:
                temp = findMin(root.right)
                root.data = temp.data
                root.right = delete(root.right, temp.data)

            return root


























                
