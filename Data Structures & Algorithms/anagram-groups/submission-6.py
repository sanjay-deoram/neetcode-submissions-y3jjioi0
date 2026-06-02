class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = defaultdict(list)
        
        for word in strs:
            char_count = tuple(sorted(word))
            word_map[char_count].append(word)
        
        return list(word_map.values())