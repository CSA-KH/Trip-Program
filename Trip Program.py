#Keenan Hui
#Advanced Computer Programming (10)
#10/22/18

#V 1.0.2

'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Howard C Davis
Final Tk
'''

from tkinter import *
from tkinter import ttk

root = Tk()
#Values
travel = StringVar()
spinval = StringVar()

#functions
def check():
   if IListbox.curselection() == () or travel.get() == '':
    topC = Toplevel()  #C = correction, basically an error message
    topC.title('Error')
    topC.minsize(width=100, height=50)
    topC.resizable(width=FALSE, height=FALSE)
    msgC = Message(topC, text = 'You did not fill out all of the options')
    msgC.pack()
    buttonE = Button(topC, text="Close", command=topC.destroy)
    buttonE.pack()
    pass
   else:
    savedata()

def clear():
<<<<<<< HEAD
   IListbox.select_clear(0,END)
   D.delete('1.0','end-1c')
   travel.set('')
=======
    IListbox.select_clear(0,END)
    D.delete('1.0','end-1c')
    travel.set('')
>>>>>>> b60ff299c64d5e36a3e98bb0b1ef8c5d9d6e4425

def savedata():
   a = str(IListbox.curselection()).replace('(','').replace(')','').replace(',','').replace('"','')  #List Box value

   TripL = open('Trip_Logger','a')
   TripL.write(IListbox.get(first=int(a), last=None) + '\n')
   TripL.write(travel.get() + '\n')
   TripL.write(SBMonth.get()+'\n')
   TripL.write(D.get('1.0','end-1c')+'\n\n')
   TripL.close()

   clear()

def about():
   top = Toplevel()
   top.title("About")
   top.minsize(width=200, height=100)
   top.resizable(width = FALSE, height = FALSE)
   msg = Message(top, text='About')
   msg2 = Message(top, text='V 1.0.2\nKeenan Hui\n\nAdded the clear after clicking the subbmit button and made months as read only.\n\nThe program is a trip logger where you can input where you went, how the trip was, when you want there, and how you got there.')
   msg.pack()
   msg2.pack()
   button = Button(top, text="Close", command=top.destroy)
   button.pack()

#Entry Box
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = 'Save', command = check)
filemenu.add_separator()
filemenu.add_command(label = 'Exit', command = root.quit)
menubar.add_cascade(label = 'File', menu = filemenu)

helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = 'About', command = about)
menubar.add_cascade(label = 'Help', menu = helpmenu)

root.config(menu=menubar)

#List Box
LBlabel = Label(root,text = 'Countries')
LBlabel.grid(row = 0, column = 0, sticky = NSEW)

IListbox = Listbox(root,height=10)
IListbox.insert(END, 'Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda','Argentina','Armenia','Aruba','Australia','Austria','Azerbaijan')
IListbox.insert(END, 'Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia and Herzegovina','Botswana','Brazil','Brunei','Bulgaria','Burkina Faso','Burma','Burundi')
IListbox.grid(row=1, column=0, sticky=(N,E,W,S), columnspan = 2)

SILB = ttk.Scrollbar(root,orient=VERTICAL, command=IListbox.yview)  # scroll bar for the itme list box
SILB.grid(row=1, column=1, sticky=(N,S), columnspan = 2)
IListbox.configure(yscrollcommand=SILB.set)

#Description box
labelD = Label(root,text = 'Description')
labelD.grid(row=0,column=3,sticky=NSEW, columnspan = 2)

D = Text(root,width=15,height=5)
D.grid(row=1,column=3,sticky=NSEW, columnspan = 2)

#Travel Log
labelT = Label(root,text = 'Travel Log')
labelT.grid(row = 2, column = 0, sticky = (N,S,E,W), columnspan = 2)

TripCB = ttk.Combobox(root,state = 'readonly', values = ['Air','Train','Car','Boat'], textvariable = travel)
TripCB.bind("<<ComboboxSelected>>")
TripCB.grid(row = 3, column = 0, sticky = (N,S,E,W))

#Spinbox for month
SBMonth = Spinbox(root, values=('January','February','March','April','May','June','July','August','September','October','November','December') , textvariable=spinval, wrap = TRUE, state = 'readonly')
SBMonth.grid(column = 0, row = 4,sticky = NSEW)

#Buttons
SButton = Button(root,text = 'Submit', command = check)
SButton.grid(row = 3, column = 3, sticky = NSEW, rowspan = 2)

CButton = Button(root,text = 'Clear', command = clear)
CButton.grid(row = 3, column = 4,sticky=NSEW, rowspan = 2)

#Others
ttk.Sizegrip(root).grid(column=999, row=999, sticky=(N,S,E,W))
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)

root.minsize(width = 350, height = 270)

root.title('Trip Program')
root.mainloop()
root.destroy()


