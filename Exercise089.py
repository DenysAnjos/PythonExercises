# Crie um programa que leia nome e duas notas de vários alunos
# e guarde tudo em uma lista composta. no final, mostre um
# boletim contendo a média de cada um e permita que o usuário
# possa mostrar as notas de cada aluno individualmente.
from time import sleep

names = list()
grades = list()
all = list()

totalStudents = count = 0
while True:
    n = str(input('Name:'))
    names.append(n)
    all.append(names)
    note1 = float(input('Grade 1:'))
    grades.append(note1)
    note2 = float(input('Grade 2:'))
    grades.append(note2)
    all.append(grades[:])
    totalStudents += 1

    check = str(input('Do you want continue?(y/n) '))
    if check in 'nN':
        break
print(f'N°   NAME    AVERAGE')
for a in range(0, totalStudents):
    print(f'{a}    {names[a]}   {(grades[a+a]+grades[a+a+1])/2}')
    sleep(0.5)

while True:
    check = int(input('Do you wanna show grades of which student? (999 to stop):'))
    if check != 999:
        print(f'The grades of {names[check+check]} is {all[check+check]}')
    else:
        break
