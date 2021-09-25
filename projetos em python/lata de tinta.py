#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
metros2= int(input("quantos metros quadrados você deseja pintar ? "))

lata= (metros2/54)

preço= lata*80

print("a quantidade de lata de tinta a ser comprada é",lata ,"litos e o preço a ser cobrado é", preço ,"R$" )
