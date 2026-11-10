class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(list)
        for key, val in enumerate(nums):
            seen[val] = seen.get(val, 0) +1
        
        arr = []
        for key, val in seen.items():
            arr.append([val, key])
        sortedArr = sorted(arr)
        result = []
        while len(result) < k:
            result.append(sortedArr.pop()[1])
        return result
        

        