line = input()
a , b , c = line.split()
higherab = (int(a) + int(b) + abs(int(a) - int(b))) / 2
higherabc = (int(higherab) + int(c) + abs(int(higherab) - int(c))) / 2
print(round(higherabc) , 'eh o maior')