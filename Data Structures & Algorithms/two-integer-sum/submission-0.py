class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map ={}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_map:
                return [nums_map[complement] , i]
            nums_map[nums[i]] = i    
        