# README.md for Parrot

Version `parrot-0.2.6+`
By Philip Hunt <cabalamat@gmail.com>
On Github at <https://github.com/cabalamat/parrot>

## What is Parrot?

Parrot is a text-based GUI builder. To use it, you write
a *.par file with your favourite text editor, then invoke
Parrot from the command line. Parrot outputs a file which is
source code that when executed will produce the GUI.

## Requirements

Parrot runs on Python 2.7 on Linux. I haven't tested it on other
OSes, but I don't anticipate any difficulties in getting it to run
on other systems.

## How to use Parrot

Go into the directory you installed Parrot into. At the command
line, type:

    $ python parrot.py

This causes Parrot to print usage information.

## How to use the Pytk backend

To use Pytk, go into the directory you installed Parrot into, and
type:

    $ python parrot.py simple2.par Pytk

Parrot will reply that it has created simple2.py. Now run this,
by typing:

    $ python simple2.py

If everything has worked, a window will appear, titled
"My second Window". Parts of the window are coloured in blue or
yellow; this is a feature to aid my debugging -- it also makes
the window look pretty :-)

## Development Roadmap

Some changes that are underway:

Future changes (in this approximate order):

* finish writing Python/Tkinter backend
* add generic attributes to .par front end
* write PIG - the Parrot Information Generator. This outputs
  information about what Backends are installed, and what
  components they understand
* improve documentation, especially programming documentation to
  encourage other people to contribute backends.
* improve lexical analysis and parsing: add preprocessor, file
  inclusion, #line directive.
* write other backends, e.g. Glade XML file backend; write Glade
  XML import module.
* (possible)write import/export routines to Parrot XML format


## Files

Parrot contains these files:

README = you're reading it now!

INTRO = introductory documentation

guicomp.txt = the original spec for parrot

CHANGES = list of changes

SPEC = specification of Parrot's file formats

Makefile = ``make clean'' will get rid of unnecessary files

parrot.py = the main module

pparser.py = parses *.par files, uses generic.py to do this

generic.py = John Aycock's SPARK parser framework, version 0.5

tokpos.py = subclasses some of the classes in SPARK-0.5, to enable
        better error reporting.

inrep.py = classes for internal representation of *.par files

backend.py = generic backend classes, real backends inherit from these

HtmlBackend.py = the HTML backend

PaxoBackend.py = the Paxo backend

PytkBackend.py = the Python/Tkinter backend

macbacl.py = code to make instances of backend classes. Works with
        the inrep.py and *Backend.py modules.

util.py = various utility functions

*.par = test files demonstrating simple GUI-specifications that Parrot
        can process

sample5.par produces sample5.py when run with the Pytk backend
        (see notes above).


