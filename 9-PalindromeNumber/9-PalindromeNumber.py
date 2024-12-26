class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_str = str(x)
        x_reverse = x_str[::-1]
        x_reverse = int(x_reverse)
        return x == x_reverse