# simple6.py
#
# This file was autogenerated by Parrot's PytkBackend module

from Tkinter import *
from Dialog import Dialog


#/////////////////////////////////////////////////////////////////////

class MyBigWindow(Frame):

   def  __init__(self, parent=None):
      Frame.__init__(self, parent)
      self.pack()
      self.createMenuBar()
      self.createGUI()
      self.master.title("My fourth Window")
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

      #----- menu "File2"
      mbutton = Menubutton(self.menubar, text='File2', underline=0)
      mbutton.pack(side=LEFT)
      menu = Menu(mbutton, tearoff=N)
      menu.add_command(label='New', command=self.New_pressed)
      menu.add_command(label='Open...', command=self.Open_pressed)
      menu.add_command(label='Save', command=self.Save_pressed)
      menu.add_command(label='Save as...', command=self.SaveAs_pressed)
      menu.add_command(label='Exit', command=self.Exit_pressed)
      mbutton['menu'] = menu

      #----- menu "File3"
      mbutton = Menubutton(self.menubar, text='File3', underline=0)
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
      par_button2 = Button(par_rowLayout1, text="Button 1")
      par_button2.pack(side=LEFT, anchor=NW)
      par_button3 = Button(par_rowLayout1, text="Button 2")
      par_button3.pack(side=LEFT, anchor=NW)
      par_button4 = Button(par_rowLayout1, text="Button 3")
      par_button4.pack(side=LEFT, anchor=NW)
      par_button5 = Button(par_rowLayout1, text="Button 4")
      par_button5.pack(side=LEFT, anchor=NW)
      par_button6 = Button(par_rowLayout1, text="Button 5")
      par_button6.pack(side=LEFT, anchor=NW)
      par_rowLayout1.pack(side=TOP, anchor=NW)
      par_rowLayout7 = Frame(self, relief=RIDGE, bd=4, bg='#eeee88')
      par_colLayout8 = Frame(par_rowLayout7, relief=RIDGE, bd=4, bg='#8888ee')
      par_label9 = Label(par_colLayout8, text="First column!")
      par_label9.pack(side=TOP, anchor=NW)
      par_button10 = Button(par_colLayout8, text="press me")
      par_button10.pack(side=TOP, anchor=NW)
      par_colLayout8.pack(side=LEFT, anchor=NW)
      par_colLayout11 = Frame(par_rowLayout7, relief=RIDGE, bd=4, bg='#8888ee')
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
      par_rowLayout14.pack(side=TOP, anchor=NW)
      check1 = Checkbutton(par_colLayout11, text='really do it?')
      check1.pack(side=TOP, anchor=NW)
      check1.config(command=self.check1_toggled)
      par_colLayout11.pack(side=LEFT, anchor=NW)
      par_colLayout17 = Frame(par_rowLayout7, relief=RIDGE, bd=4, bg='#8888ee')
      par_label18 = Label(par_colLayout17, text="Which units:")
      par_label18.pack(side=TOP, anchor=NW)
      inchRB = Radiobutton(par_colLayout17, text='inches', value='inches')
      inchRB.pack(side=TOP, anchor=NW)
      inchRB.config(command=self.inchRB_toggled)
      feetRB = Radiobutton(par_colLayout17, text='feet', value='feet')
      feetRB.pack(side=TOP, anchor=NW)
      feetRB.config(command=self.feetRB_toggled)
      yardRB = Radiobutton(par_colLayout17, text='yards', value='yards')
      yardRB.pack(side=TOP, anchor=NW)
      yardRB.config(command=self.yardRB_toggled)
      mileRB = Radiobutton(par_colLayout17, text='miles', value='miles')
      mileRB.pack(side=TOP, anchor=NW)
      mileRB.config(command=self.mileRB_toggled)
      par_colLayout17.pack(side=LEFT, anchor=NW)
      table1 = Frame(par_rowLayout7, relief=RIDGE, bd=4, bg='#ee8888')
      #getStartCode() td
      par_checkBox19 = Checkbutton(table1, text='Apple')
      par_checkBox19.grid(column=0, row=0, stick=N+W)
      #*** end td
      #getStartCode() td
      par_checkBox20 = Checkbutton(table1, text='Pear')
      par_checkBox20.grid(column=1, row=0, stick=N+W)
      #*** end td
      #getStartCode() td
      par_checkBox21 = Checkbutton(table1, text='Banana')
      par_checkBox21.grid(column=0, row=1, stick=N+W)
      #*** end td
      #getStartCode() td
      par_checkBox22 = Checkbutton(table1, text='Orange')
      par_checkBox22.grid(column=1, row=1, stick=N+W)
      #*** end td
      #getStartCode() td
      par_checkBox23 = Checkbutton(table1, text='Prune')
      par_checkBox23.grid(column=0, row=2, stick=N+W)
      #*** end td
      #getStartCode() td
      par_checkBox24 = Checkbutton(table1, text='Grape')
      par_checkBox24.grid(column=1, row=2, stick=N+W)
      #*** end td
      table1.pack(side=LEFT, anchor=NW)
      par_rowLayout7.pack(side=TOP, anchor=NW)
      par_rowLayout25 = Frame(self, relief=RIDGE, bd=4, bg='#eeee88')
      par_colLayout26 = Frame(par_rowLayout25, relief=RIDGE, bd=4, bg='#8888ee')
      par_label27 = Label(par_colLayout26, text="First column!")
      par_label27.pack(side=TOP, anchor=NW)
      par_button28 = Button(par_colLayout26, text="press me")
      par_button28.pack(side=TOP, anchor=NW)
      par_colLayout26.pack(side=LEFT, anchor=NW)
      par_colLayout29 = Frame(par_rowLayout25, relief=RIDGE, bd=4, bg='#8888ee')
      par_label30 = Label(par_colLayout29, text="Type stuff in here:")
      par_label30.pack(side=TOP, anchor=NW)
      par_textField31 = Text(par_colLayout29, height=1, width=20)
      par_textField31.insert("1.0", "abcd")
      par_textField31.pack(side=TOP, anchor=NW)
      par_rowLayout32 = Frame(par_colLayout29, relief=RIDGE, bd=4, bg='#eeee88')
      par_button33 = Button(par_rowLayout32, text="Button 6")
      par_button33.pack(side=LEFT, anchor=NW)
      par_button34 = Button(par_rowLayout32, text="Button 7")
      par_button34.pack(side=LEFT, anchor=NW)
      par_rowLayout32.pack(side=TOP, anchor=NW)
      check1 = Checkbutton(par_colLayout29, text='really do it?')
      check1.pack(side=TOP, anchor=NW)
      check1.config(command=self.check1_toggled)
      par_colLayout29.pack(side=LEFT, anchor=NW)
      par_colLayout35 = Frame(par_rowLayout25, relief=RIDGE, bd=4, bg='#8888ee')
      par_label36 = Label(par_colLayout35, text="Which units:")
      par_label36.pack(side=TOP, anchor=NW)
      inchRB = Radiobutton(par_colLayout35, text='inches', value='inches')
      inchRB.pack(side=TOP, anchor=NW)
      inchRB.config(command=self.inchRB_toggled)
      feetRB = Radiobutton(par_colLayout35, text='feet', value='feet')
      feetRB.pack(side=TOP, anchor=NW)
      feetRB.config(command=self.feetRB_toggled)
      yardRB = Radiobutton(par_colLayout35, text='yards', value='yards')
      yardRB.pack(side=TOP, anchor=NW)
      yardRB.config(command=self.yardRB_toggled)
      mileRB = Radiobutton(par_colLayout35, text='miles', value='miles')
      mileRB.pack(side=TOP, anchor=NW)
      mileRB.config(command=self.mileRB_toggled)
      par_colLayout35.pack(side=LEFT, anchor=NW)
      table1 = Frame(par_rowLayout25, relief=RIDGE, bd=4, bg='#ee8888')
      #getStartCode() td
      par_checkBox37 = Checkbutton(table1, text='Apple')
      par_checkBox37.grid(column=0, row=0, stick=N+W)
      #*** end td
      #getStartCode() td
      par_checkBox38 = Checkbutton(table1, text='Pear')
      par_checkBox38.grid(column=1, row=0, stick=N+W)
      #*** end td
      #getStartCode() td
      par_checkBox39 = Checkbutton(table1, text='Banana')
      par_checkBox39.grid(column=0, row=1, stick=N+W)
      #*** end td
      #getStartCode() td
      par_checkBox40 = Checkbutton(table1, text='Orange')
      par_checkBox40.grid(column=1, row=1, stick=N+W)
      #*** end td
      #getStartCode() td
      par_checkBox41 = Checkbutton(table1, text='Prune')
      par_checkBox41.grid(column=0, row=2, stick=N+W)
      #*** end td
      #getStartCode() td
      par_checkBox42 = Checkbutton(table1, text='Grape')
      par_checkBox42.grid(column=1, row=2, stick=N+W)
      #*** end td
      table1.pack(side=LEFT, anchor=NW)
      par_rowLayout25.pack(side=TOP, anchor=NW)
      par_rowLayout43 = Frame(self, relief=RIDGE, bd=4, bg='#eeee88')
      par_colLayout44 = Frame(par_rowLayout43, relief=RIDGE, bd=4, bg='#8888ee')
      par_label45 = Label(par_colLayout44, text="First column!")
      par_label45.pack(side=TOP, anchor=NW)
      par_button46 = Button(par_colLayout44, text="press me")
      par_button46.pack(side=TOP, anchor=NW)
      par_colLayout44.pack(side=LEFT, anchor=NW)
      par_colLayout47 = Frame(par_rowLayout43, relief=RIDGE, bd=4, bg='#8888ee')
      par_label48 = Label(par_colLayout47, text="Type stuff in here:")
      par_label48.pack(side=TOP, anchor=NW)
      par_textField49 = Text(par_colLayout47, height=1, width=20)
      par_textField49.insert("1.0", "abcd")
      par_textField49.pack(side=TOP, anchor=NW)
      par_rowLayout50 = Frame(par_colLayout47, relief=RIDGE, bd=4, bg='#eeee88')
      par_button51 = Button(par_rowLayout50, text="Button 6")
      par_button51.pack(side=LEFT, anchor=NW)
      par_button52 = Button(par_rowLayout50, text="Button 7")
      par_button52.pack(side=LEFT, anchor=NW)
      par_rowLayout50.pack(side=TOP, anchor=NW)
      check1 = Checkbutton(par_colLayout47, text='really do it?')
      check1.pack(side=TOP, anchor=NW)
      check1.config(command=self.check1_toggled)
      par_colLayout47.pack(side=LEFT, anchor=NW)
      par_colLayout53 = Frame(par_rowLayout43, relief=RIDGE, bd=4, bg='#8888ee')
      par_label54 = Label(par_colLayout53, text="Which units:")
      par_label54.pack(side=TOP, anchor=NW)
      inchRB = Radiobutton(par_colLayout53, text='inches', value='inches')
      inchRB.pack(side=TOP, anchor=NW)
      inchRB.config(command=self.inchRB_toggled)
      feetRB = Radiobutton(par_colLayout53, text='feet', value='feet')
      feetRB.pack(side=TOP, anchor=NW)
      feetRB.config(command=self.feetRB_toggled)
      yardRB = Radiobutton(par_colLayout53, text='yards', value='yards')
      yardRB.pack(side=TOP, anchor=NW)
      yardRB.config(command=self.yardRB_toggled)
      mileRB = Radiobutton(par_colLayout53, text='miles', value='miles')
      mileRB.pack(side=TOP, anchor=NW)
      mileRB.config(command=self.mileRB_toggled)
      par_colLayout53.pack(side=LEFT, anchor=NW)
      table1 = Frame(par_rowLayout43, relief=RIDGE, bd=4, bg='#ee8888')
      #getStartCode() td
      par_checkBox55 = Checkbutton(table1, text='Apple')
      par_checkBox55.grid(column=0, row=0, stick=N+W)
      #*** end td
      #getStartCode() td
      par_checkBox56 = Checkbutton(table1, text='Pear')
      par_checkBox56.grid(column=1, row=0, stick=N+W)
      #*** end td
      #getStartCode() td
      par_checkBox57 = Checkbutton(table1, text='Banana')
      par_checkBox57.grid(column=0, row=1, stick=N+W)
      #*** end td
      #getStartCode() td
      par_checkBox58 = Checkbutton(table1, text='Orange')
      par_checkBox58.grid(column=1, row=1, stick=N+W)
      #*** end td
      #getStartCode() td
      par_checkBox59 = Checkbutton(table1, text='Prune')
      par_checkBox59.grid(column=0, row=2, stick=N+W)
      #*** end td
      #getStartCode() td
      par_checkBox60 = Checkbutton(table1, text='Grape')
      par_checkBox60.grid(column=1, row=2, stick=N+W)
      #*** end td
      table1.pack(side=LEFT, anchor=NW)
      par_rowLayout43.pack(side=TOP, anchor=NW)

