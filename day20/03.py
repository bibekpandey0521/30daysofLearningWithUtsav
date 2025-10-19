import json
with open('tasks.json','r') as file:
    tasks = json.load(file)
tasks.append({"task":"Learn Python","status":"Incomplete"})

with open('tasks.json','w') as file:
    json.dump(tasks,file,indent=2)
    