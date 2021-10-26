employ = input()
hours = float(input())
pay = float(input())

salary = (round(hours) * pay)
print('NUMBER = ' + str(employ))
print('SALARY = U$' , "%.2f" % salary)