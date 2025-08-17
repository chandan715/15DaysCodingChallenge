class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1} 
        prefix_sum = 0
        res = 0
        for num in nums:
            prefix_sum += num % 2 
            if prefix_sum - k in prefix_count:
                res += prefix_count[prefix_sum - k]
            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1
        return res
        