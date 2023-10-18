# I, V, X, L, C, D and M
class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        i_to_pass = None
        for i in range(len(s)):
            if i == i_to_pass:
                pass
            else:
                if s[i] == "M":
                    result += 1000
                elif s[i] == "D":
                    result += 500
                elif s[i] == "C":
                    if i < len(s) - 1:
                        if s[i+1] == "D":
                            result += 400
                            i_to_pass = i + 1
                        elif s[i+1] == "M":
                            result += 900
                            i_to_pass = i + 1
                        else:
                            result += 100
                    else:
                        result += 100
                elif s[i] == "L":
                    result += 50
                elif s[i] == "X":
                    if i < len(s) - 1:
                        if s[i+1] == "L":
                            result += 40
                            i_to_pass = i + 1
                        elif s[i+1] == "C":
                            result += 90
                            i_to_pass = i + 1
                        else:
                            result += 10
                    else:
                        result += 10
                elif s[i] == "V":
                    result += 5
                elif s[i] == "I":
                    if i < len(s) - 1:
                        if s[i+1] == "V":
                            result += 4
                            i_to_pass = i + 1
                        elif s[i+1] == "X":
                            result += 9
                            i_to_pass = i + 1
                        else:
                            result += 1
                    else:
                        result += 1
        return result

sol = Solution()
print(sol.romanToInt("IX"))




