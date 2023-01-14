# Erika Jane T. Reyes
# Testing the finished BinarySearchTreeNode class with my full name as the content of the binary tree

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def pre_order_traversal(self):
        elements = [self.data]

        if self.left:
            elements += self.left.pre_order_traversal()
        
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.post_order_traversal()
        
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)
        
        return elements

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)

        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self

def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    strings = ["E", "R", "I", "K", "A", "J", "A", "N", "E", "T", "R", "E", "Y", "E", "S"]
    strings_tree = build_tree(strings)
    print('\n')

    # Testing the search() method
    print("Letter E is in the list?", strings_tree.search("E"))
    print("Letter K is in the list?", strings_tree.search("K"))
    print("Letter Q is in the list?", strings_tree.search("Q"))
    print('\n')

    # Testing the find_min() method
    print("Mininum element:", strings_tree.find_min())
    print('\n')

    # Testing the find_max() method
    print("Maximum element:", strings_tree.find_max())
    print('\n')

    # Testing the in_order_traversal() method
    print("In order traversal:", strings_tree.in_order_traversal())
    print('\n')

    # Testing the pre_order_traversal() method
    print("Pre order traversal:", strings_tree.pre_order_traversal())
    print('\n')

    # Testing the post_order_traversal() method
    print("Post order traversal:", strings_tree.post_order_traversal())
    print('\n')

    # Testing the delete() method
    strings_tree = build_tree(strings)
    strings_tree.delete("E")
    print("After deleting letter E:", strings_tree.in_order_traversal())

    print("\n")

    strings_tree = build_tree(strings)
    strings_tree.delete("J")
    print("After deleting letter J:", strings_tree.in_order_traversal())

    print("\n")

    strings_tree = build_tree(strings)
    strings_tree.delete("Y")
    print("After deleting letter Y:", strings_tree.in_order_traversal())
