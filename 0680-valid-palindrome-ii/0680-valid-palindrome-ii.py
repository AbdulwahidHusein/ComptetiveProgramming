class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s: str, left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # Try deleting the character on the left side
                if is_palindrome(s, left + 1, right):
                    return True
                # Try deleting the character on the right side
                if is_palindrome(s, left, right - 1):
                    return True
                # If neither deletion makes it a palindrome, return False
                return False

            left += 1
            right -= 1

        return True