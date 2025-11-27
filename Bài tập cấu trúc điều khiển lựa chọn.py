# W3A2
print('W3A2')

a_W3A2 = int(input('Nhập số a: '))
b_W3A2 = int(input('Nhập số b: '))

def Dao_So (a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b

    print('a =', a )
    print('b =', b )

Dao_So(a_W3A2, b_W3A2)

print('\n')

# W3A3
print('W3A3')

n_W3A2 = int(input('Nhập số n: '))


def Luy_Thua (n):
    if ( n > 0 and (n & (n-1)) == 0):
        print(f'{n} là luỹ thừa của 2')
    else:
        print(f'{n} không là luỹ thừa của 2')
      
Luy_Thua(n_W3A2) 

print('\n')

# W3A4
print('W3A4')

m_W3A4 = int(input('Nhập số m: '))
n_W3A4 = int(input('Nhập số n: '))


def Lam_Tron_Xuong (m, n):
    if ( n == 0):
        print(f'Phép chia không thực hiện được')
    else:
        print(f'Kết quả là:', m//n)
      
Lam_Tron_Xuong(m_W3A4, n_W3A4) 

print('\n')

# W3A5
print('W3A5')

m_W3A5 = int(input('Nhập số m: '))
n_W3A5 = int(input('Nhập số n: '))

import math

def Lam_Tron_Len (m, n):
    if ( n == 0):
        print(f'Phép chia không thực hiện được')
    else:
        print(f'Kết quả là:', math.ceil(m/n))
      
Lam_Tron_Len(m_W3A5, n_W3A5) 

print('\n')

# W3A6
print('W3A6')

x_W3A6 = int(input('Nhập số x nguyên dương: '))

while (x_W3A6 <= 0):
    print('x nhập vào không đúng')
    x_W3A6 = int(input('Nhập lại số x: '))
    

if (x_W3A6 % 2 == 0):
    print('Even')
else:
    print('Odd')

print('\n')

# W3A7
print('W3A7')

a_W3A7 = int(input('Nhập số a nguyên: '))
b_W3A7 = int(input('Nhập số b nguyên: '))

if (a_W3A7 < 0 and b_W3A7 < 0):
    print('Yes')
else:
    print('No')

print('\n')

# W3A8
print('W3A8')

a_W3A8 = str(input('Nhập một chuỗi a: '))
b_W3A8 = str(input('Nhập một chuỗi b: '))

if (len(a_W3A8) > len(b_W3A8)):
    print('True')
else:
    print('False')

print('\n')

# W3A9
print('W3A9')

a_W3A9 = int(input('Nhập một số nguyên dương a: '))
b_W3A9 = int(input('Nhập một số nguyên dương b: '))
c_W3A9 = int(input('Nhập một số nguyên dương c: '))

while (a_W3A9 <= 0 or b_W3A9 <= 0 or c_W3A9 <= 0):
    if (a_W3A9 <= 0):
        print('Số a không đúng')
        a_W3A9 = int(input('Nhập la một số nguyên dương a: '))
    elif (b_W3A9 <= 0):
        print('Số b không đúng')
        b_W3A9 = int(input('Nhập lại một số nguyên dương b: '))
    elif (c_W3A9 <= 0):
        print('Số c không đúng')
        c_W3A9 = int(input('Nhập lại một số nguyên dương c: '))        
        
def Xac_Dinh_Tam_Giac (a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Yes")
    else:
        print("No")
        
Xac_Dinh_Tam_Giac(a_W3A9, b_W3A9, c_W3A9)
        
print('\n')

# W3A10
print('W3A10')

a_W3A10 = int(input('Nhập một số nguyên dương a: '))
b_W3A10 = int(input('Nhập một số nguyên dương b: '))
c_W3A10 = int(input('Nhập một số nguyên dương c: '))
d_W3A10 = int(input('Nhập một số nguyên dương d: '))

        
def Xac_Dinh_Max (a, b, c, d):
    Max = a
    if (b > Max):
        Max = b
    if (c > Max):
        Max = c
    if (d > Max):
        Max = d
    print('Số nguyên lớn nhất là:', Max)
            
Xac_Dinh_Max(a_W3A10, b_W3A10, c_W3A10, d_W3A10)
        
print('\n')

# W3A11
print('W3A11')

a_W3A11 = int(input('Nhập một số nguyên dương a: '))
b_W3A11 = int(input('Nhập một số nguyên dương b: '))
c_W3A11 = int(input('Nhập một số nguyên dương c: '))

while (a_W3A11 <= 0 or b_W3A11 <= 0 or c_W3A11 <= 0):
    if (a_W3A11 <= 0):
        print('Số a không đúng')
        a_W3A11 = int(input('Nhập la một số nguyên dương a: '))
    elif (b_W3A11 <= 0):
        print('Số b không đúng')
        b_W3A11 = int(input('Nhập lại một số nguyên dương b: '))
    elif (c_W3A11 <= 0):
        print('Số c không đúng')
        c_W3A11 = int(input('Nhập lại một số nguyên dương c: '))        
        
def Xac_Dinh_Tam_Giac (a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if(a == b == c):
            print('Tam giác đều')
        elif (a == b or a == c or b == c):
            print('Tam giác cân')
        else:
            print('Tam giác thường')
    else:
        print("Đây không phải tam giác")
        
Xac_Dinh_Tam_Giac(a_W3A11, b_W3A11, c_W3A11)
        
print('\n')