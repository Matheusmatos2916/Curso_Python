##Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. 
N = str(input("Digite seu nome completo:")).strip()
Nome = N.split()
print("Muito prazer em te conhecer!")
print("Seu primeiro nome é {}".format(Nome[0]))
print("Seu último nome é {}".format(Nome[len(Nome)-1]))