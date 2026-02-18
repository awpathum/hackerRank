class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # abcabcbb
        max_len = 0
        l = 0
        r = 1
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        char_set = set(s[l])
        
        for i in range(len(s)-1):
            if s[r] not in char_set:
                char_set.add(s[r])
                r = r +1
            else:
                max_len = max(max_len, len(char_set))
                c = 0
                while s[r] in char_set:
                    char_set.remove(s[l])
                    l = l + 1
    
                char_set.add(s[r])
                r = r + 1
        
        max_len = max(max_len, len(char_set))

        return max_len