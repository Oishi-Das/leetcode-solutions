class Solution:
    def longestCommonPrefix(self, strs):

        strs.sort()                 # Sort the strings alphabetically

        first = strs[0]             # Take the first string
        last = strs[-1]             # Take the last string

        i = 0                       # Start from the first character

        while i < len(first) and i < len(last):

            if first[i] != last[i]: # Check if characters are different
                break               # If different, stop

            i += 1                  # Move to the next character

        return first[:i]            # Return the common part