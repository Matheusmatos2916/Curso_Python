maior = men = woman = 0
conti = ' '
while conti not in 'N':
    age = int(input('Qual é a sua idade? '))
    gender = ' '
    while gender not in 'MFNB':
        gender = str(input('Qual é o seu gênero? [M/F/NB = não binário] ')).upper().strip()

    conti = ' '
    while conti not in 'YN':
        conti = str(input('Deseja continuar? [Y/N] ')).split()[0].upper()

    if age > 18:
        maior += 1
    if gender == 'M':
        men += 1
    elif gender == 'F' and age < 20:
        woman += 1

print(f'{maior} pessoas são maiores de 18 anos, \n{men} homens foram cadastrados e \n{woman} mulheres/meninas têm menos de 20 anos')