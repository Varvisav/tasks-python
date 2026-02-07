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

def remove_task(wich_task: int):
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

def show_tasks(which_tasks):
	print("\ntwoje zadania:\n")
	if which_tasks == 0:
		print(tasks)
	elif which_tasks == 1 :
		for task in tasks:
			if task["done "] == False:
				print(task)
	elif which_tasks == 2:
		for task in tasks:
			if task["done "] == True:
				print(task)
		