# len 함수
def len_(arr):
    cnt = 0
    for _ in arr:
        cnt+=1
    return cnt
# sum 함수
def sum_(arr):
    res = 0
    for i in arr:
        res+=i
    return res
# max 함수
def max_(arr):
    max_value = int(arr[0])
    for i in range(1,len_(arr)):
        if arr[i] >= max_value:
            max_value = arr[i]
    return max_value
# min 함수
def min_(arr):
    min_value = int(arr[0])
    for i in range(1,len_(arr)):
        if arr[i] <= min_value:
            min_value = arr[i]
    return min_value
# sorted 함수
def sorted_(arr, reverse = 1):
    sorted_arr = list(arr)
    for i in range(len_(arr)):
        for j in range(len_(arr)):
            if sorted_arr[i] < sorted_arr[j]:
                sorted_arr[i],sorted_arr[j] = sorted_arr[j],sorted_arr[i]
    return sorted_arr[::reverse]
# count 메서드 함수구현
def count_(arr, check):
    cnt = [i for i in arr if i==check]
    return len_(cnt)
# index 메서드 함수구현
def index_(arr, check, start = 0, end = 0):
    if start and end:
        cnt = [i for i in range(start, end+1) if arr[i]==check]
    else:
        cnt = [i for i in range(len_(arr)) if arr[i]==check]
    return cnt[0]
# count 메서드 함수구현 / None Comprehension
def count_non_comp(arr, check):
    cnt = 0
    for i in arr:
        if i == check:
            cnt += 1
    return cnt
# index 메서드 함수구현 / None Comprehension
def index_non_comp(arr, check, start = 0, end = 0):
    if start and end:
        for i in range(start, end+1):
            if arr[i] == check:
                return i 
    else:
        for i in range(len_(arr)):
            if arr[i] == check:
                return i 
# 검증 코드
arr = [3,2,5,1,4]
# len_ 검증
arr_len = len_(arr)
str_len = len_('Hello World')
# sum_ 검증
arr_sum = sum_(arr)
# max_ 검증
arr_max = max_(arr)
# min_ 검증
arr_min = min_(arr)
# sorted_ 검증
arr_sorted1 = sorted_(arr)
arr_sorted2 = sorted_(arr,-1)
# count_ 검증
arr_count = count_(arr, 1)
str_count = count_('Hello World','l')
# index_ 검증
arr_index = index_(arr, 1)
str_index = index_('Hello World','l')
# index_ 검증 / 슬라이싱
arr_index_1 = index_(arr, 1, 2, 3)
str_index_1 = index_('Hello World','l', 6, 10)
# count_non_comp 검증
arr_count_non = count_non_comp(arr, 1)
str_count_non = count_non_comp('Hello World','l')
# index_non_comp 검증
arr_index_non = index_non_comp(arr, 1)
str_index_non = index_non_comp('Hello World','l')
# index_non_comp 검증 / 슬라이싱
arr_index_1_non = index_non_comp(arr, 1, 2, 3)
str_index_1_non = index_non_comp('Hello World','l', 6, 10)

# 출력
print(f"arr len = {arr_len}\nstr len = {str_len}\narr sum = {arr_sum}\narr max = {arr_max}\narr min = {arr_min}\n")
print(f"arr sorted1 = {arr_sorted1}\narr sorted reverse = {arr_sorted2}\n")
print(f"arr count = {arr_count}\nstr count = {str_count}\n")
print(f"arr index = {arr_index}\nstr index = {str_index}\n")
print(f"arr index set range = {arr_index_1}\nstr index set range = {str_index_1}\n")
print(f"arr count non_comp = {arr_count_non}\nstr count = {str_count_non}\n")
print(f"arr index non_comp = {arr_index_non}\nstr index = {str_index_non}\n")
print(f"arr index set range non_comp = {arr_index_1_non}\nstr index set range non_comp = {str_index_1_non}\n")