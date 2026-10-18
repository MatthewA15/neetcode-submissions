class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #nums - integers
        #target - specific integer
        #indicies i and j = integers[i] + integers[j] == target and i!=j(no repeat numbers)
        # goal is target, in order to get target we need indicies, in order to get indicies, we need integers that add to target, in order to get integers we need to go through array. 
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return




        