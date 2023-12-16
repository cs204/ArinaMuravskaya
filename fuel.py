def calculate_fuel_percentage():
    while True:
        try:
            fraction = input("Дробь: ")
            x, y = map(int, fraction.split('/'))

            if y == 0 or x < 0 or y < 0 or x > y:
                print("Некорректные входные данные. Попробуйте снова.")
                continue

            percentage = round(x / y * 100)

            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")

            break
        except ValueError:
            print("Некорректный формат. Попробуйте снова.")
        except ZeroDivisionError:
            print("Знаменатель не может быть равен нулю. Попробуйте снова.")

calculate_fuel_percentage()
