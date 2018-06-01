message = input('Enter text in Russian for encryption: ').lower()
alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
shift = int(input('Enter offset size: '))
new_mes_range = []
new_mes = ''
for i in message:
    if i not in alph:
             new_mes_range.append(i)
    else:
        new_mes_range.append(alph[alph.index(i) + shift])
for i in range(len(new_mes_range)):
    new_mes += new_mes_range[i]
print('Encrypted message: ', new_mes)