#***** methods to be redefined

   def New_pressed(self):
      print '[MyBigWindow New_pressed]'      

   def Open_pressed(self):
      print '[MyBigWindow Open_pressed]'      

   def Save_pressed(self):
      print '[MyBigWindow Save_pressed]'      

   def SaveAs_pressed(self):
      print '[MyBigWindow SaveAs_pressed]'      

   def Exit_pressed(self):
      print '[MyBigWindow Exit_pressed]'      

   def New_pressed(self):
      print '[MyBigWindow New_pressed]'      

   def Open_pressed(self):
      print '[MyBigWindow Open_pressed]'      

   def Save_pressed(self):
      print '[MyBigWindow Save_pressed]'      

   def SaveAs_pressed(self):
      print '[MyBigWindow SaveAs_pressed]'      

   def Exit_pressed(self):
      print '[MyBigWindow Exit_pressed]'      

   def New_pressed(self):
      print '[MyBigWindow New_pressed]'      

   def Open_pressed(self):
      print '[MyBigWindow Open_pressed]'      

   def Save_pressed(self):
      print '[MyBigWindow Save_pressed]'      

   def SaveAs_pressed(self):
      print '[MyBigWindow SaveAs_pressed]'      

   def Exit_pressed(self):
      print '[MyBigWindow Exit_pressed]'      

   def Copy_pressed(self):
      print '[MyBigWindow Copy_pressed]'      

   def Cut_pressed(self):
      print '[MyBigWindow Cut_pressed]'      

   def Paste_pressed(self):
      print '[MyBigWindow Paste_pressed]'      

   def About_pressed(self):
      print '[MyBigWindow About_pressed]'      

   def GettingStarted_pressed(self):
      print '[MyBigWindow GettingStarted_pressed]'      

   def Reference_pressed(self):
      print '[MyBigWindow Reference_pressed]'      

   def check1_toggled(self):
      print '[MyBigWindow check1_toggled]'      

   def inchRB_toggled(self):
      print '[MyBigWindow inchRB_toggled]'      

   def feetRB_toggled(self):
      print '[MyBigWindow feetRB_toggled]'      

   def yardRB_toggled(self):
      print '[MyBigWindow yardRB_toggled]'      

   def mileRB_toggled(self):
      print '[MyBigWindow mileRB_toggled]'      

   def check1_toggled(self):
      print '[MyBigWindow check1_toggled]'      

   def inchRB_toggled(self):
      print '[MyBigWindow inchRB_toggled]'      

   def feetRB_toggled(self):
      print '[MyBigWindow feetRB_toggled]'      

   def yardRB_toggled(self):
      print '[MyBigWindow yardRB_toggled]'      

   def mileRB_toggled(self):
      print '[MyBigWindow mileRB_toggled]'      

   def check1_toggled(self):
      print '[MyBigWindow check1_toggled]'      

   def inchRB_toggled(self):
      print '[MyBigWindow inchRB_toggled]'      

   def feetRB_toggled(self):
      print '[MyBigWindow feetRB_toggled]'      

   def yardRB_toggled(self):
      print '[MyBigWindow yardRB_toggled]'      

   def mileRB_toggled(self):
      print '[MyBigWindow mileRB_toggled]'      

#***** end of methods to be redefined

#/////////////////////////////////////////////////////////////////////

if __name__=='__main__':
   MyBigWindow().mainloop()

#/////////////////////////////////////////////////////////////////////

#(end simple6.py)
