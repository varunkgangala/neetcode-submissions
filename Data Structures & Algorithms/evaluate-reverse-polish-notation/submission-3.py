class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if tokens[i] not in ['+','-','*','/']:
                stack.append(int(tokens[i]))
            elif tokens[i]=='+':
                a=stack.pop()
                b=stack.pop()
                stack.append(b+a)
            elif tokens[i]=='-':
                a=stack.pop()
                b=stack.pop()
                stack.append(b-a)
            elif tokens[i]=='*':
                a=stack.pop()
                b=stack.pop()
                stack.append(b*a)
            elif tokens[i]=='/':
                a=stack.pop()
                b=stack.pop()
                if a==0:
                    return False
                stack.append(int(b/a))
        return stack[-1]