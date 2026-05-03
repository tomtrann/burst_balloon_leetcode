class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int greatest = candies[0];
        vector<bool> rs;
        for (int i = 0; i < candies.size(); i++) {
            if (candies[i] >= greatest){
                greatest = candies[i];
            }
        }
        for (int j = 0; j < candies.size(); j++) {
            if (candies[j] + extraCandies < greatest) {
                rs.push_back(false);
            }
            else {
                rs.push_back(true);
            }
        }
        return rs;
    }
};