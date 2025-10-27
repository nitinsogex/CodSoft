import json
import os

class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done

    def CompleteTask(self):
        self.done = True

    def to_dict(self):
        return {"title": self.title, "done": self.done}

class TodoList:
    FNAME = "To-Do.json"

    def __init__(self):
        self.tasks = self.Fetch()

    def Fetch(self):
        if os.path.exists(self.FNAME):
            with open(self.FNAME, "r") as file:
                data = json.load(file)
                return [Task(**task) for task in data]
        return []

    def Save(self):
        with open(self.FNAME, "w") as file:
            json.dump([t.to_dict() for t in self.tasks], file, indent=4)

    def Show(self):
        if not self.tasks:
            print("\nNo tasks yet!")
            input("\nPress Enter to continue...")
            return
        print("\nYour To-Do List:\n")
        for i, task in enumerate(self.tasks, start=1):
            status = "👍" if task.done else "👎"
            print(f"{i}. {task.title} {status}")
        input("\nPress Enter to continue...")

    def AddTask(self):
        title = input("\nEnter new task: ").strip()
        if title:
            self.tasks.append(Task(title))
            self.Save()
            print("\nTask added!")
        input("\nPress Enter to continue...")

    def CompleteTask(self):
        self.Show()
        if not self.tasks:
            input("\nPress Enter to continue...")
            return
        try:
            num = int(input("\nEnter task number to mark done: "))
            self.tasks[num - 1].CompleteTask()
            self.Save()
            print("\nMarked as done!")
            input("\nPress Enter to continue...")
        except (ValueError, IndexError):
            print("\nInvalid number!")
            input("\nPress Enter to continue...")

    def DeleteTask(self):
        self.Show()
        if not self.tasks:
            input("\nPress Enter to continue...")
            return
        try:
            num = int(input("\nEnter task number to delete: "))
            deleted = self.tasks.pop(num - 1)
            self.Save()
            print(f"Deleted: {deleted.title}")
            input("\nPress Enter to continue...")
        except (ValueError, IndexError):
            print("\nInvalid number!")
            input("\nPress Enter to continue...")

def main():
    todo = TodoList()

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n               --- TO-DO LIST MENU ---\n")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        match choice:
            case "1":
                todo.Show()
            case "2":
                todo.AddTask()
            case "3":
                todo.CompleteTask()
            case "4":
                todo.DeleteTask()
            case "5":
                print("\nGoodbye")
                break
            case _:
                print("\nInvalid choice! Try again.")

if __name__ == "__main__":
    main()