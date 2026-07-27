class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left < right:

            # If left is NOT a letter/number,
            # skip it
            if not s[left].isalnum():
                left += 1
                continue

            # If right is NOT a letter/number,
            # skip it
            if not s[right].isalnum():
                right -= 1
                continue

            # Now both are letters/numbers.
            # Convert to lowercase before comparing.
            if s[left].lower() != s[right].lower():
                return False

            # Characters matched → move inward
            left += 1
            right -= 1

        # No mismatch found
        return True