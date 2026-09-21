class Solution(object):
    def topKFrequent(self, nums, k):
        hashmap = {}

        for n in nums: 
            hashmap[n] = hashmap.get(n, 0) + 1
        
        maxHeap = []

        for num, freq in hashmap.items(): 
            maxHeap.append((-freq, num))
        
        heapq.heapify(maxHeap)
        res = []

        for i in range(k):
            freq, num = heapq.heappop(maxHeap)
            res.append(num)
        return res