# test.py
# 
# (c)1999 Philip Hunt
# Released under the GNU General Public Licence
#
# Program to test parts of Parrot

# Last altered: 18-Aug-1999
# History:
# 7-Aug-1999 PhilHunt: created



#-----------------------------------------------------------
# write a string into a file

def writeFile(filename, newValue):
   # at a later date, add code here to create directories
   # if they don't exist
   f = open(filename, 'w')
   f.write(newValue)
   f.close()

#-----------------------------------------------------------
# test me:

from inrep import * 
from HtmlBackend import *

import pprint
pp = pprint.PrettyPrinter(indent=4)

if __name__=='__main__':
   gi = GlobalInfo()

   cont1 = UIContainer('colLayout', gi)

   comp1 = UIComponent('button', cont1)
   comp1.attr['id'] = 'button1'
   comp1.attr['text'] = 'Press me'

   comp2 = UIComponent('button', cont1)
   comp2.attr['id'] = 'button2'
   comp2.attr['text'] = 'Don\'t press me'

   cp3 = UIComponent('label', cont1)
   cp3.attr['id'] = 'label1'
   cp3.attr['text'] = 'I\'m a label'

   cp4 = UIComponent('textField', cont1)
   cp4.attr['id'] = 'TF1'
   cp4.attr['text'] = 'write here'
   cp4.attr['cols'] = '12'

   print '---- comp1:'
   comp1.outputNormalized()
   print '---- cont1:'
   cont1.outputNormalized()
   print '---- gi:'
   gi.outputNormalized()
   
   #===== now test HTML back end:
   hb = Html_GLOBAL()
   hb.useUI(gi)
   code = hb.produceCode()
   print '-------------hb.asString():\n' + hb.asString()
   print '-------------code:', code
   writeFile("test.html", code)


#-----------------------------------------------------------


#end 
