def RhythmOnVowels(string):
    string = string.split()
    list = []
    for word in string:
        result = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                result += 1
        list.append(result)
    return len(list) == list.count(list[0])
string = input('Введите стихотворение Винни-Пуха: ')
if RhythmOnVowels(string):
    print('Парам пам-пам')
else:
    print('Пам парам')