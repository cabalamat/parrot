# tokpos.py
#
# (C) 2000 Philip Hunt
# Released under the GNU General Public Licence
#
# Contains Philip Hunt's extensions to version 0.5 of
# John Aycock's SPARK parsing framework. The purpose of the
# extensions is to cause tokens (instances of PosToken) to
# remember the line and column that they started at in the 
# input source file.

# Last altered: 12-Feb-2000
# History:
# 12-Feb-2000 PhilHunt: created

from generic import *

debug = 0 

#===========================================================
######  PosScanner                                    ######
#===========================================================

class PosScanner(GenericScanner):

   def tokenize(self, s):
      colNum = 1
      rowNum = 1
      while s:
         m = self.re.match(s)
         assert m
         groups = m.groups()
         
         #>>>> phil:
         newColNum = self.colNum = colNum
         newRowNum = self.rowNum = rowNum
         for char in s[:m.end()]:
            if char == '\012':
               newRowNum = newRowNum + 1
               newColNum = 1
            else:
               newColNum = newColNum + 1
         #<<<<     
         if debug: print "$ r:c %s:%s (%s)'%s' %s:%s " % (
            rowNum, colNum, m.end(), s[:m.end()], 
            newRowNum, newColNum
            )
               
         for i in range(len(groups)):
            #print "$$ i=%s groups[%s]={%s} $$" % (i, i, groups[i])
            if groups[i] and self.index2func.has_key(i):
               self.index2func[i](groups[i])
         #//for i
         s = s[m.end():]
         
         rowNum = newRowNum
         colNum = newColNum
      #//while s

   def addToken(self, tokenType, tokenValue):
      self.rv.append(PosToken(tokenType, tokenValue, 
         self.rowNum, self.colNum))
 
#===========================================================
######  PosToken                                      ######
#===========================================================

class PosToken:
   def __init__(self, type, attr=None, line=0, col=0):
      self.type = type
      self.attr = attr
      self.line = line
      self.col = col

   def __cmp__(self, o):
      return cmp(self.type, o)

   def __repr__(self):
      x = self.type
      if self.attr != None: 
         x = '(' + x +' ' + repr(self.attr) + ')'
      else:
         x = self.type
      if self.line > 0:
         x = x + (':%s:%s' %(self.line, self.col))
      return x
      

# end tokpos.py
