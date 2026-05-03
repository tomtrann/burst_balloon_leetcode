class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string rs = "";
        int i = 0, j = 0;

        while (i < word1.size() && j < word2.size()) {
            rs += word1[i++];
            rs += word2[j++];
        }

        // add remaining characters
        while (i < word1.size()) {
            rs += word1[i++];
        }

        while (j < word2.size()) {
            rs += word2[j++];
        }

        return rs;
    }
};