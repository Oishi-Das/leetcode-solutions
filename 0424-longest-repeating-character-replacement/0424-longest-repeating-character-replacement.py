class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        max_frequency = 0
        max_length = 0

        for right in range(len(s)):
            char = s[right]

            if char in count:
                count[char] += 1
            else:
                count[char] = 1

            max_frequency = max(max_frequency, count[char])

            while (right - left + 1) - max_frequency > k:
                left_char = s[left]
                count[left_char] -= 1
                left += 1

            length = right - left + 1

            if length > max_length:
                max_length = length

        return max_length