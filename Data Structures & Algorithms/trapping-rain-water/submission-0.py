class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        area=0
        n=len(height)
        lmax=0
        rmax=0
        left=0
        right=n-1
        while(left<right):
            lmax=max(lmax,height[left])
            rmax=max(rmax,height[right])
            if lmax<rmax:
                area+=lmax-height[left]
                left+=1
            else:
                area+=rmax-height[right]
                right-=1
        return area