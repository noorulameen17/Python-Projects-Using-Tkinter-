from tkinter import*
from tkinter import messagebox
tasks_list = []
counter = 1
def inputError():
    if enterTaskField.get() == " " :
        messagebox.showerror("Input Error")
        return 0
    return 1
def clear_taskNumberField():
    taskNumberField.delete(0.0,END)
def clear_taskField():
    enterTaskField.delete(0,END)
def insertTask():
    global counter
    value = inputError()
    if value == 0 :
        return
    content = enterTaskField.get() + "\n"
    tasks_list.append(content)
    TextArea.insert('end -1 chars',"[" + str(counter) + "]" + content)
    counter += 1
    clear_taskField()
def delete():
    global counter
    if len(tasks_list) == 0:
        messagebox.showerror("No Task")
        return
    number = taskNumberField.get(1.0, END)
    if number == "\n" :
        messagebox.showerror("Input Error")
        return
    else:
        task_no = int(number)
    clear_taskNumberField()
    tasks_list.pop(task_no - 1)
    counter -= 1
    TextArea.delete(1.0, END)
    for i in range(len(tasks_list)):
        TextArea.insert('end -1 chars', "[ "+ str(i + 1) + " ]" + tasks_list[i])
if __name__ == "__main__" :
    gui = Tk()
    gui.configure(background = "lightskyblue2")
    gui.title("To Do App")
    gui.geometry("300x300")
    enterTask = Label(gui, text = "Enter Your Task", font = "Times 12 bold", fg = "black", bg = "medium aquamarine")
    enterTaskField = Entry(gui,font ="Courier 10" )
    submit = Button(gui, text = "Submit", font = "Verdana 9 bold", fg = "Black", bg = "cadet blue", command = insertTask)
    TextArea = Text(gui, height = 5, width = 25, font = "Verdana 12 bold")
    taskNumber = Label(gui, text = "Delete Task Number",font = "Helvetica 10 bold", fg = "black", bg = "cyan")
    taskNumberField = Text(gui, height = 1, width = 3, font = "Courier 10 bold")
    delete = Button(gui, text = "Delete",font = "Helvetica 10 bold", fg = "Black", bg = "dark orange", command = delete)
    exit= Button(gui, text = "Exit",font = "Helvetica 10 bold", fg = "Black", bg = "peachpuff2", command = exit)
    enterTask.grid(row = 0, column = 2)
    enterTaskField.grid(row = 1, column = 2, ipadx = 50)
    submit.grid(row = 2, column = 2)
    TextArea.grid(row = 3, column = 2, padx = 10, sticky = W)
    taskNumber.grid(row = 4, column = 2, pady = 5)
    taskNumberField.grid(row = 5, column = 2)
    delete.grid(row = 6, column = 2, pady = 5)
    exit.grid(row = 7, column = 2)
    gui.mainloop()
