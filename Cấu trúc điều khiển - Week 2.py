# Bài 1
print('Bài 1')

Chieu_Dai = float(input('Nhập chiều dài: '))
Chieu_Rong = float(input('Nhập chiều rộng: '))

Chu_Vi_HCN = (Chieu_Dai + Chieu_Rong)*2
Dien_Tich_HCN = (Chieu_Dai*Chieu_Rong)

print('Chu vi hình chữ nhật là:', Chu_Vi_HCN)
print('Diện tích hình chữ nhật là:', Dien_Tich_HCN)

print('\n')

# Bài 2
print('Bài 2')

from math import*
Ban_Kinh = float(input('Nhập bán kính hình tròn: '))

Chu_Vi_HT = Ban_Kinh*2*3.14
Dien_Tich_HT = (Ban_Kinh**2)*3.14

print('Chu vi hình tròn là:', Chu_Vi_HT)
print('Diện tích hnhf tròn là:', Dien_Tich_HT)

print('\n')

# Bài 3
print('Bài 3')

Canh_Thu_Nhat = float(input('Nhập cạnh thứ nhất của tam giác: '))
Canh_Thu_Hai = float(input('Nhập cạnh thứ hai của tam giác: '))
Canh_Thu_Ba = float(input('Nhập cạnh thứ ba của tam giác: '))

Chu_Vi_TG = Canh_Thu_Hai + Canh_Thu_Ba + Canh_Thu_Nhat

Nua_Chu_Vi_TG = (Canh_Thu_Hai + Canh_Thu_Ba + Canh_Thu_Nhat)/2

Dien_Tich_TG = sqrt(Nua_Chu_Vi_TG*(Nua_Chu_Vi_TG - Canh_Thu_Nhat)*(Nua_Chu_Vi_TG - Canh_Thu_Hai)*(Nua_Chu_Vi_TG - Canh_Thu_Ba))

if (Canh_Thu_Nhat + Canh_Thu_Hai <= Canh_Thu_Ba) | (Canh_Thu_Nhat + Canh_Thu_Ba <= Canh_Thu_Hai) | (Canh_Thu_Ba + Canh_Thu_Hai <= Canh_Thu_Nhat):
    print('Đây không phải ba cạnh của tam giác.')

else:
    if (Canh_Thu_Nhat == Canh_Thu_Hai == Canh_Thu_Ba):
        print('Đây là tam giác đều')
        print('Chu vi tam giác là:', Chu_Vi_TG)
        print('Diện tích tam giác là:', Dien_Tich_TG)

    elif (Canh_Thu_Ba == Canh_Thu_Hai) | (Canh_Thu_Ba == Canh_Thu_Nhat) | (Canh_Thu_Nhat == Canh_Thu_Hai):
        print('Đây là tam giác cân')
        print('Chu vi tam giác là:', Chu_Vi_TG)
        print('Diện tích tam giác là:', Dien_Tich_TG)
    elif (((Canh_Thu_Nhat*Canh_Thu_Hai)/2) == Dien_Tich_TG) | (((Canh_Thu_Nhat*Canh_Thu_Ba)/2) == Dien_Tich_TG) | (((Canh_Thu_Ba*Canh_Thu_Hai)/2) == Dien_Tich_TG):
        print('Đây là tam giác vuông')
        print('Chu vi tam giác là:', Chu_Vi_TG)
        print('Diện tích tam giác là:', Dien_Tich_TG)
    else:
        print('Đây là tam giác thường')
        print('Chu vi tam giác là:', Chu_Vi_TG)
        print('Diện tích tam giác là:', Dien_Tich_TG)

print('\n')

# Bài 4
print('Bài 4')

print('Phương trình có dạng ax + b = 0')
a_B4 = float(input('Nhập số a: '))
b_B4 = float(input('Nhập số b: '))

def Phuong_Trinh_Bac_Nhat (a, b):
    Ket_Qua_B4 = (-b)/a
    return Ket_Qua_B4

print('x =', Phuong_Trinh_Bac_Nhat(a_B4, b_B4))

print('\n')

# Bài 5
print('Bài 5')

print('Phương trình có dạng ax^2 + bx + c = 0')
a_B5 = float(input('Nhập số a: '))
b_B5 = float(input('Nhập số b: '))
c_B5 = float(input('Nhập số c: '))

def Phuong_Trinh_Bac_Hai (a, b, c):
    
    Delta = b**2 - 4*a*c
    
    if (Delta < 0):
        print('Phương trình vô nghiệm')
    elif (Delta == 0):
        print('Đây là phương trình bậc nhất')
        print('x =', -b/(2*a))
    else:
        print('Phương trình có 2 nghiệm')
        print('x1 =', (b + sqrt(Delta))/(2*a))
        print('x2 =', (b - sqrt(Delta))/(2*a))

if (a_B5 == 0):
    if (b_B5 == 0):
        print('Đây không phải phương trình bậc hai')
    else:
        print('Đây là phương trình bậc nhất với x =', -(c_B5)/b_B5)
else:
    Phuong_Trinh_Bac_Hai(a_B5, b_B5, c_B5)

print('\n')

# Bài 6
print('Bài 6')

print('Nhập 3 số a, b, c cùng một hàng cách nhau 1 dấu cách')
a_B6, b_B6, c_B6 = map(float, input('Nhập 3 số a, b, c: ').split())

List_B6 = []
List_B6.append(a_B6)
List_B6.append(b_B6)
List_B6.append(c_B6)

List_B6.sort()

print('Số lớn nhất là:', List_B6[-1])

print('\n')

# Bài 7
print('Bài 7')

print('Nhập 3 số a, b, c cùng một hàng cách nhau 1 dấu cách')
a_B7, b_B7, c_B7, d_B7 = map(float, input('Nhập 3 số a, b, c, d: ').split())

List_B7 = []
List_B7.append(a_B7)
List_B7.append(b_B7)
List_B7.append(c_B7)
List_B7.append(d_B7)

List_B7.sort()

print('Số nhỏ nhất là:', List_B7[0])

print('\n')

# Bài 8
print('Bài 8')

print('Phương trình có dạng: \n ax + by = m \n cx + dy = n')

a_B8 = float(input('Nhập số a: '))
b_B8 = float(input('Nhập số b: '))
c_B8 = float(input('Nhập số c: '))
d_B8 = float(input('Nhập số d: '))
m_B8 = float(input('Nhập số m: '))
n_B8 = float(input('Nhập số n: '))

# def Phuong_Trinh_Bac_Nhat_Hai_An(a, b, c, d, m, n):
    
