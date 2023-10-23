class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_string ="".join(filter(str.isalnum, s)).lower()
        if alnum_string == "":
            return True
        leng = len(alnum_string)
        front = alnum_string[:int(leng/2)]
        if not leng % 2 == 0:
            rear = alnum_string[:int(leng/2):-1]
        else:
            rear = alnum_string[:int(leng/2)-1:-1]
        if front == rear:
            return True
        else:
            return False



sol = Solution()
print(sol.isPalindrome("AAaa"))