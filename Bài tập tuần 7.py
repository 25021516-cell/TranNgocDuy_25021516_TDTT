# # W7A1
# print("W7A1")

# lst_W7A1 = list(map(int, input().split()))
# target_W7A1 = int(input())

# def binary_search(arr, left, right, target):
#     while left <= right:
#         mid = left + (right + left) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# print(binary_search(lst_W7A1, 0, len(lst_W7A1) - 1, target_W7A1))

# # W7A2
# print("W7A2")

# lst_W7A2 = list(map(int, input().split()))
# x_W7A2 = int(input())

# def count_occurrences(arr, x) -> int:
#     count = 0
#     for i in arr:
#         if i == x:
#             count += 1
#     return count

# print(count_occurrences(lst_W7A2, x_W7A2))

# # W7A3
# print("W7A3")

# lst_W7A3 = list(map(int, input().split()))
# lst_W7A3.sort()

# for i in lst_W7A3:
#     print(i, end=' ')

# # W7A4
# print("W7A4")

# lst_W7A4 = list(map(int, input().split()))

# lst_sub_W7A4 = []
# max_count_W7A4 = 0
# most_frequent_W7A4 = None

# for i in lst_W7A4:
#     if i not in lst_sub_W7A4:
#         lst_sub_W7A4.append(i)

#         for j in lst_W7A4:
#             if i == j:
#                 count_W7A4 = lst_W7A4.count(i)
#                 if count_W7A4 > max_count_W7A4:
#                     max_count_W7A4 = count_W7A4
#                     most_frequent_W7A4 = i

# print(f'{most_frequent_W7A4} xuất hiện nhiều nhất, sớm nhất, {max_count_W7A4} lần')

# # W7A5
# print("W7A5")

# lst_W7A5 = list(map(int, input().split()))
# x_W7A5 = int(input())

# def count_pairs_with_sum(arr, X):
#     count = 0
#     seen = {}

#     for num in arr:
#         c = X - num
#         if c in seen:
#             count += seen[c]
        
#         seen[num] = seen.get(num, 0) + 1
    
#     return count

# print(count_pairs_with_sum(lst_W7A5, x_W7A5))

# # W7A6
# print("W7A6")

# lst_W7A6 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# def LOng(arr):
#     lst = []
#     for i in arr:
#         lst.extend(i)

#     return lst

# print(LOng(lst_W7A6))

# # W7A7
# print("W7A7")

# lst_W7A7 = list(map(int, input().split()))

# def Dem_Do_Dai_Nhat(arr):
#     if not arr:
#         return 0
    
#     dp  = [1] * len(arr)

#     for i in range(1, len(arr)):
#         for j in range(i):
#             if arr[i] > arr[j]:
#                 dp[i] = max(dp[i], dp[j] + 1)

#     return max(dp)

# print(Dem_Do_Dai_Nhat(lst_W7A7))

# # W7A8
# print("W7A8")

# lst_W7A8 = [[1, 4], [2, 4], [3, 6], [4, 4]]
# queries_W7A8 = [2, 3, 4, 5]

# def binary(interval, queries):
#     for i in queries:
#         arr = []
#         for j in interval:
#             count = 0
#             if j[0] <= i <= j[1]:
#                 count = j[1] - j[0] + 1
#                 if count not in arr:
#                     arr.append(count)
#         arr.sort()
#         if arr:
#             print(arr[0], end=' ')
#         else:
#             print(-1, end=' ')
                
# binary(lst_W7A8, queries_W7A8)

# # W7A9
# print("W7A9")

# lst_W7A9 = list(map(int, input().split()))

# def Tim_So_Nho_Hon(arr):

#     result = []

#     for i in range(len(arr)):
#         count = 0
#         for j in range(i + 1, len(arr)):
#             if arr[i] > arr[j]:
#                 count += 1
#         result.append(count)

#     return result

# print(Tim_So_Nho_Hon(lst_W7A9))
            
# # W7A10
# print("W7A10")

# lst_W7A10 = list(map(int, input().split()))
# m_W7A10 = int(input())

# def pre(arr, m):
#     prefix = [0] * (len(arr) + 1)
#     for i in range(len(arr)):
#         prefix[i+1] = (prefix[i] + arr[i]) % m
    
#     # Dòng 2: Khởi tạo sorted list của prefix sums
#     sorted_prefixes = []
    
#     # Dòng 3: Biến lưu kết quả
#     max_result = 0
    
#     # Dòng 4: Duyệt qua từng prefix sum
#     for i in range(1, len(prefix)):
#         current_prefix = prefix[i]
        
#         # Dòng 5: Tìm prefix lớn hơn current_prefix một chút
#         # bằng binary search
#         import bisect
#         pos = bisect.bisect_right(sorted_prefixes, current_prefix)
        
#         # Dòng 6: Nếu có phần tử lớn hơn
#         if pos < len(sorted_prefixes):
#             max_result = max(max_result, (current_prefix - sorted_prefixes[pos] + m) % m)
        
#         # Dòng 7: Cũng xét trường hợp không trừ prefix nào
#         max_result = max(max_result, current_prefix)
        
#         # Dòng 8: Thêm current_prefix vào sorted list
#         bisect.insort(sorted_prefixes, current_prefix)
    
#     # Dòng 9: Trả về kết quả
#     return max_result

# print(pre(lst_W7A10, m_W7A10))

# # W7A11
# print("W7A11")

# lst_W7A11 = str(input())
# target_W7A11 = input()

# import string

# for p in string.punctuation:
#     lst_W7A11 = lst_W7A11.replace(p, "")

# new_lst_W7A11 = lst_W7A11.split()

# def find_word(arr, target):
#     dict = {}

#     for i in arr:
#         if i not in dict:
#             dict[i] = 1
#         else:
#             dict[i] += 1

#     if target in dict:
#         return dict[target]
#     else:
#         return 0
    
# print(find_word(new_lst_W7A11, target_W7A11))

# W7A12
print("W7A12")

