class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left = 0
        count = {}
        max_length = 0

        for right in range(len(fruits)):
            fruit = fruits[right]

            if fruit in count:
                count[fruit] += 1
            else:
                count[fruit] = 1

            while len(count) > 2:
                left_fruit = fruits[left]
                count[left_fruit] -= 1

                if count[left_fruit] == 0:
                    del count[left_fruit]

                left += 1

            length = right - left + 1

            if length > max_length:
                max_length = length

        return max_length