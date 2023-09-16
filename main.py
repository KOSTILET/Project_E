
def menu():
    print('1. Сумма''\n' '2. Умножение' '\n' '3. Деление' '\n' '4. Разность' '\n' )
    l = int(input())
    if l == 1:
        buton1()
    elif l == 2:
        buton2()
    elif l == 3:
        buton3()
    elif l == 4:
        buton4()
    else:
        print("Ошибка, введите нужное число!")
        menu()

def buton1():
    but1 = input('Сколько будет чисел ?' + '\n')

    if int(but1) == 2:
        i = int(input("Введите первое число:"))
        j = int(input("Введите второе число:"))
        print(i + j)
        print()
        p = input("Вернуться в меню ?" + '\n').upper()
        if p == "ДА":
            menu()
        elif p == "НЕТ":
            print('Спасибо за визит,'+ a + '\n' + 'до свидания !')
        else:
            print("Ошибка!")

    elif int(but1) == 3:
        i = int(input("Введите первое число:"))
        j = int(input("Введите второе число:"))
        k = int(input("Введите третье число:"))
        print(i + j + k)
        print()
        p = input("Вернуться в меню ?" + '\n').upper()
        if p == "ДА":
            menu()
        elif p == "НЕТ":
            print('Спасибо за визит,'+ a + '\n' + 'до свидания !')
        else:
            print("Ошибка!")

    elif int(but1) == 4:
        i = int(input("Введите первое число:"))
        j = int(input("Введите второе число:"))
        k = int(input("Введите третье число:"))
        m = int(input("Введите четвертое число:"))
        print(i + j+ k + m)
        print()
        p = input("Вернуться в меню ?" + '\n').upper()
        if p == "ДА":
            menu()
        elif p == "НЕТ":
            print('Спасибо за визит,'+ a + '\n' + 'до свидания !')
        else:
            print("Ошибка!")

    elif int(but1) == 5:
        i = int(input("Введите первое число:"))
        j = int(input("Введите второе число:"))
        k = int(input("Введите третье число:"))
        m = int(input("Введите четвертое число:"))
        n = int(input("Введите пятое число:"))
        print(i + j+ k + m + n)
        print()
        p = input("Вернуться в меню ?" + '\n').upper()
        if p == "ДА":
            menu()
        elif p == "НЕТ":
            print('Спасибо за визит,'+ a + '\n' + 'до свидания !')
        else:
            print("Ошибка!")

    else:
        print("Ошибка в 1")

def buton2():
    but2 = input('Сколько будет чисел ?' + '\n')

    if int(but2) == 2:
        i = int(input("Введите первое число:"))
        j = int(input("Введите второе число:"))
        print(i * j)
        print()
        p = input("Вернуться в меню ?" + '\n').upper()
        if p == "ДА":
            menu()
        elif p == "НЕТ":
            print('Спасибо за визит,'+ a + '\n' + 'до свидания !')
        else:
            print("Ошибка!")

    elif int(but2) == 3:
        i = int(input("Введите первое число:"))
        j = int(input("Введите второе число:"))
        k = int(input("Введите третье число:"))
        print(i * j * k)
        print()
        p = input("Вернуться в меню ?" + '\n').upper()
        if p == "ДА":
            menu()
        elif p == "НЕТ":
            print('Спасибо за визит,'+ a + '\n' + 'до свидания !')
        else:
            print("Ошибка!")

    elif int(but2) == 4:
        i = int(input("Введите первое число:"))
        j = int(input("Введите второе число:"))
        k = int(input("Введите третье число:"))
        m = int(input("Введите четвертое число:"))
        print(i * j * k * m)
        print()
        p = input("Вернуться в меню ?" + '\n').upper()
        if p == "ДА":
            menu()
        elif p == "НЕТ":
            print('Спасибо за визит,'+ a + '\n' + 'до свидания !')
        else:
            print("Ошибка!")

    elif int(but2) == 5:
        i = int(input("Введите первое число:"))
        j = int(input("Введите второе число:"))
        k = int(input("Введите третье число:"))
        m = int(input("Введите четвертое число:"))
        n = int(input("Введите пятое число:"))
        print(i * j * k * m * n)
        print()
        p = input("Вернуться в меню ?" + '\n').upper()
        if p == "ДА":
            menu()
        elif p == "НЕТ":
            print('Спасибо за визит,'+ a + '\n' + 'до свидания !')
        else:
            print("Ошибка!")

    else:
        print("Ошибка в 2")

