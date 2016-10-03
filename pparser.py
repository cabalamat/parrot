# pparser.py
# 
# (c)1999-2000 Philip Hunt
# Released under the GNU General Public Licence
#
# Parser for Parrot *.par files. 
# This is used to scan Parrot files and put them into a
# representation in the form of instances of the classes
# defined in inrep.py.
#
# (Uses generic.py, which is John Aycock's generic parsing
# library)
#

# Last altered: 12-Feb-2000
# History:
# 13-Aug-1999 PhilHunt: created
#
# 18-Aug-1999 PhilHunt: 1st working version!
#
# 7-Sep-1999 id, text, normal attributes in any order;
# added comments.

from tokpos import *
from string import *

from inrep import *


debug = 0

#===========================================================
######  Debugging                                     ######
#===========================================================

def sayWhere(info):
   if debug:
      import traceback
      fromFun = traceback.extract_stack()[-2]
      print ">>> %s() %s" %(fromFun[2], info)




#===========================================================
######  Lexical Analysis                              ######
#===========================================================

class ScannerNoRW(PosScanner):

   def __init__(self):
      GenericScanner.__init__(self)

   def tokenize(self, input):
      self.rv = [ ]
      PosScanner.tokenize(self, input)
      return self.rv

   # later, add to my ScannerWithLineNumbers class
   #def addToken(self, tokenType, tokenValue):
   #   self.rv.append(Token(tokenType, tokenValue, 
   #      self.rowNum, self.colNum))
         

   def t_whitespace(self, s):
      r' \s+ '
      pass
      
   def t_comment1(self, s):
      r' //[^\n]*\n '
      #print "got comment1 <<<<{%s}>>>>" % s
      pass
      
   def t_comment2(self, s):
      r' /\*(.|\n)*?\*/ '
      #print "got comment2 <<<<{%s}>>>>" % s
      pass

   def t_ATSIGN(self, s):
      r' @ '
      self.addToken('@', None)

   def t_EQUALS(self, s):
      r' = '
      self.addToken('=', None)
      
   def t_DOT(self, s):
      r' \. '
      self.addToken('DOT', None)

   def t_LCURLY(self, s):
      r' \{ '
      self.addToken('{', None)

   def t_RCURLY(self, s):
      r' \} '
      self.addToken('}', None)

   def t_STRING(self, s):
      r' \"[^"]*\" '
      self.addToken('STRING',s[1:-1])

   def t_IDENTIFIER(self, s):
      r' [A-Za-z_][A-Za-z_0-9]* '
      self.addToken('IDENTIFIER', s) 
       
   def t_NUMBER(self, s):
      r' -?[0-9]+ '
      #t = Token(type='NUMBER', attr=s)
      self.addToken('NUMBER', atoi(s))


#-----------------------------------------------------------

# extend scanner to understand reserved words:


class ParrotScanner(ScannerNoRW):

   def __init__(self):
      ScannerNoRW.__init__(self)

   def t_SUB(self, s):
      r' sub '
      self.addToken('SUB', None)

   def t_CSUB(self, s):
      r' csub '
      self.addToken('CSUB', None)

   def t_FOR(self, s):
      r' for '
      self.addToken('FOR', None)


#===========================================================
######  Parsing                                       ######
#===========================================================

