class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif c == "*":
                b, a = stack.pop(), stack.pop()
                stack.append(a * b)
            elif c == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(c))
        return stack.pop()

s = Solution()
print(s.evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))