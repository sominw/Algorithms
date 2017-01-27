class TreeNode(object):
	def __init__(self, key, value, left = None, right = None, parent = None):
		self.key = key
		self.value = value
		self.leftChild = left
		self.rightChild = right
		self.parent = parent

	def hasLeftChild(self):
		return self.leftChild

	def hasRightChild(self):
		return self.rightChild

	def isLeftChild(self):
		return self.parent and self.parent.leftChild == self

	def isRightChild(self):
		return self.parent and self.parent.rightChild == self
	
	def isRoot(self):
		return not self.parent

	def isLeaf(self):
		return not (self.leftChild or self.rightChild)

	def hasBothChildren(self):
		return (self.leftChild and self.rightChild)

	def replaceNodeData(self, key, value, leftChild, rightChild):
		self.key = key
		self.value = value
		self.leftChild = leftChild
		self.rightChild = rightChild
		if self.hasLeftChild():
			self.leftChild.parent = self
		if self.hasRightChild() == self:
			self.rightChild.parent = self
		


class BST(object):
	def __init__(self):
		self.root = None
		self.size = 0


	def length(self):
		return self.size

