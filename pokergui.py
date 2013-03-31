# pokergui.py
#
# This file was autogenerated by Parrot's PytkBackend module

from Tkinter import *
from Dialog import Dialog


#/////////////////////////////////////////////////////////////////////

class PokerGui(Frame):

   def  __init__(self, parent=None):
      Frame.__init__(self, parent)
      self.pack()
      self.createMenuBar()
      self.createGUI()
      self.master.title("Poker adviser")
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
      mbutton['menu'] = menu

   def createGUI(self):
      par_colLayout1 = Frame(self, relief=RIDGE, bd=4, bg='#8888ee')
      topLabel = Label(par_colLayout1, text="topLabel")
      topLabel.pack(side=TOP, anchor=NW)
      canvas = Label(par_colLayout1, text="--- canvas will go here ---")
      canvas.pack(side=TOP, anchor=NW)
      cardChooser = Frame(par_colLayout1, relief=RIDGE, bd=4, bg='#8888ee')
      par_label2 = Label(cardChooser, text="card chooser")
      par_label2.pack(side=TOP, anchor=NW)
      cardChooserTable = Frame(cardChooser, relief=RIDGE, bd=4, bg='#ee8888')
      #getStartCode() td
      card_As = Button(cardChooserTable, text="As")
      card_As.config(command=self.card_As_pressed)
      card_As.grid(column=0, row=0, stick=N+W)
      #*** end td
      #getStartCode() td
      card_Ks = Button(cardChooserTable, text="Ks")
      card_Ks.config(command=self.card_Ks_pressed)
      card_Ks.grid(column=1, row=0, stick=N+W)
      #*** end td
      #getStartCode() td
      card_Qs = Button(cardChooserTable, text="Qs")
      card_Qs.config(command=self.card_Qs_pressed)
      card_Qs.grid(column=2, row=0, stick=N+W)
      #*** end td
      #getStartCode() td
      card_Js = Button(cardChooserTable, text="Js")
      card_Js.config(command=self.card_Js_pressed)
      card_Js.grid(column=3, row=0, stick=N+W)
      #*** end td
      #getStartCode() td
      card_Ts = Button(cardChooserTable, text="Ts")
      card_Ts.config(command=self.card_Ts_pressed)
      card_Ts.grid(column=4, row=0, stick=N+W)
      #*** end td
      #getStartCode() td
      card_9s = Button(cardChooserTable, text="9s")
      card_9s.config(command=self.card_9s_pressed)
      card_9s.grid(column=5, row=0, stick=N+W)
      #*** end td
      #getStartCode() td
      card_8s = Button(cardChooserTable, text="8s")
      card_8s.config(command=self.card_8s_pressed)
      card_8s.grid(column=6, row=0, stick=N+W)
      #*** end td
      #getStartCode() td
      card_7s = Button(cardChooserTable, text="7s")
      card_7s.config(command=self.card_7s_pressed)
      card_7s.grid(column=7, row=0, stick=N+W)
      #*** end td
      #getStartCode() td
      card_6s = Button(cardChooserTable, text="6s")
      card_6s.config(command=self.card_6s_pressed)
      card_6s.grid(column=8, row=0, stick=N+W)
      #*** end td
      #getStartCode() td
      card_5s = Button(cardChooserTable, text="5s")
      card_5s.config(command=self.card_5s_pressed)
      card_5s.grid(column=9, row=0, stick=N+W)
      #*** end td
      #getStartCode() td
      card_4s = Button(cardChooserTable, text="4s")
      card_4s.config(command=self.card_4s_pressed)
      card_4s.grid(column=10, row=0, stick=N+W)
      #*** end td
      #getStartCode() td
      card_3s = Button(cardChooserTable, text="3s")
      card_3s.config(command=self.card_3s_pressed)
      card_3s.grid(column=11, row=0, stick=N+W)
      #*** end td
      #getStartCode() td
      card_2s = Button(cardChooserTable, text="2s")
      card_2s.config(command=self.card_2s_pressed)
      card_2s.grid(column=12, row=0, stick=N+W)
      #*** end td
      #getStartCode() td
      card_Ah = Button(cardChooserTable, text="Ah")
      card_Ah.config(command=self.card_Ah_pressed)
      card_Ah.grid(column=0, row=1, stick=N+W)
      #*** end td
      #getStartCode() td
      card_Kh = Button(cardChooserTable, text="Kh")
      card_Kh.config(command=self.card_Kh_pressed)
      card_Kh.grid(column=1, row=1, stick=N+W)
      #*** end td
      #getStartCode() td
      card_Qh = Button(cardChooserTable, text="Qh")
      card_Qh.config(command=self.card_Qh_pressed)
      card_Qh.grid(column=2, row=1, stick=N+W)
      #*** end td
      #getStartCode() td
      card_Jh = Button(cardChooserTable, text="Jh")
      card_Jh.config(command=self.card_Jh_pressed)
      card_Jh.grid(column=3, row=1, stick=N+W)
      #*** end td
      #getStartCode() td
      card_Th = Button(cardChooserTable, text="Th")
      card_Th.config(command=self.card_Th_pressed)
      card_Th.grid(column=4, row=1, stick=N+W)
      #*** end td
      #getStartCode() td
      card_9h = Button(cardChooserTable, text="9h")
      card_9h.config(command=self.card_9h_pressed)
      card_9h.grid(column=5, row=1, stick=N+W)
      #*** end td
      #getStartCode() td
      card_8h = Button(cardChooserTable, text="8h")
      card_8h.config(command=self.card_8h_pressed)
      card_8h.grid(column=6, row=1, stick=N+W)
      #*** end td
      #getStartCode() td
      card_7h = Button(cardChooserTable, text="7h")
      card_7h.config(command=self.card_7h_pressed)
      card_7h.grid(column=7, row=1, stick=N+W)
      #*** end td
      #getStartCode() td
      card_6h = Button(cardChooserTable, text="6h")
      card_6h.config(command=self.card_6h_pressed)
      card_6h.grid(column=8, row=1, stick=N+W)
      #*** end td
      #getStartCode() td
      card_5h = Button(cardChooserTable, text="5h")
      card_5h.config(command=self.card_5h_pressed)
      card_5h.grid(column=9, row=1, stick=N+W)
      #*** end td
      #getStartCode() td
      card_4h = Button(cardChooserTable, text="4h")
      card_4h.config(command=self.card_4h_pressed)
      card_4h.grid(column=10, row=1, stick=N+W)
      #*** end td
      #getStartCode() td
      card_3h = Button(cardChooserTable, text="3h")
      card_3h.config(command=self.card_3h_pressed)
      card_3h.grid(column=11, row=1, stick=N+W)
      #*** end td
      #getStartCode() td
      card_2h = Button(cardChooserTable, text="2h")
      card_2h.config(command=self.card_2h_pressed)
      card_2h.grid(column=12, row=1, stick=N+W)
      #*** end td
      #getStartCode() td
      card_Ac = Button(cardChooserTable, text="Ac")
      card_Ac.config(command=self.card_Ac_pressed)
      card_Ac.grid(column=0, row=2, stick=N+W)
      #*** end td
      #getStartCode() td
      card_Kc = Button(cardChooserTable, text="Kc")
      card_Kc.config(command=self.card_Kc_pressed)
      card_Kc.grid(column=1, row=2, stick=N+W)
      #*** end td
      #getStartCode() td
      card_Qc = Button(cardChooserTable, text="Qc")
      card_Qc.config(command=self.card_Qc_pressed)
      card_Qc.grid(column=2, row=2, stick=N+W)
      #*** end td
      #getStartCode() td
      card_Jc = Button(cardChooserTable, text="Jc")
      card_Jc.config(command=self.card_Jc_pressed)
      card_Jc.grid(column=3, row=2, stick=N+W)
      #*** end td
      #getStartCode() td
      card_Tc = Button(cardChooserTable, text="Tc")
      card_Tc.config(command=self.card_Tc_pressed)
      card_Tc.grid(column=4, row=2, stick=N+W)
      #*** end td
      #getStartCode() td
      card_9c = Button(cardChooserTable, text="9c")
      card_9c.config(command=self.card_9c_pressed)
      card_9c.grid(column=5, row=2, stick=N+W)
      #*** end td
      #getStartCode() td
      card_8c = Button(cardChooserTable, text="8c")
      card_8c.config(command=self.card_8c_pressed)
      card_8c.grid(column=6, row=2, stick=N+W)
      #*** end td
      #getStartCode() td
      card_7c = Button(cardChooserTable, text="7c")
      card_7c.config(command=self.card_7c_pressed)
      card_7c.grid(column=7, row=2, stick=N+W)
      #*** end td
      #getStartCode() td
      card_6c = Button(cardChooserTable, text="6c")
      card_6c.config(command=self.card_6c_pressed)
      card_6c.grid(column=8, row=2, stick=N+W)
      #*** end td
      #getStartCode() td
      card_5c = Button(cardChooserTable, text="5c")
      card_5c.config(command=self.card_5c_pressed)
      card_5c.grid(column=9, row=2, stick=N+W)
      #*** end td
      #getStartCode() td
      card_4c = Button(cardChooserTable, text="4c")
      card_4c.config(command=self.card_4c_pressed)
      card_4c.grid(column=10, row=2, stick=N+W)
      #*** end td
      #getStartCode() td
      card_3c = Button(cardChooserTable, text="3c")
      card_3c.config(command=self.card_3c_pressed)
      card_3c.grid(column=11, row=2, stick=N+W)
      #*** end td
      #getStartCode() td
      card_2c = Button(cardChooserTable, text="2c")
      card_2c.config(command=self.card_2c_pressed)
      card_2c.grid(column=12, row=2, stick=N+W)
      #*** end td
      #getStartCode() td
      card_Ad = Button(cardChooserTable, text="Ad")
      card_Ad.config(command=self.card_Ad_pressed)
      card_Ad.grid(column=0, row=3, stick=N+W)
      #*** end td
      #getStartCode() td
      card_Kd = Button(cardChooserTable, text="Kd")
      card_Kd.config(command=self.card_Kd_pressed)
      card_Kd.grid(column=1, row=3, stick=N+W)
      #*** end td
      #getStartCode() td
      card_Qd = Button(cardChooserTable, text="Qd")
      card_Qd.config(command=self.card_Qd_pressed)
      card_Qd.grid(column=2, row=3, stick=N+W)
      #*** end td
      #getStartCode() td
      card_Jd = Button(cardChooserTable, text="Jd")
      card_Jd.config(command=self.card_Jd_pressed)
      card_Jd.grid(column=3, row=3, stick=N+W)
      #*** end td
      #getStartCode() td
      card_Td = Button(cardChooserTable, text="Td")
      card_Td.config(command=self.card_Td_pressed)
      card_Td.grid(column=4, row=3, stick=N+W)
      #*** end td
      #getStartCode() td
      card_9d = Button(cardChooserTable, text="9d")
      card_9d.config(command=self.card_9d_pressed)
      card_9d.grid(column=5, row=3, stick=N+W)
      #*** end td
      #getStartCode() td
      card_8d = Button(cardChooserTable, text="8d")
      card_8d.config(command=self.card_8d_pressed)
      card_8d.grid(column=6, row=3, stick=N+W)
      #*** end td
      #getStartCode() td
      card_7d = Button(cardChooserTable, text="7d")
      card_7d.config(command=self.card_7d_pressed)
      card_7d.grid(column=7, row=3, stick=N+W)
      #*** end td
      #getStartCode() td
      card_6d = Button(cardChooserTable, text="6d")
      card_6d.config(command=self.card_6d_pressed)
      card_6d.grid(column=8, row=3, stick=N+W)
      #*** end td
      #getStartCode() td
      card_5d = Button(cardChooserTable, text="5d")
      card_5d.config(command=self.card_5d_pressed)
      card_5d.grid(column=9, row=3, stick=N+W)
      #*** end td
      #getStartCode() td
      card_4d = Button(cardChooserTable, text="4d")
      card_4d.config(command=self.card_4d_pressed)
      card_4d.grid(column=10, row=3, stick=N+W)
      #*** end td
      #getStartCode() td
      card_3d = Button(cardChooserTable, text="3d")
      card_3d.config(command=self.card_3d_pressed)
      card_3d.grid(column=11, row=3, stick=N+W)
      #*** end td
      #getStartCode() td
      card_2d = Button(cardChooserTable, text="2d")
      card_2d.config(command=self.card_2d_pressed)
      card_2d.grid(column=12, row=3, stick=N+W)
      #*** end td
      cardChooserTable.pack(side=TOP, anchor=NW)
      cardChooser.pack(side=TOP, anchor=NW)
      probability = Frame(par_colLayout1, relief=RIDGE, bd=4, bg='#8888ee')
      pWin = Label(probability, text="win probability    20%    1:4")
      pWin.pack(side=TOP, anchor=NW)
      pWincanvas = Label(probability, text="--- pWinCanvas ---")
      pWincanvas.pack(side=TOP, anchor=NW)
      probability.pack(side=TOP, anchor=NW)
      par_colLayout1.pack(side=TOP, anchor=NW)

