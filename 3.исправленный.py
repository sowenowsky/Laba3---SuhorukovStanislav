ABC = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
word = str(input('Введите слово с маленькими буквами: ')) #слово
wordlist = list (word) #разбивает слово на список
shift = int(input('Введите желаемый сдвиг: ')) #сдвиг
k = 0
result = []
for i in ABC:
    if k > len(word) - 1:
        break
    else:
        letter = wordlist[k] #находит нужную букву
        numberletter = ABC.find(letter)  # буква в алфавите по счёту начиная с 0
        if numberletter == (-1): #исключает пробелы
            result.append('')
        else:
            result.append((ABC[(numberletter + shift)%len(ABC)])) #добавляет итоговую букву в массив
        k += 1
converresult = (' '.join(map(str,result))) #преобразование массива в строку
print ('Итоговое слово: ', converresult)


