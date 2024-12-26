class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        duplicate_x = x
        reverse_number = 0
        while duplicate_x != 0:
            last_digit = duplicate_x % 10
            reverse_number = reverse_number * 10 + last_digit
            duplicate_x = duplicate_x // 10
        return reverse_number == x