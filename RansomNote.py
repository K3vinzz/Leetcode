class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = {}
        ransom_letter = []
        magazine_dict = {}
        for letter in magazine:
            try:
                magazine_dict[letter] += 1
            except KeyError:
                magazine_dict[letter] = 1

        for letter in ransomNote:
            try:
                ransom_dict[letter] += 1
            except KeyError:
                ransom_dict[letter] = 1
                ransom_letter.append(letter)
        print(f"ran_dict = {ransom_dict}")
        print(f"mag_dict = {magazine_dict}")
        print(f"ran_letter = {ransom_letter}")
        for letter in ransom_letter:
            try:
                if ransom_dict[letter] > magazine_dict[letter]:
                    return False
            except KeyError:
                return False
        return True





solution = Solution()
print(solution.canConstruct(ransomNote="abqcddd", magazine="aabdddqqqqxcq"))


