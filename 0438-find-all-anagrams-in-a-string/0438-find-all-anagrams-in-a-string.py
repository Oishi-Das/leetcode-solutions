class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        count1 = {}
        count2 = {}
        result = []

        for char in p:
            if char in count1:
                count1[char] += 1
            else:
                count1[char] = 1

        left = 0

        for right in range(len(s)):
            char = s[right]

            if char in count2:
                count2[char] += 1
            else:
                count2[char] = 1

            if right - left + 1 > len(p):
                left_char = s[left]
                count2[left_char] -= 1

                if count2[left_char] == 0:
                    del count2[left_char]

                left += 1

            if count1 == count2:
                result.append(left)

        return result