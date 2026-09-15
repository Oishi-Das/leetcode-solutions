class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n

        def next_number(num):
            total = 0

            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10

            return total

        while True:
            slow = next_number(slow)
            fast = next_number(next_number(fast))

            if fast == 1:
                return True

            if slow == fast:
                return False
        