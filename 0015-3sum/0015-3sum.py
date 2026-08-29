class Solution:
    def threeSum(self, nums):

        # First, sort the array
        nums.sort()

        # This will store all valid triplets
        result = []

        # i chooses the first number
        for i in range(len(nums)):

            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two pointers for finding the other two numbers
            left = i + 1
            right = len(nums) - 1

            # Keep searching while the pointers haven't crossed
            while left < right:

                # Calculate the sum of the three numbers
                total = nums[i] + nums[left] + nums[right]

                # Sum is too small
                if total < 0:
                    left += 1

                # Sum is too large
                elif total > 0:
                    right -= 1

                # We found a triplet
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # Move both pointers
                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result