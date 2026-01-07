# # W7A16
# print("W7A16")

# lst_W7A16 = list(map(int, input().split()))

# lst_W7A16.sort()

# soxoa = 0

# for i in range(len(lst_W7A16) - 1):
#     count = 1
#     if lst_W7A16[i] == lst_W7A16[i + 1]:
#         count += 1
#     else:
#         if count != lst_W7A16[i]:
#             if count > lst_W7A16[i]:
#                 soxoa += count - lst_W7A16[i]
#             else:
#                 soxoa += count
#         count = 1

# # W7A21
# print("W7A21")

# N_7A21 = int(input())

# while N_7A21 <= 0 or N_7A21 > 365:
#     print("ngày nhập không hợp lệ, vui lòng nhập lại!")
#     N_7A21 = int(input())

# T_7A21 = int(input())

# while T_7A21 <= 0 or T_7A21 > 12:
#     print("tháng nhập không hợp lệ, vui lòng nhập lại!")
#     T_7A21 = int(input())

# days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# for i in range(T_7A21 - 1):
#     N_7A21 += days_in_month[i] 

# print(N_7A21)

#W7A23
print("W7A23")

str_W7A23 = input()

def Tim_Ten(s):
    Van_Ban = s.split()
    
    count = 0

    for i in Van_Ban:
        if len(i) >= 2 and i[0].isupper() and i[1:].islower() and i.isalpha():
            count += 1

    return count

print(Tim_Ten(str_W7A23))