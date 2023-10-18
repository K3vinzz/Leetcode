class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}
        s_letter_order = []
        t_letter_order = []
        i = 0
        for letter in s:
            try:
                # s_dict[letter]['count'] += 1
                s_dict[letter]['pos'].append(i)
            except KeyError:
                dict_in_letter = {'pos': [i]}
                s_dict[letter] = dict_in_letter
                s_letter_order.append(letter)
            i += 1

        i = 0
        for letter in t:
            try:
                # t_dict[letter]['count'] += 1
                t_dict[letter]['pos'].append(i)
            except KeyError:
                dict_in_letter = {'pos': [i]}
                t_dict[letter] = dict_in_letter
                t_letter_order.append(letter)
            i += 1

        if len(s_letter_order) != len(t_letter_order):
            return False

        for i in range(len(s_letter_order)):
            if s_dict[s_letter_order[i]] != t_dict[t_letter_order[i]]:
                return False
        
        return True






s = Solution()
print(s.isIsomorphic(s="aaasd", t="asaad"))





