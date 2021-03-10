class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        map_a = dict()
        for num in nums: 
            temp = target - num 
            if temp in map_a:
                results.append([temp, num])
                if map_a[temp] == 1:
                    map_a.pop(temp)
                else:
                    map_a[temp] = map_a[temp] - 1
            else:
                if num in map_a:
                    map_a[num] = map_a[num] + 1
                else:
                    map_a[num] = 1
        return results

class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        map_a = dict()
        for num in nums: 
            temp = target - num 
            jug = map_a.get(temp)
            if jug:
                results.append([temp, num])
                if jug == 1:
                    map_a.pop(temp)
                else:
                    map_a[temp] = jug - 1
            else:
                map_a[num] = map_a.get(num, 0) + 1
        return results