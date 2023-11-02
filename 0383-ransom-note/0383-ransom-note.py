class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_counter = Counter(ransomNote)
        mag_counter = Counter(magazine)

        for w in note_counter:
            if not w in mag_counter:
                return False
            else:
                if mag_counter[w] < note_counter[w]:
                    return False
        return True
        