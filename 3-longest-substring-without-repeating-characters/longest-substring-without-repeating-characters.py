class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hashSet = set()
        l = 0
        longest = 0 
        for r in range(len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1
            hashSet.add(s[r])
            longest = max(longest, r - l + 1)
        return longest
                                               
        