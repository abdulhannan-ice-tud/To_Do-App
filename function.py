def get_todos(filepath ="todos.txt"):
    with open(filepath, "r") as local_file:
        todo = local_file.readlines()
        return todo
    
def write_todos(file_arg, filepath ="todos.txt"):
    with open(filepath, "w") as file:
        file.writelines(file_arg)
