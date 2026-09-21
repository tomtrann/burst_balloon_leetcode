class Solution(object):
    def check(self, nums):
        count = 1
        if len(nums) == 1: 
            return True
            
        for i in range(1, len(nums) * 2): 
            if (nums[(i - 1) % len(nums)] <= nums[i % len(nums)]):
                count  += 1
            else:
                count = 1
            if count == len(nums):
                return True
        return False
        