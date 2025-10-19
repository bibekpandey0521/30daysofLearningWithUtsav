import json

with open('json_data','r') as file:
    tasks = json.load(file)
    print(tasks)