#***** methods to be redefined

   def New_pressed(self):
      print '[PokerGui New_pressed]'      

   def Open_pressed(self):
      print '[PokerGui Open_pressed]'      

   def Save_pressed(self):
      print '[PokerGui Save_pressed]'      

   def Copy_pressed(self):
      print '[PokerGui Copy_pressed]'      

   def Cut_pressed(self):
      print '[PokerGui Cut_pressed]'      

   def Paste_pressed(self):
      print '[PokerGui Paste_pressed]'      

   def About_pressed(self):
      print '[PokerGui About_pressed]'      

   def GettingStarted_pressed(self):
      print '[PokerGui GettingStarted_pressed]'      

   def card_As_pressed(self):
      print '[PokerGui card_As_pressed]'      

   def card_Ks_pressed(self):
      print '[PokerGui card_Ks_pressed]'      

   def card_Qs_pressed(self):
      print '[PokerGui card_Qs_pressed]'      

   def card_Js_pressed(self):
      print '[PokerGui card_Js_pressed]'      

   def card_Ts_pressed(self):
      print '[PokerGui card_Ts_pressed]'      

   def card_9s_pressed(self):
      print '[PokerGui card_9s_pressed]'      

   def card_8s_pressed(self):
      print '[PokerGui card_8s_pressed]'      

   def card_7s_pressed(self):
      print '[PokerGui card_7s_pressed]'      

   def card_6s_pressed(self):
      print '[PokerGui card_6s_pressed]'      

   def card_5s_pressed(self):
      print '[PokerGui card_5s_pressed]'      

   def card_4s_pressed(self):
      print '[PokerGui card_4s_pressed]'      

   def card_3s_pressed(self):
      print '[PokerGui card_3s_pressed]'      

   def card_2s_pressed(self):
      print '[PokerGui card_2s_pressed]'      

   def card_Ah_pressed(self):
      print '[PokerGui card_Ah_pressed]'      

   def card_Kh_pressed(self):
      print '[PokerGui card_Kh_pressed]'      

   def card_Qh_pressed(self):
      print '[PokerGui card_Qh_pressed]'      

   def card_Jh_pressed(self):
      print '[PokerGui card_Jh_pressed]'      

   def card_Th_pressed(self):
      print '[PokerGui card_Th_pressed]'      

   def card_9h_pressed(self):
      print '[PokerGui card_9h_pressed]'      

   def card_8h_pressed(self):
      print '[PokerGui card_8h_pressed]'      

   def card_7h_pressed(self):
      print '[PokerGui card_7h_pressed]'      

   def card_6h_pressed(self):
      print '[PokerGui card_6h_pressed]'      

   def card_5h_pressed(self):
      print '[PokerGui card_5h_pressed]'      

   def card_4h_pressed(self):
      print '[PokerGui card_4h_pressed]'      

   def card_3h_pressed(self):
      print '[PokerGui card_3h_pressed]'      

   def card_2h_pressed(self):
      print '[PokerGui card_2h_pressed]'      

   def card_Ac_pressed(self):
      print '[PokerGui card_Ac_pressed]'      

   def card_Kc_pressed(self):
      print '[PokerGui card_Kc_pressed]'      

   def card_Qc_pressed(self):
      print '[PokerGui card_Qc_pressed]'      

   def card_Jc_pressed(self):
      print '[PokerGui card_Jc_pressed]'      

   def card_Tc_pressed(self):
      print '[PokerGui card_Tc_pressed]'      

   def card_9c_pressed(self):
      print '[PokerGui card_9c_pressed]'      

   def card_8c_pressed(self):
      print '[PokerGui card_8c_pressed]'      

   def card_7c_pressed(self):
      print '[PokerGui card_7c_pressed]'      

   def card_6c_pressed(self):
      print '[PokerGui card_6c_pressed]'      

   def card_5c_pressed(self):
      print '[PokerGui card_5c_pressed]'      

   def card_4c_pressed(self):
      print '[PokerGui card_4c_pressed]'      

   def card_3c_pressed(self):
      print '[PokerGui card_3c_pressed]'      

   def card_2c_pressed(self):
      print '[PokerGui card_2c_pressed]'      

   def card_Ad_pressed(self):
      print '[PokerGui card_Ad_pressed]'      

   def card_Kd_pressed(self):
      print '[PokerGui card_Kd_pressed]'      

   def card_Qd_pressed(self):
      print '[PokerGui card_Qd_pressed]'      

   def card_Jd_pressed(self):
      print '[PokerGui card_Jd_pressed]'      

   def card_Td_pressed(self):
      print '[PokerGui card_Td_pressed]'      

   def card_9d_pressed(self):
      print '[PokerGui card_9d_pressed]'      

   def card_8d_pressed(self):
      print '[PokerGui card_8d_pressed]'      

   def card_7d_pressed(self):
      print '[PokerGui card_7d_pressed]'      

   def card_6d_pressed(self):
      print '[PokerGui card_6d_pressed]'      

   def card_5d_pressed(self):
      print '[PokerGui card_5d_pressed]'      

   def card_4d_pressed(self):
      print '[PokerGui card_4d_pressed]'      

   def card_3d_pressed(self):
      print '[PokerGui card_3d_pressed]'      

   def card_2d_pressed(self):
      print '[PokerGui card_2d_pressed]'      

#***** end of methods to be redefined

#/////////////////////////////////////////////////////////////////////

if __name__=='__main__':
   PokerGui().mainloop()

#/////////////////////////////////////////////////////////////////////

#(end pokergui.py)
