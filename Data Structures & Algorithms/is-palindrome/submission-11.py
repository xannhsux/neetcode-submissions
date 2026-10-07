class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        tuned_s = "".join(c for c in s if c.isalnum())

        l = 0
        r = len(tuned_s) - 1
        while l < r:
            if tuned_s[l] != tuned_s[r]:
                return False
            l += 1
            r -= 1
        return True
