# backend.py
# 
# Copyright (C) 1999-2001 Philip Hunt
# Released under the GNU General Public Licence
#
# Generic backend framework for Parrot

# Last altered: 14-Jun-2001
# History:
# 7-Aug-1999 PhilHunt: created
# 24-Aug-1999: added calcOutputFilename()
# 28-Aug-1999: now using makbacl.py

import string

from inrep import *
import makbacl

sPrefix =          '|-> '
sSubseqPrefix =    '|   '
sEndPrefix =       '+-> '
sEndSubseqPrefix = '    '

sAttrPrefix = ': '

debug = 0

#===========================================================
#####  Generic backend  ####################################
#===========================================================

# Backend_component
#
# instance variables:
# type = the component's type, e.g. 'button'
# parent = the component's parent; a Backend_container
# attr = dictionary of attributes

class Backend_component:

   def __init__(self):
      self.type = '?'
      #self.parent = myParent
      #if not isinstance(self, Backend_container):
      #   print 'in Backend_component.__init__, making a %s' \
      #      % self.__class__

      self.attr = {}

   def getAttrDoc(self):
      # return a description of the attributes understood by this
      # component type.
      # This will usually be subclassed
      return { '(none)': '(no attributes defined)' }

   # return the value of the 'id' attribute, which is usually entered
   # in the UI definition file with @id
   def getId(self):
      try:
         return self.attr['id']
      except:
         return ''
         
   # return the value of an attribute. Typically attributes are entered
   # in the UI definition file in a form attrName=attrValue
   # If the attribute doesn't exist, return None. This is a convenience
   # function; you can also use (theComponent.attr['attrName'])
   def getAttr(self, attrName):
      try:
         return self.attr[attrName]
      except:
         return None

   # return the value of the 'text' attribute, which is usually entered
   # in the UI definition file with "some text"
   def getText(self):
      try:
         return self.attr['text']
      except:
         return ''

   def asString(self, firstPrefix='', subseqPrefix=''):
      global sPrefix, sAttrPrefix
      result = '%s%s %s\n' % (firstPrefix, self.__class__ , self.type)
      for k,v in self.attr.items():
         result = result + ('%s%s%s=%s\n' % (
            subseqPrefix, sAttrPrefix, k, v ))
      return result
      
   # return this component's top-level ancestor   
   def getGlobal(self):
      if isinstance(self, Backend_GLOBAL): return self
      return self.parent.getGlobal()



#===========================================================

# instance variables:
# components = list of immediate subcomponents

class Backend_container(Backend_component):

   def __init__(self):
      #print 'in Backend_container.__init__, making a %s' \
      #   % self.__class__
      self.components = [ ]
      Backend_component.__init__(self)

   def populateSubComponents(self, uiEquivalent):      
      global sig
      #print 'populating from: %s' % uiEquivalent.getPath()
      for uiComp in uiEquivalent.getComponents():
         self.addSubComponent(uiComp)

   def addSubComponent(self, uiComp):
      isContainer = isinstance(uiComp, UIContainer)
      instance = makbacl.makeBackendInstance(sig, uiComp.type, isContainer)
      if not instance: return 
      if isContainer: instance.components = [ ]
      if debug: print 'instance=', instance
      self.components.append(instance)
      instance.type = uiComp.type
      instance.parent = self
      instance.attr = uiComp.getAllAttr()

      if isinstance(uiComp, UIContainer):
         # need to create sub-components:
         instance.populateSubComponents(uiComp)


   def getStartCode(self):
      return ''

   def getCodeBetweenComponents(self):
      return ''

   def getEndCode(self):
      return ''

   def getCodeIfEmpty(self):
      return self.getStartCode() + self.getEndCode()

   def getCode(self):
      #print "container:getCode() type=%s" % self.type
      if len(self.components)==0:
         return self.getCodeIfEmpty()
      else:
         result = self.getStartCode()
         firstIteration = 1
         for comp in self.components:
            if not firstIteration:
               result = result + self.getCodeBetweenComponents()
            #print "@@@ comp=%s;%s, result='%s'" %(comp.type, comp, result)
            v = comp.getCode()
            #print "@@@@ result_type:%s v_type:%s v='%s'" %(
            #   type(result), type(v), v)
            result = result + v
            if firstIteration:
               firstIteration = 0
         result = result + self.getEndCode()
         return result

         
   def asString(self, firstPrefix='', subseqPrefix=''):
      global sPrefix
      result = Backend_component.asString(self, firstPrefix, subseqPrefix) 
      result = result + subseqPrefix \
        + '(number of components = ' + repr(len(self.components)) + ')\n' 

      i = 0
      siz = len(self.components)
      for c in self.components:
         i = i + 1
         if i != siz:
            newPre = subseqPrefix + sPrefix
            newSub = subseqPrefix + sSubseqPrefix
         else: 
            newPre = subseqPrefix + sEndPrefix
            newSub = subseqPrefix + sEndSubseqPrefix
         result = result + c.asString(newPre, newSub)
      return result


#===========================================================
# Backend_GLOBAL is the abstract superclass of back ends
# It doesn't do a lot yet
#
# instance variables:
# gui = an instance of GlobalInfo containing a user interface
#    definition
# outputFilename = the filename that parrot.py will output the
#    results to. This is written to by parrot.py.

class Backend_GLOBAL(Backend_container):

   def useUI(self, useThisUserInterfaceDefinition):
      global sig
      sig = self.getBackendSignature()
      self.gui = useThisUserInterfaceDefinition
      self.type = self.gui.type
      self.parent = None

      self.populateSubComponents(self.gui)      
      
   def getBackendSignature(self):
      raise ImpBySubclass, 'This method should be implemented by subclass!!'

   def fileExtension(self): return '.out'

   def calcOutputFilename(self, inputFilename):
      try:
         posn = string.rindex(inputFilename, '.')
         cut = inputFilename[:posn]
      except:
         # no '.', so use the whole string
         cut = inputFilename
      return cut + self.fileExtension()

 
 
#-----------------------------------------------------------

#end 




