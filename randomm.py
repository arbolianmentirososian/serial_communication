import os
import random
import time

random_numbers = []

while True:

    for i in range(0, 6):
        random_numb = random.uniform(8.0, 15.0)
        random_numbers.append(random_numb)

    print(random_numbers)

    with open('random_numbers.txt', 'w') as rand:
        for number in random_numbers:
            rand.write(str(number))

    random_numbers.clear()
    time.sleep(12)
