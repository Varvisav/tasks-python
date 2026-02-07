
#from dane import tasks
from funkcje import show_tasks, add_new_task, remove_task, mark_task_done, save_tasks, load_tasks, tasks
import json
from datetime import date
import os



if __name__ == "__main__":
	while True:
		print("Wybiez komende:")
		print("[0] pokaz zadania")
		print("[1] dodaj nowe zadanie")
		print("[2] usuń zadanie")
		print("[3] oznacz zadanie jako wykonane")
		print("[4] zapisz do pliku tasks.json")
		print("[5] wczytaj zadania z pliku tasks.json")


		command: int = int(input("numer komendy: "))
		if command == 0:
			show_tasks(int(input("wszystkie zadania[0], zadania do zrobienia[1], zadania wykonane[2]: ")))
		
		elif command == 1:
			tittle = input("Podaj nazwe zadania: ")
			due_date = input("(opcjonalnie) Podaj termin (RRRR-MM-DD): ")
			if due_date == "":
				add_new_task(tittle)  
			else:
				add_new_task(tittle, due_date)
			
		elif command == 2:
			remove_task(int(input("podaj numer zadania: ")))
		
		elif command == 3:
			mark_task_done(int(input("podaj numer zadania: ")))
		
		elif command == 4:
			save_tasks()
		
		elif command == 5:
			load_tasks()
		
		else:
			print("nie ma takiej komendy")