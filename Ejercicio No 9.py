date_of_birth = input("Enter your date of birth in dd/mm/yyyy : ")
day, month, year = date_of_birth.split('/')

day = day.zfill(2)
month = month.zfill(2)

print(f"Day: {day}")
print(f"Month: {month}")
print(f"Year: {year}")