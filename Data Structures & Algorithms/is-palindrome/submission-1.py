class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left < right:
            # skipping non alphanumeric from left
            while left < right and not s[left].isalnum():
                left += 1
            #skipping non alphanumeric from right
            while left < right and not s[right].isalnum():
                right -= 1
            #now compare the lowercase character
            if s[left].lower() != s[right].lower():
                return False
            #move inward
            left += 1
            right -= 1
        return True
        