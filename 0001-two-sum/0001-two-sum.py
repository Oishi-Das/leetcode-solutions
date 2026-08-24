class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(len(nums)) :
            curr = nums [i]
            need = target - curr 
            if need in seen :
                return [seen[need] , i ]
            seen[curr] = i 