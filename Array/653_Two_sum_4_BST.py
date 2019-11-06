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
    def findTarget(self, root, k):
        big = root
        small = root
        while(small!=None and big!=None):
            if((big.val+small.val)==k):
                return True
            elif((big.val+small.val)>k):
                small
