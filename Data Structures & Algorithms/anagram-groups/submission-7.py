class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = defaultdict(list)
        
        for word in strs:
            word_count = [0] * 26
            for letter in word:
                word_count[ord(letter) - ord('a')]+=1
            
          
            word_map[tuple(word_count)].append(word)

        
        return list(word_map.values())