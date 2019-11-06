'''
此为leetcode——1 的变体，升序的序列可以更方便的使用其性质
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
'''
class Solution:
    def twoSum(self, numbers, target):#前两种方法同上，该处使用第三种方式,指针对撞法，首先指定两指针在列表首尾，若和大于target，则尾指针前移，
        index1 = 0      #若小于target则首指针后移，因为递增，所以指针左移则为减少，右移则为增加，效果：时间140ms，内存14.1MB，此方式相比1的第二种方式，
        index2 = len(numbers)-1#好处在于，剩下了字典存储的空间，时间复杂度O（n）
        while(index1<index2):
            if((numbers[index1]+numbers[index2])==target):
                return [index1+1,index2+1]
            elif((numbers[index1]+numbers[index2])<target):
                index1+=1
            elif((numbers[index1]+numbers[index2])>target):
                index2-=1
        return 0

if __name__=='__main__':
    c = Solution()
    ar = [2,7,11,15]
    target=9
    x = c.twoSum(ar,target)
