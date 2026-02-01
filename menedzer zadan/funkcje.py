#from dane import tasks
from datetime import date
import json
import os
tasks = [
{
"title ": "Nauczyc sie Pythona ",
"done ": False ,
"due_date ": " 2026 -01 -20 "
}
]


def add_new_task(title: str, due_date: date | None = None):
	tasks.append({"title ": title, "done ": False, "due_date": due_date})

def remove_task(wich_task):
	tasks.remove(tasks[wich_task])

def mark_task_done(which_task: int):
	tasks[which_task]["done "] = True

def save_tasks():
	with open ("tasks.json", "w") as f:
	    json.dump (tasks, f, indent = 4)

def load_tasks():

    if os.path.exists ("tasks.json"):
        with open ("tasks.json", "r") as f:
            tasks = json.load(f)
    else:
        tasks = []

def show_tasks():
	print("\nYour tasks:\n")
	print(tasks)
