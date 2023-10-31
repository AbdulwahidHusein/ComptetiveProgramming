class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        curr_dict = {}
        max_so_far = 1
        left = 0

        for right in range(len(s)):
            if s[right] in curr_dict:
                left = max(left, curr_dict[s[right]] + 1)

            curr_dict[s[right]] = right
            max_so_far = max(max_so_far, right - left + 1)

        return max_so_far