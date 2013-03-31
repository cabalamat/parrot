# simple2.py
#
# This file was autogenerated by Parrot's PytkBackend module

from Tkinter import *
from Dialog import Dialog


#/////////////////////////////////////////////////////////////////////

class MyWindow(Frame):

   def  __init__(self, parent=None):
      Frame.__init__(self, parent)
      self.pack()
      self.createMenuBar()
      self.createGUI()
      self.master.title("My second Window")
      self.master.iconname("self")

   def createMenuBar(self):
      self.menubar = Frame(self, relief=RAISED, bd=2)
      self.menubar.pack(side=TOP, fill=X)

      #----- menu "File"
      mbutton = Menubutton(self.menubar, text='File', underline=0)
      mbutton.pack(side=LEFT)
      menu = Menu(mbutton, tearoff=N)
      menu.add_command(label='New', command=self.New_pressed)
      menu.add_command(label='Open...', command=self.Open_pressed)
      menu.add_command(label='Save', command=self.Save_pressed)
      menu.add_command(label='Save as...', command=self.SaveAs_pressed)
      menu.add_command(label='Exit', command=self.Exit_pressed)
      mbutton['menu'] = menu

      #----- menu "Edit"
      mbutton = Menubutton(self.menubar, text='Edit', underline=0)
      mbutton.pack(side=LEFT)
      menu = Menu(mbutton, tearoff=N)
      menu.add_command(label='Copy', command=self.Copy_pressed)
      menu.add_command(label='Cut', command=self.Cut_pressed)
      menu.add_command(label='Paste', command=self.Paste_pressed)
      mbutton['menu'] = menu

      #----- menu "Help"
      mbutton = Menubutton(self.menubar, text='Help', underline=0)
      mbutton.pack(side=LEFT)
      menu = Menu(mbutton, tearoff=N)
      menu.add_command(label='About...', command=self.About_pressed)
      menu.add_command(label='Getting started', command=self.GettingStarted_pressed)
      menu.add_command(label='Reference manual', command=self.Reference_pressed)
      mbutton['menu'] = menu

   def createGUI(self):
      par_rowLayout1 = Frame(self, relief=RIDGE, bd=4, bg='#eeee88')
      par_colLayout2 = Frame(par_rowLayout1, relief=RIDGE, bd=4, bg='#8888ee')
      par_label3 = Label(par_colLayout2, text="First column!")
      par_label3.pack(side=TOP, anchor=NW)
      par_button4 = Button(par_colLayout2, text="press me")
      par_button4.pack(side=TOP, anchor=NW)
      par_colLayout2.pack(side=LEFT, anchor=NW)
      par_colLayout5 = Frame(par_rowLayout1, relief=RIDGE, bd=4, bg='#8888ee')
      par_button6 = Button(par_colLayout5, text="Button 1")
      par_button6.pack(side=TOP, anchor=NW)
      par_button7 = Button(par_colLayout5, text="Button 2")
      par_button7.pack(side=TOP, anchor=NW)
      par_button8 = Button(par_colLayout5, text="Button 3")
      par_button8.pack(side=TOP, anchor=NW)
      par_button9 = Button(par_colLayout5, text="Button 4")
      par_button9.pack(side=TOP, anchor=NW)
      par_button10 = Button(par_colLayout5, text="Button 5")
      par_button10.pack(side=TOP, anchor=NW)
      par_colLayout5.pack(side=LEFT, anchor=NW)
      par_colLayout11 = Frame(par_rowLayout1, relief=RIDGE, bd=4, bg='#8888ee')
      par_label12 = Label(par_colLayout11, text="Type stuff in here:")
      par_label12.pack(side=TOP, anchor=NW)
      par_textField13 = Text(par_colLayout11, height=1, width=20)
      par_textField13.insert("1.0", "abcd")
      par_textField13.pack(side=TOP, anchor=NW)
      par_rowLayout14 = Frame(par_colLayout11, relief=RIDGE, bd=4, bg='#eeee88')
      par_button15 = Button(par_rowLayout14, text="Button 6")
      par_button15.pack(side=LEFT, anchor=NW)
      par_button16 = Button(par_rowLayout14, text="Button 7")
      par_button16.pack(side=LEFT, anchor=NW)
      par_button17 = Button(par_rowLayout14, text="Button 8")
      par_button17.pack(side=LEFT, anchor=NW)
      par_rowLayout14.pack(side=TOP, anchor=NW)
      check1 = Checkbutton(par_colLayout11, text='really do it?')
      check1.pack(side=TOP, anchor=NW)
      check1.config(command=self.check1_toggled)
      par_colLayout11.pack(side=LEFT, anchor=NW)

      par_colLayout18 = Frame(par_rowLayout1, relief=RIDGE, bd=4, bg='#8888ee')
      par_label19 = Label(par_colLayout18, text="Which units:")
      par_label19.pack(side=TOP, anchor=NW)

      inchRB = Radiobutton(par_colLayout18, text='inches', value='inches')
      inchRB.pack(side=TOP, anchor=NW)
      inchRB.config(command=self.inchRB_toggled)

      feetRB = Radiobutton(par_colLayout18, text='feet', value='feet')
      feetRB.pack(side=TOP, anchor=NW)
      feetRB.config(command=self.feetRB_toggled)
      yardRB = Radiobutton(par_colLayout18, text='yards', value='yards')
      yardRB.pack(side=TOP, anchor=NW)
      yardRB.config(command=self.yardRB_toggled)
      mileRB = Radiobutton(par_colLayout18, text='miles', value='miles')
      mileRB.pack(side=TOP, anchor=NW)
      mileRB.config(command=self.mileRB_toggled)
      par_colLayout18.pack(side=LEFT, anchor=NW)

      par_table20 = Frame(par_rowLayout1, relief=RIDGE, bd=4, bg='#ee8888')
      #getStartCode() td
      par_checkBox21 = Checkbutton(par_table20, text='Apple')
      par_checkBox21.grid(column=0, row=0, stick=N+W)
      #*** end td
      #getStartCode() td
      par_checkBox22 = Checkbutton(par_table20, text='Pear')
      par_checkBox22.grid(column=1, row=0, stick=N+W)
      #*** end td
      #getStartCode() td
      par_checkBox23 = Checkbutton(par_table20, text='Banana')
      par_checkBox23.grid(column=0, row=1, stick=N+W)
      #*** end td
      #getStartCode() td
      par_checkBox24 = Checkbutton(par_table20, text='Orange')
      par_checkBox24.grid(column=1, row=1, stick=N+W)
      #*** end td
      par_table20.pack(side=LEFT, anchor=NW)
      par_rowLayout1.pack(side=TOP, anchor=NW)

