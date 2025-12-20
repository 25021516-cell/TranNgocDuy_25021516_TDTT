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

# W7A9
print("W7A9")


