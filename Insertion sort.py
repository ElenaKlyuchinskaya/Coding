b = input('Enter a list of numbers: ').split()

for i in range(len(b)):
    j = i
    while b[j] <= b[j-1] and j > 0:
        a = b[j-1]
        b[j - 1] = b[j]
        b[j] = a
        j = j-1
        print(b)