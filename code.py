""" This program creates a simple file editor 
    It cosists of four operations 
    new_file: clears current screen to give new file
    save_file: saves the contents of the current file

"""
from tkinter import *
from tkinter.filedialog import * 
from tkinter.messagebox import *

class FileEditor(): 

    filename = None

    def __init__(self):
        self.root = Tk()
        self.root.title("Nethra's Simple Python Editior")
        self.root.minsize(width = 400, height = 400)
        self.root.maxsize(width = 400, height = 400)
        self.text = Text(self.root, width = 400, height = 400)

    def new_file(self): 
        self.filename = "Untitled"
        # 0.0 position = 0th line.0th column
        self.text.delete(0.0, END) # deletes all the charaters from the first character to the end

    def save_file(self):
        contents = self.text.get(0.0, END)
        file = open(self.filename, "w")
        file.write(contents)
        file.close()

    def save_as(self):
        file = asksaveasfile(mode = "w", defaultextension=".txt")
        contents = self.text.get(0.0, END)
        try:
            file.write(contents.strip())
        except:
            showerror(title = "Error", message = "Unable to save file. An error has occured")

    def open_file(self):
        file = asksaveasfile(mode = "r")
        contents = file.read()
        self.text.delete(0.0, END)
        self.text.insert(0.0, contents)

    def start(self):
        self.text.pack() #display the text box

        menubar = Menu(self.root)
        filebar = Menu(menubar)
        filebar.add_command(label= "New", command= self.new_file)
        filebar.add_command(label= "Save", command= self.save_file)
        filebar.add_command(label= "Save As..", command= self.save_as)
        filebar.add_command(label= "Open", command= self.open_file)
        filebar.add_separator()
        filebar.add_command(label = "Quit", command=self.root.quit)
        menubar.add_cascade(label = "File", menu= filebar)

        fontbar = Menu(menubar)
        fontbar.add_command(label = "Bold")

        self.root.config(menu = menubar)
        self.root.mainloop()

if __name__ == "__main__":
    editor = FileEditor()
    editor.start()
