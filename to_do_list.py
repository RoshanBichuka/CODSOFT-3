from tkinter import *
import tkinter.messagebox


def entertask():
    def add():
        input_task = entry_task.get(1.0, "end-1c")
        if input_task == "":
            tkinter.messagebox.showwarning(title="WARNING!!!", message="PLEASE ENTER SOME TEXT")
        else:
            listbox_task.insert(END, input_task)
            root1.destroy()

    root1 = Tk()
    root1.title("ADD TASK")
    entry_task = Text(root1, width=30, height=4)
    entry_task.pack()
    button_temp = Button(root1, text="ADD TEXT", command=add)
    button_temp.pack()
    root1.mainloop()


def deletetask():
    selected = listbox_task.curselection()
    listbox_task.delete(selected[0])


def markcompleted():
    marked = listbox_task.curselection()
    temp = marked[0]
    temp_marked = listbox_task.get(marked)
    temp_marked = temp_marked + "✔"
    listbox_task.delete(temp)
    listbox_task.insert(temp, temp_marked)


window = Tk()
window.title("TO_DO_LIST")

frame_task = Frame(window)
frame_task.pack()

listbox_task = Listbox(frame_task, bg="white", fg="black", height=15, width=50, font="Century")
listbox_task.pack(side=tkinter.LEFT)

scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

entry_button = Button(window, text="ADD TEXT", width=30, command=entertask)
entry_button.pack(pady=3)

delete_button = Button(window, text="DELETE SELECTED TEXT", width=30, command=deletetask)
delete_button.pack(pady=3)

mark_button = Button(window, text="MARK AS COMPLETED", width=30, command=markcompleted)
mark_button.pack(pady=3)

window.mainloop()
