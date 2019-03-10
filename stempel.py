import datetime
import os
import time

while True:

    modification_time = os.path.getmtime('random_numbers.txt')      #wczytanie daty modyfikacji pliku z wartosciami Marginu
    dt = datetime.datetime.fromtimestamp(modification_time) #konwersja na stempel czasowy daty modyfikacji tego pliku
    now = datetime.datetime.now()                           #stempel czasowy chwili obecnej
    print(now - dt)                                         #info dla mnie o wartosci na biezaco
    delta = (now - dt).seconds                              #roznica miedzy modyfikacja pliku a obecna chwila w sekundach
    if delta > 10:                                          #jesli roznica jest wieksza niz 10s
        with open('times.txt', 'a') as results:             #otworzenie i dopisanie do pliku roznicy czasu
            results.write('Modification time was: {} seconds ago\n'.format(delta))

    with open('values.txt', 'r') as f:                      #dodanie czegokolwiek do pliku z wartosciami Marginu
        pass
    delta = 0
    time.sleep(1)





