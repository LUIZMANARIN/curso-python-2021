x1=(float(input("valor x1?: ")))
x2=(float(input('valor x2?: ')))
x3=(float(input('valor x3?: ')))
x4=(float(input('valor x4?: ')))
x5=(float(input('valor x5?: ')))

M=(x1+x2+x3+x4+x5)/5

s2=((x1-M)**2+(x2-M)**2+(x3-M)**2+(x4-M)**2+(x5-M)**2)/4
s=(s2)**(1/2)
print('o valor de M é {} de s2 {} e de s {}'. format(M,s2,s))
