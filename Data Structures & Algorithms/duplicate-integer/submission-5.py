class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        prevMap = {}

        for i, n in enumerate(nums):
            duplicate = n
            if duplicate in prevMap:
                return True
            prevMap[n] = i
        return False