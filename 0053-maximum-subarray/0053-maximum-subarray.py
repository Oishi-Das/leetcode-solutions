class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = nums[0]
        maxsum = nums[0]
        for i in range (1,len(nums),1):
            currsum = max(nums[i] , (nums[i] + currsum))
            maxsum = max(maxsum , currsum )
        return maxsum
        