class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        char_array = [ch for ch in s]
        left = 0
        right = len(s)-1

        while left < right:
            if not s[left].isalpha() or not s[right].isalpha():
                if not s[left].isalpha():
                    left += 1
                if not s[right].isalpha():
                    right -= 1
            else:
                char_array[right], char_array[left] = char_array[left],char_array[right]
                left += 1
                right -= 1
        return "".join(char_array)