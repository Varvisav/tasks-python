
#from dane import tasks
from funkcje import show_tasks, add_new_task, remove_task, mark_task_done, save_tasks, load_tasks, tasks
import json
from datetime import date
import os



if __name__ == "__main__":
	while True:
		print("chose what do you want to do:")
		print("[0] show the task list")
		print("[1] add a new task")
		print("[2] remove a task")
		print("[3] mark task done")
		print("[4] zapisz do pliku tasks.json")
		print("[5] wczytaj zadania z pliku tasks.json")


		command: int = int(input("command number: "))
		if command == 0:
			show_tasks()
		elif command == 1:
			tittle = input("Podaj nazwe zadania: ")
			due_date = input("(opcjonalnie) Podaj termin (RRRR-MM-DD): ")
			if due_date == "":
				add_new_task(tittle) 
			#elif due_date == date:
				#add_new_task(tittle, due_date) 
			else:
				add_new_task(tittle, due_date)
			
		elif command == 2:
			remove_task(input("podaj numer zadania: "))
		elif command == 3:
			mark_task_done(input("podaj numer zadania: "))
		elif command == 4:
			save_tasks()
		elif command == 5:
			load_tasks()
		else:
			print("There is no such command")