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

