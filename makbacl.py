# makbacl.py
# 
# (c)1999-2001 Philip Hunt
#
# Program to make an instance of a backend class 

# Last altered: 14-Oct-2001
# History:
# 28-Aug-1999 PhilHunt: created

debug=0

#===========================================================
# Makes an instance of a backend class, for backend (be)
# and component type (type).
# Eg. if (be) is 'html' and (type) is 'button', it will
# attempt to make a HtmlBackend.Html_button. if it cannot make
# a member of the exact class if will try to make one of
#    <backend>_container
# or:
#    <backend>_component
# depending on the value of (isKindOfContainer).
#
# Returns the instance it has just made, or (None) if it
# couldn't make anything.


def makeBackendInstance(be, type, isKindOfContainer=0):
   if debug: print '## trying to make a %s_%s... ##' % (be, type)
   backendModule = __import__(be + "Backend")
   nameStart = 'backendModule.' + be + '_'
   cl = nameStart + type
   instance = None
   try:
      instance = eval(cl + '()')
   except:
      if isKindOfContainer:
         # try to create instance of <thebackend>_container
         clTry2 = nameStart + 'container'
      else:
         #try to create instance of <thebackend>_component
         clTry2 = nameStart + 'component'
      try:
         instance = eval(clTry2 + '()')
      except:
         print ('Warning: Unable to create instance of %s or %s,' 
            + ' so ignoring this component') % (
            cl, clTry2)
   return instance



#===========================================================

# test this class:

if __name__=='__main__':
   print '===== starting makbacl.py ====='
   ob = makeBackendInstance('Html', 'button')
   print '(ob) is', ob
   ob1 = makeBackendInstance('Html', 'table')
   print '(ob1) is', ob1

#end 
