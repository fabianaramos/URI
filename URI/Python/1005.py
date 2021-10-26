A = float(input()) 
B = float(input())
formatedA = "{:.1f}".format(A)
formatedB = "{:.1f}".format(B)
wghtA = 3.5
wghtB = 7.5
C = (A * wghtA + B * wghtB) / (wghtA + wghtB)
print("MEDIA =" , "%.5f" % C)