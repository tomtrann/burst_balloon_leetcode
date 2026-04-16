class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> paths(m, vector<int>(n));
        for (int i = 0; i < n; i++) {
            paths[0][i] = 1;
        }

        for (int j = 0; j < m; j++) {
            paths[j][0] = 1;
        }

        for (int j = 1; j < m; j++) {
            for (int i = 1; i < n; i++) {
                paths[j][i] = paths[j-1][i] + paths[j][i-1];
            }
        }
        return paths[m-1][n-1];
    }
};