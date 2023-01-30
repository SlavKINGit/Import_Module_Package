import datetime

from application.db.people import get_employees
from application.salary import calculate_salary

from faker import Faker

from rich import print as printt


fake = Faker('ru_RU')

printt(f'[bold green]Имя:[/bold green] {fake.name()}',
       f'[bold magenta]Профессия:[/bold magenta] {fake.job()}',
       f'Адрес: [i]{fake.address()}[/i]',
       f'День рождения: {fake.date_of_birth()}',
       f'Цвет волос: {fake.color_name()}',
       sep='\n')


def main():
    print(datetime.datetime.now())
    get_employees()
    calculate_salary()


if __name__ == '__main__':
    main()