def buton3():
    but3 = input('Сколько будет чисел ?' + '\n')

    if int(but3) == 2:
        i = int(input("Введите первое число:"))
        j = int(input("Введите второе число:"))
        print(i // j)
        print()
        p = input("Вернуться в меню ?" + '\n').upper()
        if p == "ДА":
            menu()
        elif p == "НЕТ":
            print('Спасибо за визит,'+ a + '\n' + 'до свидания !')
        else:
            print("Ошибка!")

    elif int(but3) == 3:
        i = int(input("Введите первое число:"))
        j = int(input("Введите второе число:"))
        k = int(input("Введите третье число:"))
        print(i // j // k)
        print()
        p = input("Вернуться в меню ?" + '\n').upper()
        if p == "ДА":
            menu()
        elif p == "НЕТ":
            print('Спасибо за визит,'+ a + '\n' + 'до свидания !')
        else:
            print("Ошибка!")

    elif int(but3) == 4:
        i = int(input("Введите первое число:"))
        j = int(input("Введите второе число:"))
        k = int(input("Введите третье число:"))
        m = int(input("Введите четвертое число:"))
        print(i // j // k // m)
        print()
        p = input("Вернуться в меню ?" + '\n').upper()
        if p == "ДА":
            menu()
        elif p == "НЕТ":
            print('Спасибо за визит,'+ a + '\n' + 'до свидания !')
        else:
            print("Ошибка!")

    elif int(but3) == 5:
        i = int(input("Введите первое число:"))
        j = int(input("Введите второе число:"))
        k = int(input("Введите третье число:"))
        m = int(input("Введите четвертое число:"))
        n = int(input("Введите пятое число:"))
        print(i // j // k // m // n)
        print()
        p = input("Вернуться в меню ?" + '\n').upper()
        if p == "ДА":
            menu()
        elif p == "НЕТ":
            print('Спасибо за визит,'+ a + '\n' + 'до свидания !')
        else:
            print("Ошибка!")

    else:
        print("Ошибка в 3")

def buton4():
    but4 = input('Сколько будет чисел ?' + '\n')

    if int(but4) == 2:
        i = int(input("Введите первое число:"))
        j = int(input("Введите второе число:"))
        print(i - j)
        print()
        p = input("Вернуться в меню ?" + '\n').upper()
        if p == "ДА":
            menu()
        elif p == "НЕТ":
            print('Спасибо за визит,'+ a + '\n' + 'до свидания !')
        else:
            print("Ошибка!")

    elif int(but4) == 3:
        i = int(input("Введите первое число:"))
        j = int(input("Введите второе число:"))
        k = int(input("Введите третье число:"))
        print(i - j - k)
        print()
        p = input("Вернуться в меню ?" + '\n').upper()
        if p == "ДА":
            menu()
        elif p == "НЕТ":
            print('Спасибо за визит,'+ a + '\n' + 'до свидания !')
        else:
            print("Ошибка!")

    elif int(but4) == 4:
        i = int(input("Введите первое число:"))
        j = int(input("Введите второе число:"))
        k = int(input("Введите третье число:"))
        m = int(input("Введите четвертое число:"))
        print(i - j - k - m)
        print()
        p = input("Вернуться в меню ?" + '\n').upper()
        if p == "ДА":
            menu()
        elif p == "НЕТ":
            print('Спасибо за визит,'+ a + '\n' + 'до свидания !')
        else:
            print("Ошибка!")

    elif int(but4) == 5:
        i = int(input("Введите первое число:"))
        j = int(input("Введите второе число:"))
        k = int(input("Введите третье число:"))
        m = int(input("Введите четвертое число:"))
        n = int(input("Введите пятое число:"))
        print(i - j - k - m - n)
        print()
        p = input("Вернуться в меню ?" + '\n').upper()
        if p == "ДА":
            menu()
        elif p == "НЕТ":
            print('Спасибо за визит,'+ a + '\n' + 'до свидания !')
        else:
            print("Ошибка!")

    else:
        print("Ошибка в 4")

a = input('Введите свое имя: ')
print()
print("Здравствуйте,", a + "\n" + "Я ваш персональный бот 'Аркадий'")
print()
b = input('Чем я могу вам помочь ?' + '\n').upper()
if b == "ХОЧУ КАЛЬКУЛЯТОР":
    menu()