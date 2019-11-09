'''
题目：给你一根长度为n的绳子，请把绳子剪成m段 (m和n都是整数，n>1并且m>1)每段绳子的长度记为k[0],k[1],...,k[m].请问k[0]*k[1]*...*k[m-1]可能的最大乘积是多少？
例如，当绳子的长度为8时，我们把它剪成长度分别为2,3,3的三段，此时得到的最大乘积是18.
'''
class Solution:
    def cutRope(self, number):#此处采用动态规划的方式，dp记录每一个n的最大乘积，对每一个数，则寻求出其最大成绩值，依次递减，牛客网AC时间40ms，空间5000k，O（n^2)时间复杂度
        if(number==2):
            return 1
        elif(number==3):
            return 2
        else:
            dp = [0,1,2,3]
            i=4
            while(i<=number):
                j=1
                temp=1
                while(j<i):
                    temp=max(temp,j*dp[i-j])
                    j+=1
                dp.append(temp)
                i+=1
            return dp[number]

if __name__=='__main__':
    c = Solution()
    number = 8
    x = c.cutRope(number)
    print(x)
