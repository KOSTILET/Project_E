
def profile():
    # Создаем пустой словарь для профиля
    profile = {}

    # Запрашиваем у пользователя информацию о профиле
    profile["имя"] = input("Введите ваше имя: ")
    profile["возраст"] = input("Введите ваш возраст: ")
    profile["город"] = input("Введите ваш город: ")
    profile["email"] = input("Введите ваш email: ")

    # Выводим информацию о профиле
    print("\nВаш профиль:")
    print("Имя:", profile["имя"])
    print("Возраст:", profile["возраст"])
    print("Город:", profile["город"])
    print("Email:", profile["email"])
    lvl()

def lvl():
    print()
    print('Выбирите уровень подготовки:')
    print('1. Стажер'+'\n'+'2. Джуниер'+'\n'+'3. Мидл'+'\n'+'4. Серьер')
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
        print('Ошибка кнопок')
def buton1():
    print("Кнопка 1")

def buton2():
    print("Кнопка 2")

def buton3():
    print("Кнопка 3")

def buton4():
    print("Кнопка 4")

def privetctvie():
    B = print('Если хотите зарегистриваться напишите на цифру - 1.' + '\n' + 'Если не хотите нажмине на цифру - 2.')
    C = int(input())
    if C == 1:
        profile()
    elif C == 2:
        print('Спасибо, до свидания!' + '\n' + 'Хорошего дня!')
    else:
        privetctvie()

a = print('Здравствуйте, вы попали на онлайн курс, Python'+'\n'+'Здесь вы научить многому новому, нужно неного просто усилий)'+'\n'+'Но для начала нужно зарегистриваться')
b = print('Если хотите зарегистриваться напишите на цифру - 1.'+'\n'+'Если не хотите нажмине на цифру - 2.')
c = int(input())
if c == 1:
    profile()
elif c == 2:
    print('Спасибо, до свидания!'+'\n'+'Хорошего дня!')
else:
    privetctvie()

