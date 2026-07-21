class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
  

        n = len(nums)

        # Answer array filled with 0s
        ans = [0] * n

        # Left pointer
        left = 0

        # Right pointer
        right = n - 1

        # Fill answer from the last index
        pos = n - 1

        # Continue until pointers cross
        while left <= right:

            # Square of left element
            left_square = nums[left] * nums[left]

            # Square of right element
            right_square = nums[right] * nums[right]

            # Put the larger square at the current last position
            if left_square > right_square:

                ans[pos] = left_square

                # Move left pointer
                left += 1

            else:

                ans[pos] = right_square

                # Move right pointer
                right -= 1

            # Move to the previous position in answer array
            pos -= 1

        return ans
       
          