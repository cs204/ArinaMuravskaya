number = 50
while number > 0:
    print("Нужная сумма:", number)
    user_input = int(input("Вставьте монету: "))
    if user_input in [50, 20, 10, 5]:
        if user_input >= number:
            excess = user_input - number
            print("Ваша сдача:", excess)
        number -= user_input
