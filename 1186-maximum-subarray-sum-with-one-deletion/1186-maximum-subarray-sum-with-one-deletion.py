class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        no_delete = arr[0]
        one_delete = float("-inf")
        max_sum = arr[0]

        for i in range(1, len(arr)):
            one_delete = max(one_delete + arr[i], no_delete)
            no_delete = max(no_delete + arr[i], arr[i])

            max_sum = max(max_sum, no_delete, one_delete)

        return max_sum