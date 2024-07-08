team1_name = '"Мастера кода"'
team1_num = 6
score_1 = 40
team1_time = 1552.512

team2_name = '"Волшебники данных"'
team2_num = 6
score_2 = 42
team2_time = 2153.31451

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

print('\nВ команде %s участников: %s !' % (team1_name, team1_num))
print('В команде %s участников: %s !' % (team2_name, team2_num))
print('\nИтого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))

print('\n{} кода решила задач: {} !'.format(team1_name, score_1))
print('{} данных решила задач: {} !'.format(team2_name, score_2))

print('\n{} решили задачи за {} с'.format(team1_name, team1_time))
print('{} решили задачи за {} с'.format(team2_name, team2_time))

print(f'\nКоманды решили {score_1} и {score_2} задач.')


def challenge_result():
    if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
        result = f'Победа команды {team1_name}!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
        result = f'Победа команды {team2_name}!'
    else:
        result = 'Ничья!'
    return result


print(f'\nРезультат битвы: {challenge_result()}')

print(f'\nСегодня было решено {tasks_total} задач, в среднем по {int(time_avg)} секунды на задачу!.')
