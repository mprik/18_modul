prace = 0
tickets = int(input("Введите количество билетов:\n"))
for age in range(tickets):
    age = int(input("Введите возраст посетителя:\n"))
    if age < 18:
        prace += 0
    elif 18 <= age <= 25:
        prace += 990
    elif age > 25:
        prace += 1390
if prace == 0:
    print("Вход бесплатный!")
else:
    print("Количество билетов:", tickets, "шт.")

if tickets <= 3:
    print("К оплате:", prace, "руб.")

if tickets > 3:
    sale = prace / 100 * 10
    print("Скидка 10%:", sale, "руб.")
    print("К оплате с учетом скидки:", (prace - sale), "руб.")
