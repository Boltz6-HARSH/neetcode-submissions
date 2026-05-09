class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        #count frequency
        for num in nums:

            if num not in count:
                count[num] = 0

            count[num] += 1

        sorted_nums = sorted(count, key=count.get)

        return sorted_nums[-k:]

