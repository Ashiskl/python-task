def task():
    tasks=[]
    print("___Welcome to task managment you are at right place__")

    total_task=int(input("enter no of task you want to  do:-"))
    for i in range(1,total_task+1):
        task_name=input(f"the task you want to add {i}=")
        tasks.append(task_name)

    print(f"today's tasks are\n{tasks}")

    while True:
        operation=int(input("select what you want:-\n1-add\n2-update\n3Delete\n4-view\n5-stop\nenter:-"))
        if operation==1:
            add=input("enter task you want to add:-")
            tasks.append(add)
            print(f"thank you {add} has  been added successfully") 
        elif operation==2:
            updated_val=input("enter the task name you want to update:-")
            if updated_val in tasks:
                up=input("enter new task=")
                ind=tasks.index(updated_val)
                tasks[ind]=up
                print(f"updated task {up}")
        elif operation==3:
            del_val = input("which task you want to delete:-")
            if del_val in tasks:
                ind=tasks.index(del_val)
                del tasks[ind]
                print(f"tasks {del_val} has been deletd..")

        elif  operation ==4:
            print(f"total  tasks={tasks}")
        elif operation==5:
            print(" thank you ...")
            break
            


task()
    




