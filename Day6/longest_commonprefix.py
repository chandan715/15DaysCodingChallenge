class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        first_str = strs[0]
        for i in range(len(first_str)):
            char = first_str[i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return first_str[:i]
        return first_str

        