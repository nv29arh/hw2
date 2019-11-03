"Блок 1880 г"
"Пушкин 1799 г"
"Маяковский 1893 г"
"Ахматова 1889 г"
"Есенин 1895 г"

while True:
    year_born_block = int(input('Введите год рождения Блока'))
    if year_born_block == 1880:
        year_born_block = 1;
    else:
        year_born_block = 0


    year_born_pushkin = int(input('Введите год рождения Пушкина'))
    if year_born_pushkin == 1799:
        year_born_pushkin = 1;
    else:
        year_born_pushkin = 0


    year_born_mayakovskiy = int(input('Введите год рождения Маяковского'))
    if year_born_mayakovskiy == 1893:
        year_born_mayakovskiy = 1;
    else:
        year_born_mayakovskiy = 0


    year_born_akhmatova = int(input('Введите год рождения Ахматовой'))
    if year_born_akhmatova == 1889:
        year_born_akhmatova = 1;
    else:
        year_born_akhmatova = 0


    year_born_esenin = int(input('Введите год рождения Есенина'))
    if year_born_esenin == 1895:
        year_born_esenin = 1;
    else:
        year_born_esenin = 0

    correct_answers = int(year_born_block + year_born_pushkin + year_born_mayakovskiy + year_born_akhmatova + year_born_esenin)
    print('Количество правильных ответов', '=', correct_answers)

    uncorrect_answers = int(5 - correct_answers)
    print('Количество неправильных ответов', '=', uncorrect_answers)
    percent_of_correct_ancwers = float(correct_answers*100/5)
    print ('Процент правильных ответов =', percent_of_correct_ancwers)
    percent_of_uncorrect_answers = 100 - percent_of_correct_ancwers
    print ('Процент неправильных ответов =', percent_of_uncorrect_answers)
    cont = input('Желаете ли вы начать сначала? да/нет')
    if cont == 'нет':
        break
print('end')