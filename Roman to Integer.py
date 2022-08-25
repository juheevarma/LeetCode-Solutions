class Solution:
    def romanToInt(self, s: str) -> int:
        romanvalue = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        final_num = 0

        while i < len(s):
            if i + 1 < len(s):
                if romanvalue[s[i]] >= romanvalue[s[i + 1]]:
                    final_num += romanvalue[s[i]]
                else:
                    final_num -= romanvalue[s[i]]
            else:
                final_num += romanvalue[s[i]]
            i += 1

        return final_num
