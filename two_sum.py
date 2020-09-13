class Solution:
    def twoSum(self, nums, target):
        numsDic = {}  
        for i in range(len(nums)):
            # if remainder not in dictionary    
            if target-nums[i] not in numsDic:              
                # number/index
                numsDic[nums[i]] = i              
            else:             
                # if same number, returns first and current index
                return [numsDic[target-nums[i]], i]     

# Time complexity: O(n) to traverse the list containing n elements two times and hash table look up is O(1) time. 
# Space complexity: O(n) to store n elements

print (Solution().twoSum([3,4,3], 6))
