import json
import os

with open('resp.json') as f:
    data = json.load(f)

results = []

for series in data["results"][0]["series"]:
    columns = series["columns"]
    values = series["values"]
    temp_dict = dict(zip(columns, values))
    results.append(temp_dict)


for result in results:
    print('{} on port {} equals to {}'.format(result["type"], result["port"], result["value"]))


for margin in results:
    print('{}'.format(margin["value"]))

with open('values.txt', 'w') as values:
    for value in results:
        values.write(value['value'].__str__()+'\n')