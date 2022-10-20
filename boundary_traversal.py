'''	      1
        /\
      2   3
      /\  /\
    4  5 6  7'''
	
class node:
	def __init__(self,val):
		self.left=None
		self.right=None
		self.data=val
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)

def left(root,ans):
	if not root.left or not root.right:
	   return 
	ans.append(root.data)
	if root.left:
		left(root.left,ans)
	else:
		left(root.right,ans)
	return ans
def right(root,ans):
	if not root.left or not root.right:
	   return 

	if root.right:
		right(root.right,ans)
	else:
		right(root.left,ans)
	ans.append(root.data)	
	return ans	
def leaf(root,ans):
    if not root:
        return
    if root.left==None and root.right==None:
        ans.append(root.data)
    leaf(root.left,ans)
    leaf(root.right,ans)
    return ans
def boundary(root):
	ans=[]
	x=left(root,[])
	y=leaf(root,[])
	z=right(root,[])
	return  x+y+z

print(boundary(root))	
