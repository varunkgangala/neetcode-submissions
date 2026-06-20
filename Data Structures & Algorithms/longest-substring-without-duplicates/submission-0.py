class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr=list(s)
        max_len=0
        for left in range(len(arr)):
            res=[]
            for right in range(left,len(arr)):
                if arr[right] in res:
                    break
                res.append(arr[right])
            max_len=max(max_len,len(res))
        return max_len