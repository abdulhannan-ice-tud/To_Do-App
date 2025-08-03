import function 

while True:
    user_choice =input("Type add, show, edit, remove or exit: ")
    user_choice.strip()

    if user_choice.startswith("add"): 
        todo = user_choice[4:] 
        todos = function.get_todos() 
        todos.append(todo + "\n")
        function.write_todos(todos) 

    elif user_choice.startswith("show"): 
        todos = function.get_todos() 

        for index, text in enumerate(todos): 
            text= text.strip("\n") 
            row = f"{index + 1}-{text}" 
            print(row) 

    elif user_choice.startswith("edit"): 
        try: 
            number_to_edit = int(user_choice[5:]) 
            print(number_to_edit)
            todos = function.get_todos() 
            number_to_edit = number_to_edit - 1 
            new_todo = input("Enter new todo: ") 
            todos[number_to_edit] = new_todo + "\n" 
            function.write_todos(todos) 
        except: 
            print("Your command is not valid")
            continue

    elif user_choice[:6] == "remove": 
        try:
            number_to_remove = int(user_choice[7:])  
            todos = function.get_todos()   
            index = number_to_remove - 1 
            todo_to_remove = todos[index] 
            todos.pop(index) 
            function.write_todos(todos)  
            message = f"todo {todo_to_remove} was removed from the list." 
            print(message)
        except IndexError: 
            print("The number you enter to remove is not exist.")
            continue 
    
    elif "exit" in user_choice:
        break
    else:
        print("The command you entered is invalid")

print("Bye!")

    
           
