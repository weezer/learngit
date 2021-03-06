class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        queue = []
        for item in tokens:
            if item == "*" or item == "/" or item == "+" or item == "-":
                operand2 = queue.pop()
                operand1 = queue.pop()
                result = self.calc(item, operand1, operand2)
                queue.append(result)
            else:
                queue.append(int(item))

        return queue.pop()

    def calc(self, op, op1, op2):
        if op == "*":
            return op1 * op2
        elif op == "/":
            if op1 * op2 < 0:    # python是向下取整，即5/(-3)=-2
                return -((-op1) / op2)
            else:
                return op1 / op2
        elif op == "+":
            return op1 + op2
        else:
            return op1 - op2

if __name__ == '__main__':
    answer = Solution()
    print answer.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])