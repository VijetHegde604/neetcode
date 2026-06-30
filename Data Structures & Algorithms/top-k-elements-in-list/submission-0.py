class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Count how many times each number appears in the array.
        # Example: [1,1,2,3,3,3] -> {1:2, 2:1, 3:3}
        count = collections.Counter(nums)

        # Bucket array where the index represents the frequency.
        # freq[i] will store all numbers that appear exactly i times.
        # Maximum possible frequency is len(nums), so we need len(nums) + 1 buckets.
        freq = [[] for i in range(len(nums) + 1)]

        # Place every number into its corresponding frequency bucket.
        # Example:
        # count = {1:2, 2:1, 3:3}
        # freq[1] = [2]
        # freq[2] = [1]
        # freq[3] = [3]
        for n, c in count.items():
            freq[c].append(n)

        res = []

        # Traverse the buckets from highest frequency to lowest.
        # This ensures we collect the most frequent elements first.
        for i in range(len(freq) - 1, 0, -1):

            # Add every number present in the current frequency bucket.
            for n in freq[i]:
                res.append(n)

                # Stop as soon as we have collected k elements.
                if len(res) == k:
                    return res
