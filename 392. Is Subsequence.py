# Approach
# iterate through both the strings
# if char at both the index match, increment both indices
# else increment index at t to look for a potential match
# at the end, check whether we could match all characters in s
# Time complexity : O(len(s) + len(t))
# Space complexity : O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr1, ptr2 = 0,0
        while ptr1 < len(s) and ptr2 < len(t):
            if s[ptr1] == t[ptr2]:
                ptr1 += 1
                ptr2 += 1
            else:
                ptr2 += 1
        return ptr1 == len(s)
        
