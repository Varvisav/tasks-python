tasks = [
{
"id": 1,
"title ": "Nauczyc sie Pythona ",
"done ": False ,
"due_date ": " 2026 -01 -20 "
}
]

def add_new_task():
	title = input("Podaj nazwe zadania: ")
	due_date = input("Podaj termin (opcjonalnie): ")
	
	
	tasks.append({"title ": title, "done ": False, "due_date": due_date})

def mark_task_done():
	wich_task = int(input("podaj numer zadania: "))
	tasks[wich_task]["done "] = True


def show_tasks():
	#return("\nYour tasks:\n")
	print(tasks) 
	

show_tasks()
add_new_task()
show_tasks()
mark = input("Napisz 'yeah' by oznaczyć wybrane zadanie jako wykonane, jeśli nie chcesz nic oznaczać, napisz 'nie'")
if mark == "yeah":
	mark_task_done()
elif mark == "nie":
	print("idiota")
show_tasks()