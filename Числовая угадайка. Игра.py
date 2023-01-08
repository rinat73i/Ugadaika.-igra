import random
num = random.randint(1,100)
print("Добро пожаловать в игру!")
print("Правила игры:")
print("Необходимо угадать загаданное число! Удачи!")

#проверка введенного значения
def is_valid(num):
    if num.isdigit() and 1 <= int(num) <= 100:
        return True
    else:
        return False

#основной цикл программы
count = 0 #подсчет количества попыток
while True:    
    your_number = input("Введите ваше число:")
    
    if is_valid(your_number) == False:
        print("Введите пожалуйста числовое значение!")
        continue
    else:
        number = int(your_number)      
            
#сравнение загаданного числа с введенным числом
   
    if number < num:
        print("Ваше число меньше загаданного! Попробуйте еще раз")
        count += 1
        continue
    elif number > num:
        print("Ваше число больше загаданного! Попробуйте еще раз")
        count += 1
        continue
    else:
        count += 1
        print("Поздравляем! Вы угадали c", count,"попытки")
    print("Хотите продолжить? Напишите 'Да' или 'Нет'")
    answer = input()
    if answer.lower() == "да":
        num = random.randint(1,100)
        count = 0
        continue
    else:
        print("Спасибо за игру!")
        break