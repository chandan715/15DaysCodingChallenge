class Solution:
    def search(self, nums: List[int], target: int) -> int:
        srt=0
        end=len(nums)-1
        while srt<=end:
            mid = (srt+end)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                srt=mid+1
            elif nums[mid]>target:
                end=mid-1
        
        return -1