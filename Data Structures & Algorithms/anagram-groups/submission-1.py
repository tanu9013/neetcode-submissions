class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for words in strs:
            count = [0]*26
            for char in words:
                index = ord (char) - ord ('a')
                count [index] += 1
            key = tuple(count)
#if key not in anagram_map:
 #               anagram_map[key] = []
            anagram_map[key].append(words)
        return list (anagram_map.values())