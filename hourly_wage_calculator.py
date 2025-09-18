
def monthly_salary(annual_salary):
    return annual_salary / 12

def weekly_salary(monthly_salary):
    return monthly_salary / 4

def hourly_salary(weekly_salary, hours_work):
    return weekly_salary / hours_work

annual_salary = float(input("Enter your annual salary : "))
hours_work = float(input("Enter your number of hours worked by week : "))

month_salary = monthly_salary(annual_salary)
week_salary = weekly_salary(month_salary)
hour_salary = hourly_salary(week_salary, hours_work)

print("Your hourly salary is ", hour_salary, " euros")