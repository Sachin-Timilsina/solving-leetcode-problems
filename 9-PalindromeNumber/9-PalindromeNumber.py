class Solution:
    def isPalindrome(self, x: int) -> bool:
        xx = str(x)
        return xx == xx[::-1]