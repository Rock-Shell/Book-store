from tkinter import *
from backend import Database

database=Database('books.db')
class frontend:
    def __init__(self,window):
        self.window=window
        self.window.wm_title('BOOK STORE. SHUT UP HOJA BC')
        L=Label(self.window,text='Title')
        L.grid(row=0,column=0)

        L1=Label(self.window,text='Author')
        L1.grid(row=0,column=2)

        L2=Label(self.window,text='Year')
        L2.grid(row=1,column=0)

        L3=Label(self.window,text='ISBN')
        L3.grid(row=1,column=2)

        self.t=StringVar()
        self.e1=Entry(self.window,textvariable=self.t)
        self.e1.grid(row=0,column=1)

        self.t1=StringVar()
        self.e2=Entry(self.window,textvariable=self.t1)
        self.e2.grid(row=0,column=3)

        self.t2=StringVar()
        self.e3=Entry(self.window,textvariable=self.t2)
        self.e3.grid(row=1,column=1)

        self.t3=StringVar()
        self.e4=Entry(self.window,textvariable=self.t3)
        self.e4.grid(row=1,column=3)

        self.l1=Listbox(self.window,height=6,width=35)
        self.l1.grid(row=2,column=0,rowspan=6,columnspan=2)

        s1=Scrollbar(self.window)
        s1.grid(row=2,column=2,rowspan=6)

        self.l1.configure(yscrollcommand=s1.set)
        s1.configure(command=self.l1.yview)

        self.l1.bind('<<ListboxSelect>>',self.selected)

        b=Button(self.window,text='View all',width=12,command=self.view_c)
        b.grid(row=3,column=3)

        b1=Button(self.window,text='Search Entry',width=12,command=self.search_c)
        b1.grid(row=4,column=3)

        b2=Button(self.window,text='Add Entry',width=12,command=self.add_c)
        b2.grid(row=5,column=3)

        b3=Button(self.window,text='Update',width=12,command=self.update_c)
        b3.grid(row=6,column=3)

        b4=Button(self.window,text='Delete',width=12,command=self.del_c)
        b4.grid(row=7,column=3)

        b6=Button(self.window,text='Close',width=12,command=self.window.destroy)
        b6.grid(row=8,column=3)

        

    
    def selected(self,event):
        index=self.l1.curselection()[0]
        try:
                
            self.s_t=self.l1.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END,s_t[1])
            self.e2.delete(0,END)
            self.e2.insert(END,s_t[2])
            self.e3.delete(0,END)
            self.e3.insert(END,s_t[3])
            self.e4.delete(0,END)
            self.e4.insert(END,s_t[4])
        except:
            pass

        
        #return (s_t)
    def view_c(self):
        self.l1.delete(0,END)
        for i in database.view():
            self.l1.insert(END,i)

    def search_c(self):
        self.l1.delete(0,END)
        for i in database.search(self.t.get(),self.t1.get(),self.t2.get(),self.t3.get()):
            self.l1.insert(END,i)

    def add_c(self):
        self.l1.delete(0,END)
        if self.t.get()!='' and self.t1.get()!='' and self.t2.get()!='' and self.t3.get()!='':
            database.insert(self.t.get(),self.t1.get(),self.t2.get(),self.t3.get() )
            x=self.t.get(),self.t1.get(),self.t2.get(),self.t3.get()
            self.l1.insert(END,x)
            self.l1.insert(END,'Added successfully')

    def del_c(self):
        if self.l1.size()>0:
            database.delete(self.s_t[0])
        else:
            pass
        self.l1.delete(0,END)

    def update_c(self):
        if self.l1.size()>0:
            database.update(self.s_t[0],self.t.get(),self.t1.get(),self.t2.get(),self.t3.get())
        else:
            pass
        self.l1.delete(0,END)

    

    
window=Tk()
frontend(window)
window.mainloop()#keeps the app running and wait for any action to be done.


# login register page
# function to register
# save username and password
# function to login
# after successful login allow user to do what he want
