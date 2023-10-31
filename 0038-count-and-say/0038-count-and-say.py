class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        if n == 1:
            return "1"

        # Generate subsequent terms
        prev_term = "1"
        for _ in range(2, n + 1):
            next_term = ""
            count = 1
            for i in range(1, len(prev_term)):
                if prev_term[i] == prev_term[i - 1]:
                    count += 1
                else:
                    next_term += str(count) + prev_term[i - 1]
                    count = 1
            next_term += str(count) + prev_term[-1]
            prev_term = next_term

        return prev_term