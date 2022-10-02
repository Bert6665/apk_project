#! python3
from datetime import datetime


def norm_hour(days=datetime.now().day, month=datetime.now().month, year=datetime.now().year) -> int:
    '''Производит расчёт нормы часов за указанный период времени'''
    norm_hour = 0
    for i in range(1, days + 1):
        weekday = datetime(year, month, i).isoweekday()
        if weekday == 6 or weekday == 7:
            continue
        norm_hour += 8
    return norm_hour


def total_days(month=datetime.now().month, year=datetime.now().year) -> int:
    '''Возвращает колличество дней в месяце'''
    this_month = datetime(year, month, 1)
    if month == 12:
        second_month = datetime(year + 1, 1, 1)
    else:
        second_month = datetime(year, month + 1, 1)
    return (second_month - this_month).days


def main():
    year = 2022
    month = 5

    print(f'Колличество дней в месяце: {total_days()}')
    print(f'Норма часов в месяце: {norm_hour(total_days())}')
    print(f'Норма часов на сегодня: {norm_hour()}')


if __name__ == "__main__":
    main()
