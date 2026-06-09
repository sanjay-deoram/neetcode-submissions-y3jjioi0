class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)): # O(n^2) O(1) 
            for j in range(i+1,len(words)):
                if self.isPrefixAndSuffix(words[i],words[j]):
                    count+=1
        return count
    
    def isPrefixAndSuffix(self,str1,str2):
        """
        this O(k) where k is the length of that prefix/suffix
        different way could be take the length of str1. for eg: aba -> length is 3
        now we check str2[:len(str1)] == str1 then we know it startswith, we can do the same with 
        ends with
        """
        # if str2.startswith(str1) and str2.endswith(str1): return 1
        prefix = len(str1)
        suffix = -prefix
        if str2[:prefix] == str1 and str2[suffix:]==str1: return 1