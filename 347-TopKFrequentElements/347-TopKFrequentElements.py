# Last updated: 5/19/2025, 7:07:08 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # find k most frequent elements within array
        # freq map --> 
        # list of lists holding numbers with freq as index --> 
        # bucket sort most to least 
        map = {}
        # 0 to n+1 bc freq starts at 1
        # each indx represents freq of num, [] holds those nums
        bucket = [[] for i in range(len(nums)+1)]

        # map freq to each num
        for num in nums: 
            map[num] = 1 + map.get(num, 0)
        
        # put num into bucket at index freq
        for num, freq in map.items(): 
            bucket[freq].append(num)

        res = []
        # iterate from most to least frequent
        # range(start inclusive, end exclusive, increment by)
        for i in range(len(bucket)-1, 0, -1):
            # bucket[i] = every num in []
            for num in bucket[i]:
                # add to result until res is k long
                res.append(num)
                if len(res) == k: 
                    return res

        # Time Complexity: O(n)
        # Space Complexity: O(n)