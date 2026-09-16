class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []

        word_length = len(words[0])
        word_count = len(words)
        total_length = word_length * word_count

        if total_length > len(s):
            return []

        word_map = {}

        for word in words:
            if word in word_map:
                word_map[word] += 1
            else:
                word_map[word] = 1

        result = []

        for offset in range(word_length):
            left = offset
            right = offset
            count = 0
            current_map = {}

            while right + word_length <= len(s):
                word = s[right:right + word_length]
                right += word_length

                if word in word_map:
                    if word in current_map:
                        current_map[word] += 1
                    else:
                        current_map[word] = 1

                    count += 1

                    while current_map[word] > word_map[word]:
                        left_word = s[left:left + word_length]
                        current_map[left_word] -= 1
                        left += word_length
                        count -= 1

                    if count == word_count:
                        result.append(left)

                        left_word = s[left:left + word_length]
                        current_map[left_word] -= 1
                        left += word_length
                        count -= 1

                else:
                    current_map = {}
                    count = 0
                    left = right

        return result