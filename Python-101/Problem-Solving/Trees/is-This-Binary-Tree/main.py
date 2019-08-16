""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def checkBST(node,lv=None,rv=None):
	"""
	this will keep 2 values to compare each node to: 
	a minimum on the left branch and a maximum on the right branch. 
	if we go on the left branch we update the lv to the new minimum. 
	if we go to the right we update the rv to the new maximum.

	"""
    if not node:
        return True
    if lv and node.data >= lv: 
        return False
    if rv and node.data <= rv:
        return False
    return checkBST(node.left,node.data,rv) and checkBST(node.right,lv,node.data)