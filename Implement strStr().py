class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        i = 0
        while i < len(haystack):
            print(haystack[i:n+i])
            if haystack[i:n+i] == needle:
                return i
            i += 1
        return -1
