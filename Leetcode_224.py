def calculate(s: str) -> int:
    if len(s) == 1:
        if s != " ": return int(s)
        else: return 0

    stack = []
    sign = 1
    sum = 0
    num = 0
    for ch in s:
        # number
        if "0" <= ch <= "9":
            num = num * 10 + int(ch)

        # +
        elif ch == "+":
            sum += num * sign
            num = 0
            sign = 1

        # -
        elif ch == "-":
            sum += num * sign
            num = 0
            sign = -1

        # (
        elif ch == "(":
            stack.append(sum)
            stack.append(sign)
            sum = 0
            sign = 1

        # )
        elif ch == ")":
            sum += sign * num
            sum *= stack.pop()
            sum += stack.pop()
            num = 0

    return sum + sign * num

print(calculate("1 + 1"))



