'''
给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

案例 1:

输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

输出: True
 

案例 2:

输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

输出: False
也是TwoSum系列的变体，这次采用的是二叉搜索树的形式，同样的，借助二叉搜索树的性质，我们可以借鉴167的做法进行
'''
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def findTarget(self, root, k):      #采用树的中序遍历，便利其中每一个数，并使用一个set进行记录,二叉搜索树不存在相同元素，因此遍历后便可得到结果，执行效果：时间104ms，空间16.4MB
        s = set()                       #时间O(n),空间O(n)
        global mark
        mark=0
        self.mid_scan(root,s,k)
        if(mark==1):
            return True
        else:
            return False
    def mid_scan(self,root,s,k):
        global mark
        if root==None:
            return
        else:
            self.mid_scan(root.left,s,k)
            if((k-root.val) in s):
                mark = 1
            s.add(root.val)
            self.mid_scan(root.right,s,k)
if __name__=='__main__':
    node = TreeNode(5)
    node2 = TreeNode(3)
    node3 = TreeNode(6)
    node4 = TreeNode(2)
    node5= TreeNode(4)
    node6 = TreeNode(7)
    node.left=node2
    node.right=node3
    node2.left=node4
    node2.right=node5
    node3.right=node6
    c=Solution()
    target = 28
    x = c.findTarget(node,target)
    print(x)

