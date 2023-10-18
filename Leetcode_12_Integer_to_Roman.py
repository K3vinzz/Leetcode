class Solution:
    def intToRoman(self, num: int) -> str:
        thousand = int(num/1000)
        hundred = int((num % 1000)/100)
        ten = int((num % 100)/10)
        one = int(num % 10)
        result = ""
        # print(thousand, hundred, ten, one)
        if thousand != 0:
            for i in range(thousand):
                result += "M"

        if hundred != 0 and hundred < 5 and hundred != 4:
            for i in range(hundred):
                result += "C"
        elif hundred != 0 and hundred > 5 and hundred != 9:
            result += "D"
            for i in range(hundred - 5):
                result += "C"
        elif hundred == 4:
            result += "CD"
        elif hundred == 5:
            result += "D"
        elif hundred == 9:
            result += "CM"

        if ten != 0 and ten < 5 and ten != 4:
            for i in range(ten):
                result += "X"
        elif ten != 0 and ten > 5 and ten != 9:
            result += "L"
            for i in range(ten - 5):
                result += "X"
        elif ten == 4:
            result += "XL"
        elif ten == 5:
            result += "L"
        elif ten == 9:
            result += "XC"

        if one != 0 and one < 5 and one != 4:
            for i in range(one):
                result += "I"
        elif one != 0 and one > 5 and one != 9:
            result += "V"
            for i in range(one - 5):
                result += "I"
        elif one == 4:
            result += "IV"
        elif one == 5:
            result += "V"
        elif one == 9:
            result += "IX"

        return result





s = Solution()
print(s.intToRoman(6))

