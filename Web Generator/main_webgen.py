from tkinter import *
import tkinter as tk
import tkinter.messagebox
import webbrowser



#imported modules to have access to
#import gui_webgen
import function_webgen


class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        #self.master = master
        self.master.minsize(500,500)# (Height, Width)
        self.master.maxsize(500,500)
        self.master.title("Web Page Generator")
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(padx=(10,10) , pady=(10,10))
        self.master.protocol("WM_DELETE_WINDOW", lambda: function_webgen.ask_quit(self))

        

        self.label_body = tk.Label(self.master,text="Enter body text here")
        self.label_body.config(font=10)
        self.label_body.grid(row=0,column=0,padx=(8,3),pady=(8,4),sticky=N+E)

        self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
        self.txt_body = tk.Text(self.master,yscrollcommand=self.scrollbar1.set,font=12,width=52,height=20)
        self.scrollbar1.config(command=self.txt_body.yview)
        self.scrollbar1.grid(row=1,column=4,rowspan=2,columnspan=1,padx=(4,0),pady=(0,0),sticky=N+E+S)
        self.txt_body.grid(row=1,column=0,rowspan=2,columnspan=3,padx=(7,0),pady=(0,0),sticky=N+E+S+W)

        self.btn_create = tk.Button(self.master,width=10,height=3,text="Generate\nWeb Page",command=lambda: function_webgen.addToBody(self))
        self.btn_create.config(font=12)
        self.btn_create.grid(row=5,column=0,padx=(8,4),pady=(8,4),sticky=N+E)

        #self.btn = Button(self.master, text="Default HTML Page", width=30, height=2)
        

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<hl>" + htmlText + "<\h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        






        


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

