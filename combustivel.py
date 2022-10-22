import sys
gasolina=float(sys.argv[1])
etanol=float(sys.argv[2])
print('O argumento 1 é '+str(sys.argv[0]))
print('O argumento 2 é '+str(sys.argv[1]))
print('O argumento 3 é '+str(sys.argv[2]))
r=etanol/gasolina
if r <= 0.7:
  print('O etanol compensa mais!!')
else:
  print('A gasolina compensa mais!!')