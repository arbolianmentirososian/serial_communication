import json
from urllib.request import urlopen

with urlopen("http://headers.jsontest.com/") as response:
    header = response.read()
with urlopen("http://ip.jsontest.com/") as response2:
    ip = response2.read()
with urlopen("http://time.jsontest.com/") as response3:
    date_time = response3.read()
with urlopen("http://validate.jsontest.com/?json=%7B%22key%22:%22value%22%7D") as response4:
    validation = response4.read()
with urlopen("http://echo.jsontest.com/insert-key-here/insert-value-here/key/value") as response5:
    echo = response5.read()
with urlopen("http://md5.jsontest.com/?text=%5Btext") as response6:
    md5 = response6.read()

data = json.loads(header.decode('utf-8'))
print(json.dumps(data, indent=2))
print('####################################################################')
data2 = json.loads(ip.decode('utf-8'))
print(json.dumps(data2, indent=2))
print('####################################################################')
data3 = json.loads(date_time.decode('utf-8'))
print(json.dumps(data3, indent=2))
print('####################################################################')
data4 = json.loads(validation.decode('utf-8'))
print(json.dumps(data4, indent=2))
print('####################################################################')
data5 = json.loads(echo.decode('utf-8'))
print(json.dumps(data5, indent=2))
print('####################################################################')
data6 = json.loads(md5.decode('utf-8'))
print(json.dumps(data6, indent=2))
print('####################################################################')

with open('header.txt', 'w') as hfile:
    hfile.write(json.dumps(data, indent=2))
with open('ip.txt', 'w') as ifile:
    ifile.write(json.dumps(data2, indent=2))
with open('date_time.txt', 'w') as dtfile:
    dtfile.write(json.dumps(data3, indent=2))
with open('validation.txt', 'w') as vfile:
    vfile.write(json.dumps(data4, indent=2))
with open('echo.txt', 'w') as efile:
    efile.write(json.dumps(data5, indent=2))
with open('md5.txt', 'w') as mfile:
    mfile.write(json.dumps(data6, indent=2))

