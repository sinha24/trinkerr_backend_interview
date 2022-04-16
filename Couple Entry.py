input_arr = list(map(int, input().split()))
print("input array =", input_arr)

def sol(dress_arr):
    dress_count = {}
    
    for i in dress_arr:
        if i not in dress_count:
            dress_count[i] = 0
        dress_count[i] += 1
    
    res = 0
    
    for i in dress_count.keys():
        res += dress_count[i]*(dress_count[i]-1)//2
    
    return res
    
res = sol(input_arr)
print("result =",res)
