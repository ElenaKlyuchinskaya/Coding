c = [5, 17, 26, 42, 77, 90, 121, 233]

a = c
x = int(input())
while len(a) != 1:
    f = (len(a)//2)
    if x == a[f]:
        print('Belongs')
        break
    elif x > a[f]:
        del a[:f]
        print(a)
    else:
        del a[f:]
        print(a)

if x != a[0]:
    print('Do not belong')