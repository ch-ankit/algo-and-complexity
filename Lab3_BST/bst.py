class BSTNode:
    def __init__(self,key,value):
        self.left=None
        self.right=None
        self.parent=None
        self.key=key
        self.value=value

class BinarySearchTree:
    def __init__(self):
        self._size=0
        self.root= None

    def add(self,key,value):
        newNode=BSTNode(key,value)
        if self._size==0:
            self.root=newNode
            self._size=self._size+1
        else:
            temp=self.root
            while temp!=None:
                y=temp
                if newNode.key<temp.key:
                    temp=temp.left
                else:
                    temp=temp.right
            newNode.parent=y
            if newNode.key<y.key:
                y.left=newNode
            else:
                y.right=newNode
            self._size=self._size+1


    def search(self,key):
        node=self.search_recursion(self.root,key)
        if node:
            return node.value
        else:
            return False

        
    def search_recursion(self,node: BSTNode,key):
        if node==None:
            return False
        if key<node.key:
            return self.search_recursion(node.left,key)
        elif key>node.key:
            return self.search_recursion(node.right,key)
        else:
            return node
            
    def smallest(self):
        smallestNode=self._smallest(self.root)
        return (smallestNode.key,smallestNode.value)
     
    def _smallest(self, node:BSTNode):
        temp=node
        while temp.left!=None:
            temp=temp.left
        return temp

    def largest(self):
        largestNode=self._largest(self.root)
        return (largestNode.key,largestNode.value)

    def _largest(self,node:BSTNode):
        temp=node
        while temp.right!=None:
            temp=temp.right
        return temp
        
    def preorder_walk(self):
        walk=[]
        self._preorder_walk(self.root,walk)
        return walk
    
    def _preorder_walk(self,node:BSTNode,walk:list):
        if node!=None:
            walk.append(node.key)
            self._preorder_walk(node.left,walk)
            self._preorder_walk(node.right,walk)
        return

    def postorder_walk(self):
        walk=[]
        self._postorder_walk(self.root,walk)
        return walk

    def _postorder_walk(self,node:BSTNode,walk:list):
        if node!=None:
            self._postorder_walk(node.left,walk)
            self._postorder_walk(node.right,walk)
            walk.append(node.key)
        return
    def inorder_walk(self):
        walk=[]
        self._inorder_walk(self.root,walk)
        return walk

    def _inorder_walk(self,node:BSTNode,walk:list):
        if node!=None:
            self._inorder_walk(node.left,walk)
            walk.append(node.key)
            self._inorder_walk(node.right,walk)
        return

    def remove(self,key):
        if self._size==0:
            return
        else:
            nodeToDelete=self.search_recursion(self.root,key)
            if nodeToDelete:
                #if node to delete has no child
                if nodeToDelete.left==None and nodeToDelete.right==None:
                    if nodeToDelete.key<nodeToDelete.parent.key:
                        nodeToDelete.parent.left=None
                        del nodeToDelete
                        self._size=self._size-1
                    else:
                        nodeToDelete.parent.right=None
                        del nodeToDelete
                        self._size=self._size-1
                #if node to delete has children
                else:
                    #making the left subtree's right most child as new root
                    nodeToReplaceDeletedNode=self._largest(nodeToDelete.left)
                    #if replacing node has no children
                    if nodeToReplaceDeletedNode.left==None and nodeToReplaceDeletedNode.right==None:
                        nodeToReplaceDeletedNode.parent.left=None
                        nodeToDelete.key=nodeToReplaceDeletedNode.key
                        nodeToDelete.value=nodeToReplaceDeletedNode.value
                        del nodeToReplaceDeletedNode
                        self._size=self._size-1
                    #replacing node has left children
                    else:
                        nodeToReplaceDeletedNode.parent.left=nodeToReplaceDeletedNode.left
                        nodeToDelete.key=nodeToReplaceDeletedNode.key
                        nodeToDelete.value=nodeToReplaceDeletedNode.value
                        del nodeToReplaceDeletedNode
                        self._size=self._size-1 
                        return
            else:
                return

    def size(self):
        return self._size

if __name__=='__main__':
    bst=BinarySearchTree()
    bst.add(10, "Value for 10")
    bst.add(52, "Value for 52")
    bst.add(5, "Value for 5")
    bst.add(8, "Value for 8")
    bst.add(1, "Value for 1")
    bst.add(40, "Value for 40")
    bst.add(30, "Value for 30")
    bst.add(45, "Value for 45")
    print(bst.search(5))
    print(bst.smallest())
    print(bst.largest())
    print(bst.preorder_walk())
    print(bst.postorder_walk())
    print(bst.inorder_walk())

    







    
