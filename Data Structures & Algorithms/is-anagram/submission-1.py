class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_dict1 = {}
        word_dict2 = {}
        length1 = len(s)
        length2 = len(t)

        if length1 != length2:
            return False

        for i in range(length1):
            word_dict1[s[i]] = 1 + word_dict1.get(s[i], 0)
            word_dict2[t[i]] = 1 + word_dict2.get(t[i], 0)

        for l in word_dict1:
            if (l not in word_dict2) or (word_dict1[l] != word_dict2[l]):
                return False
        return True
