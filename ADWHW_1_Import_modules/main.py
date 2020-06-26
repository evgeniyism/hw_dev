from Advanced.ADWHW_1_Import_modules.application import salary
from Advanced.ADWHW_1_Import_modules.db import people
import datetime

if __name__ == '__main__':
    print(f'Today is {datetime.date.today()}')
    people.get_employees()
    salary.calculate_salary()