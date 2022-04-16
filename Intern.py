input_arr = list(input().split())
print("keys =", input_arr)

def sol(key_arr):
    n = len(key_arr)
    sorted_arr = []
    for i in key_arr:
        s = "".join(sorted(i))
        sorted_arr.append(s)
    
    anagram_dict = {}
    for i in range(n):
        if sorted_arr[i] not in anagram_dict:
            anagram_dict[sorted_arr[i]] = []
        anagram_dict[sorted_arr[i]].append(i)
    
    res = []
    for i in anagram_dict.keys():
        r = []
        for j in anagram_dict[i]:
            r.append(key_arr[j])
        res.append(r)
    
    return res

res = sol(input_arr)
print("result =",res)
