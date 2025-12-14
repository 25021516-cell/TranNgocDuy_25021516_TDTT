# # W5A1
# print('W5A1')

# a_W5A1 = int(input('Nhập số nguyên dương a: '))
# b_W5A1 = int(input('Nhập số nguyên dương b: '))

# def Max_Of_Two(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# print('Số lớn hơn là:', Max_Of_Two(a_W5A1, b_W5A1))

# # W5A2
# print('W5A2')

# a_W5A2 = int(input('Nhập số nguyên dương a: '))
# b_W5A2 = int(input('Nhập số nguyên dương b: '))

# def swap(a, b):
#     a = a ^ b
#     b = a ^ b
#     a = a ^ b
#     return a, b

# print(f'Giá trị ban đầu: a = {a_W5A2}, b = {b_W5A2}')
# a_W5A2, b_W5A2 = swap(a_W5A2, b_W5A2)
# print(f'Sau khi hoán đổi: a = {a_W5A2}, b = {b_W5A2}')

# # W5A3
# print('W5A3')

# n_W5A3 = int(input('Nhập số nguyên dương n: '))

# while n_W5A3 < 2:
#     n_W5A3 = int(input('Vui lòng nhập số nguyên dương n >= 2: '))

# from math import*

# def Kiem_Tra_So_Nguyen_To(n: int) -> bool:
#     if n < 2:
#         return False
#     for i in range(2, int(sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True 

# if Kiem_Tra_So_Nguyen_To(n_W5A3):
#     print(f'{n_W5A3} là số nguyên tố')
# else:
#     print(f'{n_W5A3} không phải là số nguyên tố')

# # W5A4
# print('W5A4')

# n_W5A4 = int(input('Nhập số nguyên dương n: '))

# def So_Hoan_Hao(n: int) -> bool:
#     summ = 0
#     for i in range(1, n):
#         if n % i == 0:
#             summ += i
    
#     if summ == n:
#         return True 
#     return False

# if So_Hoan_Hao(n_W5A4):
#     print(f'{n_W5A4} là số hoàn hảo')
# else:
#     print(f'{n_W5A4} không phải là số hoàn hảo')

# #W5A5
# print('W5A5')

# k_W5A5 = int(input('Nhập số nguyên dương k: '))
# number_W5A5 = map(int, input('Nhập các số nguyên dương, cách nhau bởi dấu cách: ').split()) 
# list_W5A5 = list(number_W5A5)

# def Tim_Vi_Tri(list_W5A5, k_W5A5):
#     for i in range(len(list_W5A5)):
#         if list_W5A5[i] == k_W5A5:
#             return i
#     return -1

# print(f'Vị trí của {k_W5A5} trong dãy là: {Tim_Vi_Tri(list_W5A5, k_W5A5)}')

# #W5A6
# print('W5A6')

# n_W5A6 = int(input('Nhập số nguyên dương n: '))

# def Giai_Thua(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * Giai_Thua(n - 1)
    
# print(f'{n_W5A6}! = {Giai_Thua(n_W5A6)}')

# #W5A7
# print('W5A7')

# num1_W5A7 = float(input('Nhập số thứ nhất: '))
# num2_W5A7 = float(input('Nhập số thứ hai: '))

# operat_W5A7 = str(input('Nhập phép toán (+, -, *, /): ') )

# def Tinh_Toan(num1, num2, operat):
#     if operat == '+':
#         result = num1 + num2
#     elif operat == '-': 
#         result = num1 - num2
#     elif operat == '*':
#         result = num1 * num2
#     elif operat == '/':
#         if num2 != 0:
#             result = num1 / num2
#         else:
#             return 'Lỗi: Không thể chia cho 0'
#     else:
#         return 'Lỗi: Phép toán không hợp lệ'
    
#     return round(result, 2)
    
# print(f'Kết quả của phép toán là: {Tinh_Toan(num1_W5A7, num2_W5A7, operat_W5A7)}')

# #W5A8
# print('W5A8')

# x_W5A8 = int(input('Nhập số x: '))
# y_W5A8 = int(input('Nhập số y: '))

# def Hamming(x, y):
#     xor_W5A8 = x ^ y

#     count = 0
#     while xor_W5A8 > 0:
#         count += xor_W5A8 & 1

#         xor_W5A8 >>= 1

#     return count

# print(f'Khoảng cách Hamming giữa {x_W5A8} và {y_W5A8} là: {Hamming(x_W5A8, y_W5A8)}')

# #W5A9
# print('W5A9')

# n_W5A9 = int(input('Nhập số nguyên dương n: '))

# def Tong_Cac_Chu_So(n):
#     tong = 0

#     while n > 0:
#         a = n % 10
#         tong += a
#         n //= 10

#     return tong

# print(f'Tổng các chữ số của {n_W5A9} là: {Tong_Cac_Chu_So(n_W5A9)}')

#W5A10
print('W5A10')

a_W5A10 = str(input('Nhập chuỗi a: '))
b_W5A10 = str(input('Nhập chuỗi b: '))

def Dang_Cau(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False
    
    mapping_a_to_b = {}
    mapping_b_to_a = {}

    for char_a, char_b in zip(a, b):
        if char_a in mapping_a_to_b:
            if mapping_a_to_b[char_a] != char_b:
                return False
        else:
            mapping_a_to_b[char_a] = char_b

        if char_b in mapping_b_to_a:
            if mapping_b_to_a[char_b] != char_a:
                return False
        else:
            mapping_b_to_a[char_b] = char_a

    return True

if Dang_Cau(a_W5A10, b_W5A10):
    print(f'"{a_W5A10}" và "{b_W5A10}" là đẳng cấu')
else:
    print(f'"{a_W5A10}" và "{b_W5A10}" không phải là đẳng cấu')