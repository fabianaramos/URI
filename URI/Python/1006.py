gradeA= input()
gradeB = input()
gradeC = input()

wghtA = 2
wghtB = 3
wghtC = 5

mean = (gradeA * wghtA + gradeB * wghtB + gradeC * wghtC) / (wghtA + wghtB + wghtC)
realMean = float(mean)
real = "{:.1f}".format(realMean)

print('MEDIA = ' + str(real))