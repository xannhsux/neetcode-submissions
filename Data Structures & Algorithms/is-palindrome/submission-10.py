class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned_s = "".join(c for c in s if c.isalnum())
        print(cleaned_s)

        n = len(cleaned_s)

        l = 0
        j = n - 1
        while (l < j and l < n//2):
            if cleaned_s[l] != cleaned_s[j]:
                return False
            l += 1
            j -= 1
        return True