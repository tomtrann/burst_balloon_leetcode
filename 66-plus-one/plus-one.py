class Solution(object):
    def plusOne(self, digits):
        res = [] 
        strs = ""
        for n in digits: 
            strs += str(n)
        
        newNum = int(strs) + 1
        newString = str(newNum) 
        for c in newString: 
            res.append(int(c))
        return res
        