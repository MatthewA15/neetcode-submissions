class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #nums - integers
        #target - specific integer
        #indicies i and j = integers[i] + integers[j] == target and i!=j(no repeat numbers)
        # goal is target, in order to get target we need indicies, in order to get indicies, we need integers that add to target, in order to get integers we need to go through array. 
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    
                    return [i, j]



        