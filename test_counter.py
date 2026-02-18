from collections import Counter
from typing import List

# c b a e b a b a c d
# 0 1 2 3 4 5 6 7 8 9
    # i
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        k = len(p)
        n = len(s)

        if k > n:
            return res

        p_count = Counter(p)
        window_count = Counter(s[:k])

        if window_count == p_count:
            res.append(0)

        for i in range(k, n):
            # Add new character to window
            window_count[s[i]] += 1
            

            # Remove old character from window
            window_count[s[i-k]] -= 1
            if window_count[s[i-k]] == 0:
                del window_count[s[i-k]]

            # Compare counters
            if window_count == p_count:
                res.append(i - k + 1)

        return res
