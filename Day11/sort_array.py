class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        def fun(n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and nums[left] > nums[largest]:
                largest = left
            if right < n and nums[right] > nums[largest]:
                largest = right
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                fun(n, largest)
        for i in range(n // 2 - 1, -1, -1):
            fun(n, i)
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0] 
            fun(i, 0)  
        return nums