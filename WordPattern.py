class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        # print(s_list)
        pattern_dict = {}
        s_dict = {}
        for i in range(len(pattern)):
            try:
                pattern_dict[pattern[i]].append(i)
            except KeyError:
                pattern_dict[pattern[i]] = [i]
        # print(pattern_dict)

        for i in range(len(s_list)):
            try:
                s_dict[s_list[i]].append(i)
            except KeyError:
                s_dict[s_list[i]] = [i]
        # print(s_dict)

        if not len(pattern_dict) == len(s_dict):
            return False

        p_list = [pattern_dict[key] for key in pattern_dict]
        s_list = [s_dict[key] for key in s_dict]
        # print(p_list)
        # print(s_list)
        if p_list == s_list:
            return True
        else:
            return False




sol = Solution()
print(sol.wordPattern("abba", "dog cat cat dog"))

