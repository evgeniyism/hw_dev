import datetime
from Advanced.ADWHW_1_Import_modules.application.salary import *
from Advanced.ADWHW_1_Import_modules.db.people import *

if __name__ == '__main__':
    print(f'Today is {datetime.date.today()}')
    get_employees()
    calculate_salary()