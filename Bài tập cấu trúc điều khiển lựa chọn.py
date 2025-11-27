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

# W3A12
print('W3A12')

n_W3A12 = int(input('Nhập vào số năm: '))

while (n_W3A12 < 0):
    print('Số năm nhập vào không hợp lí lắm')
    n_W3A12 = int(input('Nhập lại số năm: '))
    
if (n_W3A12 % 4 == 0 and n_W3A12 % 100 != 0):
    print('Yes')
else:
    print('No')
        
print('\n')

# W3A14
print('W3A14')

a_W3A14 = float(input('Nhập vào số thực a: '))
b_W3A14 = float(input('Nhập vào số thực b: '))

def Giai_Phuong_Trinh (a, b):
    if a == 0:
        if b == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -b / a
        print('Phương trình có nghiệm:', x)
    
Giai_Phuong_Trinh(a_W3A14, b_W3A14)
        
print('\n')

# W3A15
print('W3A15')

D_W3A15 = float(input('Nhập vào số điểm trung bình: '))

while(D_W3A15 < 0 or D_W3A15 > 10):
    print('Điểm không hoẹp lí cho lắm')
    D_W3A15 = float(input('Nhập vào lại số điểm trung bình: '))
    
if (D_W3A15 >= 8):
    print('Học sinh đạt học lực giỏi')
elif (D_W3A15 >= 6.5):
    print('Học sinh đạt học lực khá')
elif (D_W3A15 >= 5):
    print('Học sinh đạt học lực trung bình')
else:
    print('Học sinh đạt học lực yếu')
    
        
print('\n')

# W3A16
print('W3A16')

n_W3A16 = float(input('Nhập vào một số thực: '))

Tron_Xuong = int(n_W3A16)

if (n_W3A16 == Tron_Xuong):
    Tron_Len = Tron_Xuong
else:
    Tron_Len = Tron_Xuong + 1

if (n_W3A16 - Tron_Xuong < 0.5):
    Tron_Nguyen = Tron_Xuong
else:
    Tron_Nguyen = Tron_Len

print('Kết quả theo thứ tự làm tròn lên, tròn xuống, tròn tới số nguyên gần nhất là:', Tron_Len, Tron_Xuong, Tron_Nguyen)
        
print('\n')

# W3A17
print('W3A17')

a_W3A17 = int(input('Nhập số a: '))
b_W3A17 = int(input('Nhập số b: '))
c_W3A17 = int(input('Nhập số c: '))
d_W3A17 = int(input('Nhập số d: '))

def Tim_Cap_So_Nhan (a, b, c, d):
    if (a == 0):
        print('Không phải cấp số nhân')
    else:
        if(b % a == 0):
            q = b//a
            if (c == b * q and d == c * q):
                print('Đây là cấp số nhân')
            else:
                print('Không phải cấp số nhân')
        else:
            print('Không phải cấp số nhân')
        
Tim_Cap_So_Nhan(a_W3A17, b_W3A17, c_W3A17, d_W3A17)
        
print('\n')