class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        array1=list(s1)
        array2=list(s2)
        res=[]
        target=sorted(array1)
        for i in range(len(array1)):
            res.append(array2[i])
        if sorted(res)==target:
            return True
        
        for i in range(len(array1),len(array2)):
            res.pop(0)
            res.append(array2[i])
            if sorted(res)==target:
                return True
        return False