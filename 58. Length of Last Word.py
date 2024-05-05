# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastIndex = len(s) - 1
        while lastIndex >=0 and s[lastIndex] == " ":
            lastIndex -= 1
        firstIndex = lastIndex
        while firstIndex >=0 and s[firstIndex] != " ":
            firstIndex -= 1
        return lastIndex - firstIndex
        
