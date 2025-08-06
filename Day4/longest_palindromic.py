class Solution:
    def longestPalindrome(self, s: str) -> str:
        b=''
        for i in range(0,len(s)):
            for j in range(len(s),i,-1):
                if s[i:j]==s[i:j][::-1]:
                    if len(b)<len(s[i:j]):
                        b=s[i:j]
        return b
        