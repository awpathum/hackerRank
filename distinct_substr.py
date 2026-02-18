# sliding window fixed.
def countGoodSubstrings(s: str) -> int:
    count = 0
    k = 3
    char_list = list(s)
    sub_str = char_list[:k]
    # print(sub_str)
    for i in range(0,len(char_list)):
        sub_str = char_list[i:i+k]
        print(sub_str)
        if len(set(sub_str)) == k:
            count = count + 1
        
    return count

s = "xyzzaz"
print(countGoodSubstrings(s))