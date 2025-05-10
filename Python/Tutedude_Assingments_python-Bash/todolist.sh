#!/bin/bash

TODO_FILE="todo.txt"

# Create the file if it doesn't exist
touch "$TODO_FILE"

show_menu() {
    echo "======================="
    echo " Simple To-Do List"
    echo "======================="
    echo "1. View Tasks"
    echo "2. Add Task"
    echo "3. Remove Task"
    echo "4. Exit"
}

view_tasks() {
    echo
    echo "Your Tasks:"
    if [[ ! -s "$TODO_FILE" ]]; then
        echo "No tasks found."
    else
        nl -w2 -s'. ' "$TODO_FILE"
    fi
    echo
}

add_task() {
    read -p "Enter the task: " task
    echo "$task" >> "$TODO_FILE"
    echo "Task added!"
}

remove_task() {
    view_tasks
    read -p "Enter the task number to remove: " task_number
    if [[ "$task_number" =~ ^[0-9]+$ ]]; then
        sed -i "${task_number}d" "$TODO_FILE"
        echo "Task removed!"
    else
        echo "Invalid input. Please enter a valid task number."
    fi
}

while true; do
    show_menu
    read -p "Choose an option (1-4): " choice
    case $choice in
        1) view_tasks ;;
        2) add_task ;;
        3) remove_task ;;
        4) echo "Goodbye!"; exit 0 ;;
        *) echo "Invalid option. Please try again." ;;
    esac
done
