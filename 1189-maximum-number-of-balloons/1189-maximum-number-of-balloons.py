class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {}

        for ch in text:
            count[ch] = count.get(ch, 0) + 1

        # We need these characters to make "balloon"
        # b = 1, a = 1, l = 2, o = 2, n = 1

        # Start with a very large number
        # and keep finding the smallest possible number
        ans = float('inf')

        # Check each character needed for "balloon"
        for ch in "balon":

            # Number of times we can use this character
            # For l and o, we need 2 of each
            if ch == 'l' or ch == 'o':
                possible = count.get(ch, 0) // 2
            else:
                possible = count.get(ch, 0)

            # The character available the least
            # determines how many "balloon"s we can make
            ans = min(ans, possible)

        return ans