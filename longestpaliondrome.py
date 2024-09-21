def longestPalindrome(s: str) -> str:
    res = ""
    for i in range(len(s)):
        for a, b in [(i, i), (i, i + 1)]:
            while a >= 0 and b < len(s) and s[a] == s[b]:
                a -= 1
                b += 1
            if len(s[a+1:b]) > len(res):
                res = s[a+1:b]
    return res
print(longestPalindrome("babad"))  
print(longestPalindrome("cbbd"))  
