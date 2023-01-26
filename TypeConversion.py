import datetime

today = datetime.date.today()
year = today.year
birth_year = input('what year you were born? ')
age = year - int(birth_year)
print(f'your age is : {age}')