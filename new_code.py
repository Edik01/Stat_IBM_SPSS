import random

def guess_number():
    number = random.randint(1, 100)
    print("Я загадал число от 1 до 100. Попробуй угадать!")
    attempts = 0
    while True:
        try:
            guess = int(input("Твой вариант: "))
            attempts += 1
            if guess < number:
                print("Больше!")
            elif guess > number:
                print("Меньше!")
            else:
                print(f"Правильно! Ты угадал число за {attempts} попыток.")
                break
        except ValueError:
            print("Пожалуйста, введи целое число.")

if __name__ == "__main__":
    tarot_cards = [
        "Шут", "Маг", "Верховная Жрица", "Императрица", "Император", "Иерофант",
        "Влюбленные", "Колесница", "Сила", "Отшельник", "Колесо Фортуны", "Справедливость",
        "Повешенный", "Смерть", "Умеренность", "Дьявол", "Башня", "Звезда", "Луна", "Солнце",
        "Суд", "Мир"
    ]
    card = random.choice(tarot_cards)
    print("Я вытянул для тебя карту Таро...")
    print(f"Твоя карта: {card}")