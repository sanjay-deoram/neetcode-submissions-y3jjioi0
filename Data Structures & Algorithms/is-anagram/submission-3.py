class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        n is the total number of characters in the input strings.
        """
        s_list = [0]*26
        t_list = [0]*26

        for c in s:
            s_list[ord(c)-ord('a')]+=1
        
        for c in t:
            t_list[ord(c)-ord('a')]+=1
        return s_list == t_list

        

