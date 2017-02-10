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

	def replaceNodeData(self, key, value, leftChild, rightChild): #Deletion of Root
		self.key = key
		self.value = value
		self.leftChild = leftChild
		self.rightChild = rightChild
		if self.hasLeftChild():
			self.leftChild.parent = self
		if self.hasRightChild():
			self.rightChild.parent = self


class BST(object):
	def __init__(self):
		self.root = None
		self.size = 0

	def length(self):
		return self.size

	def _put(self,key,value, curr):
		if key <= curr.key:
			if curr.hasLeftChild():
				self._put(key, value, curr.hasLeftChild())
			else:
				curr.leftChild = TreeNode(key,value, parent = curr)
		else:
			if curr.hasRightChild():
				self._put(key, value, curr.hasRightChild())
			else:
				curr.rightChild = TreeNode(key, value, parent = curr)

	def put(self, key, value):
		if self.root:
			self._put(key, value, self.root)
		else:
			self.root = TreeNode(key, value)
		self.size = self.size + 1

	def __setitem__(self,k,v):
		self.put(k,v)

	def _get(self,key,curr):
		if not curr:
			return None
		elif curr.key == key:
			return curr
		elif key < curr.key:
			return self._get(key,curr.hasLeftChild())
		else:
			return self._get(key,curr.hasRightChild())

	def get(self, key):
		if self.root:
			item = self._get(key, self.root)
			if item:
				return item.value
			else:
				return None
		else:
			return None

	def __getitem__(self,key):
		return self.get(key)

	def __contains__(self,key):
		if self._get(key, self.root):
			return True
		else:
			return False

	def remove(self,curr):
		if curr.isLeaf():
			if curr == curr.parent.hasLeftChild():
				curr.parent.leftChild = None
			else:
				curr.parent.rightChild = None
		elif curr.hasBothChildren():
			pass
		else: #Has Only One Child
			

	def delete(self,key):
		rem = _get(key,self.root)
		self.remove(rem)
	def __delitem__(self,key):
		self.delete(key)

if __name__ == '__main__':
	myTree = BST()
	myTree[2] = "Second Node"
	myTree[1] = "First Node"
	myTree[3] = "Third Node"
	print ("Insertion Order: 2 1 3")
	print (myTree[2])
	print (myTree[1])
	print (myTree[3])

