
import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        #Sets title of GUI window
        self.master.title("File Transfer")

        #Creates button to select files from source dircetory
        self.sourceDir_bth = Button(text="Select Source", width=20)
        #Positions source button in GUI using tkinter grid()
        self.sourceDir_bth.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))
        self.sourceDir_btn = Button(self.master, text="Select Source", width=20, command=self.sourceDir)
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)

        #Creates entry for source directory selection
        self.source_dir = Entry(width=75)
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))
        self.destDir_btn = Button(self.master, text="Select Destination", width=20)
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15,10))
        self.destination_dir = Entry(width=75)
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))
                                    
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        self.source_dir.delete(0, END)
        self.source_dir.insert(0, selectSourceDir)


    def destDir(self):
        selectDestDir= tkinter.filedialog.askdirectory()
        self.destination_dir.delete(0, END)
        self.destination_dir.insert(0, selectDestDir)

    def transferFiles(self):
        
        source = self.source_dir.get()
        destination = self.destination_dir.get()
        source_files = os.listdir(source)
        for i in source_files:
            shutil.move(source + '/' + i, destination)
            print(i + ' was successfully transferred.')

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
