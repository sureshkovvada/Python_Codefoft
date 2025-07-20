# 📝 Simple To-Do List Program with Status Tracking

todo_list = []

def show_menu():
    print("\n📝 TO-DO LIST MENU")
    print("---------------------")
    print("1. 📋 View Tasks")
    print("2. ➕ Add Task")
    print("3. ✔️ Mark Task as Done")
    print("4. 🗑️ Remove Task")
    print("5. 🚪 Exit")

def view_tasks():
    if not todo_list:
        print("📭 Your to-do list is empty.")
    else:
        print("\n📋 Your Tasks:")
        for idx, task in enumerate(todo_list, 1):
            status = "✅ Done" if task['done'] else "❌ Not Done"
            print(f"{idx}. {task['title']} [{status}]")

def add_task():
    title = input("➕ Enter task title: ").strip()
    if title:
        task = {"title": title, "done": False}
        todo_list.append(task)
        print("✅ Task added successfully.")
    else:
        print("⚠️ Task title cannot be empty.")

def mark_done():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("✔️ Enter task number to mark as done: "))
            if 1 <= task_num <= len(todo_list):
                todo_list[task_num - 1]['done'] = True
                print("🎉 Task marked as done.")
            else:
                print("❗ Invalid task number.")
        except ValueError:
            print("❗ Please enter a valid number.")

def remove_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("🗑️ Enter task number to remove: "))
            if 1 <= task_num <= len(todo_list):
                removed = todo_list.pop(task_num - 1)
                print(f"🗑️ Removed: {removed['title']}")
            else:
                print("❗ Invalid task number.")
        except ValueError:
            print("❗ Please enter a valid number.")

# --- Main Program ---
def run_todo_list():
    print("🎯 Welcome to Your Personal To-Do List!")
    while True:
        show_menu()
        choice = input("🔸 Choose an option (1-5): ").strip()

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            remove_task()
        elif choice == '5':
            print("👋 Goodbye! Stay productive. 🧠💪")
            break
        else:
            print("❗ Invalid choice. Please try again.")

# Start the To-Do List
run_todo_list()
