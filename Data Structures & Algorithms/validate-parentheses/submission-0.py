class Solution:
    def isValid(self, s: str) -> bool:
        arr=list(s)
        stack=[]
        for i in range(len(arr)):
            if arr[i]=='[' or arr[i]=='{' or arr[i]=='(':
                stack.append(arr[i])
            elif arr[i]==']':
                if not stack or stack[-1]!='[':
                    return False
                stack.pop()
            elif arr[i]==')':
                if not stack or stack[-1]!='(':
                    return False
                stack.pop()
            elif arr[i]=='}':
                if not stack or stack[-1]!='{':
                    return False
                stack.pop()
        return len(stack)==0