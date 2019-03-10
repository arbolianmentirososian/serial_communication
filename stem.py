import datetime
import os
import time

modification_time = os.path.getmtime('new.json')
dt = datetime.datetime.fromtimestamp(modification_time)
now = datetime.datetime.now()
# print(modification_time)
# print(dt)
print(type(now - dt))
# with open('times.txt', 'a') as results:
#     results.write('Modification time was: {} ago\n'.format(now - dt))
# print(now - dt)
# time.sleep(1)

print(modification_time)