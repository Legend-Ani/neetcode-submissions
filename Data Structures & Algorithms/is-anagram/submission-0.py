class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Check the count of every unique character in s
        for char in set(s):
            if s.count(char) != t.count(char):
                return False

        return True