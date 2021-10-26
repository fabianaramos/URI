line = input()
code, quantity, value = line.split()
total = int(quantity) * float(value)

line2 = input()
code2, quantity2, value2 = line2.split()
total2 = int(quantity2) * float(value2)

topay = total + total2

print('VALOR A PAGAR: R$' , "%.2f" % topay)