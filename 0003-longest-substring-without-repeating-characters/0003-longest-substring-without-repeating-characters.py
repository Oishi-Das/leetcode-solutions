class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        count = {}
        max_length = 0

        for right in range(len(s)):
            char = s[right]

            if char in count:
                count[char] += 1
            else:
                count[char] = 1

            while count[char] > 1:
                left_char = s[left]
                count[left_char] -= 1

                if count[left_char] == 0:
                    del count[left_char]

                left += 1

            length = right - left + 1

            if length > max_length:
                max_length = length

        return max_length