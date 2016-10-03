# util.py
# 
# (c)1999 Philip Hunt
#
# Various python utility functions

# Last altered: 11-May-1999
# History:
# 28-Apr-1999 PhilHunt: created
# 11-May-1999 PH: added savePickle(), loadPickle() functions

import string, os, stat, pprint
from cPickle import *

#-----------------------------------------------------------
# return 1st index of character (c) in string (s)
# or -1 if no match
#
# Note: works for strings, lists and tuples

def strIndex(s, c):
   for i in xrange(0,len(s)):
      if s[i] == c: return i
   # no match:
   return -1

#-----------------------------------------------------------
# return 1st index of character (c) in string (s), starting
# at character position (p).
# Returns -1 if no match
#
# Note: works for strings, lists and tuples

def strIndexp(s, c, p):
   for i in xrange(p,len(s)):
      if s[i] == c: return i
   # no match:
   return -1

#-----------------------------------------------------------
# return 1st index of substring (ss) in string (s)
# or -1 if no match
#
# Note: works for strings, lists and tuples

def strIndexStr(s, ss):
   return strIndexStrp(s, ss, 0)

#-----------------------------------------------------------
# return 1st index of substring (ss) in string (s), starting
# at position (p) in (s).
# Returns -1 if no match
#
# Note: works for strings, lists and tuples

def strIndexStrp(s, ss, p):
   ls = len(s)
   lss = len(ss)
   if ls == 0 or lss == 0 or lss>ls: return 0
   for i in xrange(p,ls-lss+1):
      for j in xrange(0,lss):
         if s[i+j] != ss[j]: break
      else:
         #got match so return it
         return 
   # no match:
   return -1

#-----------------------------------------------------------
# is string (s) a directory?

def isDir(s):
   mode = os.stat(s)[stat.ST_MODE]
   return stat.S_ISDIR(mode)

#-----------------------------------------------------------
# read a file into a string

def readFile(filename):
   f = open(filename, 'r')
   s = f.read()
   f.close()
   return s

#-----------------------------------------------------------
# write a string into a file

def writeFile(filename, newValue):
   # at a later date, add code here to create directories
   # if they don't exist
   f = open(filename, 'w')
   f.write(newValue)
   f.close()


#-----------------------------------------------------------
# save a pickled file

def savePickle(filename, object):
   f = open(filename, 'w')
   p = Pickler(f)
   p.dump(object)
   f.close()

#-----------------------------------------------------------
# load a pickled file into an object

def loadPickle(filename):
   try:
      f = open(filename, 'r')
      u = Unpickler(f)
      object = u.load()
      f.close()
   except:
      object = None

   return object

#-----------------------------------------------------------

#-----------------------------------------------------------

#end 
