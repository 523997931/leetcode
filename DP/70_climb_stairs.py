'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
'''
class Solution:
    def climbStairs(self, n):#第一种采用普通的递归算法来进行,此方法没有通过，在n=38时直接超时
        if(n==1):
            return 1
        elif(n==2):
            return 2
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)

    def climbStairs_DP(self,n):#此处采用动态规划法进行,leetcode测试，时间28ms，内存13.4mb，提升很多，时间复杂度O（n）空间为O（n）
        dp = [1,2,3]
        if n<3:
            return dp[n-1]
        else:
            i = 3
            while(i<n):
                answer = dp[i-1]+dp[i-2]
                dp.append(answer)
                i+=1
            return dp[n-1]

    def climbStairs_dp_update(self, n):#此处可以进一步优化，因为不需要在之前的数据，所以可以直接用temp保存，空间复杂度为O（1）
        dp = [1, 2, 3]
        if n < 3:
            return dp[n - 1]
        else:
            i = 3
            temp1 = 2
            temp2 = 3
            answer = 0
            while (i < n):
                answer = temp1 + temp2
                temp1 = temp2
                temp2 = answer
                i += 1
            return temp2


