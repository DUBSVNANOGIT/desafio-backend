import requests
response = requests.get("https://jsonplaceholder.typicode.com/todos")
result = response.json()
def func(result):
    countCompleted = 0;
    countPending = 0
    for i in result:
        if i['completed'] == True:
            countCompleted += 1
        else:
            countPending += 1
    return countCompleted, countPending
completed, pending = func(result)
print(completed, pending)
