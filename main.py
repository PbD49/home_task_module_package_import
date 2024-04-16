import application.salary as salary
import application.db.people as people
from datetime import datetime
from app import main


if __name__ == '__main__':
    current_datetime = datetime.now()
    formatted_date = current_datetime.strftime("Сегодня %d-%m-%Y; Время: %H:%M:%S")
    print(formatted_date)
    salary.calculate_salary()
    people.get_employees()
    main()
