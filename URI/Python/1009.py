name = str(input())
salary = float(input())
sales = float(input())
perCent = 0.15

comission = sales * perCent
payment = salary + comission

print("TOTAL = R$" , "%.2f" % payment)