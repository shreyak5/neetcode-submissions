class Solution:
    def operation(self, n1: int, n2: int, op) -> int:
        if op == '+':
            return n1 + n2
        if op == '-':
            return n1 - n2
        if op == '*':
            return n1 * n2
        if op == '/':
            ans = n1 / n2
            div = n1 // n2
            return div if ans >= 0 else div + (div != ans)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']
        print(int(3.4), int(-2.3))
        for t in tokens:
            if t in ops:
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(self.operation(n1, n2, t))
            else:
                stack.append(int(t))
            
        return stack[0]
        