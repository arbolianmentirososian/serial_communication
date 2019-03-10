import datetime
import os
import time
import collections

path = '/home/mateo/PycharmProjects/untitled3/venv/learning/results'
list_of_files = ('headers.txt', 'ip.txt', 'date_time.txt', 'validation.txt', 'echo.txt', 'md5.txt')
result_file = 'times.txt'

counter = 1
delta = 0

with open(result_file, 'w') as file:
    file.truncate(0)

while True:

    with open('times.txt', 'a') as results:
        results.write('This is the {} measurement.\n\t'.format(counter))

    for i in range(6):
        modification_time = os.path.getmtime(path + '/{}'.format(list_of_files[i]))
        print(modification_time)
        dt = datetime.datetime.fromtimestamp(modification_time)
        now = datetime.datetime.now()
        delta = (now - dt).seconds

        if delta > 10:
            with open(result_file, 'a') as results:
                results.write('File: {} was modified : {} seconds ago\n\t'.format(list_of_files[i], delta))

    with open(result_file, 'a') as f:
        f.write('\r')

    delta = 0
    counter += 1
    time.sleep(10)