user_name = input('Введите ваше имя\n>>>')
user_age = input('Введите Ваш возраст\n>>> ')

if user_age.isdigit():
    user_age = int(user_age)
else:
    print(user_name, 'Ошибка ввода возраста, вводите число')
    exit()
sys_message = f'Пользователь {user_name}\nвозрасте {user_age} лет \nвошел в систему'
print(sys_message)

if user_age >= 18:
    print('Доступ разрешен в XXX')
elif user_age >= 16:
    print('Доступ к боевикам')
else:
    print('Ограниченный доступ')

print('Отсчет возраста')

temp_age = user_age
while temp_age > 0:
    if not temp_age & 1:
        temp_age -= 1
        continue
    print(temp_age)
    if temp_age == 15:
        break
    temp_age = temp_age - 1
    temp_age -= 1
else:
    print('Сработал else цикла')
