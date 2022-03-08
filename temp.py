import json
array = []
for i in range(10000, -1, -1):
    array.append(i)
with open('mergeLarge.json', 'w') as file:
        json.dump(array, file)
