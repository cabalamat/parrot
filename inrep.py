# inrep.py
# 
# (c)1999 Philip Hunt
# Released under the GNU General Public Licence
#
# Intermediate repesentation of Parrot source files

# Last altered: 24-Sep-1999
# History:
# 6-Aug-1999 PhilHunt: created
# 14-Sep-1999 PH: implementing generic attributes (sub, csub, for)

import copy

debug = 1

#===========================================================
# UIComponent
#
# A user interface component, e.g. a button, or a rowLayout. 
#
# instance variables:
# type = string containing the component's type, e.g. 'button'.
# attr = dictionary of attribute names and their values; values
#    are either string or integer
# parent = this component's container; a UIContainer or GlobalInfo

class UIComponent:

   def __init__(self, myType, myParent):
      self.type = myType
      self.attr = {}
      self.parent = myParent
      if myParent: myParent.addComponent(self)

   def getAllAttr(self):
      result = copy.deepcopy(self.parent.getAllSubAttr())
      
      typeWideAttrs = self.parent.getAllTypeWide()
      if typeWideAttrs.has_key(self.type):
         result.update(typeWideAttrs[self.type])
         
      result.update(self.attr)
      return result

   def getComponents(self):
      return [ ]


   def outputNormalized(self, prefix=''):
      print prefix + self.type,
      if self.attr.has_key('id'): 
         print '@' + self.attr['id'],
      if self.attr.has_key('text'): 
         print '"' + self.attr['text'] + '"',
      print
      for attrName, attrValue in self.attr.items():
         if attrName not in ('id','text'):
            print prefix + '   ' + outputFormOfAttr(attrName, attrValue)


   def getPath(self):
      result = self.parent.getPath() + '.' + self.type
      if self.attr.has_key('id'):
         result = result + '@' + self.attr['id']
      return result

#===========================================================
# UIContainer
#
# A user interface component which can contain other components,
# e.g. a rowLayout.
#
# instance variables:
#
# components = a list of the immediate sub-components of this object
#
# subAttr = dictionary of attribute names and their values, for all
#    sub-components of this component. E.g. if subAttr is 
#    {'font':'Helvetica'} then all sub-components have the attribute
#    font=Helvetica, unless they are redefined.
#
# typeWide = attributes inherited by a particular UIComponent
#    type. This is a dictionary, key is component type, value is
#    a dictionary of attributes for that type, e.g:
#    {'button':{'fcol':'green'}, 'label':{'font':'Helvetica'}}
#    means that buttons all default to green foreground colur, and
#    labels all default to using the helvetica font.

class UIContainer(UIComponent):

   def __init__(self, myType, myParent):
      self.components = []
      self.subAttr = {}
      self.typeWide = {}
      UIComponent.__init__(self, myType, myParent)

   def addComponent(self, myNewComponent):
      self.components.append(myNewComponent)

   def getAllSubAttr(self):
      result = copy.deepcopy(self.parent.getAllSubAttr())
      result.update(self.subAttr)
      return result

   # get all type-wide attributes for self and 
   def getAllTypeWide(self):
      result = copy.deepcopy(self.parent.getAllTypeWide())
      for k, v in self.typeWide.items():
         if result.has_key(k):
            result[k].update(v)
         result[k] = v
      return result

   def getComponents(self):
      return self.components

   def outputNormalized(self, prefix=''):
      UIComponent.outputNormalized(self, prefix)
      for k,v in self.subAttr.items():
         print prefix + ('   sub.%s="%s"' % (k, v))
      for k,v in self.typeWide.items():
         for k2, v2 in v.items():
            print prefix + ('   for.%s.%s="%s"' % (k, k2, v2))
      print prefix + '{'
      for component in self.components:
         component.outputNormalized(prefix + '   ')
      print prefix + '}'

   def addTypeWideAttr(self, typeName, attrName, attrValue):
      if not self.typeWide.has_key(typeName):
         self.typeWide[typeName] = {}
      typeDict = self.typeWide[typeName]
      typeDict[attrName] = attrValue


#===========================================================
# GlobalInfo
#
# Global information, i.e. defaults for attributes

class GlobalInfo(UIContainer):

   def __init__(self):
      UIContainer.__init__(self, 'GLOBAL', None)

   def getAllSubAttr(self):
      return self.subAttr

   def getAllTypeWide(self):
      return self.typeWide

   def getPath(self):
      return 'GLOBAL'

#===========================================================

#-----------------------------------------------------------
# some method...

def outputFormOfAttr(aName, aValue):
   if aName == 'id': return '@' + aValue
   if aName == 'text': return '"' + aValue + '"'
   result = aName + '=' + '"' + aValue + '"'
   return result

#end 
