import datetime
import argparse, json

todoFile = "tasks.json"

def save_tasks(tasks):
    try:
        with open(todoFile, "w", encoding="utf-8") as f:
            json.dump(tasks, f, ensure_ascii=False, indent=2)
    except FileNotFoundError:
        print("Brak pliku z zadaniami.")
        return[]
    except json.JSONDecodeError:
        print("Plik jest pusty lub uszkodzony.")
        return []

def load_tasks():
    try:
        with open(todoFile, "r", encoding="utf-8") as f:
                return json.load(f)
    except FileNotFoundError:
        print("Brak pliku z zadaniami.")
        return[]
    except json.JSONDecodeError:
        print("Plik jest pusty.")
        return []

        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TODO list handler")
    parser.add_argument("command", choices=["add", "list", "finish", "remove"], help="Command to execute")
    parser.add_argument("task", nargs="?", help="Task description")

    args = parser.parse_args()

    if args.command == "add":
        tasklist = load_tasks()
        if(args.task):
            tasklist.append(
                {
                    "id":len(tasklist)+1,
                    "title": args.task,
                    "finished": False,
                    "created_at": datetime.datetime.now().isoformat()
                }
            )
            save_tasks(tasklist)
        else:
            print("Brak argumentu")
    
    elif args.command == "list":
        tasklist = load_tasks()
        if not tasklist:
            print("Brak zadań.")
        else:
            for task in tasklist:
                status = "✓" if task["finished"] else " "
                date = task["created_at"][:10]
                print(f'{task["id"]}. [{status}] {task["title"]} ({date})')
    
    elif args.command == "finish":
        tasklist = load_tasks()
        task = next((t for t in tasklist if t["id"] == int(args.task)), None)
        if(task is not None):
            task["finished"] = True
            save_tasks(tasklist)
        else:
            print("Nie znaleziono zadania")
        
    elif args.command == "remove":
        tasklist = load_tasks()
        task = next((t for t in tasklist if t["id"] == int(args.task)), None)
        if(task is not None):
            tasklist.remove(task)
            save_tasks(tasklist)
        else:
            print("Nie znaleziono zadania")
                    
        