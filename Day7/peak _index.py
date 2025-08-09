class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        s=0
        end=len(arr)-1
        while s<end:
            mid=(s+end)//2
            if arr[mid] < arr[mid + 1]:
                s = mid + 1
            else:
                end = mid
        return s
        