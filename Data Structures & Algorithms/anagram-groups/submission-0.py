class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_dict = defaultdict(list)
        
        for s in strs:
            s = s.lower()
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord('a')] += 1
            char_dict[tuple(chars)].append(s)
        return list(char_dict.values())