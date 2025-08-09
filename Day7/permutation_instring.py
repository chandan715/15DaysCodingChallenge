class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = len(s1)
        t = len(s2)
        if s > t:
            return False
        count1 = [0] * 26
        count2 = [0] * 26
        for ch in s1:
            count1[ord(ch) - ord('a')] += 1
        for ch in s2[:s]:
            count2[ord(ch) - ord('a')] += 1
        if count1 == count2:
            return True
        for i in range(s, t):
            count2[ord(s2[i]) - ord('a')] += 1           
            count2[ord(s2[i - s]) - ord('a')] -= 1   
            if count1 == count2:
                return True

        return False