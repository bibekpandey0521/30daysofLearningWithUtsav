import json 
tasks = [
    {"task":"Complete Project","status":"Incomplete"}
]

with open('tasks.json','w') as file:
    json.dump(tasks,file,indent=2)