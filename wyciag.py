import json

with open('resp.json') as response:
    data = json.load(response)

#print(json.dumps(data, indent=2))

# print(json.dumps(data['results'], indent=2))


print(json.dumps(data['results'][0]['series'], indent=2))

print(type(json.dumps(data['results'][0]['series'])))