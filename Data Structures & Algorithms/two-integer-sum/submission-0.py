class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)

        for i, num in enumerate(nums):

            another = target - num

            if another in seen:
                return [seen[another], i]

            seen[num] = i





        