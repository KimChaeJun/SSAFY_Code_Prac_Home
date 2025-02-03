def len_(arr):
    cnt = 0
    for _ in arr:
        cnt+=1
    return cnt
def sum_(arr):
    res = 0
    for i in arr:
        res+=i
    return res
def max_(arr):
    max_value = 0
    for i in arr:
        if i >= max_value:
            max_value = i
    return max_value
def min_(arr):
    min_value = max_(arr)
    for i in arr:
        if i <= min_value:
            min_value = i
    return min_value
def sorted_(arr, reverse = True):
    sorted_arr = list(arr)
    if reverse:
        for i in range(len_(arr)):
            for j in range(len_(arr)):
                if sorted_arr[i] < sorted_arr[j]:
                    sorted_arr[i],sorted_arr[j] = sorted_arr[j],sorted_arr[i]
    else:
        for i in range(len_(arr)):
            for j in range(len_(arr)):
                if sorted_arr[i] > sorted_arr[j]:
                    sorted_arr[i],sorted_arr[j] = sorted_arr[j],sorted_arr[i]
    return sorted_arr
arr = [3,2,5,1,4]
arr_len = len_(arr)
str_len = len_('Hello World')
arr_sum = sum_(arr)
arr_max = max_(arr)
arr_min = min_(arr)
arr_sorted1 = sorted_(arr)
arr_sorted2 = sorted_(arr,False)
print(arr_len, arr_sum, arr_max, arr_min)
print(str_len, arr_sorted1, arr_sorted2)