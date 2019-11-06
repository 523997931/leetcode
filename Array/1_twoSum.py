class Solution:
    def twoSum(self, nums,target):#暴力方式遍历，对每一个元素查找该元素之后列表，执行效果，778ms，14.8MB，时间复杂度O(n^2)
        h = 0
        while(h<len(nums)):
            try:
                g=nums.index(target-nums[h],h+1)
                return [h,g]
            except:
                h+=1

    def twoSum_map(self,nums,target):#使用字典当作hashmap，每走一步则记录出target与该元素的差值，当遍历过程中找到差值时，则返回位置
        dictory = {}
        answer = []
        for value in nums:
            if value in dictory.keys():#一定要先进行查询，查询是否存在，再进行储存，来避免相同元素的问题，如target为6，列表为【3】，若先储存，则返回【0，0】，或者【3，3】则会出错
                return [nums.index(dictory[value]),nums.index(value,nums.index(target-value)+1)]#第二个元素需要再第一个元素之后的位置进行查找，防止单一元素进行两边
            if value not in dictory.keys():
                dictory[target-value]=value    #该算法执行效果，100ms，15MB，复杂度为O（n）
        return 0


if __name__=='__main__':
    c = Solution()
    ar = [2,7,11,5]
    target = 9
    x = c.twoSum_map(ar,target)
    print(x)