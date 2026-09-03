class Solution:
    def maximumSubarraySum(self, nums, k):

        answer = 0
        current_sum = 0
        seen = set()

        left = 0

        for right in range(len(nums)):

           
            while nums[right] in seen:
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            
            seen.add(nums[right])
            current_sum += nums[right]

           
            if right - left + 1 > k:
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            
            if right - left + 1 == k:
                answer = max(answer, current_sum)

        return answer