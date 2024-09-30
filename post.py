from textwrap import indent

from requests import post, Response
from json import dumps

API_URL = "https://jsonplaceholder.typicode.com/todos"

id = input("Introduce tu id: ")
title = input("Introduce tu tarea: ")
completed = input("Tarea completa? Y/n: ") == "y" 

todo = {
    "userID": id,
    "title": title,
    "completed": completed
}

response = post(API_URL, json=todo)
print(dumps(response.json(), indent=4), "\n")

print(response.status_code)