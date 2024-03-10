# Функція get_birthdays_per_week, яка отримує на вхід список users і виводить у консоль (за допомогою print) список користувачів, яких потрібно привітати по днях на наступному тижні.
from typing import Any
from datetime import datetime

testusers = [
    {"name": "Bill Gates", "birthday": datetime(1955, 3, 14)},
    {"name": "Elon Musk", "birthday": datetime(1971, 6, 28)},
    {"name": "Mark Zuckerberg", "birthday": datetime(1984, 3, 14)},
    {"name": "Jeff Bezos", "birthday": datetime(1964, 3, 13)},
    {"name": "Tim Cook", "birthday": datetime(1960, 11, 1)},
    {"name": "Satya Nadella", "birthday": datetime(1967, 8, 19)},
    {"name": "Larry Page", "birthday": datetime(1973, 3, 16)},
    {"name": "Sundar Pichai", "birthday": datetime(1972, 6, 10)},
    {"name": "Jack Dorsey", "birthday": datetime(1976, 3, 12)},
    {"name": "Reed Hastings", "birthday": datetime(1960, 10, 8)}
]


def get_birthdays_per_week(users: list[dict[str, Any]]) -> None:
    today = datetime.today().date()
    output: dict[str, list[str]] = {}
    users.sort(key=lambda x: (x['birthday'].month, x['birthday'].day))

    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        next_birthday = birthday.replace(year=today.year)
        if next_birthday < today:
            next_birthday = birthday.replace(year=today.year + 1)

        delta_days = (next_birthday - today).days
        if delta_days < 7:
            day = next_birthday.strftime("%A")
            day = 'Monday' if day in ('Saturday', 'Sunday') else day

            if not output.get(day):
                output[day] = []

            output[day].append(name)

    print("Next birthdays:\n")
    for day, users in output.items():
        print(f"{day}: {', '.join(users)}")


get_birthdays_per_week(testusers)
