class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for letter in s:
            try:
                s_dict[letter] += 1
            except KeyError:
                s_dict[letter] = 1

        for letter in t:
            try:
                t_dict[letter] += 1
            except KeyError:
                t_dict[letter] = 1

        if (len(s_dict) != len(t_dict)) or (s_dict != t_dict):
            return False
        else:
            return True



sol = Solution()
print(sol.isAnagram(s = "rat", t = "car"))




