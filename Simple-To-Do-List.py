#TODO list
Status = True
task = []
Check =[]

while Status==True:
    print("\n Options \n")
    print("1. Display To-Do List\n")
    print("2. Add a Task\n")
    print("3. Mark a Task as Completed\n")
    print("4. Remove a Task\n")
    print("5. Quit\n")
    select = int(input("enter your input\n"))
    if select ==5:
        Status = False
        print("thank you")
    elif select == 1:
        if len(task)==0:
            print("TODO List is empty\n")
        else:
            print("SR_NO ","> Task","> Status")
            for i in range(len(task)):
                print(i+1,">",task[i],">",Check[i])
    elif select == 2:
        content = input("Add New task\n")
        task.append(content)
        Check.append("Not Done")
    elif select == 3:
        selection = int(input("Enter SR no of task you want mark as done\n"))
        if selection <= len(task) and selection != 0:
            Check[selection-1]="done"
    elif select == 4:
        remove = int(input(" Enter SR no of task you want to remove \n"))
        if len(task)==0:
            print("TODO List is empty\n")
        else:
            task.remove(task[remove])
