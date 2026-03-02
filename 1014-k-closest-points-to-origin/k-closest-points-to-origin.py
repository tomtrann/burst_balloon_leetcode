class Solution:
    def kClosest(self, points, k):
        #Compute squared distances
        distances = [x*x + y*y for x, y in points]

        #Find kth smallest distance
        threshold = self.select(distances, k)

        #Collect k closest points
        result = []
        for point in points:
            if point[0] * point[0] + point[1] * point[1] <= threshold:
                result.append(point)

        return result[:k]

    def select(self, arr, k):
        # Base case
        if len(arr) <= 7:
            return sorted(arr)[k-1]

        # Divide into groups of 7
        groups = [arr[i:i+7] for i in range(0, len(arr), 7)]

        # Find medians 
        medians = [sorted(group)[len(group)//2] for group in groups]

        # Recursively find pivot (median of medians)
        pivot = self.select(medians, len(medians)//2 + 1)

        # Partition
        lows = [x for x in arr if x < pivot]
        highs = [x for x in arr if x > pivot]
        pivots = [x for x in arr if x == pivot]

        if k <= len(lows):
            return self.select(lows, k)
        elif k <= len(lows) + len(pivots):
            return pivot
        else:
            return self.select(highs, k - len(lows) - len(pivots))
        