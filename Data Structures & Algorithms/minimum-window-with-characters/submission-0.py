class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""

        count, window = {}, {}
        for c in t:
            count[c] = 1 + count.get(c, 0)
        
        have = 0
        need = len(count)
        res = [-1, -1]
        resLen = float("infinity")

        l = 0
        for r in range(len(s)):
            print(l)
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r]in count and count[s[r]] == window[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        if resLen != float("infinity"):
            return s[l: r + 1]
        else:
            return ""
