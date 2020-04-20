#class to create nodes of a tree
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
#height function to calculate height of left subtree and right subtree
def height(node):
    if node is None:
        return 0
    #it returns left height and right height and one root node
    return 1+max(height(node.left),height(node.right))
#function to calculate diameter of a binary tree
def diameter(node):
    if node is None:
        return 0
    lheight=height(node.left)
    rheight=height(node.right)
    #recursive call for left,right diameters
    ldiameter=diameter(node.left)
    rdiameter=diameter(node.right)
    return max(lheight+rheight+1,max(ldiameter,rdiameter))
#main function
if __name__=="__main__":
    root=Node(1)
    root.left=Node(2)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.left.right.left=Node(6)
    root.right=Node(3)
    print("diameter of given binary tree is",diameter(root))

