from getjson import Fun
import collections
import os
import time

data_list = {"http://headers.jsontest.com/": 'headers.txt',
             "http://ip.jsontest.com/": 'ip.txt',
             "http://time.jsontest.com/": 'date_time.txt',
             "http://validate.jsontest.com/?json=%7B%22key%22:%22value%22%7D": 'validation.txt',
             "http://echo.jsontest.com/insert-key-here/insert-value-here/key/value": 'echo.txt',
             "http://md5.jsontest.com/?text=%5Btext": 'md5.txt',
             }

data_list = collections.OrderedDict(sorted(data_list.items()))

while 1:
    for i in range(6):
        x = Fun(list(data_list.keys())[i - 1])
        x.print_json()
        x.save_to_file(list(data_list.values())[i - 1])

    time.sleep(Fun.interval)

