nominal = [50, 10, 5, 1]
sum = int(input("Input number: "))
number = [0, 0, 0, 0]
count = 0

for i in range(len(nominal)):
    while int(sum) >= nominal[i]:
        sum -= nominal[i]
        number[i] += 1
    print(number[i],'coin(s)','-', nominal[i], 'nominal coins')


