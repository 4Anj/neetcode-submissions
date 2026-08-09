class Solution:
    def isPalindrome(self, s: str) -> bool:
        b="".join(char.lower() for char in s if char.isalnum())
        return b==b[::-1]