#***** methods to be redefined

   def New_pressed(self):
      print '[MyWindow New_pressed]'

   def Open_pressed(self):
      print '[MyWindow Open_pressed]'

   def Save_pressed(self):
      print '[MyWindow Save_pressed]'

   def SaveAs_pressed(self):
      print '[MyWindow SaveAs_pressed]'

   def Exit_pressed(self):
      print '[MyWindow Exit_pressed]'

   def Copy_pressed(self):
      print '[MyWindow Copy_pressed]'

   def Cut_pressed(self):
      print '[MyWindow Cut_pressed]'

   def Paste_pressed(self):
      print '[MyWindow Paste_pressed]'

   def About_pressed(self):
      print '[MyWindow About_pressed]'

   def GettingStarted_pressed(self):
      print '[MyWindow GettingStarted_pressed]'

   def Reference_pressed(self):
      print '[MyWindow Reference_pressed]'

   def check1_toggled(self):
      print '[MyWindow check1_toggled]'

   def inchRB_toggled(self):
      print '[MyWindow inchRB_toggled]'

   def feetRB_toggled(self):
      print '[MyWindow feetRB_toggled]'

   def yardRB_toggled(self):
      print '[MyWindow yardRB_toggled]'

   def mileRB_toggled(self):
      print '[MyWindow mileRB_toggled]'

#***** end of methods to be redefined

#/////////////////////////////////////////////////////////////////////

if __name__=='__main__':
   MyWindow().mainloop()

#/////////////////////////////////////////////////////////////////////

#(end simple2.py)