class ParrotParser(GenericParser):

   def __init__(self, sourceText, start='compositionFile'):
      self.sourceText = sourceText
      GenericParser.__init__(self, start)
      self.gi = GlobalInfo()
 

   def parse(self, tokenList):
      self.tokenList = tokenList
      GenericParser.parse(self, tokenList)
      

   def p_compositionFile_1(self, args):
      ' compositionFile ::= compositionFile component '
      sayWhere(args)
      self.gi.addComponent(args[1])
      args[1].parent = self.gi
      
      
   def p_compositionFile_2(self, args):
      ' compositionFile ::= component '
      sayWhere(args)
      self.gi.addComponent(args[0])
      args[0].parent = self.gi
      return [args[0],]
      

   def p_component(self, args):
      ' component ::= type attributes subComponents_opt '
      sayWhere(args)
      if type(args[2]) == type([]):
         newComp = UIContainer(args[0], None)
         isContainer = 1
      else:
         newComp = UIComponent(args[0], None)
         isContainer = 0
      if args[1]:
         for attrNameValue in args[1]:
            n = attrNameValue[0]
            if n == '*sub':
               if isContainer: 
                  newComp.subAttr[attrNameValue[1]] = attrNameValue[2]
            elif n == '*csub':
               if isContainer: 
                  newComp.subAttr[attrNameValue[1]] = attrNameValue[2]
               newComp.attr[attrNameValue[1]] = attrNameValue[2]
            elif n == '*for':
               if isContainer: 
                  attrForType = attrNameValue[1]
                  attrName = attrNameValue[2]
                  attrValue = attrNameValue[3]
                  newComp.addTypeWideAttr(attrForType, attrName, attrValue)
            else:
               #>>>>> it's a normal attribute
               newComp.attr[n] = attrNameValue[1]
      if args[2]:
         for subComponent in args[2]:
            subComponent.parent = newComp
            newComp.addComponent(subComponent)
      return newComp


   def p_subComponents0(self, args):
      '  subComponents_opt ::= '
      sayWhere(args)
      return None


   def p_subComponents1(self, args):
      ' subComponents_opt ::= { components } '
      sayWhere(args)
      return args[1]


   def p_components0(self, args):
      ' components ::= components component '
      sayWhere(args)
      if type(args[0]) == type([]):
         # it's already a list
         componentList = args[0]
      else:
         componentList = [ ]
      if debug: print 'componentList=', componentList
      componentList.append(args[1])
      return componentList


   def p_components1(self, args):
      ' components ::= '
      sayWhere(args)
      return None


   def p_type(self, args):
      ' type ::= IDENTIFIER '
      sayWhere(args)
      return args[0].attr
      

   def p_componentId_opt(self, args):
      '''
         componentId_opt ::= @ IDENTIFIER
         componentId_opt ::= 
      '''
      sayWhere(args)
      if len(args) >= 2:
         return args[1].attr
      else:
         return None


   def p_str_opt(self, args):
      '''
         str_opt ::= STRING
         str_opt ::= 
      '''
      sayWhere(args)
      if len(args) >= 1:
         return args[0].attr
      else:
         return None
         

   def p_attributes(self, args):
      '''
         attributes ::= attributes attribute
         attributes ::= 
      '''
      sayWhere(args)
      if len(args) >= 2:
         attrList = args[0]
         if type(attrList) != type([]):
            attrList = [ ] 
         attrList.append(args[1])
         return attrList
      else:
         return None
     

   def p_attribute1(self, args):
      ' attribute ::= IDENTIFIER = value '
      sayWhere(args)
      return (args[0].attr, args[2])


   def p_attribute2(self, args):
      ' attribute ::= STRING '
      sayWhere(args)
      return ('text', args[0].attr)


   def p_attribute3(self, args):
      ' attribute ::= @ IDENTIFIER '
      sayWhere(args)
      return ('id', args[1].attr)

   def p_attribute4(self, args):
      ' attribute ::= SUB DOT IDENTIFIER = value '
      sayWhere(args)
      return ('*sub', args[2].attr, args[4])

   def p_attribute5(self, args):
      ' attribute ::= CSUB DOT IDENTIFIER = value '
      sayWhere(args)
      return ('*csub', args[2].attr, args[4])

   def p_attribute6(self, args):
      ' attribute ::= FOR DOT IDENTIFIER DOT IDENTIFIER = value '
      sayWhere(args)
      return ('*for', args[2].attr, args[4].attr, args[6])


   def p_value1(self, args):
      ' value ::= IDENTIFIER '
      sayWhere(args)
      return args[0].attr


   def p_value2(self, args):
      ' value ::= STRING '
      sayWhere(args)
      return args[0].attr


   def p_value3(self, args):
      ' value ::= NUMBER '
      sayWhere(args)
      return repr(args[0].attr)


   # process error messages
   def error(self, token):
      lines = split(self.sourceText, '\n')
      print "!!! Syntax error near line %d, col %d: !!!" % (
         token.line, token.col)
      # we need to subtract 1 from (token.line), because the 
      # user-visible way of counting lines starts from 1, but python
      # internally starts from 0.
      print lines[token.line - 1]
      print ('-' * (token.col-1)) + '^' 
      raise Exception, "fatal error"


#===========================================================


#-----------------------------------------------------------
# module testing:

def par2_test1():
   # test lexical analyser
   print '-----test1-----'
   s =  '  fgdgsdg = 34 @ { eee } "hell" = 34 @ { eee } ' 
   scanner = ParrotScanner()  
   res = scanner.tokenize(s) 
   for tok in res:
      print tok.type,
      if tok.attr != None: 
         print tok.attr
      else:
         print 



def par2_test2():
   # test parser
   print '----- test 2 -----'
   s = '''
   button @Button1 "Press me!" fontSize=12 

'''
   
   s = ''' 
rowLayout border=2 borderStyle=embossed 
   sub.bcol=blue csub.fcol=red 
   for.button.tooltip="A button!"
{ 
   button @Button1 "Press me!" fontSize=12 
   //label fcol="#00ff00" "My label" @label1 
}
'''
   ###   label fcol="#00ff00" "My label" @label1
   scanner = ParrotScanner()  
   res = scanner.tokenize(s) 
   print '----- test 2: lexical analysis: -----'
   for tok in res:
      print tok.type,
      if tok.attr != None: 
         print tok.attr
      else:
         print 
   print '----- test 2: parsing: -----'
   parser = ParrotParser(s)
   print 'res=', res
   parser.parse(res)
   print '----- test 2: result of parsing: -----'
   parser.gi.outputNormalized('')


if __name__=='__main__':
   #par2_test1()
   par2_test2()
   #par2_test3()
   #ex2()

#-----------------------------------------------------------
#end 


