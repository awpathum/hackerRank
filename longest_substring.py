def lengthOfLongestSubstring(s: str) -> int:
    left = right = max_len = 0
    substr_set = set()

    for right in range(len(s)):
        if s[right] in substr_set:
            max_len = max(max_len,len(substr_set))
            substr_set.remove(s[left])
            left = left + 1

        substr_set.add(s[right])
        print(f"Left: {left} | Right : {right}")
        print(substr_set)
    return max_len

print(lengthOfLongestSubstring("dvdf"))