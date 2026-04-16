class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        vector<int> arr(n);
        arr[0] = cost[0];
        arr[1] = cost[1];
        for (int i = 2; i < n; i++) {
            arr[i] = min(arr[i-1], arr[i-2]) + cost[i];
        }

        return min(arr[n-1], arr[n-2]);
    }
};