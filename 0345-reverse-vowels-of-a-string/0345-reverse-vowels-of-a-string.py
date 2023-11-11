class Solution:
    def reverseVowels(self, s: str) -> str:
        str_arr = [ch for ch in s]
        vowels = ['a','e','i','o','u', "A","E","I","O","U"]
        left = 0
        right = len(s)-1
        while left < right:
            sleft, sright = s[left], s[right] 
            if not sleft in vowels or not sright in vowels:
                if not sleft in vowels:
                    left += 1
                if not sright in vowels:
                    right -= 1
            else:
                str_arr[left], str_arr[right] = str_arr[right], str_arr[left]
                left += 1
                right -= 1
        return "".join(str_arr)