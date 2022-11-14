import json
with open('snakes.json', 'r') as json_file:
    json_data = json.load(json_file)

for key, value in json_data.items():
    print(key + ':', value)

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])

#print values from json_data
for k in json_data.keys(): 
    print(json_data[k])