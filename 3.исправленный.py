ABC = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
try:
            word = str(input('Введите слово с маленькими буквами: ')) #слово
            return b
        except ValueError:
            print("Нужно ввести букву")

wordlist = list (word) #разбивает слово на список
try:
            shift = int(input('Введите желаемый сдвиг: ')) #сдвиг
            return b
        except ValueError:
            print("Нужно ввести цифру")

k = 0
result = [] #создаем массив результатов
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


