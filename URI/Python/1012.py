line = input()
a, b, c = line.split()
pi = 3.14159
floatc = float(c)
triangle = float(a) * float(c) / 2
circle = pi * (floatc ** 2)
trapeze = (float(a) + float(b)) * float(c) / 2
square = float(b) * float(b)
rectangle = float(a) * float(b)


print('TRIANGULO:' , '%.3f' % triangle)
print('CIRCULO:' , '%.3f' % circle)
print('TRAPEZIO:' , '%.3f' % trapeze)
print('QUADRADO:' , '%.3f' % square)
print('RETANGULO:' , '%.3f' % rectangle)