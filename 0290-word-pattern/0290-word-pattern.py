class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        pairs = {}
        pairs2 = {}

        for i, p in enumerate(pattern):
            next_word = words[i]
            if p in pairs:
                if pairs[p] != next_word:
                    return False
            if next_word in pairs2:
                if pairs2[next_word] != p:
                    return False
            else:
                pairs[p] = next_word
                pairs2[next_word] = p
        
        return True