user_age: str = input('Введите Ваш возраст: ')

if user_age.isdigit():
    user_age = int(user_age)
else:
    print('Ошибка ввода возраста, вводите число')
    exit()


if user_age >= 18:
    print('Доступ разрешен в XXX')
elif user_age >= 16:
    print('Доступ к боевикам')
else:
    print('Ограниченный доступ')
