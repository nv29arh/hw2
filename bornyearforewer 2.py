while True:
    born = int(input('Год рождения Пушкина '))
    while born != 1799:
        print('Неверно!')
        born = int(input ('Год рождения Пушкина '))
    break

print ('Верно!')
print ('end')