from datetime import datetime
from threading import Thread
from time import sleep


def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1} \n')
            sleep(0.1)
    return print(f'Завершилась запись в файл {file_name}')


time1_start = datetime.now()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
time1_end = datetime.now()
time1_res = time1_end - time1_start
print(f'Работа потоков: {time1_res}')


time2_start = datetime.now()
flow1 = Thread(target=wite_words, args=(10, 'example5.txt'))
flow2 = Thread(target=wite_words, args=(30, 'example6.txt'))
flow3 = Thread(target=wite_words, args=(200, 'example7.txt'))
flow4 = Thread(target=wite_words, args=(100, 'example8.txt'))

flow1.start()
flow2.start()
flow3.start()
flow4.start()

flow1.join()
flow2.join()
flow3.join()
flow4.join()

time2_end = datetime.now()
time2_res = time2_end - time2_start
print(f'Работа потоков: {time2_res}')
