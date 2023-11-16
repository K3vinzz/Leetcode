def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 1: return 1
    l = 0
    res = 0
    window = set()
    for r in range(len(s)):
        if s[r] not in window:
            window.add(s[r])
        else:
            res = max(res, r - l)
            while s[l] != s[r]:
                window.remove(s[l])
                l += 1
            l += 1
    res = max(res, len(s) - l)
    return res








