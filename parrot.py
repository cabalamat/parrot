# parrot.py
# 
# (c) 1999-2001 Philip Hunt
# Released under the GNU General Public Licence
#
# Main program for Parrot

# Last altered: 14-Oct-2001
# History:
# 7-Aug-1999 PhilHunt: created

import sys
import util     # Phil Hunt's Python utilities
import pparser  # Parrot parser, reads *.par files


debug = 0

#===========================================================

# List of backends
# When you add a new backend, you must add it to this list

backendList = [ 'Html', 'Paxo', 'Pytk', 'Elisp' ]

# Version of Parrot. 
# This is a release number of the form a.b.c, followed an optional
# `+', which means the current version isn't a release, but contains
# code added since that release.

parrotVersion = '0.2.6+'


#===========================================================
# print messages:

def startMessage():
   print """Parrot-%s, Copyright (C) 1999-2001 Philip Hunt 
Released under the GNU General Public License""" % parrotVersion


def usage():
   print """
Usage:   python parrot.py input.par backend [output]

Where:
   input.par = Parrot file containing GUI definition.
   backend =   Name of back end to output to.
   output =    Name of output file; this defaults to the input
               file name, with the *.par extension changed to 
               something determined by the backend.

Alternate usage:   python parrot.py --info

which returns a list of backends installed.
"""

def printInfo():
   print "Parrot version: %s" % parrotVersion
   print "Backends installed:",
   for be in backendList: print be,
   print

   for be in backendList:
      print be, 'backend:'
      TheBackend = __import__(be + "Backend")
      backendGlobal = eval('TheBackend.' + be + '_GLOBAL()')
      print '   CONTAINERS:',
      for cont in backendGlobal.getContainerTypes():
         print cont,
      print '\n   COMPONENTS:',
      for comp in backendGlobal.getNonContainerTypes():
         print comp,
      print

#===========================================================

def main():
   sourceFilename = sys.argv[1]
   try:
      backendName = sys.argv[2]
   except:
      print 'Error: no backend specified.'
      print 'You must tell Parrot which backend to use.'
      usage()
      return

   try:
      source = util.readFile(sourceFilename)
   except:
      print 'Error: cannot read file "%s"' % sourceFilename
      return

   if backendName not in backendList:
      print 'Error: Parrot doesn\'t have a "%s" backend.' \
         % backendName
      print "Installed backends are:",
      for be in backendList: print be,
      print "\nParrot is aborting now."
      return

   #>>>>> create the backendGlobal variable, dependent on backend
   TheBackend = __import__(backendName + "Backend")
   backendGlobal = eval('TheBackend.' + backendName 
      + '_GLOBAL()')

   try:
      outputFilename = sys.argv[3]
   except:
      # couldn't read argv[3], so form the output filename
      # from the backend
      outputFilename = backendGlobal.calcOutputFilename(sourceFilename)
   if debug: print 'outputFilename =', outputFilename
      
   #>>>>> read input:
   if debug: print '----- main: lexical analysis: -----'
   scanner = pparser.ParrotScanner()  
   res = scanner.tokenize(source) 
   if debug: print '----- main: parsing: -----'
   # we tell the Parser what (source) is, to help it print
   # error text if necessary
   parser = pparser.ParrotParser(source)
   try:
      parser.parse(res)
   except Exception, details:
      # an error occurred while parsing
      print "Error occurred while parsing, will not create output."
      return
   if debug: 
      print '----- test 2: result of parsing: -----'
      parser.gi.outputNormalized('')

   #>>>>> generate backend object tree:
   backendGlobal.outputFilename = outputFilename
   backendGlobal.useUI(parser.gi)
   code = backendGlobal.produceCode()
   if debug: 
      print '-------------backendGlobal.asString():\n' + backendGlobal.asString()
      print '-------------code:', code
   util.writeFile(outputFilename, code)
   print 'Parrot: Created %s' % outputFilename


#-----------------------------------------------------------

startMessage()
if len(sys.argv) < 2:
   usage()
elif sys.argv[1] == '--info':
   printInfo()
else:
   main()


#end 
