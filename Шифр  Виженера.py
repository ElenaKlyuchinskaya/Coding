LineMessage = ''
MassMessage = []
alphabet = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
text = input('Введите текст для шифрования: ').lower()
key = input('Введите ключ: ')
for i in text:
    if i not in alphabet:
        MassMessage.append(i)
    else:
        MassMessage.append(alphabet[(alphabet.index(i) + len(key)) % len(alphabet)])
for i in range(len(MassMessage)):
    LineMessage += MassMessage[i]
print('Зашифрованное сообщение: ', LineMessage)