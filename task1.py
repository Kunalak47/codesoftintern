import datetime

class Task:
    """Represents a single task in a to-do list."""

    def __init__(self, description, due_date=None, completed=False):
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def mark_complete(self):
        """Marks the task as completed."""
        self.completed = True

    def __str__(self):
        """Returns a string representation of the task."""
        if self.completed:
            return "[DONE] " + self.description
        else:
            return self.description + (f" (due: {self.due_date.strftime('%Y-%m-%d')})" if self.due_date else "")

class ToDoList:
    """Represents a to-do list."""

    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date=None):
        """Adds a new task to the list."""
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_complete(self, task_index):
        """Marks the task at the given index as completed."""
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_complete()
        else:
            print("Invalid task index.")

    def view_tasks(self):
        """Prints all tasks in the list."""
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task}")

    def remove_task(self, task_index):
        """Removes the task at the given index."""
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task removed.")
        else:
            print("Invalid task index.")

def main():
    """Main function to run the to-do list application."""
    todo_list = ToDoList()

    while True:
        print("\nChoose an action:")
        print("1. Add task")
        print("2. Mark task complete")
        print("3. View tasks")
        print("4. Remove task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date_str = input("Enter due date (YYYY-MM-DD, or press Enter for no due date): ")
            if due_date_str:
                due_date = datetime.datetime.strptime(due_date_str, '%Y-%m-%d').date()
            else:
                due_date = None
            todo_list.add_task(description, due_date)
        elif choice == '2':
            todo_list.view_tasks()
            task_index = int(input("Enter the number of the task to mark complete: ")) - 1
            todo_list.mark_complete(task_index)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            todo_list.view_tasks()
            task_index = int(input("Enter the number of the task to remove: ")) - 1
            todo_list.remove_task(task_index)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()