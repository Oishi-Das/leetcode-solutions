class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            direction = nums[i] > 0
            slow = i
            fast = i

            while True:
                if (nums[slow] > 0) != direction:
                    break

                next_slow = next_index(slow)

                if (nums[fast] > 0) != direction:
                    break

                next_fast = next_index(fast)

                if (nums[next_fast] > 0) != direction:
                    break

                next_fast = next_index(next_fast)

                slow = next_slow
                fast = next_fast

                if slow == fast:
                    if slow == next_index(slow):
                        break
                    return True

            current = i

            while (nums[current] > 0) == direction:
                next_node = next_index(current)

                if (next_node == current or (nums[next_node] > 0) != direction):
                    break

                nums[current] = 0
                current = next_node

        return False
        