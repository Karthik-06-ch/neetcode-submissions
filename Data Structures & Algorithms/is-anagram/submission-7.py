class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for ch in "abcdefghijklmnopqrstuvwxyz":
            count1 = 0
            count2 = 0

            for i in range(len(s)):
                if s[i] == ch:
                    count1 += 1
                if t[i] == ch:
                    count2 += 1

            if count1 != count2:
                return False

        return True