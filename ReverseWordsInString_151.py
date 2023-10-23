class Solution:
    def reverseWords(self, s: str) -> str:
        split_list = s.split()
        result = ""
        for i in range(len(split_list) - 1, -1, -1):
            result += f"{split_list[i]} "
        result = result.rstrip()
        return result

s = Solution()
print(s.reverseWords("   Hello  "))

