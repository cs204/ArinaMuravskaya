food_calories = {
    "Apple": "Калории: 130",
    "Lime": "Калории: 20",
    "Avocado": "Калории: 50"}
user_input = input("Фрукт: ")
print(food_calories.get(user_input, ""))
if user_input not in food_calories:
    